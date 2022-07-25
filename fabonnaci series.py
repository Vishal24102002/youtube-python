#hello guys so today we are going to create a project in which we are going to print fabonacci series using python 
#so first of all what is fabonacci series it is just the sum of the previous two terms such as 0,1,1,2,3,5,8,13,21 and so on upto infinity
#so first we have to take an input fron user 
nterm=int(input("enter the ending value of the series"))
#now we have to fix two value for the starting purpose so 
a=0
b=1
print (a)
print(b)
#and now we have to use while loop over here thus
count=0
while(count<nterm):
    
    count=a+b
    print(count)
    #swapping is done here just to replace the value of a with  b and that of b with the sum of earlier 
    #numbers
    a=b
    b=count
    #lets run this code and hope for desired result
# the code works but it takes a value extra then the ending value