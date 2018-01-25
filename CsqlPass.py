# # CrackSqlite3Pass
#To Crack Password of Sqlite3-DB

# NullPass.db has no password to protect but PassDB.db

import os
import sys
import sqlite3

class CsqPass:
    def __banner(self):
        print("""
CsqPass:
        CrackSqlite3Pass
        By DeeLMind
        Github  :https://github.com/DeeLMind
        Blog    :http://www.cnblogs.com/DeeLMind
        Blog    :https://deelmind.github.io
        
        Usege:
                CsqPass.py  crack.db   pass.txt
        """)

    __PassFile = []
    __passPath = ''
    __dbPath = ''
    __sql = 'CREATE TABLE ATTACK(ID INT)'


    def __getPara(self):
        self.__dbPath = sys.argv[1]
        self.__passPath = sys.argv[2]

    # init with dbPath
    def __init__(self):
        self.__banner()
        self.__getPara()
        self.__getPass(self.__passPath)
        if self.__isExist(self.__dbPath):
            print("Not Exist dbFile")
            exit(1)

        if self.__isExist(self.__passPath):
            print("Not Exist passFile")
            exit(2)
        pass

    def __isExist(self,fileName):
        if not os.path.exists(fileName):
            return True
        else:
            return False

    def __readFile(self,fileName):

        with open(fileName,'r') as readFile:
            return readFile.readlines()

    def __getPass(self,fileName):
        self.__PassFile = self.__readFile(fileName=fileName)
        return self.__PassFile


    def attack(self):
        with sqlite3.connect(self.__dbPath) as db:
            cursor = db.cursor()





    def test(self):
        print(self.__PassFile)
        print(self.__dbPath)
        print(self.__passPath)



if __name__ == '__main__':
    c = CsqPass()
    c.test()


