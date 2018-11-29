#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = len(sys.argv)
    if arg == 0:
        print("0 arguments.")
    elif arg == 2:
        print("1 argument:")
        print("{:s}".format(sys.argv[1]))
    else:
        print("{:d} arguments:".format(arg - 1))
        for i in range(1, arg):
            print("{:d}: {:s}".format(i, sys.argv[i]))
