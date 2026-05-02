import spacy

nlp=spacy.blank("en")

doc=nlp("My name is rajvi and I am in google working as SWE and i am so passionate about what i am doing hureyy")

for tokens in doc:
    print(tokens)
