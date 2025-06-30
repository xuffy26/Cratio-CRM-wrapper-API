# 📘 Codeyoung CRM Wrapper API (Django + DRF)

---

## ✅ Project Overview

This project provides a **Django REST API wrapper** for sending lead data to the **Cratio CRM API** (used by Codeyoung) using a simplified POST structure.

---

## 🚀 Features

- Accepts clean JSON POST request at a single endpoint
- Converts it into the required Cratio CRM format
- Forwards the request to Cratio's API
- Returns Cratio's response back to the caller
- Deployable on [Render](https://render.com)

---

## 🔧 Tech Stack

- Python 3.11+
- Django 5.x
- Django REST Framework
- Gunicorn (for Render deployment)

---

## 📁 Folder Structure

```
codeyoung_project/
│
├── codeyoung_api/
│   ├── __init__.py
│   ├── urls.py            ← DRF route
│   └── views.py           ← API logic
│
├── codeyoung_project/
│   ├── __init__.py
│   ├── settings.py        ← Add ALLOWED_HOSTS
│   ├── urls.py            ← Include app routes
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md              ← (this file)
```

---

## ✅ Step-by-Step Setup (Local)

### 1. Clone the Repo

```bash
git clone https://github.com/xuffy26/Cratio-CRM-wrapper-API.git
cd Cratio-CRM-wrapper-API
```

### 2. Create Virtual Environment

```bash
python -m venv codeyoung_env
codeyoung_env\Scripts\activate     # On Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Migrate DB

```bash
python manage.py migrate
```

### 5. Run Locally

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/send-codeyoung-lead/

---

## 🔄 API Usage

### ✅ Endpoint

```
POST /send-codeyoung-lead/
Content-Type: application/json
```

### 🔽 Sample Request (cURL)

```bash
curl --location 'https://cratio-crm-wrapper-api.onrender.com/send-codeyoung-lead/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "First Name": "Subbu1",
  "Phone Number": "9488776652",
  "Email": "te22@gmail.com",
  "Lead Date": "2023-06-20",
  "Preferred Course": "Coding",
  "Assigned To": "Anu Raj"
}'
```

---

## 🌐 Deployment on Render

### ✅ Render Settings

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn codeyoung_project.wsgi:application`
- **Python Version:** 3.11+
- **Environment Variables:** (Optional) None required for now

### ✅ `ALLOWED_HOSTS` in `settings.py`

```python
ALLOWED_HOSTS = ['cratio-crm-wrapper-api.onrender.com', 'localhost', '127.0.0.1']
```

---

## 🔁 Updating the Repo

### Push local code to GitHub

```bash
git add README.md
git commit -m "Added complete README"
git push origin master
```

---

## ✅ Example Response

```json
{
  "status": 200,
  "response": {
    "result": "success",
    "message": "Record added successfully"
  }
}
```

---

## 🧑‍💻 Maintainer

- **Author**: Nizarudeen
- **Organization**: Chat360
