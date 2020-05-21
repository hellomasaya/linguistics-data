import stanfordnlp
nlp = stanfordnlp.Pipeline(lang='hi')
# Download hindi models: https://stanfordnlp.github.io/stanfordnlp/models.html#human-languages-supported-by-stanfordnlp
# on the model_path = ~/stanfordnlp_resources/
def dependencies():
    corpus = open("../../NLA/nla-project-wps/src/final/data/hinditrain_dep.txt", 'r').read()
    problems = corpus.split('\n</p>\n')
    for problem in problems:
        print("<p>")
        sentences = problem.split('\n')
        for sentence in sentences:
            print("<s>")
            # print(sentence)
            doc = nlp(sentence)
            doc.sentences[0].print_dependencies()

dependencies()