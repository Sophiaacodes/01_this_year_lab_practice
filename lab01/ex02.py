#this is the code for exercise 2 of lab 1
#in here we will calculate which percentage of the kilometers made is actually 4 work and what 4 fun
km_start = int(input("Enter the starting kilometer: "))
km_end = int(input("Enter the ending kilometer: "))
working_days = int(input("Enter the number of working days: "))
km_home_work = int(input("Enter the kilometers made from home to work: "))

#let's calculate the total kilometers made
total_km = km_end - km_start
km_work = working_days * (km_home_work * 2)  # Assuming round trip
km_fun = total_km - km_work

#now let's calculate the percentages
percentage_work = (km_work / total_km) * 100
percentage_fun = (km_fun / total_km) * 100

#print the results
print("Total kilometers made:", total_km)
print("Kilometers made for work:", km_work)
print("Kilometers made for fun:", km_fun)
print("Percentage of kilometers made for work: {:.2f}%".format(percentage_work))
print("Percentage of kilometers made for fun: {:.2f}%".format(percentage_fun))