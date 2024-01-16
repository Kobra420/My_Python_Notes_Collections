# string mutation
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]
    # return string.replace(string[position], character)
    # Test cases
# s = input()
# i, c = input().split()
S = "abracadabra"
C = "K"
i = 6
s_new = mutate_string(S, int(i), C)
print(s_new)