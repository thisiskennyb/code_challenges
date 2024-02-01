# create a hash map for the word balloon as a reference
# create another hashmap for the input string for the occurance of characters
#loop through the string hashmap and use the baloon key to subract the number of occurnaces
# if the occurances





def balloon(text):
    balloons = 0


    balloon_dict = {
        "b": 1,
        "a": 1,
        "l": 2,
        "o": 2,
        "n": 1
    }

    balloon_instance = {}

    for char in text:
        if char in balloon_dict:
            balloon_instance[char] = balloon_instance.get(char, 0) + 1


    while True:
        for char in balloon_dict:
            if balloon_instance[char] - balloon_dict[char] < 0:
                return balloons
            balloon_instance[char] -= balloon_dict[char] 
        balloons += 1

    


    




print(balloon("loonbalxballpoon"))