import sys

def parse(input_):
    file = open("./20171099_a2.txt","w+")
    lines = input_.split('\n')
    # linenumber = 0
    # lines.sort(key=len)
    lastnumber = 0
    rootnum = 0
    for line in lines:
        if line == '----------------------------------------':
            print("line")
            num = lastnumber + 1
            num = str(num)
            new = num + '\t' + '।' + '\t' + '।' + '\t' + 'PUNCT' + '\t' + 'PUNCT' + '\t' + '_' + '\t' + rootnum + '\t' + 'rsym' + '\t' + '_'+'\t'+'_'
            file.write(new)
            file.write('\n')
        file.write(str(line))
        file.write('\n')
        root = 'root'
        if root in line and line[1] == '\t':
            rootnum = str(line[0])
        elif root in line and line[1] != '\t':
            rootnum = str(line[0]) + str(line[1])

        try:
            if line[1] == '\t':
                lastnumber = int(line[0])
            else:
                lastnumber = str(line[0]) + str(line[1])
                lastnumber = int(lastnumber)
        except:
            print("not int")

        # linenumber+=1
        # tokennumber = 0
        # tokens = line.split(' ')
        # for token in tokens:
        #     tokennumber += 1
        #     file.write(str(tokennumber))
        #     file.write("\t") #8 spaces
        #     file.write(token)
        #     file.write("\n")
    file.close()

def main():
    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    parse(textinput)

main()