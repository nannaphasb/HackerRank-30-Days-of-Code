n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
   
reverse_arr = arr[::-1]
for i in reverse_arr:
    print(i, end=' ')