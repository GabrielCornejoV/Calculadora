from tkinter import *

root = Tk()
root.configure(background='#333333')
root.title('Calculadora')
root.geometry('236x168')

equation = StringVar()

def press(num):
    equation.set(equation.get() + str(num))
    print(equation.get())

def equalpress(*args):
    try:
        total = str(eval(equation.get()))
        equation.set(total)
    except:
        equation.set('error')

def clear(*args):
    equation.set('')

expression_entry = Entry(root, textvariable=equation)
expression_entry.grid(row=0, column=0, columnspan=4, sticky='nswe') # columnspan Indica que usará 4 columnas #sticky utilizará todo el ancho y alto que nuestro Entry tenga disponible

btn7 = Button(root, padx=15, pady=2, text=' 7 ', fg='#fff',background='#666' , command=lambda: press(7))
btn7.grid(row=1, column=0, sticky='nswe')

btn8 = Button(root, padx=15, pady=2,text=' 8 ', fg='#fff',background='#666' ,command=lambda: press(8))
btn8.grid(row=1, column=1, sticky='nswe')

btn9 = Button(root, text=' 9 ', fg='#fff',background='#666' ,command=lambda: press(9))
btn9.grid(row=1, column=2, sticky='nswe')

btn4 = Button(root, text=' 4 ', fg='#fff',background='#666' ,command=lambda: press(4))
btn4.grid(row=2, column=0, sticky='nswe')

btn5 = Button(root, text=' 5 ', fg='#fff',background='#666' ,command=lambda: press(5))
btn5.grid(row=2, column=1, sticky='nswe')

btn6 = Button(root, text=' 6 ', fg='#fff',background='#666' ,command=lambda: press(6))
btn6.grid(row=2, column=2, sticky='nswe')

btn1 = Button(root, text=' 1 ', fg='#fff',background='#666' ,command=lambda: press(1))
btn1.grid(row=3, column=0, sticky='nswe')

btn2 = Button(root, text=' 2 ', fg='#fff',background='#666' ,command=lambda: press(2))
btn2.grid(row=3, column=1, sticky='nswe')

btn3 = Button(root, text=' 3 ', fg='#fff',background='#666' ,command=lambda: press(3))
btn3.grid(row=3, column=2, sticky='nswe')

btn0 = Button(root, text=' 0 ', fg='#fff',background='#666' ,command=lambda: press(0))
btn0.grid(row=4, column=0, sticky='nswe', columnspan=2)

btndecimal = Button(root,  text=' . ', fg='#fff',background='#666' ,command=lambda: press('.'))
btndecimal.grid(row=4, column=2, sticky='nswe')

suma = Button(root,padx=15, pady=2, text=' + ', fg='#fff', bg='#fe9727' ,command=lambda: press('+'))
suma.grid(row=1, column=3, sticky='nswe')

resta = Button(root, text=' - ', fg='#fff', bg='#fe9727' ,command=lambda: press('-'))
resta.grid(row=2, column=3, sticky='nswe')

multiplicacion = Button(root, text=' * ', fg='#fff', bg='#fe9727' ,command=lambda: press('*'))
multiplicacion.grid(row=3, column=3, sticky='nswe')

division = Button(root, text=' / ', fg='#fff', bg='#fe9727' ,command=lambda: press('/'))
division.grid(row=4, column=3, sticky='nswe')

igual = Button(root, text=' = ', fg='#fff', bg='#fe9727', command=equalpress)   
igual.grid(row=5, column=3, sticky='nswe')

limpiar = Button(root, text=' Limpiar ', fg='#fff', bg='#999', command=clear)
limpiar.grid(row=5, column=2, sticky='nswe')

root.bind('<Return>', equalpress)
root.bind('<Delete>', clear)
expression_entry.focus()
root.mainloop()