import json

list_instancias = []

class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero
    
    def __str__(self) -> str:
        return f"{self.nombre}"
    
        
with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        try:
            datos = json.loads(linea)
            list_instancias.append(Usuario(
                datos.get("nombre"),
                datos.get("apellido"),
                datos.get("email"),
                datos.get("genero"),
            ))
            linea = usuarios.readline()
        except Exception as e:
            linea = usuarios.readline()
            with open("error.txt","a") as error:
                error.write(f"La linea {linea} arrojó el error: {str(e)}\n")
                
    print(list_instancias)
        