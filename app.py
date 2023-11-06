
import tkinter as tk
import sqlite3
from tkinter import messagebox

class InterfazSkyCord:
    def __init__(self, root):
        self.root = root
        self.root.title("SKYCORD")
        self.root.geometry("400x400")

        self.label = tk.Label(root, text="ELIJA LA OPCION")
        self.label.pack()

        #BOTONES OPCIONES
        opciones = [
            "Registro de Caja", "Registro de Administrador", "Registro de Personal",
            "Sede", "Registro de Ventas", "Registro de Egresos"
        ]
        for opcion in opciones:
            btn = tk.Button(root, text=opcion, command=lambda op=opcion: self.opcion_seleccionada(op))
            btn.pack()

    def opcion_seleccionada(self, opcion):
        if opcion == "Registro de Caja":
            self.ventana_caja()
        elif opcion == "Registro de Administrador":
            self.ventana_administrador()
        elif opcion == "Registro de Personal":
            self.ventana_personal()
        elif opcion == "Sede":
            self.ventana_sede()
        elif opcion == "Registro de Ventas":
            self.ventana_ventas()
        elif opcion == "Registro de Egresos":
            self.ventana_egresos()
        elif opcion == "Resultados":
            self.ventana_resultados()
        elif opcion == "Borrar base de datos":
            self.borrar_historial()

    def ventana_caja(self):
        self.ventana_caja = tk.Toplevel(self.root)
        self.ventana_caja.title("Registro de Caja")
        self.ventana_caja.geometry("400x400")

        self.label_base = tk.Label(self.ventana_caja, text="INGRESE LA BASE")
        self.label_base.pack()
        self.entry_base = tk.Entry(self.ventana_caja)
        self.entry_base.pack()

        self.label_monto = tk.Label(self.ventana_caja, text="INGRESA EL MONTO")
        self.label_monto.pack()
        self.entry_monto = tk.Entry(self.ventana_caja)
        self.entry_monto.pack()

        btn_finalizar = tk.Button(self.ventana_caja, text="Finalizar", command=self.agregar_caja)
        btn_finalizar.pack()

    def agregar_caja(self):
        try:
            base = self.entry_base.get()
            monto = self.entry_monto.get()

            # Conectar con la base de datos (o crearla si no existe)
            conexion = sqlite3.connect('mi_base_de_datos.db')
            cursor = conexion.cursor()

            # Crear la tabla si no existe
            cursor.execute('''CREATE TABLE IF NOT EXISTS RegistrosCaja (Base TEXT, Monto TEXT)''')

            # Insertar datos en la tabla
            cursor.execute("INSERT INTO RegistrosCaja (Base, Monto) VALUES (?, ?)", (base, monto))

            conexion.commit()
            conexion.close()

            messagebox.showinfo("Registro exitoso", "Datos de caja registrados correctamente")
            self.ventana_caja.destroy()  # Cerrar la ventana de registros

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"No se pudo agregar a la base de datos: {error}")


    def ventana_administrador(self):
        self.ventana_administrador = tk.Toplevel(self.root)
        self.ventana_administrador.title("Registro de Administrador")
        self.ventana_administrador.geometry("400x400")

        self.label_nombre = tk.Label(self.ventana_administrador, text="Nombre del administrador")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.ventana_administrador)
        self.entry_nombre.pack()

        self.label_identificacion = tk.Label(self.ventana_administrador, text="Identificación")
        self.label_identificacion.pack()
        self.entry_identificacion = tk.Entry(self.ventana_administrador)
        self.entry_identificacion.pack()

        btn_aceptar_registro = tk.Button(self.ventana_administrador, text="Aceptar", command=self.agregar_administrador)
        btn_aceptar_registro.pack()

      

    def agregar_administrador(self):
        try:
            nombre = self.entry_nombre.get()
            identificacion = self.entry_identificacion.get()

            conexion = sqlite3.connect('mi_base_de_datos_administradores.db')
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS Administradores (Nombre TEXT, Identificacion TEXT)''')

            cursor.execute("INSERT INTO Administradores (Nombre, Identificacion) VALUES (?, ?)", (nombre, identificacion))

            conexion.commit()
            conexion.close()

            messagebox.showinfo("Registro exitoso", "Datos del administrador registrados correctamente")
            self.ventana_administrador.destroy()  # Cerrar la ventana de registros

        except sqlite3.Error as error:
            messagebox.showerror("Error", f"No se pudo agregar a la base de datos: {error}")

    def ventana_personal(self):
        self.ventana_personal = tk.Toplevel(self.root)
        self.ventana_personal.title("Registro de Personal")
        self.ventana_personal.geometry("400x400")

        self.label_nombre = tk.Label(self.ventana_personal, text="Ingrese nombre empleado:")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.ventana_personal)
        self.entry_nombre.pack()

        self.label_identificacion = tk.Label(self.ventana_personal, text="Ingrese identificación:")
        self.label_identificacion.pack()
        self.entry_identificacion = tk.Entry(self.ventana_personal)
        self.entry_identificacion.pack()

        self.label_cargo = tk.Label(self.ventana_personal, text="Ingrese cargo:")
        self.label_cargo.pack()
        self.entry_cargo = tk.Entry(self.ventana_personal)
        self.entry_cargo.pack()

        btn_aceptar = tk.Button(self.ventana_personal, text="Aceptar", command=self.aceptar)
        btn_aceptar.pack()

        btn_finalizar = tk.Button(self.ventana_personal, text="Finalizar", command=self.finalizar_registros)
        btn_finalizar.pack()

    def aceptar(self):
        nombre = self.entry_nombre.get()
        identificacion = self.entry_identificacion.get()
        cargo = self.entry_cargo.get()

        print("Nombre:", nombre)
        print("Identificación:", identificacion)
        print("Cargo:", cargo)

        #inserción en la base de datos  (con SQL)
        conexion = sqlite3.connect('mi_base_de_datos_personal.db')
        cursor = conexion.cursor()

    
        cursor.execute('''CREATE TABLE IF NOT EXISTS Personal (Nombre TEXT, Identificacion TEXT, Cargo TEXT)''')

        # Insertar datos en la tabla
        cursor.execute("INSERT INTO Personal (Nombre, Identificacion, Cargo) VALUES (?, ?, ?)", (nombre, identificacion, cargo))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Registro exitoso", "Datos del empleado registrados correctamente")

    def finalizar_registros(self):
        messagebox.showinfo("Registros finalizados", "Registros de personal finalizados")
        self.ventana_personal.destroy()  # Cerrar la ventana de registros de personal

        
        
    def ventana_sede(self):
        def seleccionar_sede():
            sede_seleccionada = var.get()
            messagebox.showinfo("Sede seleccionada", f"Sede seleccionada: {sede_seleccionada}")
            self.guardar_sede(sede_seleccionada)

        ventana_sede = tk.Toplevel(self.root)
        ventana_sede.title("Seleccionar Sede")
        ventana_sede.geometry("400x400")

        label_sede = tk.Label(ventana_sede, text="Ubicación de la sede:")
        label_sede.pack()

        opciones = ["Medellin", "Itagui", "Envigado", "Belen"]

        var = tk.StringVar(ventana_sede)
        var.set(opciones[0])

        dropdown = tk.OptionMenu(ventana_sede, var, *opciones)
        dropdown.pack()

        btn_seleccionar = tk.Button(ventana_sede, text="Seleccionar", command=seleccionar_sede)
        btn_seleccionar.pack()

    def guardar_sede(self, sede):
        #inserción en la base de datos (con SQL)
        conexion = sqlite3.connect('mi_base_de_datos_sedes.db')
        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Sedes (Nombre TEXT)''')

        # Insertar datos en la tabla
        cursor.execute("INSERT INTO Sedes (Nombre) VALUES (?)", (sede,))

        conexion.commit()
        conexion.close()

    def ventana_ventas(self):
        def agregar_venta():
            medio_pago = self.var_medio_pago.get()
            valor = self.entry_valor.get()
        
            print("Medio de Pago:", medio_pago)
            print("Valor:", valor)
            self.guardar_venta(medio_pago, valor)

        def finalizar_registros():
            messagebox.showinfo("Registros finalizados", "Registros de ventas finalizados")

        ventana_ventas = tk.Toplevel(self.root)
        ventana_ventas.title("Registro de Ventas")
        ventana_ventas.geometry("400x400")

        label_medio_pago = tk.Label(ventana_ventas, text="Medio de Pago:")
        label_medio_pago.pack()

        opciones_medio_pago = ["Transferencia", "Efectivo"]
        self.var_medio_pago = tk.StringVar(ventana_ventas)
        self.var_medio_pago.set(opciones_medio_pago[0])

        dropdown_medio_pago = tk.OptionMenu(ventana_ventas, self.var_medio_pago, *opciones_medio_pago)
        dropdown_medio_pago.pack()

        label_valor = tk.Label(ventana_ventas, text="Valor:")
        label_valor.pack()
        self.entry_valor = tk.Entry(ventana_ventas)
        self.entry_valor.pack()

    
        btn_finalizar = tk.Button(ventana_ventas, text="Finalizar", command=finalizar_registros)
        btn_finalizar.pack()

    def guardar_venta(self, medio_pago, valor):
        conexion = sqlite3.connect('mi_base_de_datos_ventas.db')
        cursor = conexion.cursor()

        # Crear la tabla si no existe
        cursor.execute('''CREATE TABLE IF NOT EXISTS Ventas (MedioPago TEXT, Valor REAL)''')

        # Insertar datos en la tabla Ventas
        cursor.execute("INSERT INTO Ventas (MedioPago, Valor) VALUES (?, ?)", (medio_pago, valor))

        # Guardar los cambios y cerrar la conexión
        conexion.commit()
        conexion.close()
        pass

    def ventana_egresos(self):
        def registrar_egreso():
            tipo_egreso = self.var_tipo_egreso.get()
            monto_egreso = self.entry_monto.get()
            observaciones = self.text_observaciones.get("1.0", "end-1c")
            orden_compra = self.entry_orden_compra.get() if self.entry_orden_compra else ""
            num_factura = self.entry_num_factura.get() if self.entry_num_factura else ""

            self.guardar_egreso(tipo_egreso, monto_egreso, observaciones, orden_compra, num_factura)

        ventana_egresos = tk.Toplevel(self.root)
        ventana_egresos.title("Registro de Egresos")
        ventana_egresos.geometry("400x400")

        label_tipo_egreso = tk.Label(ventana_egresos, text="Tipo de Egreso:")
        label_tipo_egreso.pack()

        opciones_tipo_egreso = ["Arqueo", "Compra proveedores", "Otro"]
        self.var_tipo_egreso = tk.StringVar(ventana_egresos)
        self.var_tipo_egreso.set(opciones_tipo_egreso[0])

        dropdown_tipo_egreso = tk.OptionMenu(ventana_egresos, self.var_tipo_egreso, *opciones_tipo_egreso, command=self.mostrar_campos)
        dropdown_tipo_egreso.pack()

        label_monto = tk.Label(ventana_egresos, text="Monto:")
        label_monto.pack()
        self.entry_monto = tk.Entry(ventana_egresos)
        self.entry_monto.pack()

        self.entry_orden_compra = tk.Entry(ventana_egresos)
        self.entry_num_factura = tk.Entry(ventana_egresos)

        label_observaciones = tk.Label(ventana_egresos, text="Observaciones:")
        label_observaciones.pack()
        self.text_observaciones = tk.Text(ventana_egresos, height=4, width=30)
        self.text_observaciones.pack()

        btn_aceptar_egreso = tk.Button(ventana_egresos, text="Aceptar", command=registrar_egreso)
        btn_aceptar_egreso.pack()

    def mostrar_campos(self, event):
        if self.var_tipo_egreso.get() == "Compra proveedores":
            self.entry_orden_compra.pack()
            self.entry_num_factura.pack()
        else:
            self.entry_orden_compra.pack_forget()
            self.entry_num_factura.pack_forget()

    def guardar_egreso(self, tipo_egreso, monto, observaciones, orden_compra, num_factura):
        conexion = sqlite3.connect('mi_base_de_datos_egresos.db')
        cursor = conexion.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS Egresos (TipoEgreso TEXT, Monto REAL, Observaciones TEXT, OrdenCompra TEXT, NumFactura TEXT)''')

        cursor.execute("INSERT INTO Egresos (TipoEgreso, Monto, Observaciones, OrdenCompra, NumFactura) VALUES (?, ?, ?, ?, ?)", (tipo_egreso, monto, observaciones, orden_compra, num_factura))

        conexion.commit()
        conexion.close()

        messagebox.showinfo("Registro Completo", "El registro se ha completado exitosamente")


    
    def ventana_resultados(self):
        # Crea una nueva ventana para mostrar los resultados
        ventana_resultados = tk.Toplevel(self.root)
        ventana_resultados.title("Resultados")
        ventana_resultados.geometry("600x400")

    def mostrar_resultados(self):
        try:
            ventana_resultados = tk.Toplevel(self.root)
            ventana_resultados.title("Resultados")
            ventana_resultados.geometry("600x400")

            tablas = [
                ("Caja", "Registros de Caja"),
                ("Administradores", "Registros de Administradores"),
                ("Personal", "Registros de Personal"),
                ("Sedes", "Registros de Sedes"),
                ("Ventas", "Registros de Ventas"),
                ("Egresos", "Registros de Egresos")
            ]

            for tabla, etiqueta in tablas:
                self.mostrar_resultados_tabla(ventana_resultados, tabla, etiqueta)

            btn_mostrar_resultados = tk.Button(ventana_resultados, text="Cerrar", command=ventana_resultados.destroy)
            btn_mostrar_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error en la base de datos: {e}")

    def mostrar_resultados_tabla(self, ventana, nombre_tabla, texto_etiqueta):
        try:
            conexion = sqlite3.connect(f'mi_base_de_datos_{nombre_tabla.lower()}.db')
            cursor = conexion.cursor()
            cursor.execute(f'SELECT * FROM {nombre_tabla}')
            data = cursor.fetchall()
            conexion.close()

            label = tk.Label(ventana, text=texto_etiqueta)
            label.pack()

            for registro in data:
                label_registro = tk.Label(ventana, text=registro)
                label_registro.pack()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error en la base de datos: {e}")
    
    
    def borrar_base_de_datos(self):
        nombres_bases = [
            'mi_base_de_datos.db',
            'mi_base_de_datos_administradores.db',
            'mi_base_de_datos_personal.db',
            'mi_base_de_datos_sedes.db',
            'mi_base_de_datos_ventas.db',
            'mi_base_de_datos_egresos.db'
        ]

        try:
            for nombre in nombres_bases:
                conexion = sqlite3.connect(nombre)
                cursor = conexion.cursor()

                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tablas = cursor.fetchall()
                for tabla in tablas:
                    cursor.execute(f"DELETE FROM {tabla[0]};")

                conexion.commit()
                conexion.close()

            messagebox.showinfo("Borrado exitoso", "Toda la información ha sido eliminada de las bases de datos.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al borrar la base de datos: {e}")



if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazSkyCord(root)
    btn_mostrar_resultados = tk.Button(root, text="Mostrar Resultados", command=app.mostrar_resultados)
    btn_mostrar_resultados.pack()
    btn_borrar_datos = tk.Button(root, text="Borrar Datos", command=app.borrar_base_de_datos)
    btn_borrar_datos.pack()
    root.mainloop()





class Caja:
    def __init__(self):
        self.base_caja = 0
        self.monto_en_caja = 0

    def registrar_base_caja(self):
        self.base_caja = float(input("Ingrese la base de la caja: "))

    def registrar_monto_en_caja(self):
        self.monto_en_caja = float(input("Ingrese el monto actual en caja: "))

    def mostrar_estado_caja(self):
        print("Base de caja:", self.base_caja)
        print("Monto en caja:", self.monto_en_caja)


class Administrador:
    def __init__(self, nombre: str, identificacion: int):
        self.nombre = nombre
        self.identificacion = identificacion

    def mostrar_informacion(self):
        print("Nombre del administrador:", self.nombre)
        print("Identificación:", self.identificacion)


class Personal:
    CARGO_VENDEDOR = "cargo_vendedor"
    CARGO_AUXILIAR_BODEGA = "cargo_auxiliar_bodega"

    def __init__(self, nombre:str, identificacion:int, cargo:str):
        self.nombre = nombre
        self.identificacion = identificacion
        self.cargo = cargo


    @classmethod
    def registrar_personal(cls):
        # Lista para almacenar los empleados
        empleados = []

        while True:
            nombre = input("Ingrese el nombre del empleado: ")
            identificacion = int(input("Ingrese la identificación del empleado: "))
            cargo = input("Ingrese el cargo del empleado: ")

            empleado = cls(nombre, identificacion, cargo)
            empleados.append(empleado)

            otro_empleado = input("¿Desea registrar otro empleado? (Sí/No): ")
            if otro_empleado.lower() != 'sí' and otro_empleado.lower() != 'si':
                break

        return empleados
class GestionPersonal:
    administradores = []
    personal_a_cargo = []

    @classmethod
    def registrar_administrador(cls, nombre: str, identificacion: int):
        nuevo_administrador = Administrador(nombre, identificacion)
        cls.administradores.append(nuevo_administrador)

    @classmethod
    def mostrar_administradores(cls):
        print("Lista de Administradores:")
        for administrador in cls.administradores:
            administrador.mostrar_informacion()

    @classmethod
    def mostrar_personal(cls):
        print("Lista de Personal a Cargo:")
        for persona in cls.personal_a_cargo:
            print("Nombre:", persona.nombre)
            print("Identificación:", persona.identificacion)
            print("Cargo:", persona.cargo)


class Sede:
    def __init__(self, nombre:str):
        self.nombre = nombre

    def mostrar_informacion(self):
        print("Nombre de la sede:", self.nombre)


class Venta:
    MEDIO_DE_PAGO_EFECTIVO = "efectivo"
    MEDIO_DE_PAGO_TRANSFERENCIA = "transferencia"
    ventas = []
    total_ventas = 0 

    def __init__(self, consecutivo: int, monto: float, medio_pago: str, observaciones: str):
        self.consecutivo = consecutivo
        self.monto = monto
        self.medio_pago = medio_pago
        self.observaciones = observaciones
        self.__class__.ventas.append(self) 
        self.__class__.total_ventas += monto 

    @classmethod
    def registrar_venta(cls, venta):
        cls.ventas.append(venta)

    @classmethod
    def calcular_venta_efectivo(cls):
        total_efectivo = sum(venta.monto for venta in cls.ventas if venta.medio_pago == cls.MEDIO_DE_PAGO_EFECTIVO)
        return total_efectivo

    @classmethod
    def calcular_venta_transferencia(cls):
        total_transferencia = sum(venta.monto for venta in cls.ventas if venta.medio_pago == cls.MEDIO_DE_PAGO_TRANSFERENCIA)
        return total_transferencia
    
    @classmethod
    def calcular_total_ventas(cls):
        return sum(venta.monto for venta in cls.ventas)

    @classmethod
    def obtener_total_ventas(cls):
        return cls.calcular_total_ventas()

class Egreso:
    tipos_egreso = ['compra_proveedores', 'arqueo', 'otro']
    egresos = {tipo: [] for tipo in tipos_egreso}
    total_egresos = {tipo: 0 for tipo in tipos_egreso}  # Total egresos for each type

    def __init__(self, tipo: str, monto: float, observacion: str, orden_compra: str = None, num_factura: str = None):
        self.tipo = tipo
        self.monto = monto
        self.observacion = observacion
        self.orden_compra = orden_compra
        self.num_factura = num_factura

        self.__class__.egresos[tipo].append(self)  # Store the egreso in the class attribute
        self.__class__.total_egresos[tipo] += monto 
        Egreso.egresos[tipo].append(self)
    
    @classmethod
    def registrar_egresos(cls):
        tipo_egreso = input("Ingrese el tipo de egreso (compra_proveedores, arqueo u otro): ")
        monto_egreso = float(input("Ingrese el monto del egreso: "))
        observaciones_egreso = input("Ingrese observaciones del egreso: ")
        
        if tipo_egreso == 'compra_proveedores':
            orden_compra = input("Ingrese el número de orden de compra: ")
            num_factura = input("Ingrese el número de factura: ")
            cls(tipo_egreso, monto_egreso, observaciones_egreso, orden_compra, num_factura)
        else:
            cls(tipo_egreso, monto_egreso, observaciones_egreso)
    @classmethod
    def calcular_egresos_totales(cls):
        total_egresos_all = sum(sum(egreso.monto for egreso in cls.egresos[tipo]) for tipo in cls.tipos_egreso)
        return total_egresos_all

    @classmethod
    def obtener_total_egresos(cls):
        return cls.total_egresos
    


# Crear una instancia de la caja
caja = Caja()
# Registro de la sede
nombre_sede = input("Ingrese el nombre de la sede: ")
sede = Sede(nombre_sede)

# Registro de la base de la caja y el monto en caja
caja.registrar_base_caja()
caja.registrar_monto_en_caja()

# Registrar administrador
nombre_admin = input("Ingrese el nombre del administrador: ")
identificacion_admin = int(input("Ingrese la identificación del administrador: "))
GestionPersonal.registrar_administrador(nombre_admin, identificacion_admin)

# Registrar personal a cargo
print("Registro de personal a cargo:")
empleados_registrados = Personal.registrar_personal()
# Mostrar información de la sede
print("\nInformación de la sede:")
sede.mostrar_informacion()
# Mostrar información de los empleados registrados
GestionPersonal.mostrar_administradores()
print("\nInformación de los empleados registrados:")
for empleado in empleados_registrados:
    print("Nombre:", empleado.nombre)
    print("Identificación:", empleado.identificacion)
    print("Cargo:", empleado.cargo)
# Registro de ventas
num_ventas = int(input("Ingrese el número de ventas a registrar: "))
for i in range(num_ventas):
    print(f"\nRegistro de venta {i+1}:")
    consecutivo = int(input("Ingrese el consecutivo de la venta: "))
    monto = float(input("Ingrese el monto de la venta: "))
    medio_pago = input("Ingrese el medio de pago (efectivo o transferencia): ").lower()
    observaciones = input("Ingrese observaciones: ")

    venta = Venta(consecutivo, monto, medio_pago, observaciones)
    Venta.registrar_venta(venta)


# Registro de egresos
num_egresos = int(input("Ingrese el número de egresos a registrar: "))
for i in range(num_egresos):
    print(f"\nRegistro de egreso {i+1}:")
    Egreso.registrar_egresos()


# Mostrar estado de la caja
print("\nEstado de la caja:")
caja.mostrar_estado_caja()

# Calcular total de ventas por medio de pago
total_ventas_efectivo = Venta.calcular_venta_efectivo()
total_ventas_transferencia = Venta.calcular_venta_transferencia()
total_ventas = Venta.calcular_total_ventas()

print("Total de ventas en efectivo:", total_ventas_efectivo)
print("Total de ventas por transferencia:", total_ventas_transferencia)
print("Total de ventas:", total_ventas)

# Calcular total de egresos por tipo
print("Total de egresos por tipo:")
for tipo_egreso in Egreso.tipos_egreso:
    print(f"Total de egresos {tipo_egreso}:", sum(egreso.monto for egreso in Egreso.egresos[tipo_egreso]))

# Calcular total de egresos en general
total_egresos_all = Egreso.calcular_egresos_totales()
print("Total de egresos en general:", total_egresos_all)
# Mostrar información
