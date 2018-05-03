
num=int(input("Enter any number"))
i=1
j=1
while (j<num+1):
    print("multiplication table for ",j)
    for i in range(1,11):
        print(j*i)
        i=i+1 
    
    j=j+1
