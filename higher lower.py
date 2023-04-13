import random

number_list = list(range(1,101))
random_number = float(random.choice(number_list))

#print(random_number)

while True:
    try:
        user_number = int(input("Choose a number from 1 to 100. "))

        if user_number <0:
            print("Enter a positive number")
        elif(user_number) > 100:
            print("Don't go higher than 100")
        elif user_number < random_number:
            print("Higher!")
        elif user_number > random_number:
            print("Lower!")
        else:
            int(random_number)
            print(str(random_number) + " is the right number!!")
            break
    except ValueError:
        print("Enter a full number!")