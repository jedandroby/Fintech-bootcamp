#this function defines fucntions for calucating loan info

#this function defines monthly debt ratio
def calculate_monthly_debt_ratio(monthly_debt_payment, monthly_income):
    monthly_debt_ratio = int(monthly_debt_payment) / int(monthly_income)
    return monthly_debt_ratio

#this function defines the loan to value ratio
def calculate_loan_to_value_ratio(loan_amount, home_value):
    loan_to_value_ratio = int(loan_amount) / int(home_value)
    return loan_to_value_ratio

