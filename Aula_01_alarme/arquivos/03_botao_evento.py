import tkinter as tk

# funcao da acao do botao
def exibir_mensagem():
    print("Hello World!")
    
# criar uma janela
janela = tk.Tk()
janela.title("Botão Simples")

# add botao
botao = tk.Button(janela, text="Clique aqui", command=exibir_mensagem)
botao.pack()

# exibir loop principal
janela.mainloop()