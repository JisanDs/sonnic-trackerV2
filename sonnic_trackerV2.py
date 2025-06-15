import datetime
import os
import json

# ===== File Paths =====
USERS_FILE = "users.json"
SESSION_FILE = "session.txt"
DATA_DIR = "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# ===== Helper Functions =====
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

def get_data_file(name):
    return os.path.join(DATA_DIR, f"{name}.txt")

# ===== Register =====
def register_user():
    users = load_users()
    name = input("Enter your name: ")
    if name in users:
        print("User already exists. Try logging in.\n")
        return
    
    password = input("Set your password: ")
    per_day = input("Daily saving goal (৳): ")
    target = input("Total target (৳): ")

    users[name] = {"password": password, "per_day": per_day, "target": target}
    save_users(users)
    print(f"\nRegistration successful, {name}!\n")

# ===== Login =====
def login_user():
    users = load_users()
    name = input("Enter your name: ")
    password = input("Enter your password: ")

    if name in users and users[name]["password"] == password:
        with open(SESSION_FILE, "w") as f:
            f.write(name)
        print(f"\nWelcome back, {name}!")
        user_session(name, users[name])
    else:
        print("Login failed. Incorrect name or password.\n")

# ===== Session Handling =====
def get_logged_in_user():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            return f.read().strip()
    return None

def logout_user():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    print("Logged out successfully.\n")

# ===== Transaction =====
def get_current_balance(name):
    filename = get_data_file(name)
    total = 0
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                action, amount, *_ = line.strip().split(",")
                amount = int(amount)
                if action == "deposit":
                    total += amount
                elif action == "withdraw":
                    total -= amount
    return total

def add_transaction(name, action):
    amount = int(input(f"Enter amount to {action}: ৳"))
    note = ""
    if action == "withdraw":
        current_balance = get_current_balance(name)
        if amount > current_balance:
            print("Insufficient balance. Withdrawal cancelled.\n")
            return
        note = input("Why are you withdrawing? (optional): ")
    
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = get_data_file(name)
    
    with open(filename, "a") as f:
        f.write(f"{action},{amount},{date},{note}\n")
    print(f"{action.title()} of ৳{amount} added on {date}.\n")

# ===== View History =====
def show_history(name, action_filter=None):
    filename = get_data_file(name)
    if not os.path.exists(filename):
        print("No transaction history found.\n")
        return

    print(f"\n===== {action_filter.title() if action_filter else 'Full'} History =====")
    with open(filename, "r") as f:
        for line in f:
            action, amount, date, *note = line.strip().split(",")
            if action_filter and action != action_filter:
                continue
            note_text = f" — Note: {note[0]}" if note else ""
            print(f"{date} — {action.title()} ৳{amount}{note_text}")
    print("=====================\n")

# ===== Dashboard =====
def dashboard(name, user_data):
    filename = get_data_file(name)
    total = 0
    days = 0
    deposit_count = 0
    withdraw_count = 0

    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) < 3:
                    continue
                action, amount, *_ = parts
                amount = int(amount)
                if action == "deposit":
                    total += amount
                    days += 1
                    deposit_count += 1
                elif action == "withdraw":
                    total -= amount
                    withdraw_count += 1
    else:
        print("\nNo transaction history yet. Start saving today!")

    remaining = int(user_data["target"]) - total
    print("\n===== Dashboard =====")
    print(f"Total Saved: ৳{total}")
    print(f"Days Saved: {days}")
    print(f"Target Remaining: ৳{remaining}")
    print(f"Deposits: {deposit_count} | Withdrawals: {withdraw_count}")
    print("=====================\n")

# ===== Password Change =====
def change_password(name):
    users = load_users()
    current_pwd = input("Enter current password: ")
    if users[name]["password"] != current_pwd:
        print("Incorrect current password.\n")
        return
    
    new_pwd = input("Enter new password: ")
    users[name]["password"] = new_pwd
    save_users(users)
    print("Password updated successfully.\n")

# ===== Session Menu =====
def user_session(name, user_data):
    while True:
        print("\n===== Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Dashboard")
        print("4. Deposit History")
        print("5. Withdraw History")
        print("6. View Full Report")
        print("7. Change Password")
        print("8. Logout")
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(name, "deposit")
        elif choice == "2":
            add_transaction(name, "withdraw")
        elif choice == "3":
            dashboard(name, user_data)
        elif choice == "4":
            show_history(name, "deposit")
        elif choice == "5":
            show_history(name, "withdraw")
        elif choice == "6":
            show_history(name)
        elif choice == "7":
            change_password(name)
        elif choice == "8":
            logout_user()
            break
        else:
            print("Invalid option. Try again.\n")

# ===== Main Menu =====
def main():
    logged_in_user = get_logged_in_user()
    users = load_users()

    if logged_in_user and logged_in_user in users:
        print(f"\nWelcome back, {logged_in_user} (auto-login)!\n")
        user_session(logged_in_user, users[logged_in_user])
        return

    while True:
        print("\n===== Sonnic Tracker =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
            break
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()