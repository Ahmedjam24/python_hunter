usr_i=raw_input()
usr_i=int(usr_i)
usr=raw_input()
usr=usr.split()
list=[]
for i in range(0,usr_i):
    if(i%2!=0):
        if(int(usr[i])%2==0):
            list.extend(usr[i])
    else:
        if(int(usr[i])%2!=0):
            list.extend(usr[i])
temp=0
for i in list:
    if(temp!=0):
        print" "
    print i
    temp=1
