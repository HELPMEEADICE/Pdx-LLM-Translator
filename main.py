# Fucking PDX Code

import os
import sys
import yaml
import argparse
import copy
import concurrent.futures
from openai import OpenAI
from dotenv import load_dotenv
from tqdm import tqdm

# --- 1. 配置与初始化 (不变) ---
load_dotenv()
API_BASE_URL, API_KEY, MODEL_NAME = os.getenv("OPENAI_API_BASE"), os.getenv("OPENAI_API_KEY"), os.getenv("OPENAI_MODEL_NAME")
MAX_WORKERS = int(os.getenv("MAX_CONCURRENT_REQUESTS", 10))
if not all([API_BASE_URL, API_KEY, MODEL_NAME]):
    print("错误：请确保 .env 文件中已配置 OPENAI_API_BASE, OPENAI_API_KEY 和 OPENAI_MODEL_NAME")
    sys.exit(1)
client = OpenAI(base_url=API_BASE_URL, api_key=API_KEY)


# --- 2. 核心函数 (基本不变) ---

def translate_one(text: str, target_language: str, source_language: str) -> str:
    """(最简版本) 使用大模型翻译纯文本字符串。"""
    if not text: return ""
    prompt = f"""
    You are an expert translator for Paradox Interactive game localization files.
    Translate the following text from {source_language} to {target_language}.
    **Crucial instructions:**
    1.  Preserve Special Codes: Do NOT translate or alter §Y, §G, §!, etc.
    2.  Preserve Placeholders: Do NOT translate content inside [] like [From.GetName].
    3.  Return Only the Translation: Provide only the translated string, without quotes.
    **Text to translate:**
    "{text}"
    """
    max_retries = 3
    for _ in range(max_retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}], model=MODEL_NAME, temperature=0.2,
            )
            translated_text = chat_completion.choices[0].message.content.strip().strip('"')
            return translated_text
        except Exception: pass
    return text

def collect_strings_to_translate(data, path=None):
    if path is None: path = []
    strings = []
    if isinstance(data, dict):
        for k, v in data.items(): strings.extend(collect_strings_to_translate(v, path + [k]))
    elif isinstance(data, str): strings.append((path, data))
    return strings

def update_data_with_translations(data, translated_items):
    for path, text in translated_items:
        temp = data
        for part in path[:-1]: temp = temp[part]
        temp[path[-1]] = text
    return data


# --- 3. ✨✨✨ 主程序逻辑 (采用精确的 Representer 方案) ✨✨✨ ---
def main():
    parser = argparse.ArgumentParser(description="智能检测 Paradox YAML 文件语言并进行中英互译。")
    parser.add_argument("source_file", help="源语言 YAML 文件路径 (例如: my_mod_l_english.yml)")
    args = parser.parse_args()

    try:
        # ... (语言检测、并发翻译等部分和之前完全一样，此处省略以保持清晰) ...
        print(f"🧐 正在分析文件: {args.source_file}")
        with open(args.source_file, 'r', encoding='utf-8') as f: source_data = yaml.safe_load(f)
        
        source_lang_code, target_lang_code, source_lang_name, target_lang_name = "", "", "", ""
        if 'l_english' in source_data:
            source_lang_code, target_lang_code, source_lang_name, target_lang_name = 'l_english', 'l_simp_chinese', 'English', 'Simplified Chinese'
            print("➡️ 检测到源语言: 英文。准备翻译为中文...")
        elif 'l_simp_chinese' in source_data:
            source_lang_code, target_lang_code, source_lang_name, target_lang_name = 'l_simp_chinese', 'l_english', 'Simplified Chinese', 'English'
            print("➡️ 检测到源语言: 中文。准备翻译为英文...")
        else:
            print("❌ 错误：文件内容必须包含 'l_english:' 或 'l_simp_chinese:' 作为顶级键。"); sys.exit(1)

        output_file = args.source_file.replace(source_lang_code, target_lang_code)
        print(f"💾 目标文件名将被设为: {output_file}")
        all_strings = collect_strings_to_translate(source_data[source_lang_code])
        if not all_strings: print("文件中没有找到需要翻译的字符串。"); return
            
        print(f"总共找到 {len(all_strings)} 个字符串需要翻译。")
        print(f"🚀 准备启动并发翻译，最大并发数: {MAX_WORKERS}")

        all_translated_items = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            future_to_path = {executor.submit(translate_one, text, target_lang_name, source_lang_name): path for path, text in all_strings}
            for future in tqdm(concurrent.futures.as_completed(future_to_path), total=len(all_strings), desc="💪 单兵作战中", unit="串"):
                path, translated_text = future_to_path[future], future.result()
                all_translated_items.append((path, translated_text))

        print("\n🛠️ 正在用翻译结果重建文件...")
        translated_data_content = {}
        update_data_with_translations(translated_data_content, all_translated_items)
        final_output_structure = {target_lang_code: translated_data_content}

        # ✨ --- VIP 贵宾接待方案 --- ✨

        # 1. 定义我们的“VIP”字符串类型
        class DoubleQuotedString(str):
            pass

        # 2. 定义接待“VIP”的方式：用双引号
        def double_quoted_presenter(dumper, data):
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='"')

        # 3. 注册这个接待方案
        yaml.add_representer(DoubleQuotedString, double_quoted_presenter)

        # 4. 一个函数，负责给所有“值”发VIP卡（并处理换行符 \n）
        def grant_vip_status_to_values(data):
            if isinstance(data, dict):
                # 键(k)保持普通，递归处理值(v)
                return {k: grant_vip_status_to_values(v) for k, v in data.items()}
            elif isinstance(data, str):
                # 将值字符串转换为带VIP卡的类型，并提前处理好换行符
                return DoubleQuotedString(data.replace('\n', '\\n'))
            else:
                # 其他类型（如数字）不变
                return data

        print("💅 正在为所有值添加引号并处理换行符...")
        final_data_for_dump = grant_vip_status_to_values(final_output_structure)
        
        print(f"✍️ 正在将最终结果写入新文件: {output_file}")
        with open(output_file, 'w', encoding='utf-8-sig') as f:
            # 现在，dump函数会智能地只对我们标记过的“VIP”值使用双引号
            yaml.dump(
                final_data_for_dump,
                f,
                allow_unicode=True,
                sort_keys=False,
                width=1000,
                # 注意：不再需要 default_style 参数！
            )

        print(f"\n🎉 翻译大功告成！文件已保存为 {output_file}")

    except Exception as e:
        import traceback
        print(f"\n❌ 发生意外错误: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()
