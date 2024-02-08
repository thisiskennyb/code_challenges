# Create hash map with frequency of each character
# Loop through hash map and map frequency as key to character as value
# Create variable with the highest frequency
# Create a loop with a range to highest frequency and build an array using .append
# return the reversed array

def sort_by_freq(s):
    char_to_freq = {}
    freq_to_char = {}
    most_freq = 0
    freq_list = []

    for char in s:
        char_to_freq[char] = char_to_freq.get(char, 0) + 1

    for key, value in char_to_freq.items():
        if value in freq_to_char:
            freq_to_char[value].append(key)
        elif value not in freq_to_char:
            freq_to_char[value] = [key]
        most_freq = max(most_freq, value)

    for i in range(most_freq, 0, -1):
        if i in freq_to_char:
            for j in range(len(freq_to_char[i])):
                freq_list.append(freq_to_char[i][j]*i)

    return "".join(freq_list)







print(sort_by_freq("tree"))