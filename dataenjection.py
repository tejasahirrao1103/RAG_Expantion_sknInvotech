from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
import whisper
import rag as sne


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
END_COLOR = '\033[0m'

colr =['\033[91m','\033[92m','\033[93m','\033[94m']

def textloader():
    path= input("provide path of text document"+colr[2]+" WITHOUT(\" \"): "+END_COLOR).strip()
    loader = TextLoader(path)
    text_doc=loader.load()
    print(text_doc)
    print("\n\n")
    sne.rag(text_doc)


def webpage():
    path= input("provide URL"+colr[2]+" WITHOUT(\" \"): "+END_COLOR).strip()
    loader=WebBaseLoader(path)
    data=loader.load()
    print(data)
    print("\n\n")
    sne.rag(data)

def pdfloader():
    path= input("provide path of PDF document"+colr[2]+" WITHOUT(\" \"): "+END_COLOR)
    loader = PyPDFLoader(path)
    pdfload= loader.load()
    print(pdfload)
    print("\n\n")
    sne.rag(pdfload)

def doc():
    path= input("provide path of doc file"+colr[2]+" WITHOUT(\" \"): "+END_COLOR).strip()
    loader = Docx2txtLoader(path)
    docload= loader.load()
    print(docload)
    print("\n\n")
    sne.rag(docload)

def audvid():
    path= input("provide path of video/ audio document"+colr[2]+" WITHOUT(\" \"): "+END_COLOR).strip()
    model = whisper.load_model('large-v3')
    result = model.transcribe(path,task='translate')
    print(result['text'])
    print("\n\n")
    with open("text.txt", "w") as file:
        file.write(result['text'])
    loader = TextLoader("text.txt")
    text_doc=loader.load()
    sne.rag(text_doc)
    
