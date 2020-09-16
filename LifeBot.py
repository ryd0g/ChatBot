# This will give you access to the random module or library.
# choice() will randomly return an element in a list.
# Read more: https://pynative.com/python-random-choice/

from random import choice

#combine functions and conditionals to get a response from the bot
def get_mood_bot_response(user_response):

  #add some bot responses to this list
  bot_response_yes = ['Lets go for a run!', 'Gotta take the dog out now', 'Maybe you can play some games!']
  bot_response_no = ['Lets study some more', 'You should finish your work', 'Make sure you turn everything in!']

  if user_response == "yes":
    #TODO: use choice to randomly return a response from the list
    return choice(bot_response_yes)
  elif user_response == "no":
    return choice(bot_response_no)
  else:
    return "Maybe we should just get some rest."


print("Welcome to the Life Bot")
print("What are we gonna do today? ")

#TODO: we want to keep repeating until the user enters "done" what should we put here?
while True:
  user_response = input("Have you finished all your homework? ")
  if user_response == 'done':
    break
  #TODO: what goes here
  bot_response = get_mood_bot_response(user_response)
  print(bot_response)
