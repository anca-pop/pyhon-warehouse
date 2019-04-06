import pymysql.cursors

class DB:
    dbServerName = "localhost"
    dbUser = "root"
    dbPassword = "ZAQ12wsx.1"
    dbName = "depozit"
    charSet = "utf8mb4"
    cusrorType = pymysql.cursors.DictCursor
    connector = ""

    def __init__(self):
        self.connector =  pymysql.connect(host=self.dbServerName, user=self.dbUser, password=self.dbPassword,
                                   db=self.dbName, charset=self.charSet, cursorclass=self.cusrorType)

    def get_connect(self):
        return self.connector

if __name__ == "__main__":
    print ("Este un modul. Se importa, nu se executa")
