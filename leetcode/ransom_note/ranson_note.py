def ransom_note(ransomNote, magizine):
    mag_dict = {}

    for letter in magizine:
        mag_dict[letter] = mag_dict.get(letter, 0) + 1

    for let in ransomNote:
        if let in mag_dict and mag_dict[let] >= 1:
            mag_dict[let] -= 1
        else:
            return False
        
    return True

    



rnote = 'aa' 
mag = 'ab'
print(ransom_note(rnote,mag))