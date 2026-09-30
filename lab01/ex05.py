#print the interest of 5% every year for 3 years

initial_amount = 1000  
interest_rate = 0.05

for year in range(1, 4):
    interest = initial_amount * interest_rate
    initial_amount += interest
    print(f"Year {year}: ${initial_amount:.2f}")