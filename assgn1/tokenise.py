import sys

def parse(input_):
    file = open("../../NLA/nla-project-wps/src/final/data/tokens.txt","w+")
    problems = input_.split('\n</p>\n')
    for problem in problems:
        lines = problem.split('\n')
        linenumber = 0
        for line in lines:
            linenumber+=1
            tokennumber = 0
            tokens = line.split(' ')
            for token in tokens:
                tokennumber += 1
                file.write(str(tokennumber))
                file.write("        ") #8 spaces
                file.write(token)
                file.write("\n")

    file.close()

def main():
    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    parse(textinput)

main()
