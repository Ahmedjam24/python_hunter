usr_i=raw_input()
usr=raw_input()
usr=usr.split()
flag=0
for i in usr:
    count=usr.count(i)
    if(count!=1 and flag==0):
        print i
        flag=1
if(flag==0):
    print"-1"
