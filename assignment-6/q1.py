class password_manager():
    old_passwords=["1","2","3","4"]
    current_pass=old_passwords[len(old_passwords)-1]
    def get_password(cls):
        print(f"your current password is {cls.current_pass}")
    def set_password(cls):
        passw=input("enter your password you want to set\t")
        if not(passw  in cls.old_passwords):
            print("your password is set to your input")
            cls.current_pass=passw
            print(f"your current password is {cls.current_pass}")
        else:
            print("pls enter another password your input password is already there")
            passw1=input(" AGAIN !! YOU HAVE ONLY ONE ATTEMPT ENTER CAREFULLY!!! enter your password you want to set\t")
            cls.current_pass=passw1
            if not(passw1  in cls.old_passwords):
                print("your password is set to your input")
                cls.current_pass=passw1
                print(f"your current password is {cls.current_pass}")
    def is_correct(cls):
        trial=input("enter your string\t")
        if(trial==cls.current_pass):
            print("True")
        else:
            print("False")
neel=password_manager()
choice=int(input("enter your choice\t"))
if(choice!=0):
    match(choice):
        case 1:neel.get_password()
        case 2:neel.set_password()
        case 3:neel.is_correct()
        case _:print("wrong choice choose only between 1 and 3")
else:
    print("exiting rn...")
    exit()
        
            
            
    
    