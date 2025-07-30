# 🔗 URL Shortening Service

A simple RESTful API built with **Flask** to shorten long URLs, track access stats, and support CRUD operations on short links.

---

## 🚀 Features

- ✅ Create short URLs from long links
- 🔍 Retrieve original URL from a shortcode
- ✏️ Update existing short URLs
- ❌ Delete short URLs
- 📊 Track access statistics (access count, created/updated timestamps)

---

## 📦 Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite
- **Dependencies**: Flask, sqlite3

---

## 📚 API Endpoints

### ➕ Create Short URL

**POST** `/shorten`

**Request Body**:
```json
{
  "url": "https://www.example.com/some/long/url"
}
