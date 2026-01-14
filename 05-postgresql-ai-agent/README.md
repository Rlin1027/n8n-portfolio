# 05 - PostgreSQL AI Agent

Chat with your PostgreSQL/Supabase database using natural language queries.

## Demo

![Demo](./demo.gif)

## Overview

```mermaid
graph LR
    A[User Question] --> B[AI Agent]
    C[OpenAI] --> B
    D[Postgres Tool] --> B
    B --> E[SQL Query]
    E --> F[Database]
    F --> G[Natural Language Response]
```

**Features:**
- Natural language to SQL conversion
- Automatic schema discovery
- JSON data extraction and summarization
- Conversational interface

## Required Credentials

| Credential Name | Type | Purpose |
|-----------------|------|---------|
| `OpenAI Account` | OpenAI API | Query generation |
| `Postgres Account` | PostgreSQL | Database access |

## Quick Start

1. **Import workflow** into n8n
2. **Set up credentials**:
   - `OpenAI Account`
   - `Postgres Account`
3. **Activate** the workflow
4. **Ask questions** like:
   - "What tables are available?"
   - "Show me top 10 customers by revenue"

## Technologies

- LangChain AI Agent
- OpenAI GPT-4
- PostgreSQL Tool
- Supabase (optional)
