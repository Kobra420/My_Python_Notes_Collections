# key_of_maxValue_in_dict

# Find the key with the maximum value in a dictionary of numbers.

data = {
    101: 25,
    205: 45,
    307: 12,
    412: 30,
    523: 18,
    608: 50,
    719: 22,
    821: 36
}

def find_max_key(data):
    """
    Finds and returns the key with the maximum value in the given dictionary.
    """
    max_value = max(data.values())
    for key, value in data.items():
        if value == max_value:
            return key
        
    return None

print(find_max_key(data))