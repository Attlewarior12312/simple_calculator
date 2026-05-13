import tkinter as tk


def kliknij(znak):
    
    ekran.insert(tk.END, znak)

def wyczysc():
    
    ekran.delete(0, tk.END)

def oblicz():
    try:
        
        dzialanie = ekran.get()
        
        
        wynik = str(eval(dzialanie))
        
       
        wyczysc()
        ekran.insert(0, wynik)
        
    
    except ZeroDivisionError:
        wyczysc()
        ekran.insert(0, "Nie dziel przez 0!")
    except Exception:
        wyczysc()
        ekran.insert(0, "Błąd")



okno = tk.Tk()
okno.title("Mój Kalkulator")
okno.geometry("300x400")

ekran = tk.Entry(okno, font=("Arial", 20), justify="right")
ekran.grid(row=0, column=0, columnspan=4)


button_1 = tk.Button(okno, text="1", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("1"))
button_2 = tk.Button(okno, text="2", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("2"))
button_3 = tk.Button(okno, text="3", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("3"))
button_4 = tk.Button(okno, text="4", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("4"))
button_5 = tk.Button(okno, text="5", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("5"))
button_6 = tk.Button(okno, text="6", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("6"))
button_7 = tk.Button(okno, text="7", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("7"))
button_8 = tk.Button(okno, text="8", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("8"))
button_9 = tk.Button(okno, text="9", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("9"))
button_0 = tk.Button(okno, text="0", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("0"))

button_plus = tk.Button(okno, text="+", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("+"))
button_minus = tk.Button(okno, text="-", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("-"))
button_multi = tk.Button(okno, text="*", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("*"))
button_divide = tk.Button(okno, text="/", font=("Arial", 14), width=5, height=2, command=lambda: kliknij("/"))


button_clear = tk.Button(okno, text="C", font=("Arial", 14), width=5, height=2, command=wyczysc)
button_equals = tk.Button(okno, text="=", font=("Arial", 14), width=5, height=2, command=oblicz)


button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multi.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_minus.grid(row=3, column=3)

button_clear.grid(row=4, column=0)
button_0.grid(row=4, column=1)
button_equals.grid(row=4, column=2)
button_plus.grid(row=4, column=3)

okno.mainloop()
