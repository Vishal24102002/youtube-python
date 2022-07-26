n=int(input("enter numbe of your choice"))
c=n//100
if c==0:
    print( "the number entered is 2 digit")
    one=n//10
    print("first digit",one)
    second=n-(one*10)
    print("second digit is",second)
    check=(one**2)+(second**2)
    if check==n:
        print("yes it is a amstrong number",n)
    else:
        print("no it is not a amstrong number")
elif c!=0:
    print("the number is three digit")
    onee=n//100
    print("hundredth digit is ", onee)
    twoo=(n-(onee*100))//10
    #twoo=three//10
    print("tenth digit is ", twoo)
    three=(n-(onee*100))-(twoo*10)
    print("ones digit is ",three)
    equal=(onee**3)+(twoo**3)+(three**3)
    if equal==n:
        print("yes it is a amstrong number")
    else:
        print("no the entered number is not a amstrong number")
else:
    print("the number is three digit")