b = 1
while (b == 1):
    lst = []
    n = int(input("Enter number of elements in the bag (5 or more): "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    fold = len(lst)
    if (fold >= 5):
        b = 0
check=1
while(check==1):

    print(lst)
    print("if you want to add value to the bag enter add and for removing any value enter remove ")
    xxx=str(input())
    if(xxx=='add'):
        a=int(input("enter the value you want to add to the bag)"))
        lst.append(a)
    elif(xxx=='remove'):
        r=int(input("enter the value you want to remove from the bag"))
        if (len(lst) == 5):
            print("can't remove")
        else:
           lst.remove(r)
    else:
        print("error")
