import sys

class BankRequest:

    user_acc_details = []  # accname,accnumber,bank,pin,acctype,balance
    all_banks = ["UBA","Zenith","FCMB","FirstBank","GTBank","WemaBank","Diamond","Polaris","EcoBank"]
    account_type = ["Savings", "Current"]

    @classmethod
    def showMessage(bank_request):
        print("Welcome. Please enter your bank details.")

    @staticmethod
    def getUserDetails(self):
        for i in range(1):
            acc_name = str(input("enter your account name: "))
            self.user_acc_details.append(acc_name)

            acc_number = str(input("enter your account number: "))
            self.user_acc_details.append(acc_number)
            
            bank_index=0
            for i in self.all_banks:
                bank_index+=1
                print("{0}. {1}".format(bank_index, i))
            bank_name = str(input("choose your bank: "))
            getBankIndex = int(bank_name) - 1
            getBankName = self.all_banks[getBankIndex] 
            self.user_acc_details.append(getBankName)
            
            pin = str(input("enter your pin: "))
            self.user_acc_details.append(pin)
            
            acc_type_index=0
            for i in self.account_type:
                acc_type_index+=1
                print("{0}. {1}".format(acc_type_index, i))
            acc_type = str(input("enter your account type: "))
            getAccTypeIndex = int(acc_type) - 1
            getAccType = self.account_type[getAccTypeIndex] 
            self.user_acc_details.append(getAccType)
            
            balance = str(input("enter you account balance: "))
            self.user_acc_details.append(balance)
        print(self.user_acc_details)
        print("")

    @classmethod
    def validateUserDetails(self):
        bank_request = BankRequest()
        bank_request.showMessage()
        bank_request.getUserDetails(bank_request)
        input_error_found = False
        
        acc_name = self.user_acc_details[0]  #validate account name for digits starts here
        for i in str(acc_name):
            check_digit = 0
            try:
                check_digit = int(i)
                if isinstance(check_digit, int):
                    print("Input Error: Account Name can't have numbers.")
                    input_error_found = True
                    break234
            except ValueError:
                pass #validate account name for digits ends here
        
        if len(self.user_acc_details[1]) != 9: #validate account number starts here
            print("Input Error: Account number must be '9' characters long.")
            input_error_found = True
        
        acc_num = self.user_acc_details[1]
        check_str = 0
        for i in str(acc_num):
            try:
                check_str = int(i)
                if isinstance(check_str, int):
                    pass
            except ValueError:
                print("Input Error: Account number can't have texts/special characters.")
                input_error_found = True #validate account number ends here
                break

        if len(self.user_acc_details[3]) != 4: #validate account pin starts here
            print("Input Error: Account pin must be '4' characters long.")
            input_error_found = True

        acc_pin = self.user_acc_details[3]
        for i in str(acc_pin):
            try:
                check_digit = int(i)
                if isinstance(check_digit, int):
                    pass
            except ValueError:
                print("Input Error: Account pin can't have texts/special characters.")
                input_error_found = True#validate account pin ends here
                break

        balance = self.user_acc_details[5]
        for i in str(balance):
            try:
                check_digit = int(i)
                if isinstance(check_str, int):
                    pass
            except ValueError:
                print("Input Error: Account balance can't have texts/special characters.")
                input_error_found = True
                break

        if input_error_found == True:
            self.user_acc_details.clear()
            print(" ")
            BankRequest.validateUserDetails()

