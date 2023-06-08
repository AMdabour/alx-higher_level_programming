#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 1:
        print("0 arguments.")
    else:
        if len(argv) == 2:
            print("1 argument:")
        else:
            print(f"{len(argv) - 1} arguments:")
        index = 1
        for item in argv[1:]:
            print(f"{index}: {item}")
            index += 1
