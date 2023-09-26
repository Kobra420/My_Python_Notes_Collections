import random
# rand_integer = random.randint(1, 2)
# print(rand_integer)

# random float
# rand_float1 = random.random()
# random float range
# rand_float = rand_float1 * 21
# print(rand_float)
# Love Calculator using random module
#input("Enter your name:")
#input("Enter your lover's name")
#rand_integer = random.randint(1, 100)
#print(f"your Love-score is {rand_integer}%.")
states_of_India = ["Monipure"]
UTs_of_India = ["Ladakh"]
states_of_India.append("Nagaland")
states_of_India.append("Arunachaal Pradesh")
states_of_India.extend(["Arunachaal Pradesh", "Mizorum", "Assam", "Tripura", "Meghalay"])

UTs_of_India.append("Andaman & Nicobar")
UTs_of_India.append("Daman and Diu")
UTs_of_India.extend(["Pondicherry", "Lakshadweep", "Jammu and Kashmir"])
print(states_of_India, UTs_of_India, sep="\n",end="\n")
some_sates_uts = [states_of_India, UTs_of_India]
print(some_sates_uts)
some_sates_uts[0][0] = "X"
print(some_sates_uts)
print(states_of_India)
print(UTs_of_India)
print(states_of_India[len(states_of_India)-2])