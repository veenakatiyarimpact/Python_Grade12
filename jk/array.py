try:

    a = [1, 2, 3, 4, 5]
    for i in a:
        print(a[5])

except IndexError:
    print("IndexError: list index out of range")

finally:
    print("aashu")