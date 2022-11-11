"""
@utor: Andres Bayona (24/05/2021)

La aplicacion realiza la conversion de pies a metros y adicionalmente suma el valor desde
la borde del tunel del coregamma hasta el centro de dicho tunel donde se ubica la fuente de Cesio.
Adicionalmente realiza el proceso inverso a la conversion inicial.
"""

from tkinter import *
from tkinter import messagebox as MessageBox

#--------------- Interfaz grafica ------------------
raiz = Tk()
raiz.title("Coregamma")
raiz.resizable(True, True)
raiz.iconbitmap("myAvatar.ico")
raiz.geometry("320x210")
raiz.config(bg="green")
my_frame = Frame()
#my_frame.pack(side="right", anchor="n")
my_frame.pack(fill="both", expand="True")
#my_frame.pack()
my_frame.config(bg="green")
my_frame.config(width="310", height="190")
#my_frame.config(bd=20)
my_frame.config(relief="groove")
my_frame.config(cursor="hand2")



#------------ Funcion para conversion de pies a metros -----------
def conversor_ft(event):
    try:
        feet = float(feet_txt.get())

        meters = feet * 0.3048
        meters_add = meters + 0.3683

        meters = round(meters, 2)
        meters_add = round(meters_add, 2)

        profundidad_meters_result.set(meters)
        profundidad_meters_result_adition.set(meters_add)

    except ValueError:
        if feet_txt.get() != "":
            MessageBox.showinfo("Dato Errado", "Ingrese un valor numerico!")
        
        profundidad_feet.set("")
        profundidad_meters_result.set("")
        profundidad_meters_result_adition.set("")


#------------ Funcion para conversion de metros a pies -----------
def conversor_me(event):
    try:
        me = float(me_txt.get())
        
        ft = me / 0.3048
        ft_add = ft - 0.3683

        ft = round(ft, 2)
        ft_add = round(ft_add, 2)

        profundidad_feet_result.set(ft)
        profundidad_feet_result_adition.set(ft_add)

    except ValueError:
        #profundidad_meters.set("")
        if me_txt.get() != "":
                MessageBox.showinfo("Dato Errado", "Ingrese un valor numerico!")
        
        profundidad_meters.set("")
        profundidad_feet_result.set("")
        profundidad_feet_result_adition.set("")


#------------ Funcion para limpiar celdas -----------
def limpiar():
    profundidad_feet.set("")
    profundidad_meters_result.set("")
    profundidad_meters_result_adition.set("")

    profundidad_meters.set("")
    profundidad_feet_result.set("")
    profundidad_feet_result_adition.set("")


#--------------- Variables ------------------
profundidad_feet = StringVar()
profundidad_meters_result = StringVar()
profundidad_meters_result_adition = StringVar()

profundidad_meters = StringVar()
profundidad_feet_result = StringVar()
profundidad_feet_result_adition = StringVar()

#profundidad_meters.set(0)

#--------------- Titulo del ft a m -----------
title_ft = Label(my_frame, text="Conversor de pies a metros!")
title_ft.grid(row=0, column=0, columnspan=4)
title_ft.config(bg="green", fg="white")

#--------------- Titulo del m a ft -----------
title_me = Label(my_frame, text="Conversor de metros a pies!")
title_me.grid(row=3, column=0, columnspan=4)
title_me.config(bg="green", fg="white")

#--------------- Label profundidad en pies ---------------
feet = Label(my_frame, text="Profundidad: ")
feet.grid(row=1, column=0, sticky="e", padx=5, pady=5)
feet.config(bg="lightgreen")

#--------------- Label profundidad en metros -------------
meters = Label(my_frame, text="Profundidad: ")
meters.grid(row=5, column=0, sticky="e", padx=5, pady=5)
meters.config(bg="#F2965B")

#------ Label unidades en pies y simbolo flechas -------------
ft = Label(my_frame, text="(ft)  >>")
ft.grid(row=1, column=2)
ft.config(bg="green", justify="left")

#------ Label unidades en metros --------
me = Label(my_frame, text="(m)")
me.grid(row=1, column=4)
me.config(bg="green", justify="left")

#-------- Label unidades en metros adicional ----------
me_adition = Label(my_frame, text="(m)")
me_adition.grid(row=2, column=4)
me_adition.config(bg="green", justify="left")

#-------- Label unidades en metros y simbolo flechas ---------
meters_in = Label(my_frame, text="(m)  >>")
meters_in.grid(row=5, column=2)
meters_in.config(bg="green", justify="left")

#--------- Label unidades en pies ------------
ft_result = Label(my_frame, text="(ft)")
ft_result.grid(row=5, column=4)
ft_result.config(bg="green", justify="left")

#--------- Label unidades en pies adicional ----------
ft_adition = Label(my_frame, text="(ft)")
ft_adition.grid(row=6, column=4)
ft_adition.config(bg="green", justify="left")


#------ Cuadro de texto para ingresar el valor de profundad en pies --------
feet_txt = Entry(my_frame, textvariable=profundidad_feet)
feet_txt.grid(row=1, column=1, pady=5)
feet_txt.config(bg="lightgreen", width="12", justify="right")
feet_txt.focus()

#------ Cuadro de texto para resultado de conversion de pies a metros ------
meters_result = Entry(my_frame, textvariable=profundidad_meters_result)
meters_result.grid(row=1, column=3, pady=5)
meters_result.config(bg="lightgreen", width="12", justify="right", state="disabled", disabledbackground="lightgreen")

#------- Cuadro de texto para resultado de conversion de pies a metros mas adicional ------------
meters_result_adition = Entry(my_frame, textvariable=profundidad_meters_result_adition)
meters_result_adition.grid(row=2, column=3, pady=5)
meters_result_adition.config(bg="#F2965B", width="12", justify="right", state="readonly", readonlybackground="#F2965B")

#-------- Cuadro de texto para ingresar el valor de profundad en metros -----------
me_txt = Entry(my_frame, textvariable=profundidad_meters)
me_txt.grid(row=5, column=1, pady=5)
me_txt.config(bg="#F2965B", width="12", justify="right")

#-------- Cuadro de texto para resultado de conversion de metros a pies -------------
feet_result = Entry(my_frame, textvariable=profundidad_feet_result)
feet_result.grid(row=5, column=3, pady=5)
feet_result.config(bg="lightgreen", width="12", justify="right")

#--------- Cuadro de texto para resultado de conversion de metros a pies mas adicional -----------
feet_result_adition = Entry(my_frame, textvariable=profundidad_feet_result_adition)
feet_result_adition.grid(row=6, column=3, pady=5)
feet_result_adition.config(bg="#F2965B", width="12", justify="right")


raiz.bind('<KeyPress>', conversor_ft)
raiz.bind('<KeyRelease>', conversor_me)


#---------- Boton Limpiar -----------
clear_button = Button(my_frame, text="Limpiar", command=limpiar) # Acuerdese de cambiar la funciona a limpiar
clear_button.grid(row=7, column=1, pady=5)
clear_button.config(width="9")

# calc_button = Button(my_frame, text="Calcular", command=conversor_ft) # Acuerdese de cambiar la funciona a limpiar
# calc_button.grid(row=7, column=3, pady=5)
# calc_button.config(width="9")

raiz.mainloop()



