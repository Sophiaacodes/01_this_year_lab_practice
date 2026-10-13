#type of car and price
cars = { "hybrid" : 30000, "gasoline" : 31000 }
YEARS = 5
cost_of_gas = 2.01
cost_of_gpl = 0.77

#cost per liter 
KM_PER_LITER_HYBRID = 18 
KM_PER_LITER_GASOLINE = 14

while True:
    #ask what car one wants 
    print("We have hybrid and gasoline cars in store")
    car_Wanted = input("Enter what car you want: ")

    #let's make the calculations
    if car_Wanted.lower() in cars:
        km_made_string = input("How many km will you make in a year? ")
        km_made = int(float(km_made_string))

        if car_Wanted.lower() == "hybrid":
            car_price = cars["hybrid"]
            yearly_fuel_cost = (km_made / KM_PER_LITER_HYBRID) * cost_of_gpl
            total_cost = (YEARS * yearly_fuel_cost) + car_price

            print(f"An hybrid cars costs {cars['hybrid']}€")
            print(f"You will spend in 5 years for this car {total_cost : .2f}€")
            break

        else:
            car_price = cars["gasoline"]
            yearly_fuel_cost = (km_made / KM_PER_LITER_GASOLINE) * cost_of_gas
            total_cost = (YEARS * yearly_fuel_cost) + car_price
            
            print(f"A gasoline cars costs {cars['gasoline']}€")
            print(f"You will spend in 5 years for this car {total_cost : .2f}€")
            break

    else:
        print("Please enter a valid option.\n")

