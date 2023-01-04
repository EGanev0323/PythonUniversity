import math

try:
    x=int(input())
    print(math.sqrt(x))
except ValueError:
    print("Invalid")
finally:
    print("Good bye")



