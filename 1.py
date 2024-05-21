
def lower_triangular(n):
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()


def upper_triangular(n):
    for i in range(n):
        for j in range(n):
            if j < i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()


def pyramid(n):
    for i in range(n):
        # Print leading spaces
        for j in range(n - i - 1):
            print(' ', end=' ')
        # Print stars
        for k in range(2 * i + 1):
            print('*', end=' ')
        print()


n = 5
print("Lower Traingle ==> ")
lower_triangular(n)
print("Upper Traingle ==>")
upper_triangular(n)
print("Pyramid Traingle ==>")
pyramid(n)
