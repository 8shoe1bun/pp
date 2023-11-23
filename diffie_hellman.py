def power(val1, val2, div):
    if val2 == 1:
        return val1
    else:
        return (val1**val2) % div


p = int(input("Enter the prime number: "))
g = int(input("Enter the primitive root of p: "))

a = int(input("Enter the private key of A: "))
b = int(input("Enter the private key of B: "))

x = power(g, a, p)
y = power(g, b, p)

ka = power(y, a, p)
kb = power(x, b, p)

print("\nx:",x,"\ny:",y)

print("Secret key for the A:", ka)
print("Secret Key for the B:", kb)
