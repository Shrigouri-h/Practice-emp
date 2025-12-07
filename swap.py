def swap(a, b):
    return b, a

if __name__ == "__main__":
    x = 15
    y = 30

    print("Before Swapping: x =", x, "y =", y)
    x, y = swap(x, y)
    print("After Swapping:  x =", x, "y =", y)
