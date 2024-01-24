def valid_parenth(s):
    openers = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    

    stack = []


    for i in s:
        if i in openers:
            stack.append(i)
        elif stack and openers[stack[-1]] == i:
            stack.pop()
        else: return False
    return not stack







input = "()[]()"
print(valid_parenth(input))