from ast import While
from multiprocessing.resource_sharer import stop
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from pynput.keyboard import Key, Controller
import time
import mouse
import random
root = Tk()
keyboard = Controller()
n = 30
no = random.randint(700,1000)
lo = random.randint(300,1000) 

root.title('PyPianist')
root.geometry("600x200")
root.maxsize(600,200)

p = 0.2
y = 0.2
def g():
    time.sleep(p)
    keyboard.press("g")
    time.sleep(y)
    keyboard.release("g")
def a():
    time.sleep(p)
    keyboard.press("h")
    time.sleep(y)
    keyboard.release("h")
    
def c():
    time.sleep(p)
    keyboard.press("a")
    time.sleep(y)
    keyboard.release("a")
    
def b():
    time.sleep(p)
    keyboard.press("j")
    time.sleep(y)
    keyboard.release("j")
def d():
    time.sleep(p)
    keyboard.press("s")
    time.sleep(y)
    keyboard.release("s")
    
def e():
    time.sleep(p)
    keyboard.press("d")
    time.sleep(y)
    keyboard.release("d")
    
def f():
    time.sleep(p)
    keyboard.press("f")
    time.sleep(y)
    keyboard.release("f")
    
def cl():
    time.sleep(p)
    keyboard.press("w")
    time.sleep(y)
    keyboard.release("w")
    
def dl():
    time.sleep(p)
    keyboard.press("e")
    time.sleep(y)
    keyboard.release("e")

def fl():
    time.sleep(p)
    keyboard.press("t")
    time.sleep(y)
    keyboard.release("t")
    
def gl():
    time.sleep(p)
    keyboard.press("y")
    time.sleep(y)
    keyboard.release("y")
    
def al():
    time.sleep(p)
    keyboard.press("u")
    time.sleep(y)
    keyboard.release("u")
    
def cll():
    time.sleep(p)
    keyboard.press("o")
    time.sleep(y)
    keyboard.release("o")
    
def dll():
    time.sleep(p)
    keyboard.press("p")
    time.sleep(y)
    keyboard.release("p")
    
def cp():
    time.sleep(p)
    keyboard.press("k")
    time.sleep(y)
    keyboard.release("k")  
    
def dp():
    time.sleep(p)
    keyboard.press("l")
    time.sleep(y)
    keyboard.release("l")  
    
def ep():
    time.sleep(p)
    keyboard.press(";")
    time.sleep(y)
    keyboard.release(";")  
    
    
def fp():
    time.sleep(p)
    keyboard.press("'")
    time.sleep(y)
    keyboard.release("'")  
def bruh():
    time.sleep(0.8)
    mouse.move(x = no, y = 250)
    mouse.click('left')
    p = 0.01
    g()
    a()
    g()
    cp()
    b()
    g()
    g()
    a()
    g()
    dp()
    cp()
    g()
    g()
    g()
    ep()
    cp()
    cp()
    b()
    a()
    fp()
    fp()
    ep()
    cp()
    dp()
    cp()
    
def National():
    time.sleep(p)
    mouse.move(x = no, y = 250)
    mouse.click('left')
    cl()
    dl()
    f()
    f()
    f()
    f()
    f()
    f()
    f()
    f()
    f()
    dl()
    f()
    fl()
    f()
    f()
    f()
    dl()
    dl()
    dl()
    c()
    dl()
    cl()
    cl()
    gl()
    gl()
    gl()
    gl()
    gl()
    gl()
    gl()
    gl()
    g()
    al()
    gl()
    fl()
    fl()
    fl()
    fl()
    fl()
    f()
    dl()
    fl()
    f()
    f()
    f()
    f()
    f()
    f()
    dl()
    gl()
    gl()
    gl()
    fl()
    fl()
    f()
    f()
    f()
    dl()
    dl()
    dl()
    dl()
    c()
    dl()
    cl()
    cl()
    dl()
    f()
    f()
    f()
    f()
    f()
    dl()
    f()
    fl()
    f()
    fl()
    gl()
    gl()
    gl()
    fl()
    f()
    dl()
    fl()
    f()
    f()
    f()
    dl()
    dl()
    dl()
    c()
    c()
    dl()
    cl()
    cl()
    dl()
    gl()
    gl()
    gl()
    gl()
    gl()
    gl()
    gl()
    gl()
    g()
    al()
    gl()
    fl()
    fl()
    fl()
    fl()
    fl()
    f()
    dl()
    fl()
    f()
    cll()
    cp()
    cll()
    cl()
    c()
    al()
    gl()
    al()
    cl()
    dl()
    f()
    f()
    f()
    f()
    dl()
    f()
    fl()  
def Song():
    time.sleep(1)
    mouse.move(x = no, y = 250)
    mouse.click('left')
    p = 0
    a()
    e()
    a()
    a()
    e()
    a()
    c()
    b()
    a()
    gl()
    a()
    e()
    a()
    a()
    e()
    a() 
    a()
    a()
    e()
    a()
    a()
    e()
    a()
    c()
    b()
    a()
    gl()
    a()
    e()
    a()
    a()
    e()
    a() 
    a()
    a()
    e()
    a()
    a()
    e()
    a()
    c()
    b()
    a()
    gl()
    a()
    e()
    a()
    a()
    e()
    a()
    a()
    a()
    e()
    a()
    a()
    e()
    a()
    c()
    b()
    a()
    gl()
    a()
    e()
    a()
    a()
    e()
    a() 
    a()
    a()
    e()
    a()
    a()
    e()
    a()
    c()
    b()
    a()
    gl()
    a()
    e()
    a()
    a()
    e()
    a() 
    a()
    a()
    e()
    a()
    a()
    e()
    a()
    c()
    b()
    a()
    gl()
    a()
    e()
    a()
    a()
    e()
    a() 
    a()
    a()
    e()
    a()
    a()
    ep()
    a()
    cp()
    b()
    a()
    gl()
    a()
    ep()
    a()
    a()
    ep()
    a() 
    a()
    a()
    ep()
    a()
    a()
    ep()
    a()
    cp()
    b()
    a()
    gl()
    a()
    ep()
    a()
    a()
    ep()
    a() 
    a()
    a()
    ep()
    a()
    a()
    e()
    a()
    cp()
    b()
    a()

B1 = Button(root, text = 'play happy birthday',command= bruh)
B1.pack()

B2 = Button(root, text = 'play national anthem(India)', command = National)
B2.pack()
B3 = Button(root, text = 'play a song', command = Song)
B3.pack()
root.mainloop()