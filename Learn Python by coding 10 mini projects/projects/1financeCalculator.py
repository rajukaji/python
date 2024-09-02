def calculate_finances(monthly_income: float, tax_rate: float, currency: str) -> None:
    # -> is returning None
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax

    print('------------------------------------')
    print(f'Monthly income: {currency} {monthly_income:,.2f}')
    # , is a thousand separator 
    # .2f is decimal placement
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly Salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('--------------------------------------------')


# calculate_finances(100.12345, 20, '$')

def main() -> None:
    monthly_income: float = float(input('Enter your monthly salary:'))
    tax_rate: float = float(input('Enter your Tax Rate (%): '))

    calculate_finances(monthly_income, tax_rate, currency='KR')


if __name__ == '__main__':
    main()


# 1. Edit the script so that users can also enter their expenses (eg. rent, food, gym memberships)
# so they can see how much they have left over each month.
#Recreate the user input section to safely handle users inserting the wrong
#type without  crashing the program.