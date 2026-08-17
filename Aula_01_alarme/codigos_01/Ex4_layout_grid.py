import tkinter as tk

def exibir_mensagem():
    print("O botão foi clicado!")

janela = tk.Tk()

janela.title("posicionamento com Grid")

rotulo = tk.Label(janela, text="Olá, Tkinter!")

rotulo.grid(row=0, column=0, padx=10, pady=10) 

botao = tk.Button(janela, text="Clique aqui", command=exibir_mensagem)
botao.grid(row=1, column=0, padx=10, pady=10)


janela.mainloop()

