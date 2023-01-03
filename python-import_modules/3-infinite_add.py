#!/usr/bin/python3---task3
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[i])
    print(sum)
