N = int(input())
L = []
for i in range(N):
    command = input().split()
    if command[0] == 'print':
        print(L)
    elif command[0] == 'append':
        L.append(int(command[1]))
        print(L)
    elif command[0] == 'insert':
        L.insert(int(command[1]), int(command[2]))
        print(L)
    elif command[0] == 'remove':
        L.remove(int(command[1]))
        print(L)
    elif command[0] == 'reverse':
        L.reverse()
        print(L)
    elif command[0] == 'sort':
        L.sort()
        print(L)
    elif command[0] == 'pop':
        L.pop()
        print(L)
