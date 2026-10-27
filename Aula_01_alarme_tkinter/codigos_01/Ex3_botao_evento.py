import tkinter as tk

def exibir_mensagem():
    print("Hello World!")

janela = tk.Tk()

janela.title("Botão simples")

botao = tk.Button(janela, text="Clique aqui", command=exibir_mensagem)

botao.pack()

janela.mainloop()

