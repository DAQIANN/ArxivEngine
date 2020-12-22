from whoosh.index import create_in
from whoosh.fields import *
from whoosh import index
import os.path
from whoosh.qparser import QueryParser
import sys
import os
from splittingtexts import get_sents, get_related
    
class whooshFinder:
    def __init__(self, filename):
        if not os.path.exists("indexdir"):
            os.mkdir("indexdir")
        global schema
        global ix
        #schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored = True))
        schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True))
        ix = index.create_in("indexdir", schema)

        writer = ix.writer()
        #writer.add_document(title="Blah", content=u"Hello World Bruh Bruh")
        global lines
        lines = get_sents(filename)
        for key in lines:
            temp = get_related(lines, key)
            writer.add_document(title=key, content=temp)
        writer.commit()

    def whooshFind(self, check):
        endpoint = ""
        scores = []
        total = 0.0
        if check != "":
            with ix.searcher() as searcher:
                query = QueryParser("title", ix.schema).parse(check)
                results = searcher.search(query)
        
                for r in results:
                    endpoint += lines[r['title']].replace('\n', '')
                    #print(r['content'].replace('\n', ''))
                    #print (r, r.score)
                    #scores.append(r.score)
                    #total += r.score
                    # Was this results object created with terms=True?
                    #if results.has_matched_terms():
                        # What terms matched in the results?
                        #print(results.matched_terms())
                if len(endpoint) == 0:
                    return ["No Sentences Found.", ""]
                #average = (float)(total/len(endpoint))
        return endpoint.split('.')
    
    def otherFind(self, first, second):
        with ix.searcher() as s:
            r = s.search(query.Term("text", "day"))
            for hit in r:
                print(hit["text"])

#if __name__ == "__main__":
    #decompress("compressed.tar.gz")
    #get_sents("small_combine.txt")
    #compress("compressed.tar.gz", ["arxiv-metadata-oai-snapshot.json", "small_combine.txt"])
    #removeFiles(["arxiv-metadata-oai-snapshot.json", "small_combine.txt"])
    #find = whooshFinder()
    #find.otherFind("", "")    
    #while True:
        #check = input ("Enter keywords: ")
        #if check == 'stop':
            #break
        #print(find.whooshFind(check))
