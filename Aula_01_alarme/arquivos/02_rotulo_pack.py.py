import tkinter as tk 

# criar a janela
janela = tk.Tk()
janela.title("Rotulo")

# adicionar rotulo
rotulo = tk.Label(janela, text="Hello World!")
rotulo.pack()

# executa o loopprincipal
janela.mainloop()