# LangChain 官网的入门 demo
基于官网最新版 langchain v0.3 + Gemini 来写。

## 预先准备
### 环境说明
- 基于 python 3.11
- 需申请谷歌 API KEY（免费）：https://aistudio.google.com/app/apikey
- 有 jupyter notebook 环境
### 配置
配置 `config.toml` 文件，把申请到的谷歌 API KEY 填入即可。

### 启动
1. 安装依赖
    ```shell
    # 安装 uv 参考 https://github.com/astral-sh/uv?tab=readme-ov-file#installation
    # On Windows.
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

    # On macOS and Linux.
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # 安装项目依赖
    uv sync
    ```
2. 在 vscode 中打开 ipynb 文件即可

## 进度
基础组件使用
- 聊天模型调用和提示词模板使用：[chat_and_prompts.ipynb](components/chat_and_prompts.ipynb)
- 语义搜索（嵌入模型使用）：[semantic_search.ipynb](components/semantic_search.ipynb)
- 文本分类、标签（文本情绪、主题分析）：[classification.ipynb](components/classification.ipynb)

LangGraph编排
- 构建一个带记忆的聊天机器人：[chat_bot.ipynb](orchestration/chat_bot.ipynb)
- 构建一个带记忆的 Agent（需配置 TAVILY_API_KEY）：[agent.ipynb](orchestration/agent.ipynb)
- RAG 应用 part1（提问、检索、回答）：[rag_part1.ipynb](orchestration/rag_part1.ipynb)

## 参考资料
- 官方教程文档：https://python.langchain.com/docs/tutorials/
- LangChain 支持的第三方集成：https://python.langchain.com/docs/integrations/providers/all/
- Gemini 支持的所有模型：https://ai.google.dev/gemini-api/docs/models?hl=zh-cn