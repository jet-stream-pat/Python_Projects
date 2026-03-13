#password program - if password is correct - get welcome message
#if password is entered incorrectly 3 times - get access denied message
password="goat"
count=0
user=input("what is your password")
if user==password:
    print("password accepted, welcome")
else:
    while (user!=password)and (count<2):
        user=input("what is your password")
        count=count+1
    print("Access denied")
        