class ATM:

    input_error_found = False
    acc_details = BankRequest.user_acc_details
    @staticmethod
    def Menu(self):
        pin = str(input("enter account pin: "))
        try_pin=0
        while pin != self.acc_details[3]:
            print(" ")
        # acc_details[3]:
            print("Invalid Data: enter correct pin")
            try_pin+=1
            pin = str(input("enter account pin: "))
            if try_pin == 5:
                print(" Number of tries exhausted. Program will exit.")
                sys.exit()
    
        print('''        1. Withdrawal      2. QuickTeller

        3. Change Pin      4. Enquiries

        5. Exit''')

        menu_option = int(input("choose a transaction: "))
        print(" ")
        if menu_option == 1:
            ATM.withdraw()
        elif menu_option == 2:
            ATM.quickTeller()
        elif menu_option == 3:
            ATM.changePin()
        elif menu_option == 4:
            ATM.enquiries()
        elif menu_option == 5:
            ATM.exitATM()
        else:
            print("Command not recognized. I'm quite sure you saw only numbers 1-6")
            sys.exit()
    # end of menu method 
    
    def withdraw():
        # print("withdraw initiated")
        menu_amounts = [500, 1000, 2000, 5000, 10000, 15000, 20000, 40000]
        acct_balance = int(ATM.acc_details[5])
        print("")
        print("---WITHDRAWAL---")
        print('''        1. 500       5. 10000

        2. 1000      6. 15000

        3. 2000      7. 20000

        4. 5000      8. 40000

                     9. Others''')
        withdraw_options = ["1","2","3","4","5","6","8","9"]
        withdraw_amount = str(input("Choose Amount(You will be charged N65 on every transaction): "))
        while withdraw_amount not in(withdraw_options):
            withdraw_amount = str(input("Choose Amount(You will be charged N65 on every transaction): "))

        if withdraw_amount == "9":
            amount = int(input("Enter amount to wihdraw: "))
            withdraw_choice = str(input("You want to withdraw {0}. is this correct? Enter 'Yes, y' or 'No, n' (Press 'X' to cancel withdrawal): ".format(amount)))
            if withdraw_choice.casefold() == "X".casefold():
                ATM.Menu(ATM)
            elif withdraw_choice.casefold() == "Yes".casefold() or withdraw_choice.casefold() == "Y".casefold() :
                if amount >= acct_balance:
                    print("")
                    print("Insufficient Balance...Terminating Transaction")
                    choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                    print("")
                    while choose not in("1", "2"):
                        choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                        print("")
                    if choose == "1":
                        ATM.withdraw()
                    elif choose == "2":
                        ATM.Menu(ATM)
                else:
                    new_balance = acct_balance - amount
                    new_balance = new_balance - 65
                    ATM.acc_details[5] = new_balance
                    print("")
                    print("Transaction Successful")
                    choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                    print("")
                    while choose not in("1", "2"):
                        choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                        print("")
                    if choose == "1":
                        ATM.withdraw()
                    elif choose == "2":
                        ATM.Menu(ATM)
            elif withdraw_choice.casefold() == "No".casefold() or withdraw_choice.casefold() == "N".casefold():
                ATM.withdraw()
        else:    
            getWithdrawAmountIndex = int(withdraw_amount) - 1
            getWithdrawAmount = int(menu_amounts[getWithdrawAmountIndex])
            withdraw_choice = str(input("You want to withdraw {0}. is this correct? Enter 'Yes, y' or 'No, n' (Press 'X' to cancel withdrawal): ".format(getWithdrawAmount)))
            if withdraw_choice.casefold() == "X".casefold():
                ATM.Menu(ATM)
            elif withdraw_choice.casefold() == "Yes".casefold() or withdraw_choice.casefold() == "Y".casefold() :
                if getWithdrawAmount >= acct_balance:
                    print("")
                    print("Insufficient Balance...Terminating Transaction")
                    choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                    print("")
                    while choose not in("1", "2"):
                        choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                        print("")
                    if choose == "1":
                        ATM.withdraw()
                    elif choose == "2":
                        ATM.Menu(ATM)
                else:
                    new_balance = acct_balance - getWithdrawAmount
                    new_balance = new_balance - 65
                    ATM.acc_details[5] = new_balance
                    print("")
                    print("Transaction Successful")
                    choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                    print("")
                    while choose not in("1", "2"):
                        choose = str(input("Enter 1 to withdraw again OR 2 to go-to Menu: "))
                        print("")
                    if choose == "1":
                        ATM.withdraw()
                    elif choose == "2":
                        ATM.Menu(ATM)
            elif withdraw_choice.casefold() == "No".casefold() or withdraw_choice.casefold() == "N".casefold():
                ATM.withdraw()
    # end of withdraw method

    def quickTeller():
        # print("quickteller initiated")
        print("--QUICKTELLER--")
        print("1.Airtime Top-Up   2.Pay Bills")
        qt_option = str(input("Enter Option( Press 'X' to goto main menu): "))
        print("")
        while qt_option not in("1", "2", "X".casefold()):
            print("command not recognized")
            qt_option = str(input("Enter Option( Press 'X' to goto main menu): "))
            print("")
        if qt_option == "1":
            ATM.airtimeTopUp()
        elif qt_option == "2":
            ATM.payBills()
        elif qt_option.casefold() == "X".casefold():
            ATM.Menu(ATM)
    # end of quickTeller

    def airtimeTopUp():
        eof
        # print("airtimetopup initiated")
        # print("-BUY AIRTIME-")
        # mobile_number = ""
        # service_providers = ["MTN","AIRTEL","9MOBILE","GLO"]
        # acct_balance = int(ATM.acc_details[5])
        # airtime_amount = 0
        
        # print('''        1. MTN      2. AIRTEL

        # 3. 9MOBILE      4. GLO''')

        # choose_sp = str(input("Select Service Provider: "))
        # print("")
        # while choose_sp not in ("1","2","3","4","X".casefold()):
        #     choose_sp = str(input("Select Service Provider: "))
        #     print("")
        # if choose_sp.casefold() == "X".casefold():
        #     ATM.Menu(ATM)
        # else:
        #     getSPIndex = int(choose_sp) - 1
        #     getSP = service_providers[getSPIndex]
        #     print("{0} selected.".format(getSP))
        #     airtime_amount = str(input("Enter Amount: "))
        #     check_str = 0
        #     for i in str(airtime_amount):
        #         try:
        #             check_str = int(i)
        #             if isinstance(check_str, int):
        #                 pass
        #         except ValueError:
        #             print("Input Error: Amount can't have texts/special characters.")
        #             ATM.input_error_found = True #validate account number ends here
        #             break
        #     while ATM.input_error_found:
        #         airtime_amount = int(input("Enter Amount: "))
        #         ATM.input_error_found = False

    def payBills():
        # print("paybills initiated")
        print("-PAY BILLS-")
        # saved_bills = []
        iuc_number = ""
        reg_name = ""
        tv_bills = ["DSTV","GOTV"]
        acct_balance = int(ATM.acc_details[5])
        bill_amount = 5000

        print("1. DSTV    2. GOTV")
        choose_bill = str(input("Select Bill To Pay: "))
        # print("Select Bill To Pay")
        print("")
        while choose_bill not in("1","2"):
            choose_bill = str(input("Select Bill To Pay: "))
            print("")

        getTVBillIndex = int(choose_bill) - 1
        getBill = tv_bills[getTVBillIndex]
        print(getBill)
        iuc_number = str(input("Enter your IUC-Number: "))
        reg_name = str(input("Enter your Account Name: "))
        confirm_payment_options = ["yes".casefold(), "y".casefold(), "no".casefold(), "n".casefold(), "x".casefold()]
        print("You want to subscribe for Account Name: {0} IUC-Number: {1} ?".format(reg_name.upper(), iuc_number))
        confirm_payment = str(input("Enter 'Yes, y' or 'No, n' (Press 'X' to cancel payment):"))    
        while confirm_payment not in(confirm_payment_options):
            confirm_payment = str(input("Enter 'Yes, y' or 'No, n' (Press 'X' to cancel payment):"))    
        if confirm_payment.casefold() == "X".casefold():
            ATM.quickTeller()
        elif confirm_payment.casefold() == "Yes".casefold() or confirm_payment.casefold() == "Y".casefold() :
            if bill_amount >= acct_balance:
                print("")
                print("Insufficient Balance...Terminating Transaction")
                choose = str(input("Enter 1 to try again OR 2 to go-to QuickTeller Menu (Press 'X' to cancel payment): "))
                print("")
                while choose not in("1", "2", "X".casefold()):
                    choose = str(input("Enter 1 to try again OR 2 to go-to QuickTeller Menu (Press 'X' to cancel payment): "))
                    print("")
                if choose == "1":
                    ATM.payBills()
                elif choose == "2":
                    ATM.quickTeller()
                elif choose.casefold() == "X".casefold():
                        ATM.Menu(ATM)
            else:
                new_balance = acct_balance - bill_amount
                new_balance = new_balance - 10
                ATM.acc_details[5] = new_balance
                print("")
                print("Transaction Successful")
                choose = str(input("Enter 1 to subscribe again OR 2 to go-to QuickTeller Menu (Press 'X' for Menu): "))
                print("")
                while choose not in("1", "2", "X".casefold()):
                    choose = str(input("Enter 1 to subscribe again OR 2 to go-to QuickTeller Menu (Press 'X' for Menu): "))
                    print("")
                if choose == "1":
                    ATM.payBills()
                elif choose == "2":
                    ATM.quickTeller()
                elif choose.casefold() == "X".casefold():
                    ATM.Menu(ATM)
        elif confirm_payment.casefold() == "No".casefold() or confirm_payment.casefold() == "N".casefold() :
            ATM.payBills()
        elif confirm_payment_options.casefold() == "X".casefold():
            ATM.Menu(ATM)
    # end of payBills method

    def enquiries():
        # print("enquiries initiated")
        print("")
        print("---ENQUIRIES---")
        print("Account Balance for {0}".format(ATM.acc_details[0]))
        print(ATM.acc_details[5])
        print("")
        ATM.Menu(ATM)
    # end of enquiries method

    def changePin():
        # print("change pin initiated")
        error_found = False
        print("---CHANGE PIN---")
        old_pin = str(input("enter old pin: "))
        new_pin = str(input("enter new pin: "))

        if old_pin != ATM.acc_details[3]:
            print("Input Error: old pin is incorrect")
            error_found = True

        if len(new_pin) != 4:
            print("Invalid input: pin must be '4' characters")
            error_found = True
        
        for i in str(new_pin):
            try:
                check_digit = int(i)
                if isinstance(check_digit, int):
                    pass
            except ValueError:
                print("Input Error: pin can't have texts/special characters.")
                error_found = True
                break

        if new_pin == ATM.acc_details[3]:
            print(" ")
            print("Input Error: new pin match with old pin.")
            error_found = True

        if error_found == True:
            print(" ")
            error_found == False
            ATM.changePin()
        else:
            ATM.acc_details[3] = new_pin
            print("")
            ATM.Menu(ATM)
    # end of changePin method.

    def exitATM():
        # print("exit atm initiated")
        print("we value our customer...")
        sys.exit()
    # end of exit method
    

if __name__ == "__main__":
    BankRequest.validateUserDetails()
    atm = ATM()
    atm.Menu(ATM)
