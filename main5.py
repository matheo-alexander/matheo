def validartitulo(titulo):
    """Valida que el texto no esté vacío."""
    if len(titulo.strip()) > 0:
        return True
    return False

def buscarlibroportitulo(lista, titulo):
    """Busca un libro por título e introduce control de mayúsculas/minúsculas."""
    for indice, li in enumerate(lista):
        if li["titulo"].lower() == titulo.lower():
            return indice
    return -1

def agregarlibro(lista):
    titulo = input("Ingrese titulo del libro: ").strip()
    resp = validartitulo(titulo=titulo)
    if resp == False:
        print("Titulo no debe estar vacio...")
        return False
    
    # Validar que no se repita el libro
    pos = buscarlibroportitulo(lista=lista, titulo=titulo)
    if pos != -1:
        print("El libro ya se encuentra registrado...")
        return False
    
    autor = input("Ingrese autor del libro: ").strip()
    resp = validartitulo(titulo=autor)
    if resp == False:
        print("Autor no debe estar vacio...")
        return False
    
    libro = {
        "titulo": titulo,
        "autor": autor,
        "disponible": True
    }
    lista.append(libro)
    return True

def buscarlibro(lista):
    nom = input("Ingrese nombre del libro: ").strip()
    pos = buscarlibroportitulo(lista=lista, titulo=nom)
    if pos == -1:
        print("Libro no encontrado...")
        return False
    
    li = lista[pos]
    estado = "Disponible" if li["disponible"] else "Prestado"
    print(f"\nLibro Encontrado:\nTítulo: {li['titulo']}\nAutor: {li['autor']}\nEstado: {estado}")
    return True

def eliminarlibro(lista):
    nom = input("Ingrese libro a eliminar: ").strip()
    pos = buscarlibroportitulo(lista=lista, titulo=nom)
    if pos == -1:
        print("No se encontro libro...")
        return False
    lista.pop(pos)
    return True

def actualizardisponibilidad(lista):
    nom = input("Ingrese el título del libro para cambiar disponibilidad: ").strip()
    pos = buscarlibroportitulo(lista=lista, titulo=nom)
    if pos == -1:
        print("Libro no encontrado...")
        return False
    
    # Cambia el estado de True a False o de False a True automáticamente
    lista[pos]["disponible"] = not lista[pos]["disponible"]
    estado = "Disponible" if lista[pos]["disponible"] else "Prestado"
    print(f"Disponibilidad actualizada. Ahora el libro está: {estado}")
    return True

def mostrarlibros(lista):
    if len(lista) == 0:
        print("No hay libros registrados en la biblioteca...")
        return
    print("\n=== LISTA DE TODOS LOS LIBROS ===")
    for li in lista:
        estado = "Disponible" if li["disponible"] else "Prestado"
        print(f"Titulo: {li['titulo']} - Autor: {li['autor']} - Disponibilidad: {estado}")


# ---------------------------------------------------------------
# SECCIÓN 2: MENÚ PRINCIPAL Y FLUJO DE CONTROL
# ---------------------------------------------------------------

lista_libros = []

def menu():
    print('''
        ====== MENÜ PRINCIPAL ======
        1. Agregar libro
        2. Buscar libro
        3. Eliminar libro
        4. Actualizar disponibilidad
        5. Mostrar todods los libros
        6. Salir
        =============================
        ''')

def seleccion():
    try:
        op = int(input("Seleccione: "))
        if op >= 1 and op <= 6:
            return op
        return 0
    except:
        return 0

ciclo = True
while ciclo:
    menu()
    opcion = seleccion()
    
    if opcion == 1:
        print("=== AGREGAR LIBRO ===")
        resp = agregarlibro(lista_libros)
        if resp == True:
            print("Libro agregado...")
        else:
            print("No se pudo agregar libro...")
            
    elif opcion == 2:
        print("=== BUSCAR LIBRO ===")
        buscarlibro(lista_libros)
        
    elif opcion == 3:
        print("=== ELIMINAR LIBRO ===")
        resp = eliminarlibro(lista_libros)
        if resp == True:
            print("libro eliminado...")
        else:
            print("No se elimino el libro...")
            
    elif opcion == 4:
        print(" === ACTUALIZAR DISPONIBILIDAD ===")
        actualizardisponibilidad(lista_libros)
        
    elif opcion == 5:
        print("=== MOSTRAR TODOS LOS LIBROS ===")
        mostrarlibros(lista_libros)
        
    elif opcion == 6:
        print("Adios...")
        ciclo = False
        
    else:
        print("Opción inválida. Intente de nuevo...")