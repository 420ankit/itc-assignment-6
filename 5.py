s = input("Enter  your hyphne separated words.")
list = s.split('-')
x = sorted(list)
for i in range(0, len(x)-1):
    print(x[i], end="-")
print(x[len(x)-1])
