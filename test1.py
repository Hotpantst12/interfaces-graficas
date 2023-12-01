import tkinter as tk
import random

class Cliente:
    def __init__(self, id, nombre, telefono, direccion, peluquero):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion
        self.peluquero = peluquero
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
             Servicio("Coloración", "Coloración del cabello", 60, 90.0),Servicio("Tratamiento Capilar", "frenar caida del cabello", 90, 60.0)]

productos = [ProductoBelleza(1, "Champú", "Champú para todo tipo de cabello", 20.0),
             ProductoBelleza(2, "Acondicionador", "Acondicionador para todo tipo de cabello", 10.0),
             ProductoBelleza(3, "Mascarilla capilar", "tratamiento 5 en 1", 30.0)]
peluqueros = [Peluquero(1, "Juan", "Corte de pelo"),
              Peluquero(2, "Ana", "Coloración")]

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sistema de Facturación de Peluquería")

        # Crear campos de entrada para la información del cliente
        self.id_label = tk.Label(ventana, text="ID del Cliente", bg="lightblue")
        self.id_label.pack()
        self.id_entry = tk.Entry(ventana)
        self.id_entry.pack()

        self.nombre_label = tk.Label(ventana, text="Nombre del Cliente", bg="lightblue")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(ventana)
        self.nombre_entry.pack()

        self.telefono_label = tk.Label(ventana, text="Teléfono del Cliente", bg="lightblue")
        self.telefono_label.pack()
        self.telefono_entry = tk.Entry(ventana)
        self.telefono_entry.pack()

        self.direccion_label = tk.Label(ventana, text="Dirección del Cliente", bg="lightblue")
        self.direccion_label.pack()
        self.direccion_entry = tk.Entry(ventana)
        self.direccion_entry.pack()

        # Crear botones para agregar servicios y productos
        self.crear_cliente_boton = tk.Button(ventana, text="Crear Cliente", command=self.crear_cliente, bg="lightgreen")
        self.crear_cliente_boton.pack()

        self.servicio_boton = tk.Button(ventana, text="Agregar Servicio Aleatorio", command=self.agregar_servicio, bg="lightgreen")
        self.servicio_boton.pack()

        self.producto_boton = tk.Button(ventana, text="Comprar Producto Aleatorio", command=self.comprar_producto, bg="lightgreen")
        self.producto_boton.pack()

        self.factura_boton = tk.Button(ventana, text="Generar Factura", command=self.generar_factura, bg="lightgreen")
        self.factura_boton.pack()

        self.salir_boton = tk.Button(ventana, text="Salir", command=ventana.quit, bg="red")
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
        factura += f"Peluquero: {self.cliente.peluquero.nombre} (Especialización: {self.cliente.peluquero.especializacion})\n"
        factura += "\nServicios realizados:\n"
        total_servicios = 0
        for servicio in self.cliente.servicios_realizados:
            factura += f"- {servicio.nombre} ({servicio.descripcion}): {servicio.precio}€\n"
            total_servicios += servicio.precio
        factura += "\nProductos comprados:\n"
        total_productos = 0
        for producto in self.cliente.productos_comprados:
            factura += f"- {producto.nombre} ({producto.descripcion}): {producto.precio}€\n"
            total_productos += producto.precio
        factura += f"\nTotal servicios: {total_servicios}€"
        factura += f"\nTotal productos: {total_productos}€"
        factura += f"\nTotal a pagar: {total_servicios + total_productos}€"

    # Crear una nueva ventana para mostrar la factura
        factura_ventana = tk.Toplevel(self.ventana)
        factura_ventana.title("Factura")
        factura_ventana.configure(bg="lightyellow")

    # Añadir un marco para el título de la factura
        titulo_factura = tk.Label(factura_ventana, text="Factura", bg="lightblue", fg="black", font=("Helvetica", 16, "bold"))
        titulo_factura.grid(row=0, column=1)

    # Añadir un marco para el contenido de la factura
        contenido_factura = tk.Text(factura_ventana, bg="lightyellow", fg="black")
        contenido_factura.grid(row=1, column=1)
        contenido_factura.insert(tk.END, factura)

    # Centrar el texto en el widget Text
        contenido_factura.tag_configure("center", justify="center", spacing1=4)
        contenido_factura.tag_add("center", 1.0, "end")

    # Añadir marcos a los lados de la ventana de la factura
        factura_ventana.grid_rowconfigure(0, weight=1) # Hacer que la fila 0 se expanda para llenar la ventana
        factura_ventana.grid_columnconfigure(0, weight=1) # Hacer que la columna 0 se expanda para llenar la ventana

    # Crear los marcos laterales
        marco_izquierdo = tk.Frame(factura_ventana, width=5, bg="black")
        marco_izquierdo.grid(row=0, column=0, rowspan=2, sticky="ns")

        marco_derecho = tk.Frame(factura_ventana, width=5, bg="black")
        marco_derecho.grid(row=0, column=2, rowspan=2, sticky="ns")
    # Crear los marco inferior
        marco_inferior = tk.Frame(factura_ventana, height=5, bg="black")
        marco_inferior.grid(row=2, column=0, columnspan=3, sticky="ew")


    def crear_cliente(self):
        id_cliente = self.id_entry.get()
        nombre_cliente = self.nombre_entry.get()
        telefono_cliente = self.telefono_entry.get()
        direccion_cliente = self.direccion_entry.get()
        peluquero_aleatorio = random.choice(peluqueros)

        self.cliente = Cliente(id_cliente, nombre_cliente, telefono_cliente, direccion_cliente, peluquero_aleatorio)

ventana = tk.Tk()
app = Aplicacion(ventana)
ventana.mainloop()
