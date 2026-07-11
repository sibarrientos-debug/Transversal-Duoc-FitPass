def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion>0 and opcion<=6:
                return opcion
            else:
                print("Debe ingresar un número del 1-6")
        except ValueError:
            print("Debe seleccionar una opción válida")

def validar_tipo(tipo): 
    if tipo=="mensual":    
        return True
    elif tipo=="trimestral":
        return True
    elif tipo=="anual":
        return True
    else:
        return False
        
def validar_nombre(nombre):
    if nombre.strip()=="":
        return False
    else:
        return True

def validar_horario(horario):
    if horario.strip()=="":
        return False
    else:
        return True
    
def validar_duracion(duracion):
    if duracion>0:
        return True
    else:
        return False

def validar_sn(valor):
    return valor in ["s","n"]

def validar_precio(precio):
    if precio>0:
        return True
    else:
        return False
    
def validar_cupos(cupos):
    if cupos>=0:
        return True
    else:
        return False
    
def buscar_codigo(codigo,diccionario):
    for clave in diccionario:
        if clave.lower()==codigo.lower():
            return True
    return False 

def cupos_tipo(tipo,planes, inscripciones):
    total=0
    for clave in planes:
        if planes[clave][1].lower()==tipo.lower():
            total= total + inscripciones[clave][1]
    print("El total de cupos disponibles es:",total)

def busqueda_precio(p_min, p_max, inscripciones, planes):
    resultados=[]
    for clave in inscripciones:
        precio = inscripciones[clave][0]
        cupos = inscripciones[clave][1]
        if precio>=p_min and precio<=p_max and cupos!=0:
            texto=planes[clave][0]+"--"+clave
            resultados.append(texto)
    resultados.sort()    
    if resultados:
        print("Los planes encontrados son:",resultados)
    else:
        print("No hay planes en ese rango de precios")   
def actualizar_precio(codigo, nuevo_precio, inscripciones):
    if buscar_codigo(codigo, inscripciones):
        for clave in inscripciones:
            if clave.lower() == codigo.lower():
                inscripciones[clave][0] = nuevo_precio
                return True
    return False
def eliminar_plan(codigo, planes, inscripciones):
    if buscar_codigo(codigo, planes):
        for clave in list(planes.keys()):
            if clave.lower() == codigo.lower():
                del planes[clave]
                del inscripciones[clave]
                return True
    return False
def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
    if buscar_codigo(codigo, planes):
        return False
    planes[codigo] = [nombre, tipo, duracion, acceso_piscina, incluye_clases, horario]
    inscripciones[codigo] = [precio, cupos]
    return True

#PROGRAMA PRINCIPAL
planes = {
    'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
    'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
    'F003': ['Plan Estudiante', 'trimestral', 3, False, True, 'tarde'],
    'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
    'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
    'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],
}

inscripciones = {
    'F001': [14990, 30],
    'F002': [22990, 10],
    'F003': [39990, 0],
    'F004': [35990, 6],
    'F005': [159990, 2],
    'F006': [18990, 15],
}

while True:
    print("========== MENÚ PRINCIPAL ==========")
    print("1. Cupos por tipo de plan")
    print("2. Búsqueda de planes por rango de precio")
    print("3. Actualizar precio de plan")
    print("4. Agregar plan")
    print("5. Eliminar plan")
    print("6. Salir")
    print("=====================================")

    opcion = leer_opcion()

    if opcion == 1:
        tipo = input("Ingrese tipo de plan a consultar: ")
        cupos_tipo(tipo, planes, inscripciones)

    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio mínimo: "))
                p_max = int(input("Ingrese precio máximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
        busqueda_precio(p_min, p_max, inscripciones, planes)

    elif opcion == 3:
        respuesta = "s"
        while respuesta == "s":
            codigo = input("Ingrese código del plan: ")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
            except ValueError:
                print("Debe ingresar un valor entero")
                respuesta = input("¿Desea actualizar otro precio (s/n)?: ")
                continue
            if actualizar_precio(codigo, nuevo_precio, inscripciones):
                print("Precio actualizado")
            else:
                print("El código no existe")
            respuesta = input("¿Desea actualizar otro precio (s/n)?: ")

    elif opcion == 4:
        codigo = input("Ingrese código del plan: ")
        nombre = input("Ingrese nombre del plan: ")
        tipo = input("Ingrese tipo (mensual/trimestral/anual): ")
        try:
            duracion = int(input("Ingrese duración (meses): "))
        except ValueError:
            duracion = -1
        piscina = input("¿Incluye acceso a piscina? (s/n): ")
        clases = input("¿Incluye clases grupales? (s/n): ")
        horario = input("Ingrese horario: ")
        try:
            precio = int(input("Ingrese precio: "))
        except ValueError:
            precio = -1
        try:
            cupos = int(input("Ingrese cupos: "))
        except ValueError:
            cupos = -1

        if buscar_codigo(codigo, planes) or not validar_nombre(codigo):
            print("El código ya existe o no es válido")
        elif not validar_nombre(nombre):
            print("El nombre no es válido")
        elif not validar_tipo(tipo):
            print("El tipo no es válido")
        elif not validar_duracion(duracion):
            print("La duración no es válida")
        elif not validar_sn(piscina):
            print("El acceso a piscina debe ser s o n")
        elif not validar_sn(clases):
            print("Incluye clases debe ser s o n")
        elif not validar_horario(horario):
            print("El horario no es válido")
        elif not validar_precio(precio):
            print("El precio no es válido")
        elif not validar_cupos(cupos):
            print("Los cupos no son válidos")
        else:
            acceso_piscina = piscina == "s"
            incluye_clases = clases == "s"
            if agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases, horario, precio, cupos, planes, inscripciones):
                print("Plan agregado")
            else:
                print("El código ya existe")

    elif opcion == 5:
        codigo = input("Ingrese código del plan a eliminar: ")
        if eliminar_plan(codigo, planes, inscripciones):
            print("Plan eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break
