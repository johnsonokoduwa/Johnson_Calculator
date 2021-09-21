from tkinter import *
import math


expression = "" 

def press(num): 
        
        global expression 

        expression = expression + str(num) 

        equation.set(expression) 

def equalpress(): 
    
        try: 
        
                global expression 
        
                total = eval(expression)
        
                equation.set(total)
        
                expression = str(total)
                
        except:   
        
                equation.set(" Error ")
        
                expression = "" 
        
def clear(): 
    
        global expression
    
        expression = ""
    
        equation.set("")

        
def DEL(): 
    
        global expression
    
        expression = expression[:-1]
    
        equation.set(expression)
        

def sqrt(): 
    
        global expression 
    
        expression = math.sqrt(float(expression))
    
        equation.set(float(expression))
    
        expression = str(expression)

def ln(): 
    
        global expression 
    
        expression = math.log(float(expression))
    
        equation.set(float(expression))
    
        expression = str(expression) 

def log(): 
    
        global expression 
    
        expression = math.log(float(expression),10)
    
        equation.set(float(expression))
    
        expression = str(expression)
        
def square(): 
    
        global expression 
    
        expression = math.pow(float(expression),5)
    
        equation.set(float(expression))
    
        expression = str(expression)
        
def sine():
        
        global expression
        
        expression = math.sin(math.radians(float(expression)))
        
        equation.set(round(expression,10))
        
        expression = str(expression) 
        
def cosine():
        
        global expression
        
        expression = math.cos(math.radians(float(expression)))
        
        equation.set(round(expression,10))
        
        expression = str(expression)  
        
def tan():
        
        global expression
        
        expression = math.tan(math.radians(float(expression)))
        
        equation.set(round(expression,10))
        
        expression = str(expression)   
        
def sine_1():
        
        global expression
        
        expression = math.degrees(math.asin(float(expression)))
        
        equation.set(round(expression,10))
        
        expression = str(expression) 
        
def cosine_1():
        
        global expression
        
        expression = math.degrees(math.acos(float(expression)))
        
        equation.set(round(expression,10))
        
        expression = str(expression) 
        
def tan_1():
        
        global expression
        
        expression = math.degrees(math.atan(float(expression)))
        
        equation.set(round(expression,10))
        
        expression = str(expression) 

def Fjohnson():
    
        global expression
        
        A = textbox1.get()
        B = textbox2.get()
        C = textbox3.get()
        A = float(A)
        B = float(B)
        C = float(C)
        
        expression = float(((A*A)+(B*B)+(C*C)))
        
        equation.set(round(expression,10))
        
        expression = str(expression) 
        
        
