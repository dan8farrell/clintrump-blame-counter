def fib(n):
    a, b = 0, 1
    for i in range(0, n):
       a + b
    return a
file=open("fib.txt", "a")
for c in range(0, 5):
   print(fib(c))
   s = str(fib(c))
   file.write(s + "\n")
file.close()