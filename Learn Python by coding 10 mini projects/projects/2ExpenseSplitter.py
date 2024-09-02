def calculate_split(total_amount: float, number_of_people: int, currency:str) -> None:
    # return None because we are only displaying results
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one.')
    
    share_per_person: float = total_amount / number_of_people

    print(f'Total expenses : {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')

def main() -> None:
    try:
        total_amount: float = float(input('Enter the total amount of the expense: '))
        number_of_people: int = int(input('Enter the number of people sharing the expense: '))

        calculate_split(total_amount, number_of_people, currency='$')

    except ValueError as e:
        #except exception as e: could do the same , but, it is 
        #good to do it explicitly for different errors
        print(f'Error: {e}')


if __name__ == '__main__':
    main()


"""
1. Edit the script to give the user the option to enter uneven splits, such
as 20%, 40%, 40%.
2. Make it so that if the user encounters an error, the program nicely asks them to try 
again with a proper value
"""