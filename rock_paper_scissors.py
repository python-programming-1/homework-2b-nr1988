import random 
choice=random.randint(1,3)

score=0
 
human_score=0 
computer_score=0  

while True:
    human =input( "make a move! (r/s/p)") 

    print(choice)

    if choice==1:
        computer='r'
    elif choice==2:
        computer='p'
    else:
        computer='s'
    print(computer )
#human_score+=1
#computer_score+=1

    if human==computer:
        print("Its a tie")
    elif human == 'r' and computer=='s':
        print("You choice was Rock and Computer choose Scissor. You win!")
         #return [human_score+1]
    elif human =='r' and computer=='p':
        print("You choice was Rock and Computer choose Paper. Computer wins!")
        #return [computer_score+1]
    elif human =='p' and computer =='r':
        print("You choice was Paper and Computer choose Rock. You win!")
        #return[human_score+1]
    elif human =="p" and computer=='s':
        print("You choice was Paper and Computer choose Scissor. Computer wins !")
    elif human=='s' and computer=='p':
        print("Your choice was scissor and computer choose paper.You win ")
        #return[computer_score+1]
    elif human !="p" and human!="s" and human!="r":
        print("Your choice was not valid.Please try again")
    
    again=str(input("Do you want to play again?Please enter 'yes' or 'no' "))
    if again == "yes" :
        continue 
   # human =input( "make a move! (r/s/p)") 
    
    if again=="no" :
        
        print("Thanks bye!")
        
        break
    