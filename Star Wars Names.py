#Jacob Wright
#Star Wars Names
#Week Three Assignment

#prompt the user for their first name, last name, mother's maiden name, and their city of birth
firstName = input("Type your first name: ")
lastName = input("Type your last name: ")
maidenName = input("Type your mother's maiden name: ")
cityBorn = input("Type the name of the city where you were born: ")

#calculate and print the name
print(lastName[0:3]+firstName[0:2], maidenName[0:2]+cityBorn[0:3])
