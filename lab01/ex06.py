#game of codes throne contest

#points
ARYA = 87
JON = 92

#Print the Maximum points
print("Maximum points:", max(ARYA, JON))

#print the absolute difference between the points of Arya and Jon
print("Absolute difference:", abs(ARYA - JON))

#print the average points of Arya and Jon
average_points = (ARYA + JON) / 2
print("Average points:", average_points)

#INPUT POINTS FROM USER
print("\nNow, let's input the points for Arya and Jon from the user.")
user_arya = int(input("Enter the points of Arya: "))
user_jon = int(input("Enter the points of Jon: "))

#Print the Maximum points
print("Maximum points:", max(user_arya, user_jon))

#print the absolute difference between the points of Arya and Jon
print("Absolute difference:", abs(user_arya - user_jon))

#print the average points of Arya and Jon
average_points = (user_arya + user_jon) / 2
print("Average points:", average_points)