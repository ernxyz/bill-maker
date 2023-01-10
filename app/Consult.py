from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connex import *

class Consult():
    def __init__(self):
        self.window = Toplevel()
        self.window.title('Consulta')
        self.window.config()

        self.conn = DataBase()

        '''
        Widgets
        '''

        # Label

        self.label_bill_id = Label(self.window, text= 'DNI del cliente:')
        self.label_bill_id.grid(row=0, column=0)

        # Entry

        self.entry_bill_id = Entry(self.window)
        self.entry_bill_id.grid(row=0, column=1)

        # Button

        self.btn_bill_consult = Button(self.window, command= self.consult_bills, text= 'Consultar')
        self.btn_bill_consult.grid(row=0,column=2)

        # Tree

        self.tree_consult = ttk.Treeview(self.window, height= 20, columns= ('col1','col2','col3','col4','col5','col6'))
        self.tree_consult.grid(row= 1, column=0, columnspan= 7)

        self.tree_consult.heading('#0', text= 'Numero Factura', anchor= CENTER)
        self.tree_consult.heading('col1', text= 'Cliente', anchor= CENTER)
        self.tree_consult.heading('col2', text= 'Empleado', anchor= CENTER)
        self.tree_consult.heading('col3', text= 'Metodo de Pago', anchor= CENTER)
        self.tree_consult.heading('col4', text= 'Fecha', anchor= CENTER)
        self.tree_consult.heading('col5', text= 'Estado', anchor= CENTER)
        self.tree_consult.heading('col6', text= 'Total', anchor= CENTER)

    def consult_bills(self):
        records = self.tree_consult.get_children()
        for element in records:
            self.tree_consult.delete(element)

        aux = 'SELECT id_cliente FROM cliente WHERE dni="{}"'.format(self.entry_bill_id.get())
        sql = 'SELECT numero_factura, id_cliente, id_empleado, metodo_pago, fecha, id_estado, total FROM factura WHERE id_cliente=({})'.format(aux)

        self.conn.cursor.execute(sql)
        result = self.conn.cursor.fetchall()
                
        for item in result:
            # Customer
            sql = 'SELECT nombre FROM cliente WHERE id_cliente={}'.format(int(item[1]))
            self.conn.cursor.execute(sql)
            customer_name = self.conn.cursor.fetchone()

            # Employee

            sql = 'SELECT nombre FROM empleado WHERE id_empleado={}'.format(int(item[2]))
            self.conn.cursor.execute(sql)
            employee_name = self.conn.cursor.fetchone()

            # Payment

            sql = 'SELECT metodo FROM metodo WHERE id={}'.format(int(item[3]))
            self.conn.cursor.execute(sql)
            payment_method = self.conn.cursor.fetchone()

            # Estado
            sql = 'SELECT estado FROM estado WHERE id={}'.format(int(item[5]))
            self.conn.cursor.execute(sql)
            state = self.conn.cursor.fetchone()
            
            self.tree_consult.insert('', 0, text=item[0], values=(customer_name,employee_name,payment_method,item[4],state,item[6]))

    def quit(self): 
        self.window.destroy()
        self.window.quit()