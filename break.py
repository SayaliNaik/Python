password="python"
for i in range(4):
    pwd=input("Enter the password\n")
    if pwd==password:
        print("Hello")
        break
    else:
        print("wrong password, you have",3-i,"attempts left")
        i=i-1
        
    
