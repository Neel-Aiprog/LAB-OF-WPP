import random
class rock_paper_scissors():
    sysin=''
    syswin=0
    plawin=0
    round=0
    curr_round=0
    dcount=0
    round=int(input("pls enter uptil how many rounds you want to play\t"))  
    def current_round(cls):
        print(f"current round no:{cls.curr_round}")
    syschoice=["rock","paper","scissors"]
    def sys_choice(cls):
        print(f"system picks {cls.sysin}")
    for i in range(0,round):
        sysin=random.choice(syschoice)
        inp=input("pls enter your choice you want to select out of rock,paper,scissors\t")
        curr_round+=1
        print(f"system picks {sysin}")
        if(sysin==inp):
            dcount+=1
            print("||DRAW||")
        elif(sysin=="rock" and inp=="paper"):
            syswin+=1
            print("||SYSTEM WIN||")
        elif(sysin=="paper" and inp=="rock"):
            plawin+=1
            print("||YOU WIN||")
        elif(sysin=="paper"and inp=="scissors"):
            plawin+=1
            print("||YOU WIN||")
        elif(sysin=="scissors" and inp=="paper"):
            syswin+=1
            print("||SYSTEM WINS||")
        elif(sysin=="scissors" and inp=="rock"):
            plawin+=1
            print("||YOU WIN||")
        elif(sysin=="rock" and inp=="scissors"):
            syswin+=1
            print("||SYSTEM WINS||")
    def count(cls):
        print(f"the system has won {cls.syswin} times and player has won {cls.plawin} times and draw has occurred {cls.dcount} times")
play=rock_paper_scissors()
play.current_round()
play.count()
        