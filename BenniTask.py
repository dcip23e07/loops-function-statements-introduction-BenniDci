# Defining the minimum and maximum withdrawal amounts
min_withdrawal = 5 
max_withdrawal = 1000 

# Initializing the Customer balance
customer_balance = 1000  # Initial balance 

# Optional input your balance
customer_balance_input = float(input("Enter your Balance: ",)) 


# Function to withdraw money
def withdraw_money(balance): # balance is just a hint what kind of object/variable we aim our function towards 
    print("Welcome to the ATM Machine!")
    
    while True:
        want_to_withdraw = input("Do you want to withdraw money? (yes/no): ").lower() #.lower function to make certain upper case input counts too
        # So Input:'Yes' will give 'yes' in return 'YES' will give 'yes' in return too.. and so on 
        # That way only the word is important not the casing
        
        if want_to_withdraw == "no":
            print("Thank you for using our ATM. Have a nice day!")
            break  # If the answer is no we just notify the costumer an final statement and end the function

        elif want_to_withdraw == "yes":
            withdrawal_amount = float(input("Enter the amount you want to withdraw: "))
            
            if withdrawal_amount < min_withdrawal:
                print("Withdrawal amount is below the minimum allowed")
            elif withdrawal_amount > max_withdrawal:
                print("Withdrawal amount exceeds the maximum allowed ")
            elif withdrawal_amount > balance:
                print("Insufficient funds. Your balance is not enough for this withdrawal.")
            else:
                balance -= withdrawal_amount
                print(f"Withdrawal successful! Your remaining balance is €{balance:.2f}") # f.2f so the 'Money' is shown with only max 2 digits after the .
                # When all other checks are done we pass Information for the costumer about the balance

                # Format for this : def function_name(description_for_variable) 
                # This is just to asign and use this given decription_for_variable inside the function and to clearify what it is/shows
                # The variable we actually use (and add a start value) can be given externaly as in this example: costumer_balance / costumer_balance_input
            
            another_transaction = input("Do you want to perform another transaction? (yes/no): ").lower() # Nesting another if Statement 
            if another_transaction == "no":
                print("Thank you for using our ATM. Have a nice day!")
                break
            
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            # In case the custumer types other input for example sye or niiii



withdraw_money(customer_balance) # Call the function with customer_balance which we defined before.. here it is 1000

# This also works with input for example like this (with the defined variable @ top ):

# withdraw_money(customer_balance_input)