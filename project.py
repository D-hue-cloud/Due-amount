def rem(p,q):
    ans=p-q
    return ans

due=float(input("How much did you need to pay? "))
you_gave=float(input("How much did you pay? "))

if you_gave>due:
    print("The restaurant owes you £", rem(you_gave,due),"0")
elif due>you_gave:
    print("You owe the restaurant £", rem(due,you_gave))
else:
    print("You paid just right!")