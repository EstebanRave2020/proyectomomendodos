import mysql.connector
import hashlib

class Director:
    def _init_(self, nombre, apellido=None):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    def _str_(self):
        if self._apellido:
            return f"{self._nombre} {self._apellido}"
        else:
            return self._nombre

class Actor:
    def _init_(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    def _str_(self):
        return f"{self._nombre} {self._apellido}"

class Pelicula:
    def _init_(self, titulo, anno):
        self._titulo = titulo
        self._anno = anno
        self._director = None
        self._actores = []

    @property
    def titulo(self):
        return self._titulo

    @property
    def anno(self):
        return self._anno

    @property
    def director(self):
        return self._director

    @property
    def actores(self):
        return self._actores

    def asignar_director(self, director):
        self._director = director

    def agregar_actor(self, actor):
        self._actores.append(actor)

    def mostrar_info(self):
        print(f"\nInformación de la película:")
        print(f"Título: {self._titulo}")
        print(f"Año: {self._anno}")
        print(f"Director: {self._director}")
        print("Actores:")
        for actor in self._actores:
            print(actor)

    def _str_(self):
        return f"\nInformación de la película:\nTítulo: {self._titulo}\nAño: {self._anno}\nDirector: {self._director}\nActores: {', '.join(map(str, self._actores))}"

class Inicio:
    usuarios = {
        "esteban": "81dc9bdb52d04dc20036dbd8313ed055",  # Contraseña: 343
        "evant": "e10adc3949ba59abbe56e057f20f883e"   # Contraseña: 546
    }

    def _init_(self):
        self.usuario_actual = None
        self.peliculas = {}
        self.directores = {}
        self.actores = {}

    def registrar_usuario(self):
        print("Registro de usuario")
        nombre_usuario = input("Ingrese un nombre de usuario: ")

        # Verificar si el nombre de usuario ya existe
        if nombre_usuario in self.usuarios:
            print("¡Error! El nombre de usuario ya está en uso.")
            return

        # Pedir y hashear la contraseña
        contrasena = input("Ingrese una contraseña: ")
        hashed_contrasena = hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

        # Guardar el nombre de usuario y la contraseña hasheada
        self.usuarios[nombre_usuario] = hashed_contrasena
        print("¡Registro exitoso!")

        # Llevar directamente al menú de películas después del registro
        self.usuario_actual = nombre_usuario
        self.menu_peliculas()

    def iniciar_sesion(self):
        print("Inicio de sesión")
        nombre_usuario = input("Ingrese su nombre de usuario: ")

        # Verificar si el nombre de usuario existe
        if nombre_usuario not in self.usuarios:
            print("¡Error! El nombre de usuario no existe.")
            return

        # Verificar la contraseña
        contrasena = input("Ingrese su contraseña: ")
        hashed_contrasena_guardada = self.usuarios[nombre_usuario]

        # Verificar la contraseña hasheada
        if hashlib.sha256(contrasena.encode('utf-8')).hexdigest() == hashed_contrasena_guardada:
            print("¡Inicio de sesión exitoso!")

            # Llevar directamente al menú de películas después del inicio de sesión
            self.usuario_actual = nombre_usuario
            self.menu_peliculas()
        else:
            print("¡Error! Contraseña incorrecta.")

    def menu_peliculas(self):
        while True:
            print("¿Qué quieres hacer?")
            print("\n1. Agregar director")
            print("2. Mostrar directores")
            print("3. Agregar actor")
            print("4. Mostrar actores")
            print("5. Crear película")
            print("6. Mostrar películas")
            print("7. Cerrar sesión")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_director()
            elif opcion == "2":
                self.mostrar_directores()
            elif opcion == "3":
                self.agregar_actor()
            elif opcion == "4":
                self.mostrar_actores()
            elif opcion == "5":
                self.crear_pelicula(callback=lambda: print("¡Película creada exitosamente!"))
            elif opcion == "6":
                self.mostrar_peliculas()
            elif opcion == "7":
                print("Cerrando sesión.")
                self.usuario_actual = None
                break
            else:
                print("Opción no válida. Inténtelo de nuevo.")

    def agregar_director(self):
        nombre_director = input("Ingrese el nombre del director: ")
        apellido_director = input("Ingrese el apellido del director (opcional): ")

        if apellido_director:
            director = Director(nombre_director, apellido_director)
        else:
            director = Director(nombre_director)

        self.directores[(nombre_director, apellido_director)] = director
        print(f"Director {director} agregado correctamente.")

    def mostrar_directores(self):
        print("Directores:")
        for director in self.directores.values():
            print(director)

    def agregar_actor(self):
        nombre_actor = input("Ingrese el nombre del actor: ")
        apellido_actor = input("Ingrese el apellido del actor: ")
        actor = Actor(nombre_actor, apellido_actor)
        self.actores[(nombre_actor, apellido_actor)] = actor
        print(f"Actor {actor} agregado correctamente.")

    def mostrar_actores(self):
        print("Actores:")
        for actor in self.actores.values():
            print(actor)

    def crear_pelicula(self, callback=None):
        titulo_pelicula = input("Ingrese el título de la película: ")
        anno_pelicula = input("Ingrese el año de la película: ")
        pelicula = Pelicula(titulo_pelicula, anno_pelicula)
        director_pelicula = input("Ingrese el nombre del director de la película: ")
        apellido_director_pelicula = input("Ingrese el apellido del director de la película (opcional): ")

        if (director_pelicula, apellido_director_pelicula) in self.directores:
            pelicula.asignar_director(self.directores[(director_pelicula, apellido_director_pelicula)])
            print(f"Director {self.directores[(director_pelicula, apellido_director_pelicula)]} asignado correctamente a la película.")
        else:
            print("Error: Director no encontrado.")

        self.mostrar_actores()
        opcion_agregar_actor = input("¿Desea agregar un actor a la película? (s/n): ")

        while opcion_agregar_actor.lower() == "s":
            nombre_actor_pelicula = input("Ingrese el nombre del actor de la película: ")
            apellido_actor_pelicula = input("Ingrese el apellido del actor de la película: ")

            if (nombre_actor_pelicula, apellido_actor_pelicula) in self.actores:
                pelicula.agregar_actor(self.actores[(nombre_actor_pelicula, apellido_actor_pelicula)])
                print(f"Actor {self.actores[(nombre_actor_pelicula, apellido_actor_pelicula)]} agregado correctamente a la película.")
            else:
                print("Error: Actor no encontrado.")

            opcion_agregar_actor = input("¿Desea agregar otro actor a la película? (s/n): ")

        self.peliculas[titulo_pelicula] = pelicula
        pelicula.mostrar_info()

        # Llamando al callback si se proporciona
        if callback:
            callback()

    def mostrar_peliculas(self):
        print("Películas:")
        for pelicula in self.peliculas.values():
            print(pelicula)

# En el código principal, puedes definir una función de callback personalizada, por ejemplo:
def mi_callback():
    print("¡Película creada exitosamente! Hora de celebrar.")

# Crear una instancia de la clase Inicio
inicio_instancia = Inicio()

# Menú principal
while True:
    print("Bienvenido, ¿qué quieres hacer?")
    print("\n1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        inicio_instancia.registrar_usuario()
    elif opcion == "2":
        inicio_instancia.iniciar_sesion()
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
