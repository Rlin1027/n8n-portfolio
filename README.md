# n8n Portfolio

## 🚀 Projects

| # | Project | Core Value & Use Cases | Domain Knowledge & Tech Stack |
|---|---------|------------------------|-------------------------------|
| 01 | [Sentiment Analysis](./01-sentiment-analysis) | **自動化情緒監測**<br>• 電商評論監控 (Reviews)<br>• 員工滿意度調查 (HR)<br>• 社群品牌聲量分析 | **NLP & API Integration**<br>• OpenAI (Prompt Engineering)<br>• Google Sheets API<br>• Webhook Handling |
| 02 | [Slack AI Chatbot](./02-slack-ai-chatbot) | **企業內部全能助手**<br>• IT Helpdesk 第一線支援<br>• 新員工 Onboarding 助手<br>• 業務知識庫查詢 | **Conversational AI & Bot Frameworks**<br>• LangChain Agents (Memory/Tools)<br>• Slack App Configuration (Events/Scopes)<br>• RAG Concepts |
| 03 | [WordPress AI Chatbot](./03-wordpress-ai-chatbot) | **網站內容活化 (RAG)**<br>• SaaS 產品文件助手<br>• 部落格/新聞站智慧導讀<br>• 電商選購顧問 | **RAG & Vector Databases**<br>• Vector Embeddings (Supabase pgvector)<br>• Web Scraping / Content Ingestion<br>• WordPress REST API |
| 04 | [Telegram AI Assistant](./04-telegram-ai-assistant) | **行動優先生產力工具**<br>• 語音筆記轉行動清單<br>• 語言學習陪練 (Voice Interaction)<br>• 現場工程查驗語音報告 | **Audio Processing & Messaging APIs**<br>• OpenAI Whisper (Speech-to-Text)<br>• Telegram Bot API (Webhooks)<br>• Multi-modal Interaction (Voice/Text) |
| 05 | [PostgreSQL AI Agent](./05-postgresql-ai-agent) | **數據秘書 (Text-to-SQL)**<br>• 主管營收即時查詢<br>• 庫存即時查詢系統<br>• 客服訂單狀態快查 | **Database & SQL**<br>• Relational Database Schemas (SQL)<br>• LLM Function Calling<br>• Prompt Engineering for SQL Generation |
| 06 | [Database AI Chat](./06-database-ai-chat) | **對話式資料庫介面**<br>• 複雜關聯查詢簡化<br>• 資料庫結構探索<br>• 非技術人員數據獲取 | **Advanced SQL & Schema Awareness**<br>• Database Metadata Management<br>• Context Awareness (Schema Context)<br>• Natural Language Understanding |
| 07 | [SQL Agent Visualization](./07-sql-agent-visualization) | **自動化數據視覺化**<br>• 自動化週報圖表生成<br>• 銷售業績圓餅圖/折線圖<br>• 異常數據視覺化警示 | **Data Visualization & Structured Output**<br>• JSON Structured Outputs<br>• Charting Libraries/APIs (QuickChart.io)<br>• Data Aggregation & Formatting |
| 08 | [GitLab Code Review](./08-gitlab-code-review) | **代碼品質守門員**<br>• 初級代碼審查與風格建議<br>• 資安漏洞預警 (Hard-coded secrets)<br>• Documentation 強制執行 | **DevOps & CI/CD**<br>• Git Version Control Flows (MR/PR)<br>• Static Code Analysis Concepts<br>• Webhook Security & Payload Parsing |
| 09 | [Notion Vector RAG](./09-notion-vector-rag) | **企業第二大腦搜尋**<br>• 公司 SOP 智能問答<br>• 專案歷史決策回溯<br>• 個人知識庫靈感助手 | **Knowledge Management & RAG**<br>• Notion API (Block/Page Structure)<br>• Recursive Text Splitting<br>• Vector Similarity Search |
| 10 | [NocoDB Data Analyst](./10-nocodb-data-analyst) | **輕量級資料庫分析師**<br>• 活動報名名單客群分析<br>• CRM 客戶分群與再行銷<br>• 產品庫存智慧盤點建議 | **Low-Code Databases & Data Analysis**<br>• NocoDB/Airtable API Interactions<br>• Data Cleaning & Analysis Patterns<br>• Schema Discovery |

## 🔧 Quick Start

1. Deploy n8n to [Zeabur](https://zeabur.com) or run locally
2. Set up environment variables (see [credentials-guide.md](./credentials-guide.md))
3. Import any `workflow.json` into your n8n instance
4. Configure the required credentials using standardized names

## 🔑 Required Credentials

| Credential Name | Type | Used By |
|-----------------|------|---------|
| `OpenAI Account` | OpenAI API | All projects |
| `Supabase Account` | Supabase | 01, 03, 05, 09 |
| `Slack Account` | Slack API | 02 |
| `Telegram Account` | Telegram | 04 |
| `Google Sheets Account` | Google API | 01 |
| `GitLab Account` | GitLab API | 08 |
| `Postgres Account` | PostgreSQL | 05, 06, 07 |
| `NocoDB Account` | NocoDB API | 10 |

## 📁 Project Structure

```
n8n-portfolio/
├── README.md
├── .env.example
├── credentials-guide.md
└── [01-10]-*/
    ├── workflow.json
    ├── README.md
    └── demo.gif
```

## 🌐 Deployment

This portfolio is designed for [Zeabur](https://zeabur.com) deployment. See [zeabur-deployment-guide.md](./zeabur-deployment-guide.md) for details.

## 📜 License

MIT License
