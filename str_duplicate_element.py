usr_i=raw_input()
usr=raw_input()
usr=usr.split()
end=int(usr_i)
uni=0
temp=0
flag=200000
for i in range (0,end):
    start=i+1
    for j in range(start,end):
        if(usr[i]==usr[j]):
            uni=1
            if(flag!= usr[j]):
                if (temp != 0):
                    print" "
                print usr[i]
                flag=usr[j]
                temp=1
if(uni==0):
    print "unique"
