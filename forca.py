import tkinter as tk
from tkinter import messagebox
import random

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Lista de palavras
        self.palavras = ["python", "programacao", "computador", "algoritmo", 
                         "desenvolvimento", "faculdade", "tecnologia", "software"]

        # Inicializar jogo
        self.novo_jogo()

        # Widgets
        self.label_titulo = tk.Label(root, text="🎮 JOGO DA FORCA 🎮", font=("Arial", 18, "bold"))
        self.label_titulo.pack(pady=10)

        self.label_dica = tk.Label(root, text=f"Dica: a palavra tem {len(self.palavra_secreta)} letras", font=("Arial", 12))
        self.label_dica.pack()

        self.label_palavra = tk.Label(root, text=" ".join(self.letras_acertadas), font=("Arial", 20, "bold"))
        self.label_palavra.pack(pady=20)

        self.label_tentativas = tk.Label(root, text=f"Tentativas restantes: {self.tentativas}", font=("Arial", 12))
        self.label_tentativas.pack()

        self.label_erradas = tk.Label(root, text="Letras erradas: ", font=("Arial", 12), fg="red")
        self.label_erradas.pack(pady=10)

        self.entry_letra = tk.Entry(root, font=("Arial", 14), width=5, justify="center")
        self.entry_letra.pack()

        self.botao_tentar = tk.Button(root, text="Tentar", command=self.verificar_letra, font=("Arial", 12), bg="lightblue")
        self.botao_tentar.pack(pady=10)

        self.botao_novo = tk.Button(root, text="Novo Jogo", command=self.resetar, font=("Arial", 12), bg="lightgreen")
        self.botao_novo.pack(pady=5)

    def novo_jogo(self):
        self.palavra_secreta = random.choice(self.palavras)
        self.letras_acertadas = ["_"] * len(self.palavra_secreta)
        self.tentativas = 6
        self.letras_erradas = []

    def verificar_letra(self):
        letra = self.entry_letra.get().lower()
        self.entry_letra.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Atenção", "Digite apenas UMA letra válida!")
            return

        if letra in self.letras_erradas or letra in self.letras_acertadas:
            messagebox.showinfo("Aviso", "Você já tentou essa letra!")
            return

        if letra in self.palavra_secreta:
            for i, char in enumerate(self.palavra_secreta):
                if char == letra:
                    self.letras_acertadas[i] = letra
            self.label_palavra.config(text=" ".join(self.letras_acertadas))
        else:
            self.letras_erradas.append(letra)
            self.tentativas -= 1

        # Atualizar labels
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.label_erradas.config(text=f"Letras erradas: {', '.join(self.letras_erradas)}")

        # Verificar vitória ou derrota
        if "_" not in self.letras_acertadas:
            messagebox.showinfo("Parabéns!", f"Você venceu! A palavra era: {self.palavra_secreta.upper()}")
            self.resetar()
        elif self.tentativas == 0:
            messagebox.showerror("Game Over", f"Você perdeu! A palavra era: {self.palavra_secreta.upper()}")
            self.resetar()

    def resetar(self):
        self.novo_jogo()
        self.label_dica.config(text=f"Dica: a palavra tem {len(self.palavra_secreta)} letras")
        self.label_palavra.config(text=" ".join(self.letras_acertadas))
        self.label_tentativas.config(text=f"Tentativas restantes: {self.tentativas}")
        self.label_erradas.config(text="Letras erradas: ")

# Executar
if __name__ == "__main__":
    root = tk.Tk()
    JogoDaForca(root)
    root.mainloop()