if __name__ == "__main__": 
    
        gui = Tk() 
    
        gui.configure(background="grey") 

        gui.title("Johnson Okoduwa Imumbhon Calculator_Version_2") 
    
        gui.geometry("750x250") 

        equation = StringVar() 

        expression_field = Entry(gui, textvariable=equation) 
 
        expression_field.grid(columnspan=20, ipadx=310, sticky = W) 

        equation.set('Enter Your Mathematical Expression') 

        button1 = Button(gui, text=' 1 ', fg='black', bg='blue', command=lambda: press(1), height=1, width=7) 
        button1.grid(row=4, column=0) 
        
        button2 = Button(gui, text=' 2 ', fg='black', bg='blue', command=lambda: press(2), height=1, width=7) 
        button2.grid(row=4, column=1) 
        
        button3 = Button(gui, text=' 3 ', fg='black', bg='blue', command=lambda: press(3), height=1, width=7) 
        button3.grid(row=4, column=2) 
        
        button4 = Button(gui, text=' 4 ', fg='black', bg='blue', command=lambda: press(4), height=1, width=7) 
        button4.grid(row=3, column=0) 
        
        button5 = Button(gui, text=' 5 ', fg='black', bg='blue', command=lambda: press(5), height=1, width=7) 
        button5.grid(row=3, column=1) 
        
        button6 = Button(gui, text=' 6 ', fg='black', bg='blue', command=lambda: press(6), height=1, width=7) 
        button6.grid(row=3, column=2) 
        
        button7 = Button(gui, text=' 7 ', fg='black', bg='blue', command=lambda: press(7), height=1, width=7) 
        button7.grid(row=2, column=0) 
        
        button8 = Button(gui, text=' 8 ', fg='black', bg='blue', command=lambda: press(8), height=1, width=7) 
        button8.grid(row=2, column=1) 
        
        button9 = Button(gui, text=' 9 ', fg='black', bg='blue', command=lambda: press(9), height=1, width=7) 
        button9.grid(row=2, column=2) 
        
        button0 = Button(gui, text=' 0 ', fg='black', bg='blue', command=lambda: press(0), height=1, width=7) 
        button0.grid(row=5, column=1) 
        
        minus = Button(gui, text=' - ', fg='black', bg='purple', command=lambda: press("-"), height=1, width=7) 
        minus.grid(row=3, column=3) 
        
        plus = Button(gui, text=' + ', fg='black', bg='purple', command=lambda: press("+"), height=1, width=7) 
        plus.grid(row=2, column=3)
        
        multiply = Button(gui, text=' * ', fg='black', bg='purple', command=lambda: press("*"), height=1, width=7) 
        multiply.grid(row=4, column=3)
        
        divide = Button(gui, text=' / ', fg='black', bg='purple', command=lambda: press("/"), height=1, width=7) 
        divide.grid(row=5, column=3)
        
        dec = Button(gui, text=' . ', fg='black', bg='light blue', command=lambda: press("."), height=1, width=7) 
        dec.grid(row=5, column=0)
        
        equal = Button(gui, text=' = ', fg='black', bg='white', command=equalpress, height=1, width=7) 
        equal.grid(row=5, column=2)
        
        clear = Button(gui, text=' clear ', fg='black', bg='green', command=clear, height=1, width=7) 
        clear.grid(row=3, column=4)

        delete = Button(gui, text=' DeL ', fg='black', bg='green', command=DEL, height=1, width=7) 
        delete.grid(row=2, column=4)
        
        sqrt = Button(gui, text='√', fg='black', bg='green', command=sqrt, height=1, width=7) 
        sqrt.grid(row=4, column=4)
        
        sin = Button(gui, text=' Sine ', fg='black', bg='light yellow', command=sine, height=1, width=7) 
        sin.grid(row=2, column=5)
        
        cosin = Button(gui, text=' Cosine ', fg='black', bg='light yellow', command=cosine, height=1, width=7) 
        cosin.grid(row=3, column=5)
        
        tangent = Button(gui, text=' Tangent ', fg='black', bg='light yellow', command=tan, height=1, width=7) 
        tangent.grid(row=4, column=5)

        ln = Button(gui, text=' ln ', fg='black', bg='light yellow', command=ln, height=1, width=7) 
        ln.grid(row=5, column=5)
        
        isine = Button(gui, text='Sin-1 ', fg='black', bg='yellow', command=sine_1, height=1, width=7) 
        isine.grid(row=2, column=6)
        
        icos = Button(gui, text=' Cos-1 ', fg='black', bg='yellow', command=cosine_1, height=1, width=7) 
        icos.grid(row=3, column=6)
        
        itan = Button(gui, text=' Tan-1 ', fg='black', bg='yellow', command=tan_1, height=1, width=7) 
        itan.grid(row=4, column=6)

        log = Button(gui, text=' log', fg='black', bg='light yellow', command=log, height=1, width=7) 
        log.grid(row=5, column=6)
        
        textbox1 = Entry(gui,bg='dark sea green', width=7)
        textbox1.grid(row=7, column=1)

        Jt1 = Label (gui, text="A:", font=("Arial Bold", 10),bg="grey")
        Jt1.grid(row =7, column=0)

        textbox2 = Entry(gui, bg='silver', width=7)
        textbox2.grid(row=7, column=3)

        textbox3 = Entry(gui, bg='green', width=7)
        textbox3.grid(row=8, column=1)

        Jt2 = Label (gui, text="B:", font=("Arial Bold", 10),bg="grey")
        Jt2.grid(row =7, column=2)

        Jt3 = Label (gui, text="C:", font=("Arial Bold", 10),bg="grey")
        Jt3.grid(row =8, column=0)
        
        buttonCalc = Button(gui, text='SUM of (A^2+B^2+ C^2)', bg='orange', command=Fjohnson, height=1, width=35)
        buttonCalc.grid(row=7, column=4)

        buttonX = Button(gui, text=' X^5 ', fg='black', bg='blue', command=square, height=1, width=7) 
        buttonX.grid(row=5, column=4)

        space1 = Label (gui, text="", font=("Arial Bold", 10),width=12,bg="grey")
        space1.grid(row =6, column=5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
gui.mainloop() 
