#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    alfom = dir()
    for l in range(0, len(alfom)):
        if alfom[l][:2] != "__":
            print("{:s}".format(alfom[l]))
