       FITPASS GYM

ADMINISTRACIÓN MEMBRESIAS

      MENU PRINCIPAL
=============================
1. Cupos por tipo de plan
   Pide un tipo (mensual/trimestral/anual, sin distinguir mayusculas)
   y muestra el total de cupos disponibles para ese tipo.

2. Busqueda de planes por rango de precio
   Pide precio minimo y maximo (deben ser numeros enteros).
   Muestra los planes en ese rango que tengan cupos disponibles,
   ordenados alfabeticamente por nombre.

3. Actualizar precio de plan
   Pide el codigo del plan y el nuevo precio.
   Si el codigo existe, actualiza el precio; si no, avisa.
   Pregunta si desea actualizar otro precio (s/n).

4. Agregar plan
   Pide todos los datos del nuevo plan (codigo, nombre, tipo,
   duracion, acceso a piscina, clases, horario, precio, cupos).
   Valida cada dato antes de registrar. Si algo es invalido,
   no agrega el plan e informa el error.

5. Eliminar plan
   Pide el codigo del plan. Si existe, lo elimina de ambos
   registros (planes e inscripciones); si no, avisa.

6. Salir
   Termina el programa mostrando "Programa finalizado."

DATOS

El programa trabaja con dos diccionarios internos (planes e
inscripciones) que ya vienen con 6 planes de ejemplo cargados
al iniciar. Estos datos existen solo mientras el programa esta
corriendo; se pierden al cerrarlo.

