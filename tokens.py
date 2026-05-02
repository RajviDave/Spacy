import spacy

nlp=spacy.blank("en")

corpus=nlp("My name is rajvi dave")

for tokens in corpus:
    print(tokens)

#okay done