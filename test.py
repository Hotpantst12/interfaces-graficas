import tkinter as tk
import random

class Cliente:
    def __init__(self, id, nombre, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.servicios_realizados = []
        self.productos_comprados = []

    def agregar_servicio(self, servicio):
        self.servicios_realizados.append(servicio)

    def comprar_producto(self, producto):
        self.productos_comprados.append(producto)

class Servicio:
    def __init__(self, nombre, descripcion, duracion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.precio = precio

class Peluquero:
    def __init__(self, id, nombre, especializacion):
        self.id = id
        self.nombre = nombre
        self.especializacion = especializacion

class ProductoBelleza:
    def __init__(self, id, nombre, descripcion, precio):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

# Crear algunos servicios y productos constantes
servicios = [Servicio("Corte de pelo", "Un corte de pelo básico", 30, 15.0),
             Servicio("Coloración", "Coloración del cabello", 60, 30.0)]

productos = [ProductoBelleza(1, "Champú", "Champú para todo tipo de cabello", 10.0),
             ProductoBelleza(2, "Acondicionador", "Acondicionador para todo tipo de cabello", 10.0)]

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Facturación de Peluquería")

        # Crear campos de entrada para la información del cliente
        self.id_label = tk.Label(ventana, text="ID del Cliente")
        self.id_label.pack()
        self.id_entry = tk.Entry(ventana)
        self.id_entry.pack()

        self.nombre_label = tk.Label(ventana, text="Nombre del Cliente")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.pack()

        self.telefono_label = tk.Label(ventana, text="Teléfono del Cliente")
        self.telefono_label.pack()
        self.telefono_entry = tk.Entry(ventana)
        self.telefono_entry.pack()

        self.direccion_label = tk.Label(ventana, text="Dirección del Cliente")
        self.direccion_label.pack()
        self.direccion_entry = tk.Entry(ventana)
        self.direccion_entry.pack()

        # Crear botones para agregar servicios y productos
        self.crear_cliente_boton = tk.Button(ventana, text="Crear Cliente", command=self.crear_cliente)
        self.crear_cliente_boton.pack()

        self.servicio_boton = tk.Button(ventana, text="Agregar Servicio Aleatorio", command=self.agregar_servicio)
        self.servicio_boton.pack()

        self.producto_boton = tk.Button(ventana, text="Comprar Producto Aleatorio", command=self.comprar_producto)
        self.producto_boton.pack()

        self.factura_boton = tk.Button(ventana, text="Generar Factura", command=self.generar_factura)
        self.factura_boton.pack()

        self.salir_boton = tk.Button(ventana, text="Salir", command=ventana.quit)
        self.salir_boton.pack()
        
        self.cliente = None

    def agregar_servicio(self):
        servicio_aleatorio = random.choice(servicios)
        self.cliente.agregar_servicio(servicio_aleatorio)
        print(f"Servicio {servicio_aleatorio.nombre} agregado al cliente {self.cliente.nombre}")

    def comprar_producto(self):
        producto_aleatorio = random.choice(productos)
        self.cliente.comprar_producto(producto_aleatorio)
        print(f"Producto {producto_aleatorio.nombre} comprado por el cliente {self.cliente.nombre}")

    def generar_factura(self):
        factura = f"Factura para el cliente {self.cliente.nombre} (ID: {self.cliente.id})\n"
        factura += f"Dirección: {self.cliente.direccion}\n"
        factura += f"Teléfono: {self.cliente.telefono}\n"
        factura += "\nServicios realizados:\n"
        for servicio in self.cliente.servicios_realizados:
            factura += f"- {servicio.nombre} ({servicio.descripcion}): {servicio.precio}€\n"
        factura += "\nProductos comprados:\n"
        for producto in self.cliente.productos_comprados:
            factura += f"- {producto.nombre} ({producto.descripcion}): {producto.precio}€\n"

    # Crear una nueva ventana para mostrar la factura
        factura_ventana = tk.Toplevel(self.ventana)
        factura_ventana.title("Factura")
        factura_text = tk.Text(factura_ventana)
        factura_text.pack()
        factura_text.insert(tk.END, factura)


    def crear_cliente(self):
        id_cliente = self.id_entry.get()
        nombre_cliente = self.nombre_entry.get()
        telefono_cliente = self.telefono_entry.get()
        direccion_cliente = self.direccion_entry.get()

        self.cliente = Cliente(id_cliente, nombre_cliente, telefono_cliente, direccion_cliente)

ventana = tk.Tk()
app = Aplicacion(ventana)
ventana.mainloop()


