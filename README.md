# 📝 Django To-Do App

A simple and responsive To-Do web application built using **Django**, **HTML**, and **CSS**.  
Users can register, log in, and manage their personal tasks with full CRUD operations.

---

## 🚀 Features

- User Registration & Login
- Secure Authentication System
- Create Tasks
- View Task List
- Update Tasks
- Delete Tasks
- User-specific To-Do Lists
- Responsive Design

---

## 🛠 Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Authentication:** Django Built-in Auth

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install django
```

---

## 🗄 Database Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication Pages

- Register → `/register/`
- Login → `/login/`
- Logout → `/logout/`

---

## 📸 Screenshots

Add screenshots inside a `screenshots` folder and reference them:

```markdown
![Home](screenshots/home.png)
![Login](screenshots/login.png)
![Tasks](screenshots/tasks.png)
```

---

## 📌 Future Improvements

- Task deadlines & reminders
- Task categories
- Priority levels
- Search & filter
- REST API version

---

## 👩‍💻 Author

**Sama Mohamed**  
Computer Science Student  

---

## Live Demo
https://samaian.pythonanywhere.com/
