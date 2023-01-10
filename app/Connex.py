import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.Connect(host='localhost', port=3307, user= 'root', password= '', db= 'facturas')
        self.cursor = self.connection.cursor()

        print('Connection established!')

    def return_customer_id(self,dni):
        return 'SELECT id FROM cliente WHERE dni={}'.format(dni)

'''
    def buscar_usuario(self, id):
        sql = 'SELECT * FROM usuario WHERE id_usuario={}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()

            print('Id:', user[0])
            print('Id Empleado:', user[1])
            print('Usuario:', user[2])
            print('Pin:', user[3])

        except Exception as e:
            raise
    
# db = DataBase()
# db.buscar_usuario(1)
'''