import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    list_name = []
    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        if emailID.find("@gmail.com") != -1:
            list_name.append(firstName)
    for i in sorted(list_name):
        print(i)