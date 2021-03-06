import tkinter
from tkinter import*
from tkinter import messagebox
class forma(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("805x700")
        self.title("Nodos")
        self.config(bg="thistle")
        self.lb1=Label(self,text="Arboles Binarios", font="Times 17  underline",bg="thistle")
        self.lb1.place(x=50,y=10)
        self.lb2=Label(self,text="Ingrese un valor", bg="thistle", font="Times 13")
        self.lb2.place(x=50,y=90)
        self.c1=Entry(self, width=30)
        self.c1.place(x=210,y=90)
        self.b1=Button(self,text="Insertar", command=self.insertar, width=14)
        self.b1.place(x=450,y=30)
        self.b2=Button(self,text="Pre-ordenanar",command=self.mostrar_1, width=14)
        self.b2.place(x=450,y=60)
        self.b3=Button(self,text="Post-ordenanar",command=self.mostrar_3, width=14)
        self.b3.place(x=450,y=90)
        self.b4=Button(self,text="In-ordenanar",command=self.mostrar_2, width=14)
        self.b4.place(x=450,y=120)
        self.b5=Button(self,text="Mostrar datos", command=self.mostrar_datos, width=14)
        self.b5.place(x=600,y=30)
        self.raiz=None
        self.lb1=Label(self,bg="thistle")
        self.lb1.place(x=10,y=130)
        self.lb2=Label(self,bg="thistle")
        self.lb2.place(x=600,y=60)
        self.lb3=Label(self,bg="thistle")
        self.lb3.place(x=600,y=90)
        self.lb4=Label(self,bg="thistle")
        self.lb4.place(x=600,y=120)
        self.canvas=Canvas(width=780,height=500,background="white")
        self.canvas.place(x=10,y=170)
    def insertar(self):
        e=int(self.c1.get())
        if(self.raiz==None):
            self.raiz=nodo(e)
        else:
            p=self.raiz
            while True:
                if (p.ele>e):
                    if p.iz==None:
                        p.iz=nodo(e)
                        break
                    else:
                        p=p.iz
                else:
                    if p.der==None:
                        p.der=nodo(e)
                        break
                    else:
                        p=p.der
        self.c1.delete(0,END)
        self.dibujar(self.raiz,345,10,200,360,5)
    def mostrar_1(self):
        self.lb1.configure(text="Pre-order: "+self.preorder(self.raiz))
    def preorder(self,p):
        if p==None:
            return ""
        else:
            return str(p.ele)+", "+self.preorder(p.iz)+self.preorder(p.der)
    def mostrar_2(self):
        self.lb1.configure(text="In-order: "+self.inorder(self.raiz))
    def inorder(self,p):
        if p==None:
            return ""
        else:
            return  self.inorder(p.iz) + str(p.ele) + ", " + self.inorder(p.der)
    def mostrar_3(self):
        self.lb1.configure(text="Post-order: "+self.postorder(self.raiz))
    def postorder(self,p):
        if p==None:
            return ""
        else:
            return self.postorder(p.iz) + self.postorder(p.der) +str(p.ele) +", "
    def dibujar(self, p, x, y, d, ix, iy):
        if (p!=None):
            self.canvas.create_oval(x,y,x+30,y+30)
            self.canvas.create_text(x+14,y+15,text=p.ele)
            self.canvas.create_line(x+15,y+5,ix,iy)
            self.dibujar(p.iz,x-d+5,y+60,d*40//100,x+2,y+20)
            self.dibujar(p.der,x+d,y+60,d*40//100,x+20,y+20)
    def mostrar_datos(self):
        self.lb2.configure(text="Hojas      : "+str(self.hojas(self.raiz)))
        self.lb3.configure(text="Profundidad: "+str(self.profundidad(self.raiz)))
        self.lb4.configure(text="Nodos      : "+str(self.nodo(self.raiz)))
    def hojas(self,p):
        if(p==None):
            return 0
        elif p.iz==None and p.der==None:
            return 1
        else:
            return self.hojas(p.iz)+self.hojas(p.der)
    def profundidad(self,p):
        if(p==None):
            return 0
        else:
            temp1=self.profundidad(p.iz)
            temp2=self.profundidad(p.der)
            if(temp1>temp2):
                return temp1+1
            else:
                return temp2+1
    def nodo(self,p):
        if(p==None):
            return 0
        else:
            return self.nodo(p.iz)+self.nodo(p.der)+1 
class nodo:
    def __init__(self,ele,iz=None,der=None):
        self.ele=ele
        self.iz=iz   
        self.der=der   
app=forma()
app.mainloop()
#DOCUMENTACI??N INTERNA
#Programador:Sofia  Vel??squez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin:Desarrolla algoritmos computacionales creando soluciones en un lenguaje de programaci??n.
#Lenguaje: python
#Net Framewor: 4.5
#Recursos: visual studio
#Descripci??n:Es una estructura de datos jer??rquica donde cada elemento puede tener uno o m??s descendientes. Al primer elemento se le llama ra??z, ademas los elementos que no tienen descendientes se les llama hojas, los que no son ni ra??z ni hojas les podemos llamar ramas.
#Ultima modificaci??n 16/09/2021