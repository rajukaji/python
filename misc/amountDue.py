amount_due = 50
print(f"Amount Due: {amount_due}")
changes = (5,10,25)
amt = 0



while amount_due:
        userPayment = int(input("Insert changes: "))

        if amount_due == 0:
            break

        if userPayment not in changes:
             print("Only changes of 5, 10, or 25 are accepted!")
             continue
             
        if userPayment in changes:
            if userPayment > amount_due:
                 print(f"Please have another change! Due is {amount_due}")
                 continue

            amount_due -= userPayment
        
        print(f"Amount Due: {amount_due}")
            
print('Voila')
