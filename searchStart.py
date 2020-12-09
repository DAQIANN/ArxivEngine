from whoosh.index import create_in
from whoosh.fields import *
from whoosh import index
import os.path
from whoosh.qparser import QueryParser
import sys
import os
from splittingtexts import get_sents, get_related
    
class whooshFinder:
    def __init__(self):
        if not os.path.exists("indexdir"):
            os.mkdir("indexdir")
        global schema
        global ix
        schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored = True))
        ix = index.create_in("indexdir", schema)

        writer = ix.writer()
        temp = ""
        lines = get_sents("small_combine.txt")
        for key in lines:
            temp = ""
            if lines[key] != "-":
                lines, temp = get_related(lines, lines[key])
                writer.add_document(content=temp)
            
        '''
        writer.add_document(content=open("testfirst.txt", 'r').read())
        writer.add_document(content=u"This is the second example hello world.")
        writer.add_document(content=u"More examples. Examples are many.")
        '''
        writer.commit()

    def whooshFind(self, check):
        endpoint = []
        if check != "":
            with ix.searcher() as searcher:
                query = QueryParser("content", ix.schema).parse(check)
                results = searcher.search(query)
        
                for r in results:
                    endpoint.append(r['content'].replace('\n', ''))
                    #print (r, r.score)
                    # Was this results object created with terms=True?
                    #if results.has_matched_terms():
                        # What terms matched in the results?
                        #print(results.matched_terms())
            '''
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
            '''
        print(endpoint)
        return endpoint

if __name__ == "__main__":
    #decompress("compressed.tar.gz")
    #get_sents("small_combine.txt")
    #compress("compressed.tar.gz", ["arxiv-metadata-oai-snapshot.json", "small_combine.txt"])
    #removeFiles(["arxiv-metadata-oai-snapshot.json", "small_combine.txt"])
    find = whooshFinder()
    while True:
        check = input ("Enter keywords: ")
        if check == 'stop':
            break
        find.whooshFind(check)


#CREATE DOCUMENTS CONTAINING THE SAME SUBJECTS AND PUT IT ALL IN ONE TEXT FILE
#THEN USING ABOVE FIND THE DOCUMENT IT'S IN

#Get the part of the sentence before the first verb and then stop words it