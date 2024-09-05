def calculator(monthly_salary:float, tax_rate:float, currency:str)->None:
    monthly_tax :float = monthly_salary * (tax_rate/100)
    monthly_net_income :float = monthly_salary - monthly_tax
    yearly_income :float = monthly_salary * 12
    yearly_tax :float = monthly_tax * 12
    yearly_net_income :float = yearly_income - yearly_tax

    print("-------------------------------------")
    print(f'Monthly Income : {monthly_salary:,.2f} {currency}')
    print(f'Tax Rate : {tax_rate:,.0f}%')
    print(f'Monthly Tax : {monthly_tax:,.2f} {currency}')
    print(f'Monthly Net Income : {monthly_net_income:,.2f} {currency}')
    print(f'Yearly Income : {yearly_income:,.2f} {currency}')
    print(f'Yearly Tax : {yearly_tax:,.2f} {currency}')
    print(f'Yearly Net Income : {yearly_net_income:,.2f} {currency}')
    print("-------------------------------------")
    


def main()->None:
    monthly_salary:float = float(input('Enter Your Monthly Salary: '))
    tax_rate:float = float(input('Tax Rate: '))
    calculator(monthly_salary,tax_rate,currency='INR')

if __name__ == '__main__':
    main()
    
