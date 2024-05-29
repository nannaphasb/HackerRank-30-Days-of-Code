i = int(input())

for j in range(0, i):
    s = input()
    # s [::2] = start from 0 to the end of the String skipping 2 characters (even string)
    # s [1::2] = start from 1 to the end of the String skipping 2 characters (odd string)
    print(s[::2], s[1::2])