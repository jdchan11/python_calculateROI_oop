class RentalPropertyROI():
    def __init__(self, monthly_income=0, monthly_expenses=0, total_investment=0, 
                annual_cash=0, cash_on_cash = 0):
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.total_investment = total_investment
        self.annual_cash = annual_cash
        self.cash_on_cash = cash_on_cash
    
    def annualCashFlow(self):
        self.annual_cash = (self.monthly_income - self.monthly_expenses) * 12
        print(f"\nYour annual cash flow would be ${self.annual_cash}\n")

    def findMonthlyExpenses(self):
        print("\nInput the monthly amount (in dollars) of the following expenses: ")
        taxes = int(input("Taxes: "))
        insurance = int(input("Insurance: "))
        utilities = int(input("Utilities: "))
        hoa_fees = int(input("HOA Fees: "))
        landscaping = int(input("Lawn/Snow: "))
        vacancy = int(input("Vacancy: "))
        repairs = int(input("Repairs: "))
        cap_ex = int(input("Capital Expenditure: "))
        prop_manage = int(input("Property Management: "))
        mortgage = int(input("Mortgage: "))
        self.monthly_expenses = (taxes + insurance + utilities + hoa_fees
                                 + landscaping + vacancy + repairs + cap_ex
                                 + prop_manage + mortgage)
        print(f"Your monthly expenses would be ${self.monthly_expenses}")
    
    def inputMonthlyIncome(self):
        self.monthly_income = int(input("What is the monthly income on the property? "))

    def welcomeMessage(self):
        print("Welcome to the ROI Calculator! After answering some questions, " 
               "you will be able to see your cash on cash return."
               "\nLet's get started! \nFirst, ")

    def calcTotalInvest(self):
        down_pay = int(input("How much did you put down as a down payment? "))
        closing_costs = int(input("How much were closing costs? "))
        rehab_budget = int(input("How much did you spend on repairs after purchasing? "))
        misc_costs = int(input("How much were any additional costs? "))
        self.total_investment = down_pay + closing_costs + rehab_budget + misc_costs 
        print(f"Your total investment on this property is ${self.total_investment}")

    def calcROI(self):
        self.cash_on_cash = round((self.annual_cash / self.total_investment * 100), 3)
        print(f"\nYour cash on cash return on investment is {self.cash_on_cash}%")

    def recap(self):
        print(f"\nTo review: \nYour monthly income is ${self.monthly_income}.")
        print(f"Your monthly expenses are ${self.monthly_expenses}.")
        print(f"Your annual cash flow is ${self.annual_cash}")
        print(f"Your total investment is ${self.total_investment}")
        print(f"And finally, your cash on cash ROI is {self.cash_on_cash}%")

test1 = RentalPropertyROI()
def run():
    while True:
        test1.welcomeMessage()
        test1.inputMonthlyIncome()
        test1.findMonthlyExpenses()
        test1.annualCashFlow()
        test1.calcTotalInvest()
        test1.calcROI()
        test1.recap()
        response = input("\nThank you for using our ROI calculator! Are you done, yes or no? ") 
        if response.lower() == 'yes':
            print("Glad you got the answers you came for!\n")
            break

run()
        
