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
    # or use this
    tar.extractall(members=members)
    # close the file
    tar.close()


nlp = spacy.load('en_core_web_sm')

def get_sents(filename):
    d_sents = {}
    with open(filename, 'r') as outfile:
        line = outfile.readline()
        while line:
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
                if temp not in d_sents:
                    d_sents[temp] = line.rstrip() + '.'
                else:
                    d_sents[temp] = line.rstrip() + '.' + d_sents[temp]
                #print(temp)
            line = outfile.readline()
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

def get_related(lines, check):
    line = ""
    if check in lines:
        line = lines[check]
        '''
        if lines[key] != "-":
            if lines[key].strip() == check.strip():
                line += key
                line += "."
                lines[key] = "-"
        '''
    return line

def removeFiles(paths):
    try:
        for i in paths:
            os.remove(i)
    except OSError as e:
        print("Error: %s : %s" % ("extracted", e.strerror))

#if __name__ == "__main__":
    #decompress("compressed.tar.gz")
    #somethign, some = get_related(get_sents("small_combine.txt"), "we")
    #print(some)
    #compress("compressed.tar.gz", ["arxiv-metadata-oai-snapshot.json", "small_combine.txt"])
    #removeFiles(["arxiv-metadata-oai-snapshot.json", "small_combine.txt"])
    '''
    test = "We give a data structure that supports both operations in O(1) time on the RAM model and requires ${\cal B}(n,m) + o(n) + O(\lg \lg m)$ bits to store a set of size $n$, where ${\cal B}(n,m) = \ceil{\lg {m \choose n}}$ is the minimum number of bits required to store any $n$-element subset from a universe of size $m$"
    rah = test.split()
    diff_sent = ""
    for i in rah:
        if not rah.is_stop():
            diff_sent += i
            diff_sent += " "
    print(diff_sent)
    blob = nlp(test)
    sentence = next(blob.sents)
    for ent in sentence:
        print(ent, ent.dep_)
    '''
    




