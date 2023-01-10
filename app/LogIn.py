from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Connex import *
from datetime import datetime

class LogIn():

    def __init__(self):
        self.conn = DataBase()
        self.window = Tk()
        self.window.geometry('400x400+500+50')
        self.window.title('LogIn')
        self.window.resizable(0,0)


        self.today_date = datetime.today().strftime('%Y-%m-%d')
        
        '''
        Widgets
        '''

        # Frame

        self.frame_header = Label(self.window, bg="brown", height=6)
        self.frame_header.pack(fill=X)

        # Labels

        self.label_logo = ttk.Label(self.frame_header, text= 'PeruDelivery')
        self.label_logo.place(x=125, y=35)
        self.label_logo.config(font= ('Arial', 20))

        self.label_username = ttk.Label(self.window, text= 'Usuario')
        self.label_username.place(x=165, y=120)
        self.label_username.config(padding=1, font= ('Arial', 15))

        self.label_pin = ttk.Label(self.window, text= 'Pin')
        self.label_pin.place(x=180, y=210)
        self.label_pin.config(padding=1, font= ('Arial', 15))

        # Entries

        self.entry_username = Entry(self.window, width= 30)
        self.entry_username.place(x=115, y=155)

        self.entry_pin = Entry(self.window, width= 30)
        self.entry_pin.place(x=115, y=250)

        # Buttons

        self.button_login = ttk.Button(self.window, command= self.verificar, text= 'Log In')
        self.button_login.place(x=220, y=320)


        self.button_exit = ttk.Button(self.window, command= self.quit, text= 'Exit')
        self.button_exit.place(x=120, y=320)

        '''
        Loop
        '''
        
        self.window.mainloop()

    def verificar(self):
        username = self.entry_username.get()
        pin = self.entry_pin.get()
        
        if username != '' or pin != '':
            try:
                sql = "SELECT usuario, pin, id_empleado FROM usuario WHERE usuario='{}'".format(username)
                result = self.conn.cursor.execute(sql)
                result = self.conn.cursor.fetchone()

                if result[0] == username and result[1] == int(pin):
                    self.create_bill(result[2], self.today_date)
                    # sql = "UPDATE factura SET id_empleado={} WHERE numero_factura={}".format(result[2],)

                    self.ventana_app()
                else:
                    messagebox.showinfo("Información", "Usuario o pin incorrectos.")
            except Exception as e:
                messagebox.showinfo("Información", "Usuario o pin incorrectos")
            
        else:
            messagebox.showinfo("Información", "Uno de los campos está vacío")

    def ventana_app(self):
        from App import App
        self.window.withdraw()
        app = App()

    def create_bill(self,id_empleado, today_date):
        try:
            sql = "INSERT INTO factura(id_empleado,fecha) VALUES({},'{}')".format(id_empleado,today_date)
            self.conn.cursor.execute(sql)
            self.conn.connection.commit()

        except Exception as e:
            messagebox.showinfo("Información", "Algo salió mal, intente más tarde.")

    def quit(self):
        self.window.destroy()
        self.window.quit()
