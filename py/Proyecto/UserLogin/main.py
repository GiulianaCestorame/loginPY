from tkinter import *
from tkinter import ttk as ttk
import tkinter as tk
import tkinter
from usuarios import usuario
from tkinter import messagebox as Messagebox 
from generico import genericos as  utl



root = Tk() #creamos ventana principal
usuarios = [] #lista de usuarios, deberia tener persistencia 
bloqueados = [] #lista de bloqueados , deberia tener persistencia 

passusuario = StringVar()
dniusuario = StringVar()
correousuario = StringVar()
telefonousuario = StringVar()
nombreusuario = StringVar()
apellidousuario=StringVar()

registroframe = Frame(root, bg="lightblue")



def hide_frame(frame):
    if frame:
        frame.pack_forget()
    else:
        print("El marco es None.")


def show_frame(frame):
    if frame:
        frame.pack(fill="both", expand=True)





def validate_password(new_value):
    if len(new_value) >= 6:
        return True
    else:
        Messagebox.showerror("Error", "La contraseña debe tener al menos 6 caracteres.")
        return False

        



def createGUI():
   # root = Tk() #creamos ventana principal
    root.title("Inicio de sesion")
    root.geometry('800x500')
    root.config(bg="lightblue")
    utl.centrar_ventana(root,800,500)


#PARA INICIO DE SESION
#CREO un nuevo frame para el logo
#label q va a tener la imagen 
 #   logo = utl.leer_imagen("./imagenes/OIP.jpg",(200,200))
    logo = utl.leer_imagen("./imagenes/OIP.jpg",(200,200))

        
    frame_logo = tk.Frame(root, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6') # frame  del logo
    frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        
 #aca posiciono la imagen en un label
    label = tk.Label(frame_logo, image=logo,bg='#3a7ff6')
    label.place(x=0,y=0,relwidth=1,relheight=1)

#frame para que quede mas lindo la parte del nombre inicio
    #frame form top
    frame_form_top = tk.Frame(root,height=50,bd=0, relief=tk.SOLID, bg='black')
    frame_form_top.pack(side="top",fill=tk.X)

    title = tk.Label(frame_form_top,text="Inicio de sesion",font=('Times',30), fg="black",bg='#fcfcfc', pady=50)
    title.pack(expand=tk.YES,fill=tk.BOTH)

#frame del formulario 
    mainframe = tk.Frame(root,height=50,bd=0, relief=tk.SOLID, bg='#fcfcfc')
    mainframe.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)

#textos o titulos
   

    dnilabel = Label(mainframe,text="DNI: ", font=('Times', 14),fg="#666a88",bg="#fcfcfc")
    dnilabel.pack(fill=tk.X,padx=20,pady=5)
  #con el pack se agregar a la interfaz
   #entradas de texto  
    dnientry = Entry(mainframe,textvariable=dniusuario)
    dnientry.pack(fill=tk.X,padx=20,pady=10) 


    passlabel = Label(mainframe,text="Contraseña: ", font=('Times', 14),fg="#666a88",bg="#fcfcfc")
    passlabel.pack(fill=tk.X,padx=20,pady=5)


    passentry = Entry(mainframe,textvariable=passusuario,show="*")
    passentry.pack(fill=tk.X,padx=20,pady=10)

#botones 
    iniciarSesionB = ttk.Button(mainframe,text="Iniciar Sesion",command=iniciarSesion)
    iniciarSesionB.pack(fill=tk.X,padx=20,pady=10)
 #con command digo q cuando apreten el boton se va a ejecutar esa funcion
    def ocultar():
        hide_frame(mainframe)
        hide_frame(frame_form_top)
        show_frame(registroframe)
    
    registrarseB = ttk.Button(mainframe,text="Crea una nueva cuenta",command=ocultar)
    registrarseB.pack(fill=tk.X,padx=20,pady=10)




#vuelve a inicio
    def volverr(frame):
      dni = dnirentry.get()
      passwd = contraseniaentry.get()
      correo = correoentry.get()
      nombre = nombreentry.get()
      apellido = apellidoentry.get()
      telefono = telefonoentry.get()
      usu = usuario(dni,passwd,correo,nombre,apellido,telefono)
      usuarios.append(usu)
      hide_frame(frame)
      show_frame(frame_form_top)
      show_frame(mainframe)



     

   #INTERFACE REGISTRO
    titulo = Label(registroframe,text="Registrarte",font=('Times',30),fg="black",bg="lightblue", pady=50)
    titulo.pack(expand=tk.NO,fill=tk.BOTH)
   
    def on_entry_click(event):
    #"""Función para manejar el evento clic en el Entry."""
       if contraseniaentry.get() == "123456":
          contraseniaentry.delete(0, END)
          contraseniaentry.config(show="*")  # Mostrar el contenido de la contraseña

    dnirentry = Entry(registroframe,fg="gray50")
    dnirentry.insert(0,"Dni")
    dnirentry.pack(fill=tk.X,padx=20,pady=10) 
    
    nombreentry = Entry(registroframe,textvariable=nombreusuario,fg="gray50")
    nombreentry.insert(0,"Nombre")
    nombreentry.pack(fill=tk.X,padx=20,pady=10) 

    apellidoentry = Entry(registroframe,textvariable=apellidousuario,fg="gray50")
    apellidoentry.insert(0,"Apellido")
    apellidoentry.pack(fill=tk.X,padx=20,pady=10) 

    correoentry = Entry(registroframe,textvariable=correousuario,fg="gray50")
    correoentry.insert(0,"Email")
    correoentry.pack(fill=tk.X,padx=20,pady=10) 

    
    contraseniaentry = Entry(registroframe, textvariable=passusuario, validate="key", validatecommand=(validate_password, "%P"))
    contraseniaentry.insert(0,"123456")
    contraseniaentry.bind("<Button-1>", on_entry_click)
    contraseniaentry.pack(fill=tk.X, padx=20, pady=10)

    telefonoentry = Entry(registroframe,fg="gray50")
    telefonoentry.insert(0,"221000000")
    telefonoentry.pack(fill=tk.X,padx=20,pady=10)

    volver = ttk.Button(registroframe, text="Volver a Inicio", command=lambda: volverr(registroframe))
    volver.pack(fill=tk.X, padx=20, pady=10)





    root.mainloop()


#problemas con los entrys ,arreglar







def iniciarSesion():
     #busco en la lista de usuarios si conicide el dni con alguno
     #si coincide me voy a fijar si la contraseña es valida
     encontre=False
     for user in usuarios:
         if user.dni== dniusuario.get():
            test = user.conectar(passusuario.get())
            encontre=True
            break
    #si existe el usuario veo la contraseña
     if encontre!=True:
        Messagebox.showerror("Error","Error, no existe usuario con ese dni.")
     else: 
        if test==3:
           Messagebox.showinfo("Conectado","Se inicio sesion con exito")
    # Por ahora, simplemente redireccionamos al frame de registro
           #hide_frame(mainframe)
         #  show_frame(register_frame)
        else:
            if test==2 or test == 1:
               Messagebox.showerror("Error","Contraseña incorrecta, vuelva a intentar")
            else:
                 if test == 0 or test < 0:
                    if(test==0):
                        bloqueados.append(user) #lo agrego a la lista de bloqueados que dsp deberia tener el administrador
                    Messagebox.showerror("Bloqueado","Contraseña incorrecta, su cuenta permanecera bloqueada")
        


#voy a usar el mismo file no se si esta bien

def registrarse():
     #creo usuario y lo agrego a la lista 
    
      hide_frame(root)
      show_frame(registroframe)


if __name__=="__main__":  
   # user1=usuario(input("ingrese el DNI: "),input("Ingrese la contraseña: "))
    user1=usuario("123","g","correog","giu","c","1234") #creo usuario para probar
    usuarios.append(user1)
    createGUI()  #funcion que crea la interface 

