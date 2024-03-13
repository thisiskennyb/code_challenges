# Input: string of DNA
# Initiale a hashset mapping complimentary symbols
# Initialize empty array to append symbol compliments
# Loop through input string and append complimentary values to empty array

def comp_dna(dna):
    
    compliments = {
        "T": "A",
        "A": "T",
        "C": "G",
        "G": "C"
    }

    complimentary_dna = [compliments[char] for char in dna]

    # for char in dna:
    #     complimentary_dna.append(compliments[char])

    return "".join(complimentary_dna)


print(comp_dna("ATTGC"))