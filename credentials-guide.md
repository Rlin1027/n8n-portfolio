# n8n Credentials Setup Guide

This guide explains how to set up credentials for all workflows in this portfolio.

## Environment Variables for Zeabur

Set these in your Zeabur dashboard under **Variables**:

```env
# OpenAI (Required for all projects)
OPENAI_API_KEY=sk-xxx

# Supabase (Projects: 01, 03, 05, 09)
SUPABASE_URL=https://xxx.supabase.co
SUPABASE_ANON_KEY=eyJxxx
SUPABASE_SERVICE_KEY=eyJxxx

# Slack (Project: 02)
SLACK_BOT_TOKEN=xoxb-xxx
SLACK_SIGNING_SECRET=xxx

# Telegram (Project: 04)
TELEGRAM_BOT_TOKEN=123456:ABC-xxx

# Google (Project: 01)
GOOGLE_SHEETS_CREDENTIALS={"type":"service_account",...}

# GitLab (Project: 08)
GITLAB_ACCESS_TOKEN=glpat-xxx

# NocoDB (Project: 10)
NOCODB_API_KEY=xxx
NOCODB_BASE_URL=https://xxx
```

## n8n Credential Names

Create these credentials in n8n with the exact names below:

| Credential Name | Type | How to Get |
|-----------------|------|------------|
| `OpenAI Account` | OpenAI API | [platform.openai.com](https://platform.openai.com/api-keys) |
| `Supabase Account` | Supabase API | Project Settings → API |
| `Slack Account` | Slack API | [api.slack.com](https://api.slack.com/apps) |
| `Telegram Account` | Telegram API | Talk to [@BotFather](https://t.me/BotFather) |
| `Google Sheets Account` | Google Service Account | [console.cloud.google.com](https://console.cloud.google.com) |
| `GitLab Account` | GitLab API | Settings → Access Tokens |
| `Postgres Account` | PostgreSQL | Your database connection |
| `NocoDB Account` | NocoDB API | NocoDB Settings → API Tokens |

## Step-by-Step: OpenAI Setup

1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Click **Create new secret key**
3. Copy the key (starts with `sk-`)
4. In n8n: **Credentials** → **New** → **OpenAI API**
5. Name it exactly: `OpenAI Account`
6. Paste your API key and save

## Step-by-Step: Supabase Setup

1. Create a project at [supabase.com](https://supabase.com)
2. Go to **Project Settings** → **API**
3. Copy: URL, anon key, service_role key
4. In n8n: **Credentials** → **New** → **Supabase API**
5. Name it: `Supabase Account`
6. Enter URL and service_role key

## Step-by-Step: Slack Bot Setup

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Click **Create New App** → **From scratch**
3. Add OAuth Scopes: `chat:write`, `app_mentions:read`, `channels:history`
4. Install to workspace and copy **Bot User OAuth Token**
5. In n8n: Create credential named `Slack Account`

## Step-by-Step: Telegram Bot Setup

1. Open Telegram, search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` and follow prompts
3. Copy the token (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)
4. In n8n: Create credential named `Telegram Account`
