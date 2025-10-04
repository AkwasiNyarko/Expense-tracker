# 💰 Expense Tracker

A simple command-line expense tracking application built with Python. Track your spending, categorize expenses, and generate detailed summary reports.

## ✨ Features

- **Add Expenses**: Record expenses with amount, category, and optional description
- **View All Expenses**: Display a complete list of all recorded expenses
- **Summary Reports**: Generate detailed reports showing spending by category with percentages
- **Delete Expenses**: Remove unwanted expense entries
- **Persistent Storage**: All expenses are saved to a JSON file for data persistence
- **User-Friendly Interface**: Clean, formatted console output with visual separators

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker.git
cd expense-tracker
```

2. Run the application:
```bash
python expense_tracker.py
```

No additional dependencies required! Uses only Python standard library.

## 📖 Usage

### Main Menu Options

1. **Add Expense**: Enter amount, category, and optional description
2. **View All Expenses**: See a formatted list of all your expenses
3. **Generate Summary Report**: View spending breakdown by category with percentages
4. **Delete Expense**: Remove an expense by its number
5. **Exit**: Close the application

### Example Usage

```bash
EXPENSE TRACKER
1. Add Expense
2. View All Expenses
3. Generate Summary Report
4. Delete Expense
5. Exit

Enter your choice (1-5): 1
Enter amount: $50.00
Enter category (e.g., food, transport, entertainment): food
Enter description (optional): Grocery shopping

✓ Expense added: $50.0 for food
```

### Sample Summary Report

```
EXPENSE SUMMARY REPORT
======================================================================
Report Generated: 2025-10-04 14:30:00
Total Expenses Recorded: 5

CATEGORY             AMOUNT          PERCENTAGE     
----------------------------------------------------------------------
Food                 $150.00         50.0%
Transport            $75.00          25.0%
Entertainment        $75.00          25.0%
----------------------------------------------------------------------
TOTAL                $300.00         100.0%
======================================================================
```

## 💾 Data Storage

Expenses are automatically saved to `expenses.json` in the same directory as the script. The file is created automatically on first use and updated with each operation.

### Data Format

```json
[
    {
        "date": "2025-10-04 14:30:00",
        "amount": 50.0,
        "category": "food",
        "description": "Grocery shopping"
    }
]
```

## 🛠️ Technical Details

- **Language**: Python 3
- **Storage**: JSON file-based persistence
- **Libraries Used**: 
  - `json` - Data serialization
  - `os` - File operations
  - `datetime` - Timestamp generation
  - `collections.defaultdict` - Category aggregation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👤 Author

**Akwasi Nyarko**

- LinkedIn: [@akwasinyarko](https://www.linkedin.com/in/akwasinyarko)
- GitHub: [@AkwasiNyarko](https://github.com/AkwasiNyarko)

## 🌟 Future Enhancements

- Budget setting and alerts
- Export to CSV/PDF
- Monthly/yearly trend analysis
- Graphical charts and visualizations
- Multiple user support
- Currency conversion

---

⭐ If you found this project helpful, please give it a star!