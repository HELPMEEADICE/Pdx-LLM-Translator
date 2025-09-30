# Pdx-LLM-Translator: Paradox 游戏模组本地化文件智能翻译器

![GitHub repo size](https://img.shields.io/github/repo-size/HELPMEEADICE/Pdx-LLM-Translator?style=for-the-badge)
![Python Version](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

你是否曾为手动翻译 Paradox 游戏（如群星 Stellaris、十字军之王 Crusader Kings、维多利亚 Victoria、钢铁雄心 Hearts of Iron 等）的本地化 `.yml` 文件而感到烦恼？现在，有了 `Pdx-LLM-Translator`，你可以将这项繁琐的工作交给 AI，实现一键式、高质量、格式完美的自动翻译！

## ✨ 项目亮点

*   **智能语言检测**：自动识别源文件是中文 (`l_simp_chinese`) 还是英文 (`l_english`)，并生成对应语言的目标文件。
*   **格式完美保留**：
    *   精确保留 P 社特有的颜色代码（如 `§Y`, `§!` 等）。
    *   完整保留变量括号（如 `[From.GetName]`），绝不误译。
    *   完美处理换行符，输出为 P 社引擎兼容的 `"...\n..."` 格式。
    *   **严格遵守 `key: "value"` 格式**，键（key）不加引号，值（value）一律加上双引号。
*   **并发处理，风驰电掣**：利用多线程并发请求大语言模型 API，极大缩短翻译等待时间。
*   **进度可视化**：使用 `tqdm` 进度条，实时展示翻译进度，一切尽在掌握。
*   **配置灵活**：通过简单的 `.env` 文件即可配置 API 地址、密钥、模型名称和并发数。
*   **高度容错**：内置重试机制，应对偶尔的网络波动或 API 请求失败。

## 🚀 性能与模型推荐

为了在**成本**和**翻译质量**之间取得最佳平衡，作者强烈推荐使用以下几款轻量级、高速度的大语言模型：

1.  **Gemini-2.5-Flash-Lite**：Google 出品的最新一代轻量模型，在速度、质量和成本效益上达到了惊人的平衡，是本项目翻译任务的**首选推荐**。
2.  **Grok 4 Fast**：xAI 的高效模型，以其快速的响应和优异的性能著称，非常适合处理大量的文本翻译请求。
3.  **DeepSeek-V3.2**：一款开源模型，在代码和自然语言处理方面表现出色，作为备选同样能提供可靠的翻译结果。

这些模型通常具有更低的调用成本和更快的响应速度，同时其翻译能力足以胜任游戏本地化场景。当然，您也可以根据自己的需求配置如 `GPT-4` 等更强大的模型。

## 🛠️ 安装与使用指南

### 步骤 1: 克隆项目

将本项目代码克隆到您的本地设备。

```bash
git clone https://github.com/HELPMEEADICE/Pdx-LLM-Translator.git
cd your-repo-name
```

### 步骤 2: 安装依赖

推荐使用虚拟环境。项目依赖项非常简洁：

```bash
# 创建并激活虚拟环境 (可选但推荐)
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 安装必要的库
pip install -r requirements.txt
```

文件 `requirements.txt` 应包含以下内容：

```txt
pyyaml
openai
python-dotenv
tqdm
```

### 步骤 3: 创建并配置 `.env` 文件

在项目根目录下创建一个名为 `.env` 的文件，并填入您的 API 信息。**请勿将此文件上传到公开的代码仓库！**

```ini
# .env

# 您的 LLM API 服务地址，例如 OpenAI 官方或本地/第三方代理
OPENAI_API_BASE="http://127.0.0.1:8000/v1"

# 您的 API 密钥
OPENAI_API_KEY="your-secret-api-key"

# 您希望使用的模型名称
OPENAI_MODEL_NAME="gemini-2.5-flash-lite"

# 最大并发请求数，请根据您的硬件和API提供商的限制进行调整
MAX_CONCURRENT_REQUESTS=20
```

### 步骤 4: 执行翻译！

将您想要翻译的 `.yml` 文件（例如 `my_mod_l_english.yml`）放入项目文件夹中，然后运行以下命令：

```bash
python translate_pdx_yml.py my_mod_l_english.yml
```

脚本将会：
1.  检测到文件名中的 `l_english`。
2.  自动将目标语言设置为 `l_simp_chinese`。
3.  开始翻译，并显示进度条。
4.  完成后，在同一目录下生成一个名为 `my_mod_l_simp_chinese.yml` 的新文件，内容已全部翻译并完美格式化。

反之，如果您提供一个中文文件 `my_mod_l_simp_chinese.yml`，它也会智能地翻译回英文 `my_mod_l_english.yml`。

## 📜 许可证

本项目采用 [MIT License](LICENSE) 授权。您可以自由地使用、修改和分发，但请保留原始的版权和许可声明。