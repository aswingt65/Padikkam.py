import random
while True:
  print('1.Roll the dice\n2.Exit')
  option = int(input("Select you option(1/2) : "))
  if option==1:
    number = random.randint(1,6)
    print("------------------------")
    print("The Dice landed on : ",number)
    print("------------------------")
  elif option==2:
    break
  else:
    print("Invalid option")