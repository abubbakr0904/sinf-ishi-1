ism = input("Ismlar kiriting : ")
if len(ism) != 0: 
    li = ism.split(" ")
    g = ""
    if len(li) == 1:
        print(li[0] , "like this")
    else : 
        for i in li[:-1]:
            g += i + " "
        g += " and " + li[-1] + " like this"
        print(g) 
else:
    print("no one like this")