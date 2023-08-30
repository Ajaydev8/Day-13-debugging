############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()
# problem: range function does not include the last number given here that is 20 hence nothing is getting printed.
# If you check it with 19 then you'll see the print!
# Another way to debug is change the range 20 to 21 and you'll get it.


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])
# By reproducing the bug we will understand where the problem is.
# You can also use thonny to see where the problem lies.
# The problem here was randint was set in the range of (1, 6) while list numbers are ranged from (0, 5)


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   # changed from year > 1994
#   print("You are a Gen Z.")
# Here the problem was that year > 1994 and year < 1994 did not include the number 1994


# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")
# Here f string was missing with the indentation error
# Another major error was the int function was not assigned in the age input hence it was a string.

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# In this method I learned how to use the print statement in each line to debug the code.


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])
# In this lesson I learned to use a debugger and some apps like thonny to debug some complex problem.
# It was a silly identation error.
