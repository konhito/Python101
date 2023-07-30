#  #String concatenation
#  youtuber = input("Subscribe to: ")

# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

# # 1) maldibs
# adj = input("Adjective: ")
# Verb = input("Verb: ")
# Verb2 = input("Verb: ")
# famous_person = input("Famous person: ")

# mablib = f"Computer programing is so {adj}! It make me so excited all the time because  I love to {Verb}. Stay hydrated and {Verb2} like you are {famous_person}  "
# print(mablib)

# #2) Random Number Gusser
# import random

# def guess(x):
#   random_number = random.randint(1, x)
#   guess = 0
#   while guess != random_number:
#     guess = int(input(f"Guess a number btw 1 and {x}: "))
#     if guess < random_number:
#       print("sorry, guess agai,. Too low. ")
#     elif guess > random_number:
#       print("Sorry, guess again, Too high ")

#   print(f"yay, Congrats you have gueesed the number {random_number} ")

# #3) compuer_random_number_gusser
# import random
# def computer_guess(x):
#   low = 1
#   high = x
#   feedback = ''
#   while feedback != 'c':

#     if low != high:
#         guess = random.randint(low, high)
#     else:
#       guess = low
#     feedback = input(f'Is {guess} to high(H), too low(L), or correct (C)?? ').lower()
#     if feedback == 'h':
#       high = guess - 1
#     elif feedback == 'l':
#       low = guess + 1

#   print(f'yay!, The Computer  have gussed the correct number{guess}')

# computer_guess(10)

# #4) Rock paper and scissors

# import random
# def play():
#   user = input ("'r' for rock, 'p' for paper,'s' for scissors: ")
#   computer = random.choice(['r','p','s'])
#   print(f"This is what computer chose: {computer}")

#   if user == computer:
#    return 'It is tie'
#   if is_win(user, computer):
#     return 'you win'

#   return ' you lost'

# def is_win(player, opponent):
#   if(player  == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#     return True

# print(play())
