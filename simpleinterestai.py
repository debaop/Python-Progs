p = float(input("Enter the money:"))
t = float(input("Enter the time :"))
r = float(input("Enter the persentage:"))

# calculate interest
i = p * r * t / 100

# display interest
print(f"Final interest is {i:.2f}")