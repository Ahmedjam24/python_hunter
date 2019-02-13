usr_n=int(raw_input())
usr_arr=raw_input()
usr_arr=usr_arr.split()
min=int(usr_arr[0])
for i in range(0,usr_n):
    for j in range (0,usr_n):
        if(int(usr_arr[i])>int(usr_arr[j])):
            t=usr_arr[i]
            usr_arr[i]=usr_arr[j]
            usr_arr[j]=t
for i in usr_arr:
    print i
