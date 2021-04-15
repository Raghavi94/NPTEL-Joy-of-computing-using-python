


def coll(num):
    count=1
    while(num!=1):
        if(num%2==0):
            num=int(num/2)
            count=count+1
        else:
            num=(num*3)+1
            count=count+1
    print(num,count)
coll(20)     
            
