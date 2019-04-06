class Category:
    connectionObject = ''

    def __init__(self, conn):
        self.connectionObject = conn

    def add(self, name):
        response = {'exit-code': 1, 'msg': 'ceva s-a stricat pe drum'}
        try:
            cursorObject = self.connectionObject.cursor()
            sqlQuery = "INSERT INTO `categoria` (`denc`) VALUES (%s)"
            cursorObject.execute(sqlQuery, (name))
            self.connectionObject.commit()
            response = {'exit-code': 0, 'msg': 'cateoria a fost adaugata'}
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            return response

    def get_all_categories(self):
        response = {}
        try:
            cursorObject = self.connectionObject.cursor()
            sqlQuery = "SELECT * FROM `categoria`"
            cursorObject.execute(sqlQuery)
            response = cursorObject.fetchall()
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            return response

if __name__ == "__main__":
    print ("Este un modul. Se importa, nu se executa")
