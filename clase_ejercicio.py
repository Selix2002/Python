from dataclasses import dataclass

@dataclass
class Libro:
    title = str
    autor = str
    isbn = str
    disponible = bool 
    
    def mostrar_info(self):
        if self.disponible:
            return f"Autor:{self.autor} ; Titulo:{self.title} ; Estado: Disponible"
        else:
            return f"Autor:{self.autor} ; Titulo:{self.title} ; Estado: No disponible"
    def prestar(self):
        if self.disponible:
            self.disponible = False
    def devolver(self):
        if not self.disponible:
            self.disponible = True
@dataclass
class Usuario:
    nombre = str
    id_usuario = str
    prestamos = list[Libro]

    def tomar_libro(self, other: "Libro"):
        if other.disponible:
            self.prestamos.append(other)
        else:
            return "El libro no esta disponible"
    def devolver(self, other: "Libro"):
        if other in self.prestamos:
            self.prestamos.remove(other)
            other.disponible = True
        else:
            return "Este usuario no tiene el libro especificado"

@dataclass
class Biblioteca:
    nombre = str
    libros = list[Libro]
    usuarios = list[Usuario]

    def agregar_bibloteca(self):
        self.nombre = input("Agregue una biblioteca: ")
    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ").strip().lower()
        autor = input("Ingrese el nombre del autor: ").strip()
        isbn = input("Ingrese el ISBN del libro: ").strip()
        
        if titulo in self.libros:
            print("El libro ya existe en la biblioteca.")
            return

        libro = Libro(titulo=titulo, autor=autor, isbn=isbn)
        self.libros.append(libro)
        print(f"Libro '{titulo}' agregado correctamente.")

    def registrar_usuario(self):
        user = Usuario()
        user.nombre = input("Ingrese el nombre del usuario: ")
        user.id_usuario = input("Ingrese la ID: ")
        self.usuarios.append(user)

    def mostrar_libro_disponibles(self):
        for libro in self.libros:
            print(self.libros[libro])
    def buscar_libro_por_titulo(self, titulo: str) -> "Libro | None":
        return self.libros.get(titulo.lower())


biblio1 = Biblioteca()
biblio1.agregar_bibloteca()
biblio1.agregar_libro()