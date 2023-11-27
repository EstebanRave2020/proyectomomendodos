class Pelicula:
    directores = {}
    actores = {}

    def _init_(self, titulo, anno):
        self.titulo = titulo
        self.anno = anno
        self.director = None
        self.actores = []

    def asignar_director(self, nombre_director, apellido_director):
        if (nombre_director, apellido_director) in self.directores:
            self.director = self.directores[(nombre_director, apellido_director)]
            print(f"Director {self.director} asignado correctamente a la película.")
        else:
            print("Error: Director no encontrado.")

    def agregar_actor(self, nombre_actor, apellido_actor):
        if (nombre_actor, apellido_actor) in self.actores:
            print("Error: Este actor ya está en la película.")
        elif (nombre_actor, apellido_actor) in actor.actores:
            actor = actor.actores[(nombre_actor, apellido_actor)]
            self.actores.append(actor)
            print(f"Actor {actor} agregado correctamente a la película.")
        else:
            print("Error: Actor no encontrado.")

    def mostrar_info(self):
        print(f"\nInformación de la película:")
        print(f"Título: {self.titulo}")
        print(f"Año: {self.anno}")
        print(f"Director: {self.director}")
        print("Actores:")
        for actor in self.actores:
            print(actor)
