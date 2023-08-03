
#################################################################
#######DEFINING FUNCTIONS TO PERFORM OPERATION ON SHAPES.#######
#################################################################

b=["square","rectangle","triangle","circle"]
    
def sq():
    s1=float(input(print("Enter side")))
    print("Perimeter = ", s1*4," units")
    print("Area = ",s1*s1," sq. units")

def rect():
    l=float(input(print("Enter Length =")))
    b=float(input(print("Enter Breadth =")))
    print("Perimeter = ", 2*(l+b)," units")
    print("Area = ",l*b," sq. units")

def tri():
    s1=float(input(print("Enter side1 =")))
    s2=float(input(print("Enter side2 =")))
    s3=float(input(print("Enter side3 =")))
    #we'll find area with the help of Heron's formuka.
    sp=float((s1+s2+s3)/2)
    print("Perimeter = ", s1+s2+s3," units")
    print("Area = ",((sp*(sp-s1)*(sp-s2)*(sp-s3))**0.5)," sq. units")

def cir():
    r=float(input(print("Enter Radius =")))
    print("Perimeter = ", 2*3.14*r," units")
    print("Area = ",22/7*r*r," sq. units")

#################################################################
#################################################################

def main():
    a = input(print("Enter name of shape = "))
    #taking shape to perform operations
    for i in b:
        if i==a.lower():#lower() function is used to avoid any capital letter.
            print("It's  a 2d shape.")
            print("Tell us more about shape...")


            #this is to perform operations
            if i=="circle":
                cir()
            elif i=="square":
                sq()
            elif i=="rectangle":
                rect()
            elif i=="triangle":
                tri()
            else:
                print("please choose from following list :")
                print(b)
                
    main() #this calling is to run program on loop after ending one operastion.

main() #this calling is to run main program which will work in frontend or to start program.

#################################################################
#NOTE- YOU CAN ADD MORE SHAPES BY ADDING THEM INTO LIST AND ENTERING THEIR RESPECTIVE FORMULA.
#################################################################

