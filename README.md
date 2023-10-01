# BudgetCalc
Simple budget calculator

## Simple README for the Monthly Budget Calculator

### Purpose:
This script helps users track their monthly expenses against a pre-defined budget. It calculates whether the user has exceeded the budget or has savings left after accounting for all expenses.

### Description:

1. **Welcome Message**: 
   - The user is greeted with a welcome message upon running the script.

2. **Set Monthly Budget**: 
   - The user is prompted to enter their total budget for the month. This amount is stored in the variable `Budget`.

3. **Display Initial Budget**:
   - The script then displays the total monthly budget that the user provided.

4. **Expense Categories**:
   - A predefined list of expenses is provided in the `Expenses` variable. This list includes categories like Housing, Food, Car, etc.
   - These expense categories are displayed to the user.

5. **Record Expenses**:
   - For each category in the `Expenses` list, the user is prompted to enter the actual amount they spent in that category.
   - As each expense is entered, the amount is deducted from the initial `Budget`, updating the remaining budget.

6. **Budget Evaluation**:
   - After all expenses are recorded, the script evaluates the remaining budget.
   - If the remaining budget is positive (i.e., `Budget > 0`), the user is informed that they are under budget and by what amount.
   - If the remaining budget is negative, the user is informed that they have exceeded their budget and by what amount.

### How to Use:
1. Run the script.
2. Enter your total budget for the month when prompted.
3. For each expense category displayed (like Housing, Food, etc.), enter the actual amount you spent in that category.
4. After all expense amounts are entered, the script will inform you if you are under or over your budget and by what amount.
