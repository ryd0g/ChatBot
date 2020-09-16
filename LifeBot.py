# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#function to get response from user
def get_life_bot_response(user_response):

  #add some bot responses to this list
  bot_response_yes = ['Lets go for a run!', 'Gotta take the dog out now', 'Maybe you can play some games!']
  bot_response_no = ['Lets study some more', 'You should finish your work', 'Make sure you turn everything in!']
  bot_response_almost = ['Only a little bit more to go!', 'Get it done!', 'Keep it up!']

  #yes, no, almost, or else responses
  if user_response == "yes":
    return choice(bot_response_yes)
  elif user_response == "no":
    return choice(bot_response_no)
  elif user_response == "almost":
    return choice(bot_response_almost)
  else:
    return "Maybe we should just get some rest."

#function for asking how many hours the user worked
def hours_response(hours):

  bot_response_low = ['Maybe you should study some more', 'Keep going!', 'Put in a bit more time']
  bot_response_high = ['Maybe its time for a break', 'Good work for the day!', 'Now that is dedication']

  if int(hours) <= 1:
    return choice(bot_response_low)
  elif int(hours) >= 2:
    return choice(bot_response_high)


print("Welcome to the Life Bot")
print("Let us see how you are doing today. ")

#while loop to ask for input until user inputs 'done'
while True:
  user_response = input("Have you finished your work for the day? ")
  if user_response == 'done':
    break

  bot_response = get_life_bot_response(user_response)
  print(bot_response)

while True:
  hours = input("How many hours did you spend studying? ")
  if hours == 'done':
    break

  bot_respone = hours_response(hours)
  print(bot_respone)