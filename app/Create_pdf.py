# ruta C:\Program Files\wkhtmltopdf

import jinja2
import pdfkit
from Connex import *

conn = DataBase()
sql = ''

razon_social = 'PeruDelivery S.A.'
empresa_ruc = '9898989'
empresa_tlf = '104546'
empresa_direccion = 'Av. Siempre Viva, 115'

# Num Factura

sql = 'SELECT numero_factura FROM factura ORDER BY numero_factura DESC'
result = conn.cursor.execute(sql)
result = conn.cursor.fetchone()
numero_factura = int(result[0])

# Cliente
sql = 'SELECT dni, nombre, empresa, direccion, tlf FROM cliente WHERE id_cliente=(SELECT id_cliente FROM factura WHERE numero_factura={})'.format(numero_factura)
conn.cursor.execute(sql)
results = conn.cursor.fetchall()

for result in results:
    cliente_dni = result[0]
    cliente_nombre = result[1]
    cliente_empresa = result[2]
    cliente_tlf = result[3]
    cliente_direccion = result[4]

# Datos

sql = 'SELECT fecha FROM factura ORDER BY numero_factura DESC'
result = conn.cursor.execute(sql)
result = conn.cursor.fetchone()
fecha = result[0]

aux = 'SELECT id_estado FROM factura ORDER BY numero_factura DESC'
result = conn.cursor.execute(aux)
result = conn.cursor.fetchone()
aux1 = int(result[0])

sql = 'SELECT estado FROM estado WHERE id=({})'.format(aux1)
result = conn.cursor.execute(sql)
result = conn.cursor.fetchone()
factura_estado = result[0]

aux = 'SELECT metodo_pago FROM factura ORDER BY numero_factura DESC'
result = conn.cursor.execute(aux)
result = conn.cursor.fetchone()
aux1 = int(result[0])

aux = 'SELECT metodo_pago FROM factura ORDER BY numero_factura DESC'
sql = 'SELECT metodo FROM metodo WHERE id=({})'.format(aux1)
result = conn.cursor.execute(sql)
result = conn.cursor.fetchone()
factura_metodo_pago = result[0]

# Montos

sql = 'SELECT subtotal FROM factura ORDER BY numero_factura DESC'
result = conn.cursor.execute(sql)
result = conn.cursor.fetchone()
subtotal = int(result[0])

sql = 'SELECT total FROM factura ORDER BY numero_factura DESC'
result = conn.cursor.execute(sql)
result = conn.cursor.fetchone()
total = int(result[0])

# Productos

nombres = []
cantidades = []
precios = []
lineales = []

sql = 'SELECT id_producto, cantidad, precio, total_lineal FROM factura_detalle WHERE numero_factura={}'.format(numero_factura)
result = conn.cursor.execute(sql)
results = conn.cursor.fetchall()
for result in results:
    
    # Nombres

    sql = 'SELECT nombre FROM producto WHERE id_producto={}'.format(int(result[0]))
    conn.cursor.execute(sql)
    aux = conn.cursor.fetchone()
    nombres.append(aux)

    cantidades.append(result[1])
    precios.append(result[2])
    lineales.append(result[3])


if (len(nombres)>0):
    
    context = {
        'razon_social': razon_social,
        'empresa_ruc': empresa_ruc,
        'empresa_tlf': empresa_tlf,
        'empresa_direccion': empresa_direccion,
        'cliente_dni': cliente_dni,
        'cliente_nombre': cliente_nombre,
        'cliente_empresa': cliente_empresa,
        'cliente_tlf': cliente_tlf,
        'cliente_direccion': cliente_direccion,
        'fecha': fecha,
        'factura_estado': factura_estado,
        'factura_metodo_pago': factura_metodo_pago,
        'producto_nombre1': nombres[0],
        'producto_unidades1': cantidades[0],
        'producto_precio1': precios[0],
        'producto_precio_lineal1': lineales[0],
        'subtotal': subtotal,
        'total': total
    }

    if (len(nombres)>1):
        context['producto_nombre2'] = nombres[1]
        context['producto_unidades2'] = cantidades[1]
        context['producto_precio2'] = precios[1]
        context['producto_precio_lineal2'] = lineales[1]

        if (len(nombres)>2):
            context['producto_nombre3'] = nombres[2]
            context['producto_unidades3'] = cantidades[2]
            context['producto_precio3'] = precios[2]
            context['producto_precio_lineal3'] = lineales[2]
        
            if (len(nombres)>3):
                context['producto_nombre4'] = nombres[3]
                context['producto_unidades4'] = cantidades[3]
                context['producto_precio4'] = precios[3]
                context['producto_precio_lineal4'] = lineales[3]

                if (len(nombres)>4):
                    context['producto_nombre5'] = nombres[4]
                    context['producto_unidades5'] = cantidades[4]
                    context['producto_precio5'] = precios[4]
                    context['producto_precio_lineal5'] = lineales[4]

                    if (len(nombres)>5):
                        context['producto_nombre6'] = nombres[5]
                        context['producto_unidades6'] = cantidades[5]
                        context['producto_precio6'] = precios[5]
                        context['producto_precio_lineal6'] = lineales[5]

                        if (len(nombres)>6):
                            context['producto_nombre7'] = nombres[6]
                            context['producto_unidades7'] = cantidades[6]
                            context['producto_precio7'] = precios[6]
                            context['producto_precio_lineal7'] = lineales[6]

                            if (len(nombres)>7):
                                context['producto_nombre8'] = nombres[7]
                                context['producto_unidades8'] = cantidades[7]
                                context['producto_precio8'] = precios[7]
                                context['producto_precio_lineal8'] = lineales[7]

                                if (len(nombres)>8):
                                    context['producto_nombre9'] = nombres[8]
                                    context['producto_unidades9'] = cantidades[8]
                                    context['producto_precio9'] = precios[8]
                                    context['producto_precio_lineal9'] = lineales[8]

                                    if (len(nombres)>9):
                                        context['producto_nombre10'] = nombres[9]
                                        context['producto_unidades10'] = cantidades[9]
                                        context['producto_precio10'] = precios[9]
                                        context['producto_precio_lineal10'] = lineales[9]

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader= template_loader)

html_template = 'template.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe')
output_pdf = 'Factura.pdf'

def create_pdf():
    pdfkit.from_string(output_text, output_pdf, configuration= config, css= 'style.css')
