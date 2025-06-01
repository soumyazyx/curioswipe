# 🧱 CurioSwipe – Tech Stack Overview

CurioSwipe is a mobile application that delivers swipeable, curiosity-driven topics (randomized or interest-based), optionally with text-to-speech audio playback. Designed to be used while commuting — even with Android Auto — it's a "snackable curiosity companion" built for modern users.

---

## ✅ Project Summary

| Component     | Description                                     |
|---------------|-------------------------------------------------|
| **Goal**      | Deliver engaging, short topics on swipe         |
| **Extras**    | Audio playback, interest curation, geo-aware    |
| **Modes**     | Swipeable cards, hands-free via Android Auto    |

---

## 🔹 Backend

- **Framework**: [Django](https://www.djangoproject.com/)  
- **API Layer**: Django REST Framework (DRF)  
- **Language**: Python  
- **Key Features**:
  - Admin dashboard out of the box
  - Token-auth-enabled API endpoints
  - ORM for easy DB access

---

## 🔹 Database

- **Engine**: Oracle Autonomous Database (ADB)
- **Schemas**:
  - `curioswipe_dev` – development and testing
  - `curioswipe_prod` – production usage
- **Driver**: [`oracledb`](https://pypi.org/project/oracledb/) (preferred) or `cx_Oracle`
- **Why Oracle?**:
  - Already in use (e.g., trivia app)
  - High performance
  - Avoids SQLite/PostgreSQL switching

---

## 🔹 Hosting

- **Cloud Provider**: Oracle Cloud Infrastructure (OCI)
- **Environment**:
  - ARM-based Compute instance (Ubuntu)
  - Oracle ADB integrated
- **Deployment Plan**:
  - Local testing using Django dev server
  - Future move to `gunicorn + nginx` for production

---

## 🔹 Android Mobile App

- **Language**: Kotlin
- **UI Framework**: Jetpack Compose
- **Networking**: Retrofit or Ktor
- **Audio**: Android Text-to-Speech (TTS)
- **Key Goals**:
  - Swipeable UI for topics
  - Interest selection screen
  - Android Auto compatibility (voice playback mode)

---

## 🔸 Optional Future Enhancements

- **Personalization**:
  - User interest categories
  - Geo-location relevance
  - Context-aware curation
- **External Content Sources**:
  - Wikipedia / Wikidata
  - News APIs
  - OpenAI APIs (for summarization or generation)
- **Analytics**: Basic usage tracking

---

## 📂 Repo Structure (upcoming)
```
curioswipe/
│
├── backend/ # Django project
│ ├── curioswipe/ # Core Django app
│ └── requirements.txt # Python dependencies
│
├── mobile/ # Android app (Jetpack Compose)
│ ├── app/ # Kotlin source code
│ └── build.gradle # Gradle config
│
├── docs/ # Documentation
│ └── tech-stack.md # This file
│
└── README.md
```

---

## 🛠️ Next Steps

1. Scaffold Django backend connected to `curioswipe_dev` schema
2. Build a basic `/api/topic/` endpoint
3. Set up Android app skeleton with swipe + TTS playback
4. Integrate both systems for first E2E test

---

