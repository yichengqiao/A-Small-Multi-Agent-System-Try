# Multi-Agent System for Query Processing

## Overview

This project demonstrates a **Multi-Agent System (MAS)** designed to process user queries by delegating tasks to specialized agents. Each agent performs a specific role, from understanding the query to retrieving relevant information and synthesizing an answer.

The system uses **Flask** to provide a web-based user interface for interaction. It integrates **Natural Language Processing (NLP)** and **API calls** for intelligent query processing and information retrieval.

---

## Features

- **Task Manager Agent**: Orchestrates the workflow by delegating tasks to other agents.
- **Question Understanding Agent**: Analyzes the user's query to extract intent and keywords using NLP.
- **Information Retrieval Agent**: Fetches relevant data from Wikipedia API based on the keywords.
- **Answer Synthesis Agent**: Combines retrieved data into a coherent and user-friendly response.
- **Web Interface**: Simple and intuitive Flask-based interface for user interaction.

---

## Project Structure

```plaintext
multi_agent_system/
│
├── app.py                        # Main Flask application
├── task_manager_agent.py         # Task Manager Agent implementation
├── question_understanding_agent.py # NLP-based Question Understanding Agent
├── information_retrieval_agent.py  # Wikipedia API-based Retrieval Agent
├── answer_synthesis_agent.py       # Agent for synthesizing the final response
├── requirements.txt              # Python dependencies
├── Procfile                      # Heroku process configuration file
├── runtime.txt                   # Specifies Python runtime version
├── templates/
│   └── index.html                # Web interface template
└── README.md                     # Project documentation
```

---

## Installation

Follow these steps to set up and run the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/multi-agent-system.git
cd multi-agent-system
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\\Scripts\\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download spaCy Language Model
The project uses `spaCy` for natural language processing. Download the required language model:
```bash
python -m spacy download en_core_web_sm
```

### 5. Run the Application
Start the Flask development server:
```bash
python app.py
```

### 6. Access the Web Interface
Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

---

## Usage

1. Enter a query into the text box on the web interface.
   - Example: `What are the key features of Python?`
2. Submit the query to trigger the system.
3. View:
   - **Query Analysis**: Intent and extracted keywords.
   - **Retrieved Information**: Relevant articles and summaries.
   - **Final Answer**: Synthesized response combining all data.

---

## Deployment

### Deploying to Heroku

1. Install Heroku CLI: [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli).
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a new app:
   ```bash
   heroku create
   ```
4. Push the project to Heroku:
   ```bash
   git push heroku main
   ```
5. Open the deployed application:
   ```bash
   heroku open
   ```

---

## Examples

### Example Query
**Input**: `What is Python used for?`

**Output**:
- **Intent**: Informational
- **Keywords**: Python, used
- **Retrieved Information**:
  1. Python (programming language): Python is a high-level, interpreted language used for general-purpose programming. (Link)
- **Final Answer**: Python is a high-level, interpreted language used for general-purpose programming.

---

## Technologies Used

- **Python**: Core language for development.
- **Flask**: Web framework for building the interface.
- **spaCy**: For natural language processing.
- **Wikipedia API**: For retrieving data.

---

## Contribution

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`feature/my-feature`).
3. Commit your changes.
4. Push to the branch.
5. Create a Pull Request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments

- [spaCy](https://spacy.io/) for NLP.
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) for data retrieval.
- Flask for building the web application.

---

## Contact

For any queries or issues, feel free to open an issue in the repository or contact the maintainer at [yichengqiao21@gmail.com].


---
### Multi-Agent System 项目 GitHub 中文版 README

以下是项目的中文版本 README，适合放在 GitHub 项目中，帮助中文用户理解和使用该项目。

---

# 多智能体系统查询处理

## 项目概述

该项目展示了一个基于 **多智能体系统 (Multi-Agent System, MAS)** 的智能查询处理系统。通过将任务分配给不同的专用智能体，系统能够分解复杂任务并高效完成。每个智能体负责特定的角色，例如分析问题、检索信息和合成答案。

系统使用 **Flask** 提供基于网页的用户界面，并集成了 **自然语言处理 (NLP)** 和 **API 调用** 以实现智能化的查询处理。

---

## 功能特色

- **任务管理智能体 (Task Manager Agent)**：负责协调各智能体，管理任务流。
- **问题理解智能体 (Question Understanding Agent)**：通过 NLP 分析用户的查询，提取意图和关键词。
- **信息检索智能体 (Information Retrieval Agent)**：基于关键词调用 Wikipedia API 检索相关信息。
- **答案合成智能体 (Answer Synthesis Agent)**：将检索到的信息整理为用户友好的答案。
- **网页界面**：基于 Flask 的简单交互式界面，方便用户使用。

---

## 项目结构

```plaintext
multi_agent_system/
│
├── app.py                        # Flask 应用主文件
├── task_manager_agent.py         # 任务管理智能体
├── question_understanding_agent.py # NLP 问题理解智能体
├── information_retrieval_agent.py  # Wikipedia API 信息检索智能体
├── answer_synthesis_agent.py       # 答案合成智能体
├── requirements.txt              # Python 依赖库
├── Procfile                      # Heroku 部署配置文件
├── runtime.txt                   # 指定 Python 运行版本
├── templates/
│   └── index.html                # 网页界面 HTML 模板
└── README.md                     # 项目文档
```

---

## 安装步骤

按照以下步骤在本地运行项目：

### 1. 克隆仓库
```bash
git clone https://github.com/your-username/multi-agent-system.git
cd multi-agent-system
```

### 2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate   # Windows 上运行: venv\\Scripts\\activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 下载 spaCy 语言模型
本项目使用 `spaCy` 进行自然语言处理。下载所需的语言模型：
```bash
python -m spacy download en_core_web_sm
```

### 5. 运行应用程序
启动 Flask 开发服务器：
```bash
python app.py
```

### 6. 访问网页界面
打开浏览器，访问：
```
http://127.0.0.1:5000/
```

---

## 使用说明

1. 在网页界面的文本框中输入查询问题。
   - 示例：`What are the key features of Python?`
2. 提交问题，触发系统运行。
3. 查看以下结果：
   - **查询分析**：提取的意图和关键词。
   - **检索信息**：与查询相关的文章和摘要。
   - **最终答案**：合成后的综合答案。

---

## 部署指南

### 部署到 Heroku

1. 安装 Heroku CLI：[Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)。
2. 登录 Heroku：
   ```bash
   heroku login
   ```
3. 创建一个新的 Heroku 应用：
   ```bash
   heroku create
   ```
4. 推送项目到 Heroku：
   ```bash
   git push heroku main
   ```
5. 打开已部署的应用程序：
   ```bash
   heroku open
   ```

---

## 示例

### 示例查询
**输入**：`What is Python used for?`

**输出**：
- **意图**：信息性 (Informational)
- **关键词**：Python, used
- **检索信息**：
  1. Python (programming language): Python 是一种高级解释型语言，广泛用于通用编程。（链接）
- **最终答案**：Python 是一种高级解释型语言，广泛用于通用编程。

---

## 技术栈

- **Python**：开发的核心语言。
- **Flask**：构建网页界面的 Web 框架。
- **spaCy**：用于自然语言处理。
- **Wikipedia API**：用于检索数据。

---

## 如何贡献

欢迎贡献代码或建议！请按照以下步骤：
1. Fork 本仓库。
2. 创建一个新分支（`feature/my-feature`）。
3. 提交修改。
4. 推送到分支。
5. 创建 Pull Request。

---

## 许可证

本项目基于 MIT 许可证发布。详细信息请参见 `LICENSE` 文件。

---

## 致谢

- [spaCy](https://spacy.io/) 提供的自然语言处理功能。
- [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) 用于数据检索。
- Flask 提供的 Web 应用支持。

---

## 联系方式

如有任何问题或建议，请通过 GitHub Issues 提交，或联系维护者：[yichengqiao21@gmail.com]。
```

---

