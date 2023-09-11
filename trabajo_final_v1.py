from guizero import App, PushButton, Text, TextBox, Window, Picture, info, ListBox, ButtonGroup, Box

# Abrir ventana alumno

def abrir_ventana_alumno():
    ventana_alumno.show(wait=True)

# abrir ventana Docente

def check_password():
    password = password_box.value
    if password == "123":
        info("Acceso concedido", "Contraseña correcta")
        ventana_docente.show(wait=True)
    else:
        info("Acceso denegado", "Contraseña incorrecta")

# Ventana password

def abrir_password_dialogo():
    global password_box  # Declarar la variable como global
    password_app = App("Ingrese la contraseña", width=300, height=100)
    password_app.bg="#ffb910"
    password_box = TextBox(password_app, width=20, hide_text=True)
    password_box.bg="white"
    submit_button = PushButton(password_app, text="Ingresar", command=check_password)
    submit_button.bg="white"
    password_app.focus()  
    password_app.display()

# generar y agregar preguntas y opciones

def agregar_pregunta():
    dato = input_pregunta.value
    lista_pregunta.append(dato)
    pregunta_box.append(dato)
    input_pregunta.clear()
    with open("pregunta.txt", "w") as archivo:
        for elemento in lista_pregunta:
            archivo.write(str(elemento) + "\n")

def agregar_opciones():
    dato = input_opciones.value
    lista_opciones.append(dato)
    opciones_box.append(dato)
    input_opciones.clear()
    with open("opciones.txt", "w") as archivo:
        for elemento in lista_opciones:
            archivo.write(str(elemento) + "\n")

# ACTUALIZA LOS DATOS DE LAS OPCIONES

def actualizarTitulo():
    leerPreguntasAlumnos()
    texto.clear() # limpia la lista del ButtonGroup
    for el in pregunta:
        texto.append(el)

def actualizarDatos():
    leerOpcionesAlumnos()
    eleccion.clear() 
    for el in opciones:
        eleccion.append(el)

def cerrar_ventana_al():
    if ventana_alumno.yesno("Cerrar", "¿Está seguro de querer salir?"):
        ventana_alumno.destroy()

def cerrar_ventana():
    ventana_docente.hide()

def llamarFuncionesDeActualizar1():
    actualizarTitulo()
    actualizarDatos()
    cerrar_ventana()
    eleccion.value=None

# Guardar opcion alumno

def actualizar():
    with open("pregunta.txt", "w") as archivo:
        for elemento in lista_pregunta:
            archivo.write(str(elemento) + "\n")
    with open("opciones.txt", "w") as archivo:
        for elemento in lista_opciones:
            archivo.write(str(elemento) + "\n")

def respuesta_alumno():
    elemento = eleccion.value
    with open("respuestas.txt", "w") as archivo:
        archivo.write(str(elemento) + "\n")

# ***** PROGRAMA PRINCIPAL *****

# Ventanas Inicio - Docente - Alumno

app = App(title="Inicio", height=500, width=500, bg="white")
box = Box(app, layout="grid")
ventana_docente = Window(app, title="Docentes", height=600, width=600, bg="#faff73")
ventana_docente.hide()
box = Box(ventana_docente, layout="grid")
ventana_alumno = Window(app, title="Alumnos", width=600, height=500, bg="#faff73" )
ventana_alumno.hide()
box = Box(ventana_alumno, layout="grid")
app.icon = "icono.png"

# Ingresar a ventana docente
espacio = Box(app, height=20)
mensaje = Text(app, text="Bienvenido a la encuesta", color="red", size=17)
espacio = Box(app, height=20)
btn_alumnos = PushButton(app, text="alumnos", width=12, command=abrir_ventana_alumno)
btn_alumnos.bg = "#ffb910"
espacio = Box(app, height=20)
btn_docentes = PushButton(app, text="Docentes", width=12, command=abrir_password_dialogo)
btn_docentes.bg="#ffb910"
imagen = Picture(app, image="icon-256x256.png", align="bottom")

#button = PushButton(app, text="Ingresar contraseña", command=abrir_password_dialogo)

