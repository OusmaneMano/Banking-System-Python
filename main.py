from account import InsufficientFondError
from bank import Bank

BANK_NAME = "ManoBank"

def print_header(title: str) -> None:
    print(f"\n {'-' * 20}")
    print(f" {title}")
    print(f" {'-' *20}")

def print_menu() -> None:
    print(f"{'+'*30}\n{'+'*30}")
    print(f"{BANK_NAME} -- Main Menu")
    print("1: Register new customer")
    print("2: List all customer")
    print("3: Open new account")
    print("4: View customer accounts ")
    print("5: Deposit")
    print("6: Withdraw")
    print("7: View account transaction")
    print("8: Bank summary report")
    print("0: Exit")

def get_float_input(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value")
            else:
                return value
        except ValueError:
            print("Invalid input: Please enter valid value")

def register_customer(bank: Bank) -> None:
    print_header("Register new customer")
    try:
        name = input("Full name: ").strip()
        email = input("Email: ").strip()
        phone = input("Phone: ").strip()
        customer = bank.add_customer(name, email, phone)
        print("Customer registered successfully")
        print(f" {customer}")
    except ValueError as e:
        print(f"Error: {e}")

def list_customer(bank: Bank) -> None:
    print_header("All customer")
    customers = bank.list_customer()
    if not customers:
        print("There is no customer register")
        return
    for customer in customers:
        print(f" {customer}")

def open_account(bank: Bank) -> None:
    print_header("Open new account")
    try:
        customer_id = input("Customer _ID: ").strip()
        print("Choose account type: saving/current")
        account_type = input("Account type: ").strip().lower()
        account = bank.open_account(customer_id, account_type)
        print("Account open successfully")
        print(f" {account}")
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

def view_customer_account(bank: Bank) -> None:
    print_header("Customer account")
    customer_id = input("Customer ID: ").strip()
    try:
        bank.find_customer(customer_id)
        accounts = bank.get_customer_account(customer_id)
        if not accounts:
            print("This customer has no account yet")
            return
        for account in accounts:
            print(f" {account}")
    except KeyError as e:
        print(f"Error: {e}")

def deposit_funds(bank: Bank) -> None:
    print_header("Deposit fund")
    try:
        account_no = input("Account N°: ").strip()
        amount = get_float_input("Amount €  :")
        transaction = bank.deposit(account_no, amount)
        update_account = bank.find_account(account_no)
        print(f" {transaction}")
        print(f"New Balance: {update_account.get_balance()}")
    except KeyError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"error: {e}")

def withdraw_funds(bank: Bank) -> None:
    print_header("Withdraw fund")

    try:
        account_no = input("Account N°: ").strip()
        amount = get_float_input("Amount €   :")
        transaction = bank.withdraw(account_no, amount)
        update_account = bank.find_account(account_no)
        print(f"{transaction}")
        print(f"New balance: {update_account.get_balance()}")
    except KeyError as e:
        print(f"Error: {e}")
    except InsufficientFondError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

def view_transaction(bank: Bank) -> None:
    print_header("Account transaction history")
    try:
        account_no = input("Account N°: ").strip()
        bank.find_account(account_no)
        transactions = bank.get_account_transaction(account_no)
        if not transactions:
            return
        for txt in transactions:
            print(f" {txt}")
    except KeyError as e:
        print(f" {e}")

def bank_report(bank: Bank) -> None:
    print()
    print(bank.get_reports())

def main() -> None:
    bank = Bank(BANK_NAME)
    print(f"Welcome to {BANK_NAME}")

    handlers = {
        "1": register_customer,
        "2": list_customer,
        "3": open_account,
        "4": view_customer_account,
        "5": deposit_funds,
        "6": withdraw_funds,
        "7": view_transaction,
        "8": bank_report
    }
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()

        if choice == "0":
            print(f"\n Goodbye! Thank you for using {BANK_NAME}")
            break
        elif choice in handlers:
            handlers[choice](bank)
        else:
            print("Invalid choice! Please choose from the menu")

if __name__ == "__main__":
    main()

