import json
import spacy
import tarfile
from tqdm import tqdm
import os

'''
Compress and decompress code from https://www.thepythoncode.com/article/compress-decompress-files-tarfile-python
'''
def compress(tar_file, members):
    """
    Adds files (`members`) to a tar_file and compress it
    """
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()

def decompress(tar_file, members=None):
    """
    Extracts `tar_file` and puts the `members` to `path`.
    If members is None, all members on `tar_file` will be extracted.
    """
    tar = tarfile.open(tar_file, mode="r:gz")
    if members is None:
        members = tar.getmembers()
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    '''
    for member in progress:
        tar.extract(member, path=path)
        # set the progress description of the progress bar
        progress.set_description(f"Extracting {member.name}")
    '''
    # or use this
    tar.extractall(members=members)
    # close the file
    tar.close()


nlp = spacy.load('en_core_web_sm')

def get_sents(filename):
    sents = []
    d_sents = {}
    with open(filename, 'r') as outfile:
        line = outfile.readline()
        count = 0
        while True:
            if count > 10000:
                break
            count += 1
            if len(line) > 5:
                #sents.append(line)
                about_test = nlp(line)
                temp = ""
                for chunk in about_test.noun_chunks:
                    #print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
                    if chunk.root.dep_ == 'nsubj' or chunk.root.dep_ == 'nsubjpass': 
                        for p in chunk:
                            if not p.is_stop and str(p).isalpha():
                                temp += p.lemma_
                                temp += " "
                        break
                d_sents[line] = temp
            line = outfile.readline()
    #make dictionary and put second value as the subject of sentence
    return d_sents

def get_subject(lines, index):
    subject = []
    #print("DONE")
    count = 0
    for i in lines:
        about_test = nlp(i)
        #test_sent = list(about_test)
        temp = ""
        #for i in range(len(test_sent)):
        for chunk in about_test.noun_chunks:
            temp = ""
            #print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
            if chunk.root.dep_ == 'nsubj' or chunk.root.dep_ == 'nsubjpass': 
                for p in chunk:
                    if not p.is_stop and str(p).isalpha():
                        temp += p.lemma_
                        temp += " "
                    
            if len(temp) > 1: 
                subject.append(i)
                break
        count += 1
        print(count)
                        
    return subject

def get_related(lines, subject, check):
    line = ""
    for i in len(subject):
        if subject[i] != "-":
            if check == subject[i]:
                line += lines[i]
                line += " "
    return line

def get_subject_two(lines, subj):
    subject = []
    #print("DONE")
    count = 0
    for i in lines:
        about_test = nlp(i)
        #test_sent = list(about_test)
        temp = ""
        #for i in range(len(test_sent)):
        for chunk in about_test.noun_chunks:
            temp = ""
            #print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
            if chunk.root.dep_ == 'nsubj' or chunk.root.dep_ == 'nsubjpass': 
                for p in chunk:
                    if not p.is_stop and str(p).isalpha():
                        temp += p.lemma_
                        temp += " "
                    
            if len(temp) > 1 and (temp.strip() is subj.strip()): 
                subject.append(i)
            break         
    return subject

def get_subject_dict(lines, index):
    subject = []
    #print("DONE")
    count = 0
    for i in lines:
        about_test = nlp(i)
        #test_sent = list(about_test)
        temp = ""
        #for i in range(len(test_sent)):
        for chunk in about_test.noun_chunks:
            temp = ""
            #print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)
            if chunk.root.dep_ == 'nsubj' or chunk.root.dep_ == 'nsubjpass': 
                for p in chunk:
                    if not p.is_stop and str(p).isalpha():
                        temp += p.lemma_
                        temp += " "
                    
            if len(temp) > 1: 
                subject.append(i)
        count += 1
        print(count)
        break
                        
    return subject

if __name__ == "__main__":
    decompress("compressed.tar.gz")
    get_sents("small_combine.txt")
    compress("compressed.tar.gz", ["arxiv-metadata-oai-snapshot.json", "small_combine.txt"])

    try:
        os.remove("arxiv-metadata-oai-snapshot.json")
        os.remove("small_combine.txt")
    except OSError as e:
        print("Error: %s : %s" % ("extracted", e.strerror))
    




