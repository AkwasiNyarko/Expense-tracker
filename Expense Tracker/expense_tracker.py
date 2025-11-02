import json
import os
from datetime import datetime
from collections import defaultdict

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_expenses(self):
        """Save expenses to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.expenses, f, indent=4)
    
    def add_expense(self, amount, category, description=''):
        """Add a new expense"""
        expense = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'amount': float(amount),
            'category': category.lower(),
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()
        print(f"\n✓ Expense added: ${amount} for {category}")
    
    def view_expenses(self):
        """View all expenses"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return
        
        print("\n" + "="*70)
        print("ALL EXPENSES")
        print("="*70)
        for i, exp in enumerate(self.expenses, 1):
            print(f"\n{i}. Date: {exp['date']}")
            print(f"   Amount: ${exp['amount']:.2f}")
            print(f"   Category: {exp['category'].title()}")
            if exp['description']:
                print(f"   Description: {exp['description']}")
        print("="*70)
    
    def generate_summary(self):
        """Generate summary report with structured output"""
        if not self.expenses:
            print("\nNo expenses to summarize.")
            return
        
        # Calculate totals by category
        category_totals = defaultdict(float)
        total_spent = 0
        
        for exp in self.expenses:
            category_totals[exp['category']] += exp['amount']
            total_spent += exp['amount']
        
        # Print structured summary report
        print("\n" + "="*70)
        print("EXPENSE SUMMARY REPORT")
        print("="*70)
        print(f"\nReport Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Expenses Recorded: {len(self.expenses)}")
        print(f"\n{'CATEGORY':<20} {'AMOUNT':<15} {'PERCENTAGE':<15}")
        print("-"*70)
        
        for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total_spent) * 100
            print(f"{category.title():<20} ${amount:<14.2f} {percentage:.1f}%")
        
        print("-"*70)
        print(f"{'TOTAL':<20} ${total_spent:<14.2f} 100.0%")
        print("="*70)
    
    def delete_expense(self, index):
        """Delete an expense by index"""
        if 0 <= index < len(self.expenses):
            deleted = self.expenses.pop(index)
            self.save_expenses()
            print(f"\n✓ Deleted expense: ${deleted['amount']} for {deleted['category']}")
        else:
            print("\n✗ Invalid expense number.")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n" + "="*70)
        print("EXPENSE TRACKER")
        print("="*70)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Generate Summary Report")
        print("4. Delete Expense")
        print("5. Exit")
        print("="*70)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            try:
                amount = float(input("Enter amount: $"))
                category = input("Enter category (e.g., food, transport, entertainment): ").strip()
                description = input("Enter description (optional): ").strip()
                tracker.add_expense(amount, category, description)
            except ValueError:
                print("\n✗ Invalid amount. Please enter a number.")
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            tracker.generate_summary()
        
        elif choice == '4':
            tracker.view_expenses()
            try:
                index = int(input("\nEnter expense number to delete: ")) - 1
                tracker.delete_expense(index)
            except ValueError:
                print("\n✗ Invalid input.")
        
        elif choice == '5':
            print("\nThank you for using Expense Tracker!")
            break
        
        else:
            print("\n✗ Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()