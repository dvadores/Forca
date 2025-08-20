# Jogo da Forca Completo
import random

def jogo_da_forca():
    palavras = ["python", "programacao", "computador", "algoritmo", 
                "desenvolvimento", "faculdade", "tecnologia", "software"]
    
    palavra_secreta = random.choice(palavras)
    letras_acertadas = ['_'] * len(palavra_secreta)
    tentativas = 6
    letras_erradas = []
    
    print("=== JOGO DA FORCA ===")
    print("Adivinhe a palavra relacionada a tecnologia!")
    print(f"Dica: a palavra tem {len(palavra_secreta)} letras")
    
    while tentativas > 0 and '_' in letras_acertadas:
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Tentativas restantes: {tentativas}")
        if letras_erradas:
            print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        letra = input("Digite uma letra: ").lower()
        
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra!")
            continue
            
        if letra in letras_erradas or letra in letras_acertadas:
            print("Voce ja tentou esta letra!")
            continue
            
        if letra in palavra_secreta:
            for i, char in enumerate(palavra_secreta):
                if char == letra:
                    letras_acertadas[i] = letra
            print("Letra correta!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra errada!")
    
    if '_' not in letras_acertadas:
        print(f"\nParabens! Voce acertou a palavra: {palavra_secreta.upper()}")
        print("VOCE VENCEU!")
    else:
        print(f"\nGame Over! A palavra era: {palavra_secreta.upper()}")
        print("FIM DE JOGO")

# Executar o jogo
if __name__ == "__main__":
    jogo_da_forca()
