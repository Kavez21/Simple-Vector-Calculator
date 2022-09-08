

print('''**********///WELCOME TO CALCULATION OF VECTORS///*************''')

option=input('''Select an option
Enter "1" Find Cross Product
Enter "2" Find Scalar Product
Enter "3" Find The angle
Enter "4" Find The Modulus
''')

if option=='1':
    i_vector = float(input("Type i:  "))
    j_vector = float(input("Type j: "))
    k_vector = float(input("Type k: "))
    ii_vector = float(input("Type i: "))
    jj_vector = float(input("Type j: "))
    kk_vector = float(input("Type k: "))

    cross_1 = (j_vector * kk_vector) - (k_vector * jj_vector)
    cross_2 = (i_vector * kk_vector) - (k_vector * ii_vector)
    cross_3 = (i_vector * jj_vector) - (j_vector * ii_vector)
    print(cross_1, 'i'',', cross_2, 'j'',', cross_3, 'k''.')


elif option=='2':
    i_vector=float(input("Type i:  "))
    ii_vector=float(input("Type i: "))
    j_vector=float(input("Type j: "))
    jj_vector=float(input("Type j: "))
    k_vector=float(input("Type k: "))
    kk_vector=float(input("Type k: "))

    scalar_1=(i_vector*ii_vector)
    scalar_2=(j_vector*jj_vector)
    scalar_3=(k_vector*kk_vector)
    print(scalar_1,'i', scalar_2,'j',scalar_3,'k')

elif option=='3':
    angle=input('''Select an option
    Enter "1" To find SINE
    Enter "2" To find COS 
    Option: ''' )

    if angle== '1' :
        print("Welcome")

    else :
        print("Get Out")
    print("θ")

elif option=='4' :
    mod_vector1=float(input("Type i:  "))
    mod_vector2=float(input("Type j: "))
    mod_vector3=float(input("Type k: "))

    mod_vector11 = pow(mod_vector1, 2)
    mod_vector22= pow(mod_vector2, 2)
    mod_vector33 = pow(mod_vector3, 2)

    mod_vector= mod_vector11+mod_vector22+mod_vector33
    modular=sqrt(mod_vector)

    print(modular)



else:
    print("Wrong Input")










                    
