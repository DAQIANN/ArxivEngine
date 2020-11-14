import json
import spacy

nlp = spacy.load('en_core_web_sm')
data = []
for line in open('arxiv-metadata-oai-snapshot.json', 'r'):
    data.append(json.loads(line))

print(data[0]['abstract'].replace('\n', ' '))

with open("combine.txt", "w") as outfile:
    for i in data:
        temp = i['abstract'].replace('\n', ' ')
        about_test = nlp(temp)
        test_sent = list(about_test.sents)
        for j in test_sent:
            if j.text != '' or j.text != ' ':
                outfile.write(j.text + '\n')

