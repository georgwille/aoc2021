fin = open("input_10.txt")

cscore = {")": 3, "]": 57, "}": 1197, ">": 25137}

isclosing = {"(": ")", "[": "]", "{": "}", "<": ">"}

opening = "([{<"
closing = ")]}>"

errorscore = 0

for line in fin:
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        if char in closing:
            if char == isclosing[stack[-1]]:
                stack.pop()
            else:
                errorscore += cscore[char]
                break

print(errorscore)
