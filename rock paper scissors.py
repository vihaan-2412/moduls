import random
while True:
   user = input("Enter your choice (rock, paper, scissors): ").lower()
   computer = random.choice(['rock', 'paper', 'scissors'])
   print(f"Computer chose: {computer}")
   print(f"You chose: {user}")
   if user == computer:
    print("It's a tie!")
   elif user == 'rock' and computer == 'scissors':
        print("You win!")
   elif user == 'paper' and computer == 'rock':
        print("You win!")
   elif user == 'scissors' and computer == 'paper':
        print("You win!")
   elif user == 'scissors' and computer == 'rock':
        print("Computer wins!")
   elif user == 'paper' and computer == 'scissors':
        print("Computer wins!")
   elif user == 'rock' and computer == 'paper':
         print("Computer wins!")

   opinion = input("Do you want to play again? (yes/no): ").lower()
   if opinion == 'yes':
    continue
   elif opinion == 'no':
    print("Thanks for playing!")
    break