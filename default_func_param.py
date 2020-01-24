# WRITE A FUNCTION THAT TAKES TWO VALUES FROM A USER AND SUM THEM UP.
# IF NO VALUES ARE PROVIDED, ASSUME DEFAULT VALUES OF 3 AND 5


def add(x=3, y=5):
    print(x + y)


try:

    first = int(input('enter first value: '))
    second = int(input('enter second value: '))

except ValueError:
    first = 3
    second = 5

add(first, second)
