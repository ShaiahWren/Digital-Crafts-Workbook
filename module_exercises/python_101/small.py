## 1

# name = input("Enter name: ")
# print("Hello, "+name+"!") 

## 2

# name = input("What is your name? ".upper())

# greet = f"Hello, {name.upper()}!".upper()
# length = f"Your name has {len(name)} in it! Awesome!".upper()

# print(greet + " " + length)

## 3
# print("Please fill in the blanks: ")
# name = input("Name: ")
# subject = input("Subject: ")
# print(f"{name}\'s favorite subject in school is {subject}.")

## 4
# while True:
#     day = int(input('Day (0-6)? '))
#     if day == 0:
#         print("Sunday")
#     elif day == 1:
#         print("Monday")
#     elif day == 2:
#         print("Tuesday")
#     elif day == 3:
#         print("Wednesday")
#     elif day == 4:
#         print("Thursday")
#     elif day == 5:
#         print("Frday")
#     elif day == 6:
#         print("Saturday")
#     else:
#         print("Try again")

## 5
while True:
    day = int(input('Day (0-6)? '))
    if day == 5 or day == 6:
        print("Sleep in")
    elif day == 0 or day == 1 or day == 2 or day == 3 or day == 4:
        print("Wake up!!")
    else:
        print("Try again")

