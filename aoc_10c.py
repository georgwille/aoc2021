fin = open("input_10.txt")

c1score = {")": 3, "]": 57, "}": 1197, ">": 25137}
c2score = {')':1,']':2,'}':3,'>':4}

isclosing = {'(':')', '[':']','{':'}','<':'>'}

opening = '([{<'
closing = ')]}>'

errorscore = 0
lscores = []

for line in fin:
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if char == isclosing[stack[-1]]:
                stack.pop()
            else:
                errorscore += c1score[char]
                break
        elif char == "\n" and stack:
            compscore = 0
            for char in stack[::-1]:
                compscore = compscore*5 + c2score[isclosing[char]]
            lscores.append(compscore)

print(errorscore)
lscores.sort()          
print(lscores[len(lscores)//2])
