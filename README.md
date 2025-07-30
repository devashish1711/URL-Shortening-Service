# 🔗 URL Shortening Service

A simple RESTful API built with **Flask** that allows users to shorten long URLs. The API supports full **CRUD operations**, tracks the number of times each short URL is accessed, and stores data using **SQLite**.

---

## 🚀 Features

- ✅ Shorten long URLs
- 📥 Retrieve original URLs from short codes
- ✏️ Update shortened URLs
- ❌ Delete short URLs
- 📊 Get access statistics (click count)

---

## 🧪 API Endpoints

### ➕ Create Short URL

**POST** `/shorten`

**Request:**
```json
{
  "url": "https://www.example.com/some/long/url"
````

**Response:**

```json
{
  "url": "https://www.example.com/some/long/url",
  "shortCode": "AbC123",
  "createdAt": "2025-07-30T12:00:00Z",
  "updatedAt": "2025-07-30T12:00:00Z"
}
```

---

### 📥 Retrieve Original URL

**GET** `/shorten/<shortCode>`

Example:
`GET /shorten/AbC123`

**Response:**

```json
{
  "url": "https://www.example.com/some/long/url"
}
```

---

### 🔁 Update Short URL

**PUT** `/shorten/<shortCode>`

**Request:**

```json
{
  "url": "https://www.example.com/updated/url"
}
```

**Response:**

```json
{
  "url": "https://www.example.com/updated/url",
  "shortCode": "AbC123",
  "updatedAt": "2025-07-30T12:30:00Z"
}
```

---

### ❌ Delete Short URL

**DELETE** `/shorten/<shortCode>`

**Response:**
`204 No Content`

---

### 📊 Get URL Statistics

**GET** `/shorten/<shortCode>/stats`

**Response:**

```json
{
  "url": "https://www.example.com",
  "shortCode": "AbC123",
  "createdAt": "2025-07-30T12:00:00Z",
  "updatedAt": "2025-07-30T12:30:00Z",
  "accessCount": 5
}
```

---

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Database**: SQLite
* **API Testing**: curl, Postman

---

## 🧑‍💻 Setup Instructions

Follow these steps to run the project locally:

### 1. Clone the repository

```bash
git clone https://github.com/devashish1711/URL-Shortening-Service.git
cd URL-Shortening-Service
```

### 2. Create a virtual environment

```bash
python -m venv venv
# On Windows
source venv/Scripts/activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask server

```bash
python app.py
```

The app will run at:
📍 `http://127.0.0.1:5000`

---

✅ Built with ❤️ by [@devashish1711](https://github.com/devashish1711)

