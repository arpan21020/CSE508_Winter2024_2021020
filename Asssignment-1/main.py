from Components.generatingDatasets import datasetGen
from Components.boolean_queries import BooleanQueries
from Components.phrase_queries import PhraseQueries

def menu():
    print("\n" + "-"*20)
    print(" "*5 + "Menu:")
    print("-"*20)
    print("1. \033[1m5 sample files before and after performing reprocessing\033[0m")
    print("2. \033[1mBoolean Queries\033[0m")
    print("2. \033[1mPhrase Queries\033[0m")
    print("-"*20)
def samples():
    for i in range(1,6):
        print("\n\033[1mBefor Preprocessing:\033[0m")
        
        print(f"Sample File {i} :")
        with open(f'./text_files/file{i}.txt', 'r') as file:
            print(file.read())
        print("\n")
        print("\n\033[1mAfter Reprocessing:\033[0m")
        print(f"Sample File {i} :")
        with open(f'./Dataset/file{i}.txt', 'r') as file:
            print(file.read())
        print("\n")
        
def boolean_queries():
    n=int(input("\nNumber of queries to execute: "))
    for i in range(n):
        query=input("Input Sequence : ")
        operations=input("Operations separated by comma :")
        
        obj=BooleanQueries(query,operations.split(','))
        documents_retrieved=obj.processing_operations()
        
        print("\n\033[1mOutput : \033[0m")
        print(f"Query {i+1} : {obj.query_form()}")
        print(f"Number of documents retrieved for query {i+1} : {len(documents_retrieved)}")
        print("Documents Retrieved : ",end="")
        [print(doc, end=',') for doc in documents_retrieved]
        print("\n")
    
def phrase_queries():
    n=int(input("\nNumber of queries to execute: "))
    for i in range(n):
        query=input("Input Sequence : ")
        
        obj=PhraseQueries(query)
        documents_retrieved=obj.processing_query()
        
        print("\n\033[1mOutput : \033[0m")
        print(f"Number of documents retrieved for query {i+1} : {len(documents_retrieved)}")
        print("Documents Retrieved : ",end="")
        [print(doc, end=',') for doc in documents_retrieved]
        print("\n")
        
if __name__ == "__main__":
    datasetGen()
    while(True):
        menu()
        choice = input("Choose an option: ")
        if choice == "1":
            samples()
        elif choice == "2":
            boolean_queries()
        elif choice == "3":
            phrase_queries()
        else:
            print("Invalid choice. Please choose a valid option.")
        
    