data = {
    101: 25,
    205: 45,
    523: 18,
    307: 12,
    412: 30,
    608: 50,
    719: 22,
    821: 36
}

# sorting dictionary in ascending order of values
ascnd_dict = sorted(data.items())
# sorting dictionary in descending order of values
dscnd_dict = sorted(data.items(), reverse = True)
print(f"ascending values --> {ascnd_dict}")
print(f"descending values --> {dscnd_dict}")
