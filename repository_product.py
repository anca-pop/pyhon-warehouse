class Product:
    connectionObject = ''

    def __init__(self, conn):
        self.connectionObject = conn

    def add(self, category_id, product_name, product_price):
        response = {'exit-code': 1, 'msg': 'ceva s-a stricat pe drum'}
        try:
            cursorObject = self.connectionObject.cursor()
            sqlQuery = "INSERT INTO `produs` (`idc`,`denp`,`pret`) VALUES (%s,%s,%s)"
            cursorObject.execute(sqlQuery, (category_id, product_name, product_price))
            self.connectionObject.commit()
            response = {'exit-code': 0, 'msg': 'produsul a fost adaugata'}
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            return response

    def get_all_products(self):
            response = {}
            try:
                cursorObject = self.connectionObject.cursor()
                sqlQuery = "SELECT `idp`, `denp` FROM `produs`"
                cursorObject.execute(sqlQuery)
                response = cursorObject.fetchall()
            except Exception as e:
                print("Exeception occured:{}".format(e))
            finally:
                return response

if __name__ == "__main__":
    print ("Este un modul. Se importa, nu se executa")
