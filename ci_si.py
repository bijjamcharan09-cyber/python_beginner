p = int(input("enter amount : "))
print("principle amount = ", p)
c = int(input("enter time in months : "))
t = c / 12
print("time in years = ", t)
r = int(input("enter rate in percentage(%) : "))
print("rate = ", r)
i = int(p) * float(t) * int(r) / 100
print('simple intrest = ', i)
if float(t) > 3:
    i = p * (1 + r / 100) ** t - p
    print("compound intrest : ", i)
