import tkinter as tk
import math


conta = ""
def adicionar_conta(symbol):
    global conta
    if symbol == 'log':
        conta += 'ath.log('
    if symbol == 'sqrt':
        conta += 'ath.sqrt'
    else:
        conta += str(symbol)
        text_result.delete(1.0,"end")
        text_result.insert(1.0, conta)
    

def testar_calc():
    global conta
    try:
        conta = str(eval(conta))
        text_result.delete(1.0,"end")    
        text_result.insert(1.0, conta)
    except:
        limpar()
        text_result.insert(1.0, "Syntax Error")
        pass

def apagar_ultimo():
    global conta
    conta = conta[:-1]
    text_result.delete(1.0,"end")
    text_result.insert(1.0, conta)

def limpar():
    global conta
    conta = ""
    text_result.delete(1.0, "end")

def calcular_seno():
    global conta
    try:
        result = round(math.sin(math.radians(float(conta))), 14)
        text_result.delete(1.0,"end")
        text_result.insert(1.0, str(result))
    except:
        limpar()
        text_result.insert(1.0, "Syntax Error")
        pass

def calcular_cosseno():
    global conta
    try:
        result = round(math.cos(math.radians(float(conta))), 14)
        text_result.delete(1.0,"end")
        text_result.insert(1.0, str(result))
    except:
        limpar()
        text_result.insert(1.0, "Syntax Error")
        pass

def calcular_tangente():
    global conta
    try:
        result = round(math.tan(math.radians(float(conta))), 14)
        text_result.delete(1.0,"end")
        text_result.insert(1.0, str(result))
    except:
        limpar()
        text_result.insert(1.0, "Syntax Error")
        pass

root = tk.Tk()
root.geometry("355x310")


text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=6)


btn_1 = tk.Button(root, text="1", command=lambda:adicionar_conta(1), width=5, font=("Arial", 14))
btn_1.grid(row=6, column=1)

btn_2 = tk.Button(root, text="2", command=lambda:adicionar_conta(2), width=5, font=("Arial", 14))
btn_2.grid(row=6, column=2)

btn_3 = tk.Button(root, text="3", command=lambda:adicionar_conta(3), width=5, font=("Arial", 14))
btn_3.grid(row=6, column=3)

btn_4 = tk.Button(root, text="4", command=lambda:adicionar_conta(4), width=5, font=("Arial", 14))
btn_4.grid(row=5, column=1)

btn_5 = tk.Button(root, text="5", command=lambda:adicionar_conta(5), width=5, font=("Arial", 14))
btn_5.grid(row=5, column=2)

btn_6 = tk.Button(root, text="6", command=lambda:adicionar_conta(6), width=5, font=("Arial", 14))
btn_6.grid(row=5, column=3)

btn_7 = tk.Button(root, text="7", command=lambda:adicionar_conta(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda:adicionar_conta(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda:adicionar_conta(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

btn_10 = tk.Button(root, text="0", command=lambda:adicionar_conta(0), width=5, font=("Arial", 14))
btn_10.grid(row=7, column=2)

#BUTOES OPERAÇÕES
btn_soma = tk.Button(root, text="+", command=lambda:adicionar_conta("+"),width=5, font=("Arial", 14))
btn_soma.grid(row=5, column=5)

btn_subt = tk.Button(root, text="-", command=lambda:adicionar_conta("-"),width=5, font=("Arial", 14))
btn_subt.grid(row=6, column=5)

btn_multi = tk.Button(root, text="*", command=lambda:adicionar_conta("*"),width=5, font=("Arial", 14))
btn_multi.grid(row=4, column=5)

btn_divis = tk.Button(root, text="/", command=lambda:adicionar_conta("/"),width=5, font=("Arial", 14))
btn_divis.grid(row=3, column=5)

#RAIZ QUADRADA
btn_sqrt = tk.Button(root, text="√", command=lambda:adicionar_conta('math.sqrt('), width=5, font=("Arial", 14))
btn_sqrt.grid(row=7, column=4)

#ELEVAR AO QUADRADRO
btn_quad = tk.Button(root, text="x^2", command=lambda:adicionar_conta('**2'), width=5, font=("Arial", 14))
btn_quad.grid(row=7, column=5)

#LOGARITMO
btn_log = tk.Button(root, text="log", command=lambda:adicionar_conta('math.log('), width=5, font=("Arial", 14))
btn_log.grid(row=6, column=4)

#COSSENO
btn_cos = tk.Button(root, text="cos", command=calcular_cosseno, width=5, font=("Arial", 14))
btn_cos.grid(row=3, column=4)

#SENO
btn_sin = tk.Button(root, text="sin", command=calcular_seno, width=5, font=("Arial", 14))
btn_sin.grid(row=4, column=4)

#TANGENTE
btn_tan = tk.Button(root, text="tan", command=calcular_tangente, width=5, font=("Arial", 14))
btn_tan.grid(row=5, column=4)

#BUTOES FUNCIONAIS
btn_virgula = tk.Button(root, text=".", command=lambda:adicionar_conta("."),width=5, font=("Arial", 14))
btn_virgula.grid(row=7, column=3)

btn_abir = tk.Button(root, text="(", command=lambda:adicionar_conta("("),width=5, font=("Arial", 14))
btn_abir.grid(row=3, column=1)

btn_fechar = tk.Button(root, text=")", command=lambda:adicionar_conta(")"),width=5, font=("Arial", 14))
btn_fechar.grid(row=3, column=2)

btn_igual = tk.Button(root, text="=", command=testar_calc,width=11, font=("Arial", 14), fg='white', bg='#1875C5')
btn_igual.grid(row=8, column=4, columnspan=2)

btn_limpar = tk.Button(root, text="C", command=limpar,width=5, font=("Arial", 14))
btn_limpar.grid(row=3, column=3)

btn_apagar = tk.Button(root, text="<<", command=apagar_ultimo, width=5, font=("Arial", 14))
btn_apagar.grid(row=7, column=1)

root.mainloop()