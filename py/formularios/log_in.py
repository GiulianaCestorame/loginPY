import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import Proyecto.UserLogin.generico as utl
from formularios.form_maestro import MasterPanel

class App:
    def __init__(self) -> None:
        self.ventana = tk.Tk() #frame (su root)
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)


        logo = utl.leer_imagen("./imagenes/OIP.jpg",(200,200))


        frame_logo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6') #segundo frame  su main
        frame_logo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        
        #aca posiciono la imagen en un label
        label = tk.Label( frame_logo, image=logo,bg='#3a7ff6')
        label.place(x=0,y=0,relwidth=1,relheight=1)
      
      
      #frame form 
   
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right",expand=tk.YES,fill=tk.BOTH)

#frame form top
        frame_form_top = tk.Frame(frame_form,height=50,bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top",fill=tk.X)

        title = tk.Label(frame_form_top,text="Inicio de sesion",font=('Times',30), fg="black",bg='#fcfcfc', pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

#frame from fill
        frame_form_fill = tk.Frame(frame_form,height=50,bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)
  #casillas
        etiqueta_usuario = tk.Label(frame_form_fill, text="DNI", font=('Times', 14),fg="#666a88",bg="#fcfcfc")
        etiqueta_usuario.pack(fill=tk.X,padx=20,pady=5)
      
        self.usuario = ttk.Entry(frame_form_fill,font=('Times',14))
        self.usuario.pack(fill=tk.X,padx=20,pady=10)


        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg="#fcfcfc")
        etiqueta_password.pack(fill=tk.X,padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill,font=('Times',14))
        self.password.pack(fill=tk.X,padx=20,pady=10) 
        self.password.config(show="*")

        self.ventana.mainloop()





    