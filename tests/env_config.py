import os
import sys

# print(sys.path)
absPath = os.path.abspath(__file__) 
dirA = os.path.dirname(absPath)
dbTestPath = os.path.join(dirA ,"databaseTest.db")
# srcPath = os.path.join(os.path.dirname(dirA),"src" )
# sys.path.append(srcPath)
# print(sys.path)

from repository import database_definitions



def create_test_database(path):
    print(f"Creating test data base in {path} ...")
    database_definitions.dbConnection().setConection(path)
    print("Test data base created!")

def main():
    create_test_database(dbTestPath)