#n=int(input("Enter N : "))

#if n%2==0:
    #print(n," Is Not Prime")
#else:
    #for i in range(3,int(n/2)+1,2):
        #if n%i==0:
            #print(n," Is Not Prime")
            #break
    #else:
        #print(n," Is Prime")
print("*****************************************************")

n=int(input("Enter N :"))

if n%2==0:
    print(n,"is not prime")
else:
    for i in range(3,int(n/2)+1,2):
        if n%i==0:
            print(n,"is Not Prime")
            break
    else:
        print(n,"Is Prime")
print("*****************************************************")







            
    
    
