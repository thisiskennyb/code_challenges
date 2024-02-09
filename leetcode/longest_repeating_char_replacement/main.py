def charReplacement(s, k):
    left = right = ans = 0
    most_freq_char = 0

    char_counts = {}

    while right < len(s):
        char_counts[s[right]] = char_counts.get(s[right], 0) + 1

        window_size = right - left + 1
        for char in char_counts:
            most_freq_char = max(most_freq_char, char_counts[char])
        
        if window_size - most_freq_char <= k:
            ans = max(ans, window_size)
        else:
            char_counts[s[left]] -= 1
            left += 1
        right += 1
    return ans