S = input().strip()
try:
    i = int(S)
    print(S)
except ValueError:
    print("Bad String")