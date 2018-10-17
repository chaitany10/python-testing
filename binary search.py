def binary(l,u,a,x):
    mid = (l+u)//2
    if(l<u):
        if(x<a[mid]):
            binary(l,mid-1,a,x)
        elif(x>a[mid]):
            binary(mid+1,u,a,x)
        else:
            print("Element found at position "+str(mid+1))
    else:
        print("element not found")

n=int(input("enter no. of elements"))
a=[]
for i in range(n):
    a.append(int(input("enter an array")))

x=int(input("elemnt to be found"))
binary(0,n,a,x)