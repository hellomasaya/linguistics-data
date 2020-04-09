import os

def changeName(): 
    for count, filename in enumerate(os.listdir("./AnnCorra/Training/")): 
        dst = "train" + str(count) + ".txt"
        src = './AnnCorra/Training/'+ filename 
        dst = './AnnCorra/Training/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 

# changeName()

def makeOneTrainFile():
    data = ""
    for filename in (os.listdir("./AnnCorra/Development/")):
        filename = './AnnCorra/Development/' + filename
        file_ = open(filename, 'r')
        content = file_.read()
        data += content
        file_.close()
    
    file_ = open('final_dev.txt', 'w')
    file_.write(data)
    file_.close()

makeOneTrainFile()