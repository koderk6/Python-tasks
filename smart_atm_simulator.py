# smart atm simulator
correct_pin = "1234"
balance = 5000
print(" SMART ATM SYSTEMS ONLINE ".center(40, "💲"))
print(" WELCOME DEAR USER! ".center(54,"-"))
print("-".center(54,"-"))
print(" 🔒 Please enter your pin below 🔒\n>", end=" ")
enteredPassword = input()
if enteredPassword == correct_pin:
    while(True):
        print("What are we going to do today? (please enter your choice number below)")
        print("1. Withdraw ⬇️  💵")
        print("2. Check Balance ⚖️  💵")
        print("3. Exit \n> ", end=" ")
        choice = int(input())
        if choice == 1:
            amountWithdrawed = int(input("Please input the amount to withdraw: "))
            if amountWithdrawed > balance:
                print("❎ Sorry, your balance is insufficient. ❎")
            else:
                balance -= amountWithdrawed
                print(f"✅ Operation completed successfully. ✅\nRemaining balance: {balance}")
        elif choice == 2:
            print(f"💵 Your current balance = {balance} 💵")
        elif choice == 3:
            print("Exiting the system... 🚶🚶")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("❌ Incorrect PIN. Access denied. ❌")