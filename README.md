# 🎓 CSVTU Student Portal (Flask)

A Flask-based web application that helps CSVTU students quickly access **official semester results and admit cards** by redirecting them to the DigiVarsity portal using validated inputs.

> ⚠️ This application does **not store, fetch, or modify any student data**.  
> It only redirects users to the **official CSVTU DigiVarsity website**.

---

## ✨ Features

- 🔢 12-digit roll number validation
- 📄 Redirect to **Semester Results**
- 🪪 Redirect to **Admit Cards**
- 🎯 Supports **Regular, RTRV, and Backlog** exam types
- 📚 Semester and Exam Session selection
- 🔐 DigiVarsity login requirement notice
- 🖥️ Clean, responsive UI
- ⚡ Lightweight Flask backend

---

## 🔐 Important Notice (DigiVarsity Login Required)

> 🔑 **Users must log in to the DigiVarsity portal first** before accessing results or admit cards.  
> If the user is not logged in, DigiVarsity will automatically redirect to the login page.

🔗 DigiVarsity Login:  
https://csvtu.digivarsity.online

---

## 🛠️ Tech Stack

- **Python (Flask)** – Backend routing & validation
- **HTML5 + CSS3** – Frontend UI
- **Jinja2** – Templating engine
- **CSVTU DigiVarsity Portal** – Official data source (redirect only)

---

## 📂 Project Structure

```text
├── app.py
├── templates/
│   └── index.html
├── README.md

---