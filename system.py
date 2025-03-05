import datetime

class ExpenseTracker:
    """
    Expense Tracker Application
    This application allows users to input their daily expenses, categorize them, store them in memory,
    and analyze their spending through summaries and category-wise expenditure.
    """
    
    def __init__(self):
        """Initialize the expense tracker with an in-memory data structure."""
        self.expenses = []

    def add_expense(self, amount, category, description=""):
        """Add a new expense with amount, category, and description."""
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
            
            expense = {
                "amount": amount,
                "category": category.strip().title(),
                "description": description.strip(),
                "date": str(datetime.date.today())
            }
            self.expenses.append(expense)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")

    def get_expenses(self, category=None):
        """Retrieve expenses, optionally filtered by category."""
        if category:
            category = category.strip().title()
            return [exp for exp in self.expenses if exp["category"] == category]
        return self.expenses

    def monthly_summary(self):
        """Provide a summary of expenses for the current month."""
        current_month = datetime.date.today().strftime("%Y-%m")
        monthly_expenses = [exp for exp in self.expenses if exp["date"].startswith(current_month)]
        total_spent = sum(exp["amount"] for exp in monthly_expenses)
        print(f"Total expenses for {current_month}: ${total_spent:.2f}")

    def category_summary(self):
        """Provide a breakdown of expenses by category."""
        category_totals = {}
        for exp in self.expenses:
            category = exp["category"]
            category_totals[category] = category_totals.get(category, 0) + exp["amount"]
        
        print("Category-wise Expenditure:")
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")

# Example usage
if __name__ == "__main__":
    tracker = ExpenseTracker()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Category Summary")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = input("Enter amount: ")
            category = input("Enter category (e.g., Food, Transport, Entertainment): ")
            description = input("Enter description (optional): ")
            tracker.add_expense(amount, category, description)
        elif choice == "2":
            category = input("Enter category to filter (or press Enter to view all): ")
            expenses = tracker.get_expenses(category if category else None)
            if expenses:
                for exp in expenses:
                    print(exp)
            else:
                print("No expenses found.")
        elif choice == "3":
            tracker.monthly_summary()
        elif choice == "4":
            tracker.category_summary()
        elif choice == "5":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
