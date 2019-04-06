class Operation:
    connectionObject = ''

    def __init__(self, conn):
        self.connectionObject = conn

    def add(self, product_id, type, quantity, operation_date):
        response = {'exit-code': 1, 'msg': 'ceva s-a stricat pe drum'}
        try:
            cursorObject = self.connectionObject.cursor()
            sqlQuery = "INSERT INTO `operatiuni` (`idp`,`tip`,`cant`,`data`) VALUES (%s,%s,%s,%s)"
            cursorObject.execute(sqlQuery, (product_id, type, quantity, operation_date))
            self.connectionObject.commit()
            response = {'exit-code': 0, 'msg': 'operatiunea a fost adaugata'}
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            return response

    def get_operation_by_product_and_date(self, product_id, start_date, end_date):
        response = {}
        try:
            cursorObject = self.connectionObject.cursor()
            sqlQuery = """SELECT o.data, o.cant
                          FROM `produs` as p
                          INNER JOIN `operatiuni` as o
                          ON p.idp = o.idp
                          WHERE p.idp = %s
                          AND o.data BETWEEN %s AND %s
                          ORDER BY o.data 
                        """
            cursorObject.execute(sqlQuery,(product_id, start_date, end_date))
            response = cursorObject.fetchall()
        except Exception as e:
            print("Exeception occured:{}".format(e))
        finally:
            return response

if __name__ == "__main__":
    print ("Este un modul. Se importa, nu se executa")
