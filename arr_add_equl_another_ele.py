usr_i=raw_input()
usr_i=int(usr_i)
usr=raw_input()
usr=usr.split()
for i in range(0,usr_i):
    for j in range (i+1,usr_i):
        for k in range(j+1,usr_i):
            if(int(usr[i])+int(usr[j])==int(usr[k])):
                temp=0
                if(temp!=0):
                    print"\n"
                print usr[i]+" "+usr[j]+" "+usr[k]
