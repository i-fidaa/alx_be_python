n = int(input("Enter the size of the pattern: "))
i = 0
while i < n :
    for j in range(n):
        print("*", end="")
    print()
    i += 1