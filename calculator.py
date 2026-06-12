#get input user for the first number
num1=float(input("enter first number: "))
print("num1=",num1)

#get input for operator
sign=input("sign (+,-,*,/,^,%) :")
print("sign=",sign)

#get input for the second number
num2=float(input("enter second number: "))
print("num2=",num2)
if sign =="+":
    s=num1 + num2
    print("sum=",s)
elif sign =="-":
    d=num1 - num2
    print("difference=",d)
elif sign=="*":
    m=num1 * num2
    print("multiplication=",m)
elif sign=="/":
    q=num1 / num2
    print("quotient=",q)
elif sign=="%":
    r=num1 % num2
    print("remainder=",r)
elif sign=="^":
    result=num1 ** num2
    print("exponent=",result)
