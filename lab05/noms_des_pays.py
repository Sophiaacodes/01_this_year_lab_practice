#LES NOMS DE PAYS
#for those who are gonna read my code, I'm sorry... I didn't know what else to do on a Friday night
#I'm gonna try to be clear and concise and use as much as possible annotations
#First I'm setting up the space with lists and logic and the last part of the code I'm doing the program functioning

#EXCEPTIONS AND VOWELS
#masculine exception names
MASCULINE_EXCEPTIONS = {
    "belize", "cambodge", "mexique", 
    "mozambique", "zaïre", "zimbabwe"
}

#dictionary of plurals
PLURAL_COUNTRIES = {
    "etats-unis": "les Etats-Unis",
    "états-unis": "les États-Unis",
    "pays-bas": "les Pays-Bas"
}

#all of vowels (also the french ones)
VOWELS = {'a', 'e', 'i', 'o', 'u', 'y', 'é', 'è', 'ê', 'à', 'â'}

#DEFINING LOGIC
def country_with_article(name: str) -> str:
    raw_name = name.strip()
    clean_name = raw_name.lower()

    #avoiding empty strings
    if not clean_name:
        return ""

    #plural countries
    elif clean_name in PLURAL_COUNTRIES:
        return PLURAL_COUNTRIES[clean_name]

    #vowels
    elif clean_name[0] in VOWELS:
        return f"l'{raw_name}"

    #female names
    elif clean_name[-1] == "e" and clean_name not in MASCULINE_EXCEPTIONS:
        return f"la {raw_name}"

    #male names
    else:
            return f"le {raw_name}"
     
#MAIN FUNCTION OF PROGRAM
def main(): 

    #INTRODUCTION
    print("WELCOME TO THE ARTICLE SETTING SYSTEM!")
    print("-"*45)
    print("This program will help you to find the correct article for a French country name.")
    print("\nFirst and foremost, a question. Please, answer with yes or no.")

    #adding a little whimsy with the different languages and nested loops
    #LANGUAGE
    while True:
        #asking the user if they speak french
        lang = input("Do you speak French? ").strip()
        lang_formatted = lang.lower()

        #the code for the ones that speak french doesn't have a list to choose from
        if lang_formatted == "yes":
            #same code as the one in english, but I'm changing the language and doesn't have the list
            print("\nBienvenue dans ce programme pour le noms des pays.")
            print("Veuillez saisir un nom pour obtenir l'article correspondant.")

            #adding a nested while loop to governate the possible options
            while True:
                chosen_country = input("\nNom du pays: ")
            
                result = country_with_article(chosen_country)
            
                if result:
                    print(result.title())
            
                #adding multiple possibility of that to try
                print("\nVoulez vois tester un autre nom?")
            
                while True:
                    continuing = input("Ecrivez 'oui' pour continuer, 'non' pour quitter: ").strip()
            
                    if continuing.lower() == "oui":
                        break
            
                    elif continuing.lower() == "non":
                        print("\nMERCI D'AVOIR UTILISE CE PROGRAMME!\n")
                        exit()
            
                    else:
                        print("\nErreur. Repondez par 'oui' ou 'non'.")


        #the code for those that don't speak french has a list of examples so that the user doesn't have to google the terms
        elif lang_formatted == "no":
            print("\nOk, no problem. Let me explain how it works:")
            print("\tFrench country names use 'le' for masculine names, except for a few special cases, and 'la' for feminine")
            print("\tHowever, if the country name starts with a vowel, use 'l’' and 'les' for plurals.")

            #list of name options
            name_options = ["Canada", "Japon", "Brésil", "France", "Suisse", "Chine", "Italie", "Allemagne", "États-Unis", "Zimbabwe"]
            name_options.sort()

            print("\nYou can google the name you want to try.")
            print("Or choose from this list:")

            for name in name_options:
                print(f"- {name}")

            #adding a nested while loop to governate the possible options
            while True:
                chosen_country = input("\nEnter here a name: ")

                result = country_with_article(chosen_country)

                if result:
                    print(result.title())

                #adding multiple possibility of that to try
                print("\nDo you want to try another name?")

                while True:
                    continuing = input("Print yes if you want to try another name, no if you want to stop: ").strip()

                    if continuing.lower() == "yes":
                        break

                    elif continuing.lower() == "no":
                        print("\nTHANK YOU FOR USING THIS PROGRAM!\n")
                        exit()

                    else:
                        print("\nPlease, enter a valid option.")

        else:
            print("\nPlease, write only 'yes' or 'no'")

if __name__ in "__main__":
    main()