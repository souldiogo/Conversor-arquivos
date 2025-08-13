from pacote_convert import converter_arquivo, encontrar_arquivo
from pacote_convert import limpar_terminal
import winsound
import os
import time

# Tocar o som no final da conversão
def tocar_som_conclusao():
    winsound.Beep(1000, 300)
    
# Exibir os formatos suportados
if __name__ == "__main__":
    colunas = [
        ["Imagens", "Documentos Word", "PDF"],
        ["jpeg",           "docx",     "pdf"],
        ["png",             "",           ""],
        ["bmp",             "",           ""],
        ["gif",             "",           ""],
        ["",                "",           ""]
    ]

    def exibir_cabecalho():
        print("\n" + "Super Conversor".center(41, "="))
        print("   Formatos suportados para conversão\n")
        for linha in colunas:
            print("   {:<10} {:<18} {:<10}".format(*linha))
        print("\nDigite 'sair' a qualquer momento para encerrar.\n")

    def banner(texto, largura_total=89):
        if len(texto) >= largura_total:
            largura_total = len(texto) + 4
        linha = texto.center(largura_total, "=")
        base = "=" * largura_total
        return linha, base

    while True:
        limpar_terminal()
        exibir_cabecalho()
        # Loop principal do programa
        arquivo = input("Nome do arquivo: ")
        if not arquivo:
            print("Por favor, digite o nome do arquivo.\n")
            continue
        if arquivo.strip().lower() == "sair":
            print("Programa encerrado.") 
            break

        caminho = encontrar_arquivo(arquivo)
        if not caminho:
            print("=" * 70)
            print("Arquivo não encontrado! Verifique se o nome do arquivo está correto.")
            print("=" * 70 + "\n")
            time.sleep(6)
            continue

        # Define o formato automaticamente para conversão
        extensao = os.path.splitext(caminho)[1].lower()
        if extensao in [".doc", ".docx"]:
            formato = "pdf"
            print(f"Convertendo para PDF. Aguarde...\n")
        elif extensao == ".pdf":
            formato = "docx"
            print(f"Convertendo para documento. Aguarde!...\n")
        elif extensao in [".jpg", ".jpeg", ".png", ".bmp", ".gif"]:
            formato = input("Para qual formato deseja converter: ")
            if formato == "sair":
                print("Programa encerrado.")
                break
        else:
            print("Formato não suportado para conversão.")
            continue
    
        #Realiza a conversão do arquivo
        resultado = converter_arquivo(caminho, formato)
        if resultado.startswith("Erro"):
            print("ERRO".center(41, "="))
            time.sleep(5)
        else:
            tocar_som_conclusao()
            print("CONCLUÍDO".center(41, "="))
            time.sleep(6)

