def collatz(num):
    
    while num > 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1

        print(num)

try:
    num = int(input())
    collatz(num)

except ValueError:
            print('Invalid. Input must be an integer.')
