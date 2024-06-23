class usuario():
    numUsuario = 0
    def __init__(self,dni,passw,correo,nom,ape,telefono) :
        self.dni = dni
        self.contra = passw
        self.correo = correo         
        self.telefono = telefono
        self.nombre = nom 
        self.apellido = ape
        self.conectado = False
        self.intentos = 3


      #cada vez que se crea un usuario se incrementa en uno
        usuario.numUsuario+=1
    
    def conectar(self,contrasenia):
        myContra=contrasenia
        if myContra== self.contra:
            self.conectado=True
            self.intentos=3
        else:
           self.intentos-=1
           if self.intentos>0: #esto es para probar en la terminal
              print("contraseña incorrecta, intentelo de vuelta")
              print("cantidad de intentos restantes: " ,self.intentos)
        return self.intentos

     
    #cerrar sesion
    def desconectar(self):
        if self.conectado:
            print("se cerro sesion con exito")
            self.conectado=False
        else:
            print("Error , no inicio sesion")

   #imprimo el usuario
    def __str__(self) -> str:
        if self.conectado:
            conect="conectado"
        else:
            conect = "desconectado"
        return f"Mi DNI es {self.dni} y estoy {conect}"
 
# user1 = usuario(input("ingrese dni: "), input("ingrese su contraseña: "))
# print(user1)

# user1.conectar()
# print(user1)

# user1.desconectar()
# print(user1)