num = int(input())
phonebook = dict()
for i in range(num):
    inp = input()
    inp = inp.split()
    phonebook[inp[0]] = phonebook.get(inp[0] ,inp[1])

while 1:
    try:
        name = input()
        if name in phonebook:
            print(str(name) + "=" + str(phonebook[name]))
        else:
            print("Not found")
    except:
        break