__author__ = "Tadj Cazaubon"

"""
Program calulates savings after 5 years of interest given interest rate and initial savings as user inputs.
Revised 07/09/21
"""


initial = float(input("\n> Initial Savings: "))
interest = float(input("\n> Interest Rate as a Percentage: "))

years = 1

#total saving amount is set to inital amount
yearly_total = initial

while years<=5:

    #increment years
    years+=1

    #Interest for that year
    yearly_interest = (yearly_total*(interest/100))

    #that year's interest added to savings
    yearly_total+=yearly_interest
    print(f"\n> Year: {years} Interest: {yearly_total} Yearly Interest: {yearly_interest} \n")

print(f"\n> The value of your savings after 5 years is: {round(yearly_total)} \n")