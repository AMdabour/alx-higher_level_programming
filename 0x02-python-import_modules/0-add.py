#!/usr/bin/python3
# skip thhe code if it imported
if __name__ == "__main__":
    a = 1
    b = 2

    from add_0 import add
    result = add(1, 2)
    print("{} + {} = {}".format(a, b, result))
