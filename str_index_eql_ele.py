usr_i=raw_input()
usr_i=int(usr_i)
usr=raw_input()
usr=usr.split()
temp=0
for i in range(0,usr_i):
    if(i==int(usr[i])):
        if(temp!=0):
            print" "
        print i
        temp=1
