import sys

def parse(input_):
    file = open("./assgn2_20171099.txt","w+")
    lines = input_.split('\n')
    linenumber = 0
    lines.sort(key=len)
    for line in lines:
        linenumber+=1
        tokennumber = 0
        tokens = line.split(' ')
        for token in tokens:
            tokennumber += 1
            file.write(str(tokennumber))
            file.write("\t") #8 spaces
            file.write(token)
            file.write("\n")
    file.close()

def main():
    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    parse(textinput)

main()
