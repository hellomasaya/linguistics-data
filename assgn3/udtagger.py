import stanfordnlp
nlp = stanfordnlp.Pipeline(lang='hi')

def dependencies():
    corpus = open('corpus_1055.txt', 'r')
    corpus = corpus.read()
    sentences = corpus.split('\n')
    tokennum = 0
    for sentence in sentences:
        print("<s>")
        doc = nlp(sentence)
        doc.sentences[0].print_dependencies()
        tokens = sentence.split(' ')
        for token in tokens:
            tokennum +=1
    print(tokennum)