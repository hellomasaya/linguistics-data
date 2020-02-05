import sys

def parse(input_):
    file = open('tokens_1055.txt', 'w+')
    lines = input_.split('\n')
    # print("Number of lines:", len(lines))
    linenumber = 0
    tokennumber = 0
    for line in lines:
        last = line[-1]
        line = line[:-1] + ' ' + str(last)
        linenumber+=1
        tokens = line.split(' ')
        for token in tokens:
            tokennumber += 1
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
            # file.write("\t") #8 spaces
            file.write(str(token))
            # file.write("        ") #8 spaces
            # file.write("POS")
            # file.write("        ") #8 spaces
            # file.write("Morph")
            # file.write("dep")
            file.write("\n")

    file.close()
    # print(tokennumber)


def compare():
    f2 = open('dep_1055.txt', 'r')
    # f3 = open('tokens_1055.txt', 'r')
    f2=f2.read()
    # f3=f3.read()
    sen = f2.split("<s>")
    for line in sen:
        line = line.split("\n")
        for a_line in line:
            words = a_line.split(',')

            words[0]=words[0].lstrip('(\'')
            words[0]=words[0].rstrip('\'')
            print(words[0])

            
            # for word in words[0]:
                # print(word,"\n\n\n")
                # tokens = word.split("\'")
                # print(tokens,"\n\n\n\n")


def main():
    filehandle = open(sys.argv[1], 'r')
    textinput = filehandle.read()
    parse(textinput)
    compare()

main()
