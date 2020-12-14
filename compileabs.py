import json
import spacy

nlp = spacy.load('en_core_web_sm')
data = []
count = 0
for line in open('arxiv-metadata-oai-snapshot.json', 'r'):
    if count > 10000:
        break
    data.append(json.loads(line))
    count += 1

print(data[0]['abstract'].replace('\n', ' '))

with open("small_combine.txt", "w") as outfile:
    for i in data:
        temp = i['abstract'].replace('\n', ' ')
        #about_test = nlp(temp)
        test_sent = list(temp.split('.'))
        for j in test_sent:
            if j != '' or j != ' ':
                outfile.write(j + '\n')

