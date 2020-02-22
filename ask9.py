'''Τριπλασιάζω το χ, προσθέτω 1 και στην συνέχεια προσθέτω τα ψηφία του χ. 
Η διαδικασία επαναμβάνεται μέχρι ο χ να γίνει μονοψήφιος'''
x=int(input("Please, insert a number!"))
print ('x=',3*x+1)
x=3*x+1
x = str(x)
while len(x)>1:
    s=0
    for i in range (0,len(x)):
        print ("digit=",x[i])
        s=s+int(x[i])
    print("sum=",s)
    x = str(s)
