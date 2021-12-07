print("Welcome to Rock Paper Scissor\n")
choice = input("type rock, paper, or scissors to play\n")
i = 1

while i == 1:
  if choice == "rock":
   print(">paper\n...")
   print("you lose")
   choice = input("try again?\n")
  elif choice == "paper":
   print(">scissors\n...")
   print("you lose")
   choice = input("try again?\n")
  elif choice == "scissors":
   print(">rock\n...")
   print("you lose")
   choice = input("try again?\n")
  elif choice == "gun":
    print(">AAAAH!")
    print("...\nyou win")
    i -= 1
  else:
    print("...\nthats not an option!")
    choice = input("try again?\n")






