from game_data import data
from os import system
from art import logo, vs
import random
A=''
B=''
def select_random(data):
  global A
  global B
  A = random.choice(data)
  B = random.choice(data)

user_score = 0
select_random(data)
A_followers = A['follower_count']
B_followers = B['follower_count']

while True:
  print(logo)
  print(f"""
  Compare A: {A['name']}, a {A['description']}, from {A['country']}
  {vs}
  Against B: {B['name']}, a {B['description']}, from {B['country']}
  """)

  if A_followers > B_followers:
    greater_followers = 'A'
  elif A_followers < B_followers:
    greater_followers = 'B'
  user_score = 0
  user_choice = input("Who has more followers? Type 'A' or 'B': ")

  if user_choice == greater_followers:
    sys("CLR")
    user_score += 1
    print(f"You were right! Your current score is: {user_score}")
    A = B
    B = random.choice(data)
    
  elif user_choice != greater_followers:
    sys("CLR")
    print(logo)
    print("Sorry, that was the wrong choice. You lost.")
    break