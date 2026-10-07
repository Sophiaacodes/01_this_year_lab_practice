#make a time conversion function
#this program makes a user input a time in the hh:mm format and converts into a second format

input_time = input("Enter time in hh:mm format: ")
hours, minutes = input_time.split(":") #we split the input string into hours and minutes using the colon as a delimiter
#we convert the hours and minutes to integers
hours = int(hours)
minutes = int(minutes)
#we calculate the total time in seconds by multiplying the hours by 3600 and the minutes by 60, then adding them together
seconds = (hours * 3600 + minutes * 60) 

print(f"The time in seconds is: {seconds} seconds")

#in this part of the program user imputs a time in seconds and the program converts it into hh:mm format
input_seconds = int(input("Enter time in seconds: "))
hours = input_seconds // 3600
minutes = (input_seconds % 3600) // 60 #we devide the remaining seconds by 60 to get the minutes
seconds = input_seconds % 60 #we use the modulus operator to get the remaining seconds after calculating hours and minutes

print(f"The time in hh:mm format is: {hours:02d}:{minutes:02d}:{seconds:02d}")
