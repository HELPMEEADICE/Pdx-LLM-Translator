# Pdx-LLM-Translator: 颠覆P社游戏翻译的终极武器

<p align="center">
  <img src="https://img.shields.io/badge/状态-革命已至-red?style=for-the-badge" />
  <img src="https://img.shields.io/github/stars/HELPMEEADICE/Pdx-LLM-Translator?style=for-the-badge&logo=github&color=yellow" />
  <img src="https://img.shields.io/github/forks/HELPMEEADICE/Pdx-LLM-Translator?style=for-the-badge&logo=github&color=green" />
</p>

<h2 align="center">“P社游戏翻译将被颠覆，全自动化中英互译正式上线。”</h2>

---

你，是否还在为几万行本地化文本而肝脑涂地？
你，是否还在无尽的复制、粘贴、翻译、校对中消磨生命？
你，是否还在被 `§Y`、`[Root.GetName]` 和各种换行符折磨到深夜？

**现在，这一切都将成为历史。**

`Pdx-LLM-Translator` 是一款专为 **Paradox 游戏模组（群星、钢丝、十字军之王、维多利亚等）** 打造的、革命性的本地化文件翻译工具。它将彻底解放你的生产力，让翻译不再是负担，而是创作的翅膀。

## 💥 凭什么“颠覆”一切？

| 曾经的炼狱模式 (手动翻译)                                    | **现在的天堂模式 (一键AI搞定)**                                   |
| ------------------------------------------------------------ | ----------------------------------------------------------------- |
| 😭 大量文本，望而生畏                                         | ⚡️ **速度革命**：上万行文本，一杯咖啡的时间即可搞定！          |
| 🤯 变量代码 `[xxx]` 被误译，游戏报错                         | 🧠 **格式金身**：像素级完美保留所有P社特殊代码、变量和颜色标记  |
| 🤬 引号、换行符格式混乱，进游戏全是BUG                       | 🛡️ **格式洁癖**：严格生成 `key: "value"` 标准格式，杜绝一切格式错误 |
| 😵 中英互译？得全部重来一遍                                  | 🔄 **无缝切换**：智能识别语言，自动完成中英双向互译          |
| 💸 使用昂贵的大模型，钱包在哭泣                               | 🎯 **智能引擎**：专为轻量级高效模型优化，成本暴降，质量不减！     |

## 🚀 性能怪兽：推荐引擎

忘记那些又贵又慢的“屠龙刀”吧！对于游戏翻译这种“庖丁解牛”的活，我们需要的是最锋利、最迅捷的匕首。本项目作者强烈推荐以下**经过实战检验的高效费比模型**：

*   🥇 **Gemini-2.5-Flash-Lite (首选)**: Google 新一代闪电侠，速度、质量、价格的完美结合体。用它，就对了。
*   🥈 **Grok 4 Fast**: 马斯克的xAI出品，一个字，快！应对海量文本翻译的绝佳选择。
*   🥉 **DeepSeek-V3.2**: 国产开源之光，表现优异，同样是值得信赖的可靠伙伴。

**用最少的成本，换取最大的生产力解放，这才是Modder的极客精神！**

## 🛠️ 三步部署，即刻起飞！

无需复杂的环境配置，三步之内，让你的翻译工作进入全自动时代。

### 步驟 1：克隆革命的火种 🔥

在你的电脑上，打开终端，输入：

```bash
git clone https://github.com/HELPMEEADICE/Pdx-LLM-Translator.git
cd Pdx-LLM-Translator
```

### 步驟 2：武装你的环境 ⚙️

我们推荐使用虚拟环境，干净又卫生。

```bash
# 创建并激活虚拟环境
python -m venv venv
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# 安装依赖，就像给机枪上膛
pip install -r requirements.txt
```

`requirements.txt` 文件内容:
```txt
pyyaml
openai
python-dotenv
tqdm
```

### 步驟 3：填入你的“万能钥匙” 🔑

在项目根目录，创建一个 `.env` 文件。这是你的私人密钥库，**绝对不要泄露给任何人！**

```ini
# .env

# 你的API中转站或官方地址
OPENAI_API_BASE="http://127.0.0.1:8000/v1"

# 你的API密钥
OPENAI_API_KEY="your-secret-api-key"

# 你选择的“引擎”名称
OPENAI_MODEL_NAME="gemini-2.5-flash-lite"

# 并发数，决定了你的“火力”有多猛！根据你的API限制调整
MAX_CONCURRENT_REQUESTS=20
```

## 🚀 发射！

准备好你的 `.yml` 文件（例如 `my_mod_l_english.yml`），将它放在项目目录里。

然后，在终端中，执行这句魔咒：

```bash
python translate_pdx_yml.py my_mod_l_english.yml
```

**接下来，你只需靠在椅子上，欣赏进度条的飞速前进。**

奇迹发生后，一个完美翻译、格式无瑕的 `my_mod_l_simp_chinese.yml` 文件将自动出现在你的面前。

---

## 🌟 加入这场翻译革命！

**这是一个为Modder而生的工具。** 如果它解放了你的双手，点亮了你的创作灵感，请不要吝啬你的 **Star**！

你的支持，是这场革命继续前进的最大动力。

**是时候告别重复劳动，拥抱真正的创造了。立即下载，体验颠覆性的翻译快感！**