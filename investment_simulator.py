import random

def main():
    while True:
        try:
            starting_capital = float(input("What is your starting capital? "))
            monthly_contribution = float(input("Enter your monthly contribution: "))
            years = int(input("How long are you plannning to invest(yrs)? "))
            simulations = int(input("Enter number of simulations: "))
            if validate(starting_capital, monthly_contribution, years, simulations):
                break
        except(ValueError):
            print("Enter valid numerical value")
            continue
    portfolios = run_simulation(starting_capital, monthly_contribution, years, simulations)
    highest, lowest, average = statistics(portfolios)
    print(f"Lowest final value: R{lowest}\nHighest final value: R{highest}\nAverage: R{average}")

def simulate_investment(starting_capital, monthly_contribution, years):
    portfolio = starting_capital
    for month in range(years*12):
        portfolio += portfolio*random.uniform(-0.05, 0.05) + monthly_contribution
    return round(portfolio, 2)
        
def run_simulation(starting_capital, monthly_contribution, years, num_of_sim):
    portfolios = []
    for i in range(num_of_sim):
        portfolios.append(simulate_investment(starting_capital, monthly_contribution, years))
    return portfolios
    
def statistics(portfolios):
    average = round(sum(portfolios) / len(portfolios), 2)
    lowest = min(portfolios)
    highest = max(portfolios)
    return (highest, lowest, average)

def validate(starting_capital, monthly_contribution, years, simulations):
    if starting_capital < 0 or monthly_contribution < 0 or years <= 0 or simulations <= 0:
        print("Enter valid numerical values")
        return False
    return True
        
main()
