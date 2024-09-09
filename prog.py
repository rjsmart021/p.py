#Python Object Oriented Programing
class BudgetCategory:
    def __init__(self, Income, Expenses, Savings):
        self.income = income
        self.expenses = expenses
        self.Savings = Savings
   # Getter and setter for category name
    def get_category_name(self):
        return self._category_name

    def set_category_name(self, new_name):
        self._category_name = new_name

    # Getter and setter for allocated budget
    def get_allocated_budget(self):
        return self._allocated_budget

    def set_allocated_budget(self, new_budget):
        if new_budget >= 0:
            self._allocated_budget = new_budget
        else:
            print("Invalid budget amount. Budget should be a positive number.")

    # Getter for expenses
    def get_expenses(self):
        return self._expenses

    # Setter for expenses (optional, since expenses are managed internally)
    def set_expenses(self, amount):
        self._expenses = amount

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount >= 0:
            self._expenses += amount
        else:
            print("Invalid expense amount. Expense should be a positive number.")

    # Method to calculate remaining budget
    def remaining_budget(self):
        return self._allocated_budget - self._expenses

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self._category_name}")
        print(f"Allocated Budget: ${self._allocated_budget}")
        print(f"Expenses: ${self._expenses}")
        print(f"Remaining Budget: ${self.remaining_budget()}")


# Example usage
if __name__ == "__main__":
    food_category = BudgetCategory("Food", 500)
    food_category.add_expense(100)
    food_category.display_category_summary()

    # Test setters
    food_category.set_category_name("Groceries")
    food_category.set_allocated_budget(600)
    food_category.add_expense(50)

    food_category.display_category_summary()

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
