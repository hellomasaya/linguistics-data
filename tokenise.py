import sys

def parse(input_):
    file = open("assgn_1055.txt","w+")
    lines = input_.split('\n')
    # print("Number of lines:", len(lines))
    linenumber = 0
    tokennumber = 0
    lines.sort(key=len)
    for line in lines:
        file.write(line)
        file.write("\n")
        # if line[-1] == '.':
            # line = line[:-1] + ' ' + '.'
        # linenumber+=1
        # tokens = line.split(' ')
        # for token in tokens:
            # tokennumber += 1
#             if(linenumber<10 and tokennumber<10):
#                 token_id = '00' + str(linenumber) + '00' + str(tokennumber)
#             elif(linenumber<10 and tokennumber>9 and tokennumber < 100):
#                 token_id = '00' + str(linenumber) + '0' + str(tokennumber)
#             elif(linenumber<10 and tokennumber > 99):
#                 token_id = '00' + str(linenumber) + str(tokennumber)
#             elif(linenumber>9 and linenumber<100 and tokennumber<10):
#                 token_id = '0' + str(linenumber) + '00' + str(tokennumber)
#             elif(linenumber>9 and linenumber<100 and tokennumber>9 and tokennumber < 100):
#                 token_id = '0' + str(linenumber) + '0' + str(tokennumber)
#             elif(linenumber>9 and linenumber<100 and tokennumber > 99):
#                 token_id = '0' + str(linenumber) + str(tokennumber)
#             elif(linenumber>99 and tokennumber<10):
#                 token_id = str(linenumber) + '00' + str(tokennumber)
#             elif(linenumber>99 and tokennumber>9 and tokennumber < 100):
#                 token_id = str(linenumber) + '0' + str(tokennumber)
#             elif(linenumber>99 and tokennumber > 99):
#                 token_id = str(linenumber) + str(tokennumber)

            # print(token_id, token, "\n")
#            file.write(str(linenumber))
#            file.write(":") #8 spaces
            # file.write(str(tokennumber))
            # # file.write(token_id)
            # file.write("        ") #8 spaces
            # file.write(token)
            # file.write("        ") #8 spaces
            # file.write("POS")
            # file.write("        ") #8 spaces
            # file.write("Morph")
            # file.write("dep")
            # file.write("\n")

    file.close()

def main():
    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    parse(textinput)

main()
