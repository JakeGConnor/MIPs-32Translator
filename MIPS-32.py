fp1 = open("mips_funct.txt", "r")
fp2 = open("mips_opcodes.txt", "r")
fp3 = open("mips_registers.txt", "r")
fp5 = open("Output.txt", "w")

temp = []
opcode = {}
funct = {}
reg = {}
raw = []
sc = 0
j = {}

def getOp(op):

    ans = ""
    
    fp = opcode[op]
    i = 0
    num = 6
    fp = int(fp)
    
    while(i < num):
        
        z = fp % 2
        fp = fp / 2
        ans = str(z) + ans

        i = i + 1

    return ans
        

def getReg(c):

    ans = ""
    
    if c.isdigit():
        i = 0
        num = 5
        fp = int(c)
        
        while(i < num):
        
            z = fp % 2
            fp = fp / 2
            ans = str(z) + ans

            i = i + 1

    else:
    
        fp = reg[c]
        i = 0
        num = 5
        fp = int(fp)
    
        while(i < num):
        
            z = fp % 2
            fp = fp / 2
            ans = str(z) + ans

            i = i + 1

    return ans

def getFunct(c):
    ans = ""
    
    fp = funct[c]
    i = 0
    num = 6
    fp = int(fp)
    
    while(i < num):
        
        z = fp % 2
        fp = fp / 2
        ans = str(z) + ans

        i = i + 1

    return ans

def immediate(c):
    ans = ""
    
    i = 0
    num = 16
    
    if(c.isdigit()):
        fp = int(c)
        
        while(i < num):
        
            z = fp % 2
            fp = fp / 2
            ans = str(z) + ans

            i = i + 1

    elif c in j.keys():

        fp = j[c]
        fp = int(fp)
        
        while(i < num):
        
            z = fp % 2
            fp = fp / 2
            ans = str(z) + ans

            i = i + 1

    elif c not in j.keys():
            j[c] = 10000

            fp = j[c]
            fp = int(fp)
        
            while(i < num):
        
                z = fp % 2
                fp = fp / 2
                ans = str(z) + ans

                i = i + 1
        
    else:
        
        fp = reg[c]
        fp = int(fp)
        
        while(i < num):
        
            z = fp % 2
            fp = fp / 2
            ans = str(z) + ans

            i = i + 1

    return ans

def ta(c):

    ans = ""
    
    if c in j.keys():
        
        i = 0
        num = 26
        fp = j[c]

        while(i < num):
        
            z = fp % 2
            fp = fp / 2
            ans = str(z) + ans

            i = i + 1

    else:
        i = 0
        num = 26
        fp = opcode[c]
        fp = int(fp)

        while(i < num):
        
            z = fp % 2
            fp = fp / 2
            ans = str(z) + ans

            i = i + 1

    return ans

while(True):

    line = fp1.readline()

    if(line == ""):
        break

    line = line.strip()
    line = line.split()

    temp = [line]

    funct[line[0]] = line[1]

while(True):

    line = fp2.readline()

    if(line == ""):
        break

    line = line.strip()
    line = line.split()

    temp = [line]

    opcode[line[0]] = line[1]

while(True):

    line = fp3.readline()

    if(line == ""):
        break

    line = line.strip()
    line = line.split()

    temp = [line]

    reg[line[0]] = line[1]

fp1.close()
fp2.close()
fp3.close()

f = raw_input("Enter input MIPS program: ")

fp4 = open(f, "r")

while True:

    line = fp4.readline()

    if(line == ""):
        line = fp4.readline()
        
    if(line == ""):
        break

    line = line.strip()
    line = line.replace(',', '')
    line = line.replace('(', ' ')
    line = line.replace(')', ' ')
    line = line.replace('.', '. ')
    line = line.replace(':', ' :')
    line = line.replace('##**', '')
    line = line.split()

    raw = [line]

    if(line[0] == "."):
        continue

    if(len(line) > 1):
        if(line[1] == ":"):
            j[line[0]] = 2000 + sc
            sc = sc + 1000

            continue

    if(line[0] == "la"):

        if line[0] not in j:
            j[line[2]] = 2000 + sc
            sc = sc + 1000

    if(line[0] == "syscall"):
        continue

    if(line[0] == "data"):
        break

    op = getOp(line[0])

    if(opcode[line[0]] == "0"):

        if(line[0] == "move"):
            rs = getReg(line[1])
            rd = getReg(line[2])
            rt = getReg("$zero")
            fcode = getFunct(line[0])

            print(("%s\t%s\t%s\t%s") % (line[0], line[1], line[2], line[0]))

        else:
            rs = getReg(line[1])
            rd = getReg(line[2])
            rt = getReg(line[3])
            fcode = getFunct(line[0])

            print(("%s\t%s\t%s\t%s\t%s") % (line[0], line[1], line[2], line[3], line[0]))

        fp5.write(("\n%s%s%s%s00000%s") % (op, rs, rd, rt, fcode))
        
    elif(int(opcode[line[0]]) == 1 or int(opcode[line[0]]) > 3):

        if(line[0] == "li" or line[0] == "la"):
            rs = getReg(line[1])
            rt = getReg("$zero")
            im = immediate(line[2])

            print (("%s\t%s\t%s") % (line[0], line[1], line[2]))

            fp5.write(("\n%s%s%s%s") % (op, rs, rt, im))
            
        else:
            rs = getReg(line[1])
            rt = getReg(line[2])
            im = immediate(line[3])

            print(("%s\t%s\t%s\t%s") % (line[0], line[1], line[2], line[3]))

            fp5.write(("\n%s%s%s%s") % (op, rs, rt, im))

    else:

        ta = ta(line[0])
        print(("%s\t%s") % (line[0], line[1]))

        fp5.write(("\n%s%s") % (op, ta))
        

fp5.close()
fp4.close()
