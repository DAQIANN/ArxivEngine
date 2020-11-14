from whoosh.index import create_in
from whoosh.fields import *
from whoosh import index
import os.path
from whoosh.qparser import QueryParser
import sys
import os

def whooshSetup():
    global schema
    global ix
    schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored = True))
    ix = index.create_in("indexdir", schema)

def whooshFind(check):
    if not os.path.exists("indexdir"):
        os.mkdir("indexdir")

    if check == "":
        whooshSetup()
        writer = ix.writer()
        temp = ""
        for i in range(3):
            temp += "Example of hello world"
            writer.add_document(content=temp)
        '''
        writer.add_document(content=open("testfirst.txt", 'r').read())
        writer.add_document(content=u"This is the second example hello world.")
        writer.add_document(content=u"More examples. Examples are many.")
        '''
        writer.add_document(content=open("combine.txt", 'r').read())
        writer.commit()

    if check != "":
        with ix.searcher() as searcher:
            query = QueryParser("content", ix.schema).parse(check)
            results = searcher.search(query, terms=True)
     
            for r in results:
                print (r, r.score)
                # Was this results object created with terms=True?
                if results.has_matched_terms():
                    # What terms matched in the results?
                    print(results.matched_terms())
         
            # What terms matched in each hit?
            print ("matched terms")
            for hit in results:
                print(hit.matched_terms())

        found = results.scored_length()
        if results.has_exact_length():
            print("Scored", found, "of exactly", len(results), "documents")
        else:
            low = results.estimated_min_length()
            high = results.estimated_length()
 
            print("Scored", found, "of between", low, "and", high, "documents")

if __name__ == "__main__":
    whooshFind(sys.argv[1])
    check = ""
    while True:
        check = input ("Enter keywords: ")
        if check == 'stop':
            break
        whooshFind(check)


#CREATE DOCUMENTS CONTAINING THE SAME SUBJECTS AND PUT IT ALL IN ONE TEXT FILE
#THEN USING ABOVE FIND THE DOCUMENT IT'S IN

#Get the part of the sentence before the first verb and then stop words it