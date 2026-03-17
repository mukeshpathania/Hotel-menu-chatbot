# 🍽️ Hotel Menu Chatbot (Flask + Python)

<p align="center">
A simple AI-style chatbot that helps users browse a restaurant menu and place orders online.
</p>

---

## 📌 Project Overview

The **Hotel Menu Chatbot** is a Python web application built using **Flask** that allows users to interact with a chatbot to:

- View restaurant menu categories
- Browse menu items
- Add items to an order
- Provide delivery details

The chatbot reads menu data from a **JSON file** and dynamically displays menu options through a simple web interface.

---

## 🚀 Features

- 💬 Interactive chatbot interface  
- 📋 Displays menu categories and items  
- 🛒 Add items to order cart  
- 📍 Collects delivery location  
- 📞 Collects phone number for order confirmation  
- ⚡ Lightweight Flask web application  

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Backend logic |
| Flask | Web framework |
| HTML | Frontend interface |
| CSS | Styling |
| JSON | Menu data storage |

---

## 📂 Project Structure

```
Hotel-menu-chatbot/
│
├── main.py              # Flask backend
├── menu.json            # Menu data
│
├── templates/
│   └── index.html       # Chatbot UI
│
├── static/
│   └── style.css        # Styling
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/hotel-menu-chatbot.git
cd hotel-menu-chatbot
```

### 2️⃣ Install required packages

```
pip install flask
```

---

## ▶️ Run the Application

Run the Flask server:

```
python main.py
```

Then open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 💡 How It Works

1. The chatbot loads menu data from **menu.json**.
2. Users type commands in the chatbot interface.
3. The bot shows:
   - Menu categories
   - Food items
4. Users can add items to their cart.
5. The bot collects delivery details (location & phone number).
6. Order confirmation is displayed.

---

## 📸 Example Interaction

```
User: Show menu

Bot:
1. Starters
2. Main Course
3. Drinks

User: Main Course

Bot:
Paneer Butter Masala
Dal Makhani
Veg Biryani
```

---

## 🔮 Future Improvements

- 🤖 Add NLP using AI chatbot models  
- 💳 Add online payment integration  
- 📱 Mobile responsive UI  
- 🧾 Order history feature  
- 🔐 User authentication  

---

## 👨‍💻 Author

**Mukesh Pathania**  
MCA Student | Python Developer

---

⭐ If you like this project, consider giving it a **star on GitHub**!
