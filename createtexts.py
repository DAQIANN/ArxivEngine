import json
import spacy

file_n = "intro_text.txt"
nlp = spacy.load('en_core_web_sm')

'''
intro_file_text = open(file_n).read()
intro_doc = nlp(intro_file_text)
print([token.text for token in intro_doc])
'''
about_text = ('Gus Proto is a Python developer currently'
                    ' working for a London-based Fintech'
                    ' company. He is interested in learning'
                    ' Natural Language Processing.')

about_doc = nlp(about_text)
sentences = list(about_doc.sents)
#print(sentences)
'''
for token in about_doc:
    print (token, token.idx, token.text_with_ws,
        token.is_alpha, token.is_punct, token.is_space,
        token.shape_, token.is_stop)

def set_custom_boundaries(doc):
        # Adds support to use `...` as the delimiter for sentence detection
    for token in doc[:-1]:
        if token.text == '...':
            doc[token.i+1].is_sent_start = True
    return doc

ellipsis_text = ('Gus, can you, ... never mind, I forgot'
                ' what I was saying. So, do you think'
                ' we should ...')
# Load a new model instance
custom_nlp = spacy.load('en_core_web_sm')
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)
'''

test_abs = ("A fully differential calculation in perturbative quantum chromodynamics is"
" presented for the production of massive photon pairs at hadron colliders. All"
" next-to-leading order perturbative contributions from quark-antiquark,"
" gluon-(anti)quark, and gluon-gluon subprocesses are included, as well as"
" all-orders resummation of initial-state gluon radiation valid at"
" next-to-next-to-leading logarithmic accuracy. The region of phase space is"
" specified in which the calculation is most reliable. Good agreement is"
" demonstrated with data from the Fermilab Tevatron, and predictions are made for"
" more detailed tests with CDF and DO data. Predictions are shown for"
" distributions of diphoton pairs produced at the energy of the Large Hadron"
" Collider (LHC). Distributions of the diphoton pairs from the decay of a Higgs"
" boson are contrasted with those produced from QCD processes at the LHC, showing"
" that enhanced sensitivity to the signal can be obtained with judicious"
" selection of events.")

about_test = nlp(test_abs)
test_sent = list(about_test.sents)
#print(test_sent)

subject = []
temp = ""
for i in range(len(test_sent)):
    for chunk in test_sent[i].noun_chunks:
        temp = ""
        #print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
        if chunk.root.dep_ == 'nsubj' or chunk.root.dep_ == 'nsubjpass': 
            for p in chunk:
                if not p.is_stop and str(p).isalpha():
                    temp += p.lemma_
                    temp += " "
            subject.append(temp)
        if temp != ' ': print(temp)
        break        
        #if chunk.root.dep_ == "nsubj":
        #    print(chunk.text)

#print(len(test_sent))
#print(len(subject))

with open('combine.txt', 'r') as outfile:
    temp = outfile.readline()
    while temp != '':
        print(temp)      
        temp = outfile.readline()

'''
small_test = nlp(str(',D^{k}_{x}(u_{x}-u^{2}))]$$ into the equation $$v_{t}=(D^{3}_{x}+4vD_{x}+2v_{x})[s(x,v,{{\partial v}\over{\partial x }},'))
for chunk in small_test:
    if chunk.lemma_.isalpha(): print(chunk.lemma_)
'''
        