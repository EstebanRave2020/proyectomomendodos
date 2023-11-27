class Actor:
    actores = {}

    def _init_(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def _str_(self):
        return f"{self.nombre} {self.apellido}"

    def agregar_actor(self, nombre_actor, apellido_actor):
        actor = Actor(nombre_actor, apellido_actor)
        self.actores[(nombre_actor, apellido_actor)] = actor
        print(f"Actor {actor} agregado correctamente.")

    def mostrar_actores(self):
        print("Actores:")
        for actor in self.actores.values():
            print(actor)
