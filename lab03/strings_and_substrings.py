#prepping the two lists
long_sequence = []
short_sequence = []

#list of the possible letters
letters = ["A", "C", "T", "G"]

while True:
    print("CHOSE A LETTER BETWEEN A, C, T, G")

    #let's select the letters for the long sequence
    while True:
        if len(long_sequence) <= 9 :
            user_input = input("Letter: ")
            if user_input.upper() in letters:
                #store letter in long sequence
                long_sequence.append(user_input)
            else:
                print("Please use one of the following letters: A, C, T, G")
        else:
            print("Ok, now let's find if a random sequence is in your DNA")
            print(15*'-')
            break

    print("\nCHOSE A LETTER BETWEEN A, C, T, G")  
    #let's select the letter for the short sequence
    while True:
        if len(short_sequence) <= 4 :
            user_input = input("Letter: ")
            if user_input.upper() in letters:
              #store letter in short sequence
              short_sequence.append(user_input)
            else:
                print("Please use one of the following letters: A, C, T, G")
        else:
            break
    break

#print(long_sequence)
#print(short_sequence)

#make the sequence in strings
long_str = "".join(long_sequence)
short_str = "".join(short_sequence)

#verify that the sequence is contained in long sequence
if short_str in long_str:
    print("I. the 'long sequence' contains the 'short sequence'")

    #verify where the short sequence start
    #let's make a list to save the positions
    position = []

    #let's read through the string 
    for i in range(len(long_str) - len(short_str) +1):
        #extracting the protion of the string
        if long_str[i:i+len(short_str)] == short_str:
            position.append(i)

    print(f"II. The short sequence starts at index/indices: {position}")
    print(f"III. The short sequence is contained {len(position)} times.")

else:
    print("I. No, the long sequence does not contain the short sequence.")