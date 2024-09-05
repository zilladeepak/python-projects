import json

def load_rate(json_file: str)->dict[str,dict]:
    with open(json_file, 'r') as file:
        return json.load(file)

def convert(amount:float, base:str, to:str, rates:dict[str,dict])->float:
    base :str = base.lower()
    to :str = to.lower()

    from_rate : dict|None = rates.get(base)
    to_rate : dict|None = rates.get(to)

    if from_rate is not None and to_rate is not None:
        if base == 'eur':
            final_amount = amount*to_rate['rate']
        else:
            final_amount =  amount*(to_rate['rate']/from_rate['rate'])
        return final_amount
    else:
        print('from rate or to rate are None')
        return 0.0

def main() ->None:
    while True:
        amount :float = float(input("Enter the amount to convert: "))
        base :str = input('Enter the Base Currency: ')
        to :str = input("Enter the Currency to convert to: ")
        rates :dict[str,dict] = load_rate('rates.json')
        result = convert(amount, base, to, rates=rates)
        print(f'Amount after converting from {base} to {to} is {result:,.2f}')

        restart :str = input("Want to convert again (y/n): ")
        if restart != 'y':
            exit()

if __name__ == '__main__':
    main()
