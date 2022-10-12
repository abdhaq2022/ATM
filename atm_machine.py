"""
        today we will create an ATM machine
        first we need to create few functions
        function for withdraw
        function for deposit
        function for if they want to continue
        function for checking the balance
"""

available_balance = 0


def deposit():
    while True:
        global available_balance
        print()
        customer = int(input('how much you want to deposit today: '))
        if customer == 0:
            print('you deposit must be greater than 0')
        elif customer > 0:
            available_balance += customer
            print()
            print(f'you deposited ${available_balance} today.')
            print()
            print(f'YOUR TOTAL BALANCE IS ${available_balance}')
            print('\n\n')
            print('---------------')
            customer = input('do you want to deposit more? ')
            if customer == 'yes':
                continue
            else:
                main(available_balance)
        else:
            quit()


def withdraw():
    while True:
        global available_balance
        print()
        customer = int(input('how much you want to withdraw today? '))
        if customer == 0:
            print('withdraw must be greater that zero!')
            continue

        elif customer <= available_balance:
            available_balance -= customer
            print(f'you withdraw ${customer} today.')
            print()
            print('------------')
            print(f'you remaining balance is ${available_balance}.')

        else:
            print(f'not enough money to withdraw!')
            print()
            if available_balance > 0:
                print()
                print(f'your available balance is ${available_balance}')
                print('--------------')
                customer = input('do you want to withdraw available balance? ')
                if customer == 'yes':
                    continue
            else:
                deposit()


def main(balance):
    while True:
        print()
        customers = input('what would like to do today? check the balance, deposit or withdraw: ').lower()
        if customers == 'balance':
            print()
            print(f'Total balance ${balance}')
            print()
        elif customers == 'deposit':
            deposit()
        elif customers == 'withdraw':
            withdraw()
        else:
            print('not a valid option')


main(available_balance)


### second way with some bugs


def deposit():
    balances = 0
    withdraws = 0
    while True:
        customer = input('Do you want to (Deposit or Withdraw?): ')
        if customer == 'no':
            break
        if customer == 'd':
            amount = input('How much you would like to deposit today?: $')
            if amount.isdigit():
                amount = int(amount)
                if amount == 0:  # predicting the input of 0 to avoid crash for code.
                    print()
                    print('Zero is not a valid number to withdraw!')
                    print('\n\n')
                else:
                    balances += amount
                    print('---------------------')
                    print(f'your have successfully deposited ${amount}')
                    print(f'your total balance is ${balances}')
                    print('---------------------')
                    print('\n\n')
            else:
                print('Please enter a whole digit numbers!')

                # we should predict all scenarios for the input 1- if customer type more there balance,
                # 2- the balance is 0 to type 0, if they type only zero 3 - if they type alphabetic, or just press
                # enter.
        elif customer == 'w':
            amount = input('How much you would like to withdraw today?: $')
            if amount.isdigit():
                amount = int(amount)
                available_balance = balances - withdraws
                if amount == 0:  # predicting the input of 0 to avoid crash for code.
                    print()
                    print('Zero is not a valid number to withdraw!')
                    print('\n\n')
                elif amount <= available_balance:  # in this scenario they withdraw if they don't have enough money
                    withdraws += amount
                    available_balance = balances - withdraws
                    print('---------------------')
                    print(f'you have successfully withdrew ${amount}')
                    print('---------------------')
                    print(f'your remaining balance is ${available_balance}')
                    print('---------------------')
                    print('\n\n')
                else:
                    print("you don't have enough money in your account")
                    print(f"your available balance is ${available_balance}")
                    print()
            else:
                print('Please enter a whole digit numbers!')
        else:
            print('Invalid Input Try Again')
    return balances, withdraws


def main():
    while True:
        customers = input(
            'Welcome to Bank Of Majid 😃 What would like to do today? for ( Deposit and Withdraw) Type continue ? ').lower()
        if customers == 'continue':
            deposit()
        elif customers == 'customer service':
            print('We are so sorry for the inconvenience, just a moment we will direct your to our available agent!')

        else:
            print('Bye Bye')


main()
