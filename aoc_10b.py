fin = open("input_10.txt")

cscore = {')':1,']':2,'}':3,'>':4}

isclosing = {'(':')', '[':']','{':'}','<':'>'}

opening = '([{<'
closing = ')]}>'

lscores = []

for line in fin:
    stack = []
    for char in line:
        if char in opening:
            stack.append(char)
        if char in closing:
            if char == isclosing[stack[-1]]:
                stack.pop()
            else:
                break
        if char == "\n" and stack:
            compscore = 0
            for char in stack[::-1]:
                compscore = compscore*5 + cscore[isclosing[char]]
            lscores.append(compscore)

lscores.sort()          
print(lscores[len(lscores)//2])
