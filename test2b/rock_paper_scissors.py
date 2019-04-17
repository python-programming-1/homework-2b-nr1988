import random 
choice=random.randint(1,3)

score=0
 
    
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
    #return [human_score+1]
    print("You choice was Rock and Computer choose Scissor. You win!")
elif human =='r' and computer=='p':
    print("You choice was Rock and Computer choose Paper. Computer wins!")
elif human =='p' and computer =='r':
    #return[human_score+1]
    print("You choice was Paper and Computer choose Rock. You win!")
elif human =="p" and computer=='s':
    print("You choice was Paper and Computer choose Scissor. Computer wins !")
elif human !="p" and human!="s" and human!="r":
    print("Your choice was not valid.Please try again")
    
again=str(input("Do you want to play again?Please enter 'yes' or 'no' "))
if again == "yes" :
    human =input( "make a move! (r/s/p)") 
if again=="no" :
    
    print("Thanks bye!")
    