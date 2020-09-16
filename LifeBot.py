# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#function to get response from user
def get_life_bot_response(user_response):

  #add some bot responses to this list
  bot_response_yes = ['Lets go for a run!', 'Gotta take the dog out now', 'Maybe you can play some games!']
  bot_response_no = ['Lets study some more', 'You should finish your work', 'Make sure you turn everything in!']

  #yes, no, or else responses
  if user_response == "yes":
    return choice(bot_response_yes)
  elif user_response == "no":
    return choice(bot_response_no)
  else:
    return "Maybe we should just get some rest."


print("Welcome to the Life Bot")
print("Let/'s see how you are doing today. ")

#while loop to ask for input until user inputs 'done'
while True:
  user_response = input("Have you finished all your homework? ")
  if user_response == 'done':
    break
  
  bot_response = get_life_bot_response(user_response)
  print(bot_response)
