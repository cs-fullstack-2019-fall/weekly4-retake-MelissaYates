# # weekly4-retake
#
# You must push BEFORE 9:00am or your answers will not be graded.
#
# Do NOT use any notes or previous projects on this test. Each individual question file has the same questions as the README.
#
# # 1. Ask a user for their first name and age. Print "[NAME] is [AGE] years old"
#
# userInput = input("What is your first name?")
# userInput1 = int(input("What is your age?"))
# print(f'{userInput} is {userInput1} years old')
# # 2. Ask the user to enter their age. Check if they entered a value between 0 and 125. If valid, print "REAL AGE".
# # If invalid print “NOT A REAL AGE!!!”
# userAge = int(input("Please enter your age."))
# if userAge> 0 and userAge<125:
#     print ('REAL AGE.')
# # 3. Use a for loop to print every 4 numbers from -50 to 50.
# for i in range(-50,51,4):
#     print(i)
# 4. Ask the user to enter a number to add to a total. Keep asking the user to enter a number until they enter 0.
# Afterward, print the total of all numbers entered.
# userAdd = int(input("Please enter a number to add. Enter '0' to quit."))
# total = 0
# while userAdd != 0:
#     total = total + userAdd
#     userAdd = int(input("Please enter a number to add. Enter '0' to quit."))
# print(total)

# 5. Create an array of 4 names. Print one string that has all of the arrays separated by commas.
# arrayOfNames = ['Julius', 'Mario','Hopeton','Patrice']
# print(f'{arrayOfNames[0]},{arrayOfNames[1]},{arrayOfNames[2]},{arrayOfNames[3]}')
# 6. Create a function that’s passed three integer numbers. Print the sum of the first two numbers and
# return the product of the second two numbers.
# def num(num1, num2, num3):
#     print (num1 + num2)
#     return num2 * num3
# new_num = num(2,4,5)
# print (new_num)


# 7. Create the class Boardgame with name, price, pieceCount, and publisher properties/attributes.
# Create a class method that will change the price of the book. Outside of the class, create three objects of the class Boardgame.
# Print the three boardgame objects using the newly created objects.
# class Boardgame:
#     def __init__(self, name, price, pieceCount, publisher):
#         self.name = name
#         self.price = price
#         self.pieceCount = pieceCount
#         self.publisher = publisher
#     def changePrice(self):
#         self.price + newPrice
#
#
# boardgame1 = Boardgame("Checkers", 12,23, "Gringle")
# boardgame2 = Boardgame("Monopoly", 10, 10, "Pager")
# boardgame3 = Boardgame("From Egypt to Canaan", 23, 7, "ABC")
# print(f'Board game: {boardgame1.name} Price:{boardgame1.price} Piece Count:{boardgame1.pieceCount} Publisher{boardgame1.publisher}, \nBoard game:{boardgame2.name} Price:{boardgame2.price} Piece count:{boardgame2.pieceCount} Publisher:{boardgame2.publisher}, \nBoard game:{boardgame3.name} Price:{boardgame3.price} Piece count:{boardgame3.pieceCount} Publisher:{boardgame3.publisher}')
# # 8. Create a function that takes a string array and returns a string array with the letter 's' at the end of each element.
# # Call the function.
#
# def string_array():
#     s = ["Apple", "Banana", "Pear","Melon"]
#     new_string = []
#     for i in s:
#
# string_array()
# 9. Create a function that has a parameter of an integer array and
# returns only the positive numbers in the array. Call the function

def arrayOfNumbers(list_numbers):
    for i in numbers:
        return i>0
print(i)

numbers = [-1,2,5,0,-4]
arrayOfNumbers(numbers)

# 10. Create a Puppy class. It should have properties name and color.
# Create a program that will ask a user to enter the name, then the color of a puppy until they enter 'q' to quit.
# # Put each entry in an array.
#
# class Puppy:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
# userInput = input("What is the name of the puppy? Enter 'q' to quit.")
# userInput2 = input("What is the color of the puppy?")
# puppy_types = []
# while userInput != 'q':
#     puppy_types = puppy_types(userInput +" "+userInput2)
# userInput = input("What is the name of the puppy? Enter 'q' to quit.")
# userInput2 = input("What is the color of the puppy?")



