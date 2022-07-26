# so let get to the code for amstrong number let get started
#first we have to take input from the user 
n=int(input("ener the number which has to checked"))
#not we have to check weather the number is two digit or three digit number so we are going to use 
#if else coditions 
c=n//100
if c==0:
    print("the entered number is a two digit number")
    #as if we divide any two digit number lets say 34/100=0.34 but // means approx value so 
    #34//100=0 therefore we are able to know that the number is two digit
elif c!=0:
    print("the number is three digits")

else:
    print("the number is more than 4 digits")
    #this program will tell us weather the number is three digit or two digit 
    #the next part will be continued in next upcoming video
   # thanks for watching