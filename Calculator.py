print("------------------------------Welcome to my calculator------------------------------")
import math
import sys
n1 = int(input("Enter a number to be calculated: "))
n2 = int(input("Enter a number to be calculated: "))

while True:
    print("Enter 1 to calculate Sum ")
    print("Enter 2 to calculate division ")
    print("Enter 3 to calculate multiplication ")
    print("Enter 4 to calculate power ")
    print("Enter 5 to calculate substraction ")
    print("Enter 6 to calculate modulus of a number ")
    print("Enter 7 to calculate floor division of a number ")
    print("Enter 8 to calculate percentage")
    print("Enter 9 to calculate log, sin, cos")
    choice=0
    choice= int(input("Enter your choice "))

    if choice==0 or choice>9:
         print("Invalid choice, Try again")
         continue

    if(choice==1):
        sum= n1 + n2
        print("The sum is" , sum)

    elif(choice==2):
        if n2==0:
            print("Cannot divide by 0")
        else:
            division = n1/n2 
            print("The division is" , division)
    
    elif(choice==3):
       multiplication= n1*n2
       print("The multiplication is" , multiplication)

    elif(choice==4):
        a=int(input("Enter the value of power "))
        num= int(input("Choose 1st or 2nd number or 3 for both "))
        if num==1:
            power1= n1**a
            print("The power is"  , power1 )
        elif num==2:
            power2= n2**a 
            print("The power is"  , power2 )
        else:
            power1= n1**a
            power2= n2**a
            print("The power of n1 is"  , power1 )
            print("The power of n2 is"  , power2 )

    elif(choice==5):
        substraction= n1-n2
        print("The substraction is", substraction )

    elif(choice==6):
        if n2==0:
            print("Cannot divide by 0")
        else:
            modulus= n1%n2
            print("The modulus is ", modulus)

    elif(choice==7):
        if n2==0:
            print("Cannot divide by 0")
        else:
            floor= n1//n2
            print("The floor division of a number is ", floor)

    elif(choice==8):
        if n2==0:
            print("Cannot divide by 0")
        else:
            percentage= (n1/n2)*100
            print("The percentage is ", percentage)

    elif(choice==9):
        Num=int(input("enter 1 for log , 2 for cos , 3 for sin "))
        if(Num==1):
          print("The log of n1 is", math.log(n1),"The log of n2 is", math.log(n2) )
        elif(Num==2):
            print( "The cos of n1 is", math.cos(n1),"The cos of n2 is", math.cos(n2))
        elif(Num==3):
            print("The sin of n1 is", math.sin(n1),"The sin of n2 is", math.sin(n2)) 

    again= input("Continue? yes/no: ")
    if again== "no":
        break
