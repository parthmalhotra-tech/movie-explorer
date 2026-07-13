# 🎬 Movie Explorer

Movie Explorer is a full-stack web application built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL** that allows users to search movies, view detailed information, and maintain a personalized watchlist.

🌐 **Live Demo:** https://movie-explorer-snu5.onrender.com/

---

## ✨ Features

- 🔐 User Authentication (Sign Up, Login, Logout)
- 🚀 Automatic login after signup
- 👤 User Profile Page
- 🎥 Search and browse movies
- 📄 View detailed movie information
- ⭐ Personalized watchlist
- 🔒 Session-based authentication
- 🗄️ PostgreSQL database with Supabase
- 📱 Responsive design

---

## 🛠️ Tech Stack

**Backend**
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL (Supabase)
- SQLite (Local Development)

**Frontend**
- HTML
- CSS
- Jinja2 Templates

**Deployment**
- Render

---

## 📂 Project Structure

```text
movie-explorer/
│
├── app.py
├── database.py
├── models.py
├── crud.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── main_page.html
│   ├── movie_details.html
│   ├── login.html
│   ├── signup.html
│   ├── profile.html
│   └── watchlist.html
│
└── static/
    └── css/
        ├── main_page.css
        ├── movie_details.css
        ├── login.css
        ├── signup.css
        ├── profile.css
        └── watchlist.css
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/movie-explorer.git
cd movie-explorer
pip install -r requirements.txt
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🗄️ Database

- SQLite for local development
- PostgreSQL (Supabase) for production deployment

---

## 🎯 Future Improvements

- 🔒 Password hashing using bcrypt
- 🎭 Search movies by genre
- 🔍 Search suggestions and autocomplete
- 📄 Pagination
- ⭐ Ratings and reviews
- 🎬 Movie recommendation system
- 🌙 Dark/Light mode

---

## 👨‍💻 Author

**Parth Malhotra**

LinkedIn: www.linkedin.com/in/parth-malhotra07092007
GitHub: https://github.com/parthmalhotra-tech