# Ingreso datos ventana docente
imagen = Picture(ventana_docente, image="pexels-steve-johnson-1269968.jpg",width=250, height=600, align="left")
imagen = Picture(ventana_alumno, image="pexels-steve-johnson-1269968.jpg",width=300, height=500, align="left")
#content_box = (ventana_docente, align="left", height="fill", border=True)
espacio = Box(ventana_docente, height=10)
Text (ventana_docente,"Ingrese pregunta", size="15", color="#fe6323")
espacio = Box(ventana_docente, height=10)
input_pregunta = TextBox(ventana_docente, width=50)
input_pregunta.bg="white"
espacio = Box(ventana_docente, height=10)
agregar_button = PushButton(ventana_docente, text="Agregar", width="12", command=agregar_pregunta)
agregar_button.bg="#ffb910"
espacio = Box(ventana_docente, height=10)
pregunta_box = ListBox(ventana_docente, items=[], width=300, height=80)
pregunta_box.bg="white"
Text (ventana_docente, "-----------------------------------------------------------------------------------", size="10", color="#fe6323")
Text(ventana_docente, "Ingrese opciones", size="15", color="#fe6323")
espacio = Box(ventana_docente, height=10)
input_opciones = TextBox(ventana_docente, width=50)
input_opciones.bg="white"
espacio = Box(ventana_docente, height=10)
agregar_button = PushButton(ventana_docente, text="Agregar",width="12", command=agregar_opciones)
agregar_button.bg="#ffb910"
espacio = Box(ventana_docente, height=10)
opciones_box = ListBox(ventana_docente, items=[], width=300, height=80)
opciones_box.bg="white"
espacio = Box(ventana_docente, height=10)
btn_cerrar = PushButton(ventana_docente, text="Salir",width="12", command=llamarFuncionesDeActualizar1)
btn_cerrar.bg="#ffb910"
espacio = Box(ventana_docente, height=10)

def limpiarButtonGroup():
    pregunta_box.clear()
    opciones_box.clear()
    pregunta[:]=[]
    opciones[:]=[]
    with open("pregunta.txt", "w") as archivo:
        for elemento in lista_pregunta:
            archivo.write(str(elemento) + "\n")
    with open("opciones.txt", "w") as archivo:
        archivo.write(str(elemento) + "\n")

limpiar = PushButton(ventana_docente, text="Limpiar",width="12", command=limpiarButtonGroup)
limpiar.bg="#ffb910"
lista_pregunta = []
lista_opciones = []

# Ventana alumno
pregunta = []
opciones = []
def leerPreguntasAlumnos():
    pregunta[:]=[] # LIMPIA EL DICCIONARIO
    with open('pregunta.txt', 'r') as archivo: 
        lineas = archivo.readlines()           
    for linea in lineas:         
        linea = linea.strip()    
        elementos = linea.split(",")     
        pregunta.extend([str(elemento) for elemento in elementos])

def leerOpcionesAlumnos():
    opciones[:] = []

    with open('opciones.txt', 'r') as archivo: 
        lineas = archivo.readlines()           
    for linea in lineas:          
        linea = linea.strip()     
        elementos = linea.split(",")    
        opciones.extend([str(elemento) for elemento in elementos])

# LEE LOS DATOS EN LOS ARCHIVOS LA PRIMERA VEZ
leerPreguntasAlumnos()
leerOpcionesAlumnos()

#  ventana_alumno.hide()

espacio = Box(ventana_alumno, height=20)
texto=Text(ventana_alumno, [pregunta])
espacio = Box(ventana_alumno, height=20)
eleccion = ButtonGroup(ventana_alumno, options=opciones)
espacio = Box(ventana_alumno, height=20)
btn_enviar = PushButton(ventana_alumno, text="Enviar", command=respuesta_alumno, width=20)
btn_enviar.bg="#ffb910"
espacio = Box(ventana_alumno, height=20)
btn_salir = PushButton(ventana_alumno, text="Salir", width=20, command=cerrar_ventana_al)
btn_salir.bg="#ffb910"
app.display()