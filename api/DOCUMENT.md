# 📘 Hook Hack Internal API Docs

This document describes the internal API hosted at https://api.hook-hack.com.  
All endpoints accept POST requests with JSON-formatted payloads.

---

## ✅ Common Settings

- Base URL: https://api.hook-hack.com
- Method: POST
- Content-Type: application/json
- Auth: None (internal use)

### General Request Format

{
  "input": {
    "demo": true,
    ...
  }
}

---

## 🔍 /scrape-list

Description:  
Returns a list of TikTok ad videos. If "demo" is true, mock data is returned.

Endpoint:  
POST /scrape-list

Request Example:

{
  "input": {
    "demo": true,
    "searchword": "cosmetics",
    "amount": 10
  }
}

Response Example (demo=true):

{
  "success": true,
  "data": [
    {
      "url": "https://www.tiktok.com/@example/video/123",
      "like": 389000,
      "number": 1
    },
    ...
  ]
}

---

## 🔍 /scrape-indivisual

Description:  
Returns detailed comment and stat data from a single TikTok video.

Endpoint:  
POST /scrape-indivisual

Request Example:

{
  "input": {
    "demo": true,
    "url": "https://www.tiktok.com/@example/video/123",
    "amount": 10
  }
}

Response Example (demo=true):

{
  "success": true,
  "data": {
    "comments": [
      {
        "name": "User A",
        "like": 1000,
        "text": "Sample comment",
        "number": 1
      },
      ...
    ],
    "datas": {
      "likes": 389000,
      "comments": 2164,
      "saves": 47800,
      "shares": 4479
    }
  }
}

---

## 🧠 /generate-hook

Description:  
Generates a TikTok "hook" structure idea.

Endpoint:  
POST /generate-hook

Request Example:

{
  "input": {
    "demo": true,
    "searchword": "pores"
  }
}

Response Example (demo=true):

{
  "success": true,
  "data": "This is a DEMO DATA."
}

---

## 🧠 /generate-content

Description:  
Generates advertising content concepts or prompt structures.

Endpoint:  
POST /generate-content

Request Example:

{
  "input": {
    "demo": true,
    "keyword": "glow skin"
  }
}

Response Example (demo=true):

{
  "success": true,
  "data": "This is a DEMO DATA."
}

---

## 🛠 Error Response Format (common)

{
  "success": false,
  "error": "error message here"
}

---

## 🔐 Swagger UI (for testing)

https://api.hook-hack.com/docs  
→ Interactive UI for testing endpoints (internal only recommended)

---

## 📝 Notes

- Set "demo": true to test without triggering actual scraping or generation
- In production mode, each endpoint executes run_flow() logic from submodules

---