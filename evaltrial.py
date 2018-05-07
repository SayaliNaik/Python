N = int(input())
list1=[]
for i in range(N):
    cmd=input().split()
    command=cmd[0]
    if len(cmd)>1:
        index=int(cmd[1])
        if len(cmd)>2:
            number=int(cmd[2])
            if command=='insert':
                list1.insert(index,number)
                if command=='append':
                    list1.append(index)
                    if command=='remove':
                        list1.remove(index)
                        if command=='print':
                            print(list1)
                            if command=='pop':
                                list1.pop()
                                if command=='reverse':
                                    list1.reverse()
                                    elif command=='sort':
                                        list1.sort()






if __name__ == '__main__':
    N = int(input())
    for N in range(0,1): 
        List = [] 
        List.insert(0,5) 
        List.insert(1,10) 
        List.insert(0,6) 
        print(List) 
        List.remove(6) 
        List.append(9) 
        List.append(1) 
        List.sort() 
        print(List) 
        List.remove(10) 
        List.reverse() 
        print(List)




arg1 = input()
l = []
for _ in range(int(arg1)):
    s = input().split()
    if (s[0] != 'print'):
        eval("l.{}(".format(s[0])+','.join(s[1:])+")")
    else:
        print(l)
