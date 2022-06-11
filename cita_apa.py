#--------------------------CITA APA------------------------------------#
# 03/05/2021
# Santiago, Chile
# Eddie Casañas
#----------------------------------------------------------------------#

def web():
	print("\nGENERADOR DE FUENTE APA PARA WEB:\n ")
	autor = input("Autor/Autores (EJ: Gallegos, R & Pietri, U): ")
	año = input("Año de publicacion (EJ: 2021 ): ")
	titulo = input("Titulo del articulo (EJ: Historia de Chile): ")
	fecha = input("Fecha de recuperacion (EJ: mayo 1, 2021): ")
	url = input("Enlace del articulo (EJ: wikipedia.org): ")
	
	print("\nFICHA BIBLIOGRAFICA:\n")
	ficha = autor.title() + " (" + año + "). " + titulo.title() + ". Recuperado en " + fecha + ", de " + url
	print(ficha)
	print("\nRecuperar ficha en cita_apa.txt")
	archivo = "cita_apa.txt"
	with open(archivo, "a") as file_object:
		file_object.write(ficha + "\n")
		
	
	

def libro():
	print("\nGENERADOR DE FUENTE APA PARA LIBROS:\n ")
	autor = input("Autor/Autores (EJ: Silva, M & Cervantes, M): ")
	año = input("Año de publicacion (EJ: 2021): ")
	titulo = input("Titulo del libro (EJ: Cuando quiero llorar, no lloro): ")
	lugar = input("Lugar de publicacion (EJ: Caracas, Venezuela): ")
	editorial = input("Editorial (EJ: Santillana): ")
	
	print("\nFICHA BIBLIOGRAFICA:\n")
	ficha = autor.title() + " (" + año + "). " + titulo.title() + ". " + lugar.title() + ": " + editorial.title()
	print(ficha)
	print("\nRecuperar ficha en cita_apa.txt")
	
	archivo = "cita_apa.txt"
	with open(archivo, "a") as file_object:
		file_object.write(ficha + "\n")
		

while True:
	print("\nElegir el medio que se quiere citar: ")
	print("(1): Web")
	print("(2): Libro")
	opcion = input()
	if opcion.lower().strip() == "1":
		web()
		pregunta = input("\n¿Deseas imprimir otra ficha? (y/n): ")
		if pregunta.lower().strip() == "y":
			continue
		else:
			break
	elif opcion.lower().strip() == "2":
		libro()
		pregunta = input("\n¿Deseas imprimir otra ficha? (y/n): ")
		if pregunta.lower().strip() == "y":
			continue
		else:
			break
