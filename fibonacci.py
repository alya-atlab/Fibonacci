x = int(input("Enter x: "))
f = [0, 1]

for i in range(2, x):
    f.append(0)
    f[i] = f[i - 1] + f[i - 2]
    
print(f)
    