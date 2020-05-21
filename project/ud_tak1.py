import stanfordnlp
nlp = stanfordnlp.Pipeline(lang='hi')
# Download hindi models: https://stanfordnlp.github.io/stanfordnlp/models.html#human-languages-supported-by-stanfordnlp
# on the model_path = ~/stanfordnlp_resources/

def dependencies():
    corpus = open('../project/anntask1-raw-sent.txt', 'r').read()
#     corpus = "रम खाना खाने गया।\n"
    sentences = corpus.split('\n')
    count =0
    for sentence in sentences:
        count+=1
        print("<s>", count)
        doc = nlp(sentence)
        doc.sentences[0].print_dependencies()
#     print(count)

# run on terminal to get the output: python3 assgn1.py > dependency_asgn1.txt
## where assign1.py has **this cell and the above ones only**
dependencies()