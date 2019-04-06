class DDLquerys:
    connectionObject = ''
    
    def __init__(self, conn):
        self.connectionObject = conn

    def create_tables(self):

        response = {'exit-code': 1, 'msg': 'ceva s-a stricat pe drum'}

        try:

            # Create a cursor object

            cursorObject = self.connectionObject.cursor()

            # SQL query string

            sqlQuery = """CREATE TABLE `categoria` (
                            `idc` int(11) NOT NULL AUTO_INCREMENT,
                            `denc` varchar(255) DEFAULT NULL,
                            PRIMARY KEY (`idc`))"""

            # Execute the sqlQuery

            cursorObject.execute(sqlQuery)

            sqlQuery = """CREATE TABLE `produs` (
                          `idp` int(11) NOT NULL AUTO_INCREMENT,
                          `idc` int(11) NOT NULL,
                          `denp` varchar(255) DEFAULT NULL,
                          `pret` decimal(8,2) DEFAULT '0.00',
                          PRIMARY KEY (`idp`),
                          KEY `fk_cat` (`idc`),
                          CONSTRAINT `fk_cat` FOREIGN KEY (`idc`) REFERENCES `categoria` (`idc`) ON DELETE CASCADE) """

            # Execute the sqlQuery

            cursorObject.execute(sqlQuery)

            sqlQuery = """CREATE TABLE `operatiuni` (
                          `ido` int(11) NOT NULL AUTO_INCREMENT,
                          `idp` int(11) NOT NULL,
                          `tip` tinyint(5) NOT NULL DEFAULT '1',
                          `cant` decimal(10,3) DEFAULT '0.000',
                          `data` date DEFAULT NULL,
                          PRIMARY KEY (`ido`),
                          KEY `fk_prod` (`idp`),
                          CONSTRAINT `fk_prod` FOREIGN KEY (`idp`) REFERENCES `produs` (`idp`) ON DELETE CASCADE) """

            cursorObject.execute(sqlQuery)
            # SQL query string

            sqlQuery = "show tables"

            # Execute the sqlQuery

            cursorObject.execute(sqlQuery)

            # Fetch all the rows

            rows = cursorObject.fetchall()

            for row in rows:
                print(row)

            response = {'exit-code':0, 'msg': 's-au creat'}

        except Exception as e:

            print("Exeception occured:{}".format(e))


        finally:

            self.connectionObject.close()

            return response