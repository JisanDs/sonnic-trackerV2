# 💰 Sonnic Tracker v2

A simple yet powerful **command-line based personal finance tracker** built with Python.  
Helps you **track your savings**, **set daily goals**, and **monitor your progress** toward a financial target.

---

## 🆚 What's New in v2 (Compared to Sonnic Tracker v1)

> Major improvements from version 1 ➡ version 2:

✅ **Login system** added (with session memory)  
✅ **Daily and total saving goals** support  
✅ **Dashboard view**: Shows deposit, withdrawal, days tracked  
✅ **Withdrawal option** with optional notes  
✅ **Password change system** added  
✅ **Logout and re-login support**  
✅ **Cleaner code and structured storage** (per-user transaction file)  
✅ Improved **error handling** and **user input validation**

> 📌 v1 was only capable of deposit tracking without login, session, or dashboard.

---

## ✨ Features

- 👤 User Registration & Login (with session auto-login)
- 🔐 Password Management (Change Password)
- 💸 Track Deposits & Withdrawals with optional notes
- 📈 Dashboard Summary: total saved, days saved, deposits, withdrawals
- 📜 View transaction history (deposit/withdraw/full)
- 🎯 Set personal saving goals (daily and total target)
- 🔓 Logout & Secure Session Handling
- 🗃️ Data stored locally (JSON & TXT)

---

## 📂 File Structure

```
Sonnic-Tracker/
│
├── users.json          # User info (username, password, goal, target)
├── session.txt         # Keeps track of logged-in user
├── data/               # Individual user transaction files
│   └── yourname.txt    # Format: action,amount,date,note
├── sonnic_tracker.py   # Main application script
└── README.md           # You're reading it 😄
```

---

## 🚀 How to Run

1. **Clone or Download** the repo:

```bash
git clone https://github.com/yourusername/sonnic-tracker.git
cd sonnic-tracker
```

2. **Run the App:**

```bash
python sonnic_tracker.py
```

No additional libraries required — just **pure Python** 🐍.

---

## 🛠️ Requirements

- Python 3.x
- Runs on Windows, Linux, or macOS terminal

---

## 📌 Usage Flow

```
1️⃣ Register
2️⃣ Set daily saving goal & target
3️⃣ Login
4️⃣ Start saving (Deposit)
5️⃣ Withdraw when needed (optional note)
6️⃣ View dashboard to monitor progress
7️⃣ Logout when done
```

---

## 🧠 Example Transaction File

```
deposit,100,2025-06-10,
withdraw,50,2025-06-11,Emergency
deposit,150,2025-06-12,
```

---

## 📊 Future Improvements (Suggestions)

- GUI version using Tkinter or PyQt
- Export report as PDF or Excel
- Password masking using `getpass`
- Unique day tracking on dashboard
- Multi-language support (e.g., বাংলা 🇧🇩)

---

## 🤝 Author

**Jisan Shadowmoor**  
🔥 Learner | 🧠 Problem Solver | 💻 Python Enthusiast  
[Email me](mailto:mdjisan01823jis@gmail.com)

---

## 🪪 License

This project is open-source and free to use for personal or educational purposes.