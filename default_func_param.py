# WRITE A FUNCTION THAT TAKES TWO VALUES FROM A USER AND SUM THEM UP.
# IF NO VALUES ARE PROVIDED, ASSUME DEFAULT VALUES OF 3 AND 5


def add(x=3, y=5):
    print(x + y)


try:

    first = int(float(input('enter first value: ')))
    second = int(float(input('enter second value: ')))
    add(first, second)

except ValueError:
    add()


