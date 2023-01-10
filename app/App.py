from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connex import *

class App():
    def __init__(self):
        self.window = Toplevel()
        self.window.title('Facturación')
        self.window.protocol('WM_DELETE_WINDOW', self.quit)
        self.window.config()

        # Helpers

        self.conn = DataBase()
        self.bill_number = self.get_bill()

        self.customers = []
        self.show_customers()
        self.customer = StringVar(self.window)
        self.customer.set('')

        self.payment_methods = []
        self.show_payment_method()
        self.payment_method = StringVar(self.window)
        self.payment_method.set('')

        self.bill_states = []
        self.show_bill_state()
        self.bill_state = StringVar(self.window)
        self.bill_state.set('')

        self.products = []
        self.show_products()

        '''
        Widgets
        '''

        # Frame

        self.frame_father = Frame(self.window)
        self.frame_father.grid(row=1,column=0,columnspan=4)

        # Customer

        self.frame_customer = LabelFrame(self.frame_father, text='Información del Cliente')
        self.frame_customer.grid(row=0,column=0,columnspan=4, pady=5, padx= 5,  sticky= W + E)

        self.label_customer_dni = ttk.Label(self.frame_customer, text='DNI:')
        # self.label_customer_dni.focus()
        self.label_customer_dni.grid(row=0,column=0, pady= 1)

        self.option_customer_dni = OptionMenu(self.frame_customer, self.customer, *self.customers)
        self.option_customer_dni.grid(row=0,column=1, pady= 1)

        self.btn_customer_save = ttk.Button(self.frame_customer, command= self.save_customer, text='Guardar')
        self.btn_customer_save.grid(row=1,column=2, pady= 1)

        # Bill info

        self.frame_info = LabelFrame(self.frame_father, text='Información de Factura')
        self.frame_info.grid(row=4,column=0, columnspan=4, pady=5, padx= 5,  sticky= W + E)

        self.label_info_state = ttk.Label(self.frame_info, text='Estado:')
        self.label_info_state.grid(row=4,column=0, pady= 1)

        self.option_info_state = OptionMenu(self.frame_info, self.bill_state, *self.bill_states)
        self.option_info_state.grid(row=4,column=1, pady= 1)

        self.label_info_payment = ttk.Label(self.frame_info, text='Método de pago:')
        self.label_info_payment.grid(row=4,column=2, pady= 1)

        self.option_info_payment = OptionMenu(self.frame_info, self.payment_method, *self.payment_methods)
        self.option_info_payment.grid(row=4,column=3, pady= 1)

        self.btn_info_save = ttk.Button(self.frame_info, command= self.save_bill_info, text='Guardar')
        self.btn_info_save.grid(row=5,column=2, pady= 1)

        # Products

        self.frame_product = LabelFrame(self.frame_father, text='Productos')
        self.frame_product.grid(row=6,column=0, columnspan=4, pady=5, padx= 5, sticky= W + E)

        self.label_product_name = Label(self.frame_product, text= 'Nombre:')
        self.label_product_name.grid(row=6,column=0, pady= 1)


        self.combobox_product = ttk.Combobox(self.frame_product, value= self.products)
        self.combobox_product.grid(row=6,column=1, pady= 1)

        self.label_product_quantity = Label(self.frame_product, text= 'Cantidad:')
        self.label_product_quantity.grid(row=7,column=0, pady= 1)

        self.entry_product_quantity = Entry(self.frame_product)
        self.entry_product_quantity.grid(row=7,column=1, pady= 1)

        self.btn_product_delete = ttk.Button(self.frame_product, command= self.delete_product, text='Eliminar')
        self.btn_product_delete.grid(row=8,column=1, pady= 1)

        self.btn_product_save = ttk.Button(self.frame_product, command= self.add_product, text='Agregar')
        self.btn_product_save.grid(row=8,column=2, pady= 1)

        # Acciones

        self.btn_consultar_factura = Button(self.window, command= self.ventana_consulta, text= 'Consultar')
        self.btn_consultar_factura.grid(row=8,column=0, pady=5, sticky= E)
        self.btn_consultar_factura.config(bg='red', fg='white')

        self.btn_imprimir_factura = Button(self.window, command= self.create, text= 'Imprimir')
        self.btn_imprimir_factura.grid(row=8,column=2, pady=5, sticky= W)
        self.btn_imprimir_factura.config(bg='red', fg='white')

        # Tree

        self.tree = ttk.Treeview(self.window, height= 14, columns= ('col1','col2','col3'))
        self.tree.grid(row= 9, column=0, columnspan= 3, padx=10)

        self.tree.heading('#0', text= 'Nombre', anchor= CENTER)
        self.tree.heading('col1', text= 'Precio', anchor= CENTER)
        self.tree.heading('col2', text= 'Cantidad', anchor= CENTER)
        self.tree.heading('col3', text= 'Total lineal', anchor= CENTER)

    '''
    Métodos
    '''

    # Customer

    def show_customers(self):
        sql = 'SELECT dni FROM cliente'
        self.conn.cursor.execute(sql)
        results = self.conn.cursor.fetchall()

        for result in results:
            self.customers.append(result[0])

    def save_customer(self):
        sql = 'UPDATE factura SET id_cliente=(SELECT id_cliente FROM cliente WHERE dni="{}") WHERE numero_factura={}'.format(self.customer.get(), self.bill_number)
        self.conn.cursor.execute(sql)
        self.conn.connection.commit()
        messagebox.showinfo('Informacion','Guardado con éxito!')

    # Products

    def get_products(self):
        # Cleaning table
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        try:
            subtotal = 0
            sql = 'SELECT id_producto, precio, cantidad, total_lineal FROM factura_detalle WHERE numero_factura={}'.format(self.bill_number)
            self.conn.cursor.execute(sql)
            items = self.conn.cursor.fetchall()

            for item in items:
                # Nombre producto
                sql = 'SELECT nombre FROM producto WHERE id_producto={}'.format(int(item[0]))
                self.conn.cursor.execute(sql)
                product_name = self.conn.cursor.fetchone()

                self.tree.insert('', 0, text=product_name, values=(item[1],item[2],item[3]))
                subtotal += item[3]
            total = subtotal + (subtotal * 0.18) 

            sql = 'UPDATE factura SET subtotal={}, total={} WHERE numero_factura={}'.format(subtotal,total, self.bill_number)
            self.conn.cursor.execute(sql)
            self.conn.connection.commit()

            self.tree.insert('',11, text='', values='')
            self.tree.insert('',12, text='', values= ('','Subtotal:',subtotal))
            self.tree.insert('',13, text='', values= ('','IGV:', '18%'))
            self.tree.insert('',14, text='', values= ('','Total:',total))

        except Exception as e:
            pass

    def validation(self):
        return len(self.combobox_product.get()) != 0

    def add_product(self):
        if self.validation():
            if (len(self.tree.get_children()) < 14):
                aux = self.combobox_product.get()
                product = aux.split(' ')
                id_product = 'SELECT id_producto FROM producto WHERE nombre="{}"'.format(product[0])
                sql = 'INSERT INTO factura_detalle(numero_factura, id_producto, cantidad, precio, total_lineal) VALUES({},({}),{},{},{})'.format(self.bill_number, id_product, int(self.entry_product_quantity.get()), int(product[1]), (int(product[1])*int(self.entry_product_quantity.get())))

                self.conn.cursor.execute(sql)
                self.conn.connection.commit()
                messagebox.showinfo('Información', 'Guardado con éxito!')
                self.entry_product_quantity.delete(0, END)
            else:
                messagebox.showinfo('Información', 'Limite de productos alcanzado!')
        else:
            messagebox.showinfo('Información', 'Seleccione el producto y la cantidad!')
        self.get_products()

    def delete_product(self):
        try:
            name = self.tree.item(self.tree.selection())['text']
            aux = 'SELECT id_producto FROM producto WHERE nombre="{}"'.format(name)
            sql = 'DELETE FROM factura_detalle WHERE id_producto =({}) AND numero_factura={}'.format(aux,self.bill_number)
            self.conn.cursor.execute(sql)
            self.conn.connection.commit()
            messagebox.showinfo('Información', 'Eliminado con éxito!')
            self.get_products()
        except Exception as e:
            pass
        
    def show_products(self):
        sql = 'SELECT nombre, precio FROM producto'
        self.conn.cursor.execute(sql)
        results = self.conn.cursor.fetchall()

        for result in results:
            self.products.append(result)

    # Bill

    def show_bill_state(self):
        sql = 'SELECT estado FROM estado'
        self.conn.cursor.execute(sql)
        results = self.conn.cursor.fetchall()

        for result in results:
            self.bill_states.append(result[0])

    def show_payment_method(self):
        sql = 'SELECT metodo FROM metodo'
        self.conn.cursor.execute(sql)
        results = self.conn.cursor.fetchall()

        for result in results:
            self.payment_methods.append(result[0])

    def save_bill_info(self):
        sql = 'UPDATE factura SET metodo_pago=(SELECT id FROM metodo WHERE metodo="{}"), id_estado=(SELECT id FROM estado WHERE estado="{}") WHERE numero_factura={}'.format(self.payment_method.get(),self.bill_state.get(), self.bill_number)
        self.conn.cursor.execute(sql)
        self.conn.connection.commit()
        messagebox.showinfo('Informacion','Guardado con éxito!')

    # Quit

    def quit(self):
        self.window.destroy()
        self.window.quit()
    
    # Helpers

    def get_bill(self):
        sql = 'SELECT numero_factura FROM factura ORDER BY numero_factura DESC'
        result = self.conn.cursor.execute(sql)
        result = self.conn.cursor.fetchone()
        return int(result[0])


    def execute_query(self, query, parameters = ()):
        result = self.conn.cursor.execute(query,parameters)
        self.conn.connection.commit()
        
        return result

    def create(self):
        from Create_pdf import create_pdf
        create_pdf()

    def ventana_consulta(self):
        from Consult import Consult
        consult = Consult()