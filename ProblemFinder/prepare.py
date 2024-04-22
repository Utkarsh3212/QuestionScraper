import chardet
import os

def find_encoding(fname):
    r_file = open(fname, 'rb').read()
    result = chardet.detect(r_file)
    charenc = result['encoding']
    return charenc

filename = 'Scraper/QDATA/index.txt'
QDATA_filename='Scraper/QDATA'
my_encoding = find_encoding(filename)


def reader(index):
    pathName=os.path.join(QDATA_filename,index)
    filePath=os.path.join(pathName,index+".txt")
    tLine=[]
    with open(filePath,'r') as f:
        for line in f:
            if "Example:" or "Example 1:" in line:
                break
            tLine.append(line)
    return ' '.join(tLine)


with open(filename, 'r', encoding=my_encoding) as f:
    qLines = f.readlines()

def preprocess(doc_text):
    terms = [term.lower() for term in doc_text.strip().split()[1:]]
    return terms

vocab = {}
documents = []
for index, line in enumerate(qLines):
    line+=reader(str(index+1))
    tokens=preprocess(line)
    documents.append(tokens)
    tokens=set(tokens)
    for token in tokens:
        if token not in vocab:
            vocab[token]=1
        else:
            vocab[token]+=1

vocab=dict(sorted(vocab.items(),key=lambda item:item[1],reverse=True))

with open('vocab.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % key)

with open('idf-values.txt', 'w') as f:
    for key in vocab.keys():
        f.write("%s\n" % vocab[key])

with open('documents.txt', 'w') as f:
    for document in documents:
        f.write("%s\n" % ' '.join(document))

inverted_index={}

for index,document in enumerate(documents):
    for token in document:
        if token not in inverted_index:
            inverted_index[token]=[index]
        else:
            inverted_index[token].append(index)

with open('inverted_index.txt','w') as f:
    for key in inverted_index.keys():
        print(key,inverted_index[key])
        inverted_index[key]=list(set(inverted_index[key]))
        f.write("%s\n" % key)
        f.write("%s\n" % ' '.join(str(doc_id) for doc_id in inverted_index[key]))