from dataclasses import dataclass
from dataclasses import dataclass, field


@dataclass
class Libro:
    title: str
    autor: str
    isbn: str
    disponible: bool = True

    
    def mostrar_info(self):
        if self.disponible:
            return print(f"Autor:{self.autor} ; Titulo:{self.title} ; Estado: Disponible")
        else:
            return print(f"Autor:{self.autor} ; Titulo:{self.title} ; Estado: No disponible")
    def prestar(self):
        if self.disponible:
            self.disponible = False
    def devolver(self):
        if not self.disponible:
            self.disponible = True
@dataclass
class Usuario:
    nombre : str = ""
    id_usuario : str = ""
    prestamos: list[Libro] = field(default_factory=list)

    def tomar_libro(self, other: "Libro"):
        if other.disponible:
            self.prestamos.append(other)
        else:
            return print("El libro no esta disponible")
    def devolver(self, other: "Libro"):
        if other in self.prestamos:
            self.prestamos.remove(other)
            other.disponible = True
        else:
            return print("Este usuario no tiene el libro especificado")

@dataclass
class Biblioteca:
    nombre: str = ""
    libros: list[Libro] = field(default_factory=list)
    usuarios: list[Usuario] = field(default_factory=list)


    def agregar_bibloteca(self):
        self.nombre = input("Agregue una biblioteca: ")
    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el nombre del autor: ")
        isbn = input("Ingrese el ISBN del libro: ")
        
        if titulo in self.libros:
            print("El libro ya existe en la biblioteca.")
            return

        libro = Libro(title=titulo, autor=autor, isbn=isbn)
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
        for libro in self.libros:
            if libro.title.lower() == titulo.lower():
                return libro.mostrar_info()
        return print("NO CACHO BROTHER")  

biblio1 = Biblioteca()
biblio1.agregar_bibloteca()
biblio1.agregar_libro()
biblio1.buscar_libro_por_titulo("aaa")
