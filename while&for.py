#WHILE LOOP EXAMPLE: CONTINUOUS ADDITION
total = 0
while True:
    calcu = int(input("Enter a number to add (press 0 to stop): "))
    if calcu == 0:
        break
    total += calcu

print(f"The total sum of the numbers is {total}.")


#FOR LOOP EXAMPLE: POWER TABLE
number = int(input("Enter a number as a base: "))
n = int(input("Enter the number of powers you are looking for: "))
power = 1

print(f"Presenting a power table of {number}:")
for exponent in range(n+1):
    print(f"{number} to the power of {exponent} is {power}.")
    power *= number



