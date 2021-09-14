explanation = "This program calculates "
explanation += "the linear combination "
explanation += "of to numbers that is equal to "
explanation += "its greatest common divisor"

print(explanation)

num1 = input("Enter the first number\n")
num2 = input("Enter the second number\n")

def getGCD(m, n):
    if (n == 0 or m == 0):
        if (n == 0 and
            m == 0):
            return 1
        elif (m == 0):
            return abs(n)
        elif (n == 0):
            return abs(m)
    elif (n % m == 0 or 
        m % n == 0):
        return min(abs(m), abs(n))
    else:
        dividend = m
        divisor = n
        remainder = 0
        result = 0
        while True:
            result = remainder
            remainder = abs(dividend % divisor)
            dividend = divisor
            divisor = remainder
            if (remainder == 0):
                return result

def combination (m, n):
    x, y = 0, 0
    gcd = getGCD(m, n)
    comb = m * x + n * y
    while True:
        if (abs(comb) == abs (gcd)):
            if (comb == gcd):
                return x, y
            else:
                return -x, -y

        elif (gcd > comb):
            if (m == 0):
                y += 1
            else:
                x += 1
        elif (gcd < comb and n != 0):
            if (n == 0):
                x -= 1
            else:
                y -= 1
        comb = m * x + n * y

gcd = getGCD(int(num1), int(num2))

x, y = combination(int(num1), int(num2))

print("{}({}) + {}({}) = {}".format
      (num1, x, num2, y, gcd))