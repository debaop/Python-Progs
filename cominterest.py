p =float(input("Enter the total money : "))
r =float(input("Enter the Persentage here :"))
t =float(input("Enter the time here:"))
s = (p * ((1+ r / 100) ** t))
i= (p * ((1+ r / 100) ** t)) - p
print("""You have two choice if you write 's' you get the total with interest.
 But if you choose 'i' you only get the interest   """)
inp_i=input("Enter your choise:")
if inp_i == "s" :


 print( "Here is the compound interest of  " + str(p) +f" is : {s:.2f}" )
elif inp_i== "i":
 print(f" Here is the only interest: :  {i:.2f}")
else:
    print("You have selected no choise.....so try next time")