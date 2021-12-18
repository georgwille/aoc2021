fin = open('input_18.txt')

def magnitude(sfnumber):
    v = 0
    for i,f in ((0,3),(1,2)):
        if type(sfnumber[i]) is int:
            v += f*int(sfnumber[i])
        else:
            v += f*magnitude(sfnumber[i])
    return v

def nreduce(nstring):
    nstring = nstring.replace(' ','')
    has_changed = True
    while has_changed:
        has_changed = False
        ldn_pos = 0 # left neighbor digit
        rdn_pos = -1 # right neighbor digit
        depth = 0
        for i,char in enumerate(nstring):
            if char.isdigit():
                ldn_pos = i
            if char==']':
                depth -= 1
            if char=='[':
                depth += 1
                if depth == 5: # explode
                    lb_pos = i # left bracket
                    co_pos = nstring.index(',',i) # comma
                    rb_pos = nstring.index(']',i) # right bracket
                    ex_left = nstring[lb_pos+1:co_pos] # what flies left
                    ex_right = nstring[co_pos+1:rb_pos] # what flies right
                    for j in range(rb_pos,len(nstring)):
                        if nstring[j].isdigit():
                            rdn_pos = j
                            break
                    linsert = '+'+ex_left if ldn_pos > 0 else ''
                    rinsert = ex_right+'+' if rdn_pos > 0 else ''
                    nstring = (nstring[:ldn_pos+1]+
                           linsert+
                           nstring[ldn_pos+1:lb_pos]+
                           '0'+
                           nstring[rb_pos+1:rdn_pos]+
                           rinsert+
                           nstring[rdn_pos:]
                           )
                    nstring=str(eval(nstring)).replace(' ','')
                    has_changed = True
                    break
        if has_changed:
            continue
        ldn_pos_right = 0         
        for i,char in enumerate(nstring):
            if char.isdigit():
                ldn_pos = i
                for j in range(i+1,len(nstring)):
                    if not nstring[j].isdigit():
                        ldn_pos_right = j-1
                        break
                if ldn_pos_right > ldn_pos: # split
                    to_split = int(nstring[ldn_pos:ldn_pos_right+1])
                    nstring = (nstring[:ldn_pos]+
                            '['+
                            str(to_split//2)+
                            ','+
                            str((to_split+1)//2)+
                            ']'+
                            nstring[ldn_pos_right+1:]
                    )
                    has_changed = True
                    break
    return nstring

numbers = [line.strip() for line in fin]
maxsum = 0

for i,n1 in enumerate(numbers):
    for j,n2 in enumerate(numbers):
        if i == j:
            continue
        nsum = nreduce('['+n1+','+n2+']')
        maxsum = max(maxsum,magnitude(eval(nsum)))

print(maxsum)
