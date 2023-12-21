# Dictionary Words as keys and frequencies of the words as values
word_list = ["adventure", "exploration", "curiosity", "knowledge", "serendipity", "wanderlust", "discovery", "perception", "insight", "inquisitive", "exploration", "curiosity", "knowledge","exploration", "curiosity", "knowledge","adventure","serendipity", "wanderlust", "discovery","adventure","serendipity", "wanderlust", "discovery","adventure","wanderlust", "discovery", "perception", "insight", "inquisitive","wanderlust", "discovery", "perception", "insight", "inquisitive","perception","serendipity", "wanderlust", "discovery", "insight", "inquisitive","perception", "insight", "inquisitive"]

# Using a dictionary to count word frequencies
word_frequencies = {}
for word in word_list:
    if word in word_frequencies:
        word_frequencies[word] += 1
    else:
        word_frequencies[word] = 1

# Displaying word frequencies
print("Word Frequencies:")
for word, frequency in word_frequencies.items():
    print(f"word - {word}: Frquencie - {frequency}")
