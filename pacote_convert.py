import os
import pdf2docx
import logging
from PIL import Image
import pandas as pd
import warnings
import sys
import time

def limpar_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        print("\033[2J\033[H", end="")

# Ignorar apenas o ParserWarning
warnings.simplefilter("ignore", category=pd.errors.ParserWarning)

# Função mostra_erro
def mostrar_erro(msg):
    print("ERRO".center(68, "="))
    print(msg)
    time.sleep(6)

# Função para encontrar o caminho do arquivo informado
def encontrar_arquivo(nome_arquivo):
    # Se o usúario informar um caminho absoluto e o arquivo existir
    if os.path.isabs(nome_arquivo) and os.path.exists(nome_arquivo) and os.path.isfile(nome_arquivo):
        return nome_arquivo
    
    # Define o diretório base dependendo se está rodando como script ou executável
    if getattr(sys, 'frozen', False):
        base_dir = os.path.dirname(sys.executable)
    else:
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Diretórios padrão do sistema, porém, usa-se diretório completo se estiver no Documents(Documentos)
    documentos_pt = os.path.join(os.path.expanduser("~"), "Documentos")
    documents_en = os.path.join(os.path.expanduser("~"), "Documents")

    diretorios = [
        base_dir,
        os.getcwd(),
        os.path.expanduser("~/Downloads"),
        documentos_pt,
        documents_en
    ]
    
    # Adiciona o diretório do executável (Caso esteja rodando como um exe)
    if getattr(sys, '_MEIPASS', False):
        diretorios.insert(0, sys._MEIPASS)
        
    # Procura o arquivo nos diretórios listados
    for diretorio in diretorios:
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        if os.path.exists(caminho_arquivo):
            return caminho_arquivo
    return None

def detectar_separador(arquivo):
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            linha = f.readline()
    except UnicodeError:
        with open(arquivo, 'r', encoding="cp1252") as f:
            linha = f.readline()

        if linha.count(';') > linha.count(','):
            return ';'
        else:
            return ','
# Função para converter arquivos entre formatos suportados
def converter_arquivo(arquivo, formato):
    try:
        # Obtém a extensão do arquivo
        extensao = os.path.splitext(arquivo)[1].lower()
        # Formato maiúsculas, converte para minúsculas
        formato = formato.lower()
        # Converte imagens entre formatos suportados
        if extensao in [".jpeg", ".png", ".bmp", ".gif"]:
            imagem = Image.open(arquivo)
            nome = os.path.splitext(arquivo)[0]
            novo_arquivo = f"{nome}.{formato}"
            imagem = imagem.convert("RGB")
            imagem.save(novo_arquivo, format=formato.upper())
            return f"Imagem convertida com sucesso para {novo_arquivo}"

        # Converte arquivos Word para PDF
        elif extensao in [".docx"] and formato == "pdf":
            logging.getLogger("comtypes").setLevel(logging.CRITICAL)
            import comtypes.client
            word = comtypes.client.CreateObject('Word.Application')
            doc = word.Documents.Open(arquivo)
            novo_arquivo = f"{os.path.splitext(arquivo)[0]}.pdf"
            doc.SaveAs(novo_arquivo, FileFormat=17)  # 17 é o formato para PDF
            doc.Close()
            word.Quit()
            return f"Documento convertido com sucesso para {novo_arquivo}"

        # Converte arquivos PDF para Word
        elif extensao == ".pdf" and formato in ["docx", "doc"]:
            novo_arquivo = f"{os.path.splitext(arquivo)[0]}.docx"
            converter = pdf2docx.Converter(arquivo)
            converter.convert(novo_arquivo, start=0, end=None)
            converter.close()
            return f"PDF convertido com sucesso para {novo_arquivo}"

        # Converter arquivos Excel (.xlsx) para CSV
        elif extensao == ".xlsx" and formato == "csv":
            try:
                df = pd.read_excel(arquivo)
                novo_arquivo = f"{os.path.splitext(arquivo)[0]}.csv"
                df.to_csv(novo_arquivo, index=False)
                return f"Planilha Excel convertida com sucesso para {novo_arquivo}"
            except Exception as e:
                return f"Error ao converter .xlsx para .csv: {e}"

        # Converter arquivos CSV para excel (.xlsx)
        elif extensao == ".csv" and formato == "xlsx":
            try:
                sep = detectar_separador(arquivo)
                df = pd.read_csv(arquivo, encoding="cp1252", sep=sep)
                if df.empty:
                    return f"Error: O arquivo CSV está vazio ou mal formatado."
                novo_arquivo = f"{os.path.splitext(arquivo)[0]}.xlsx"
                df.to_excel(novo_arquivo, index=False, engine='openpyxl')
                return f"Arquivo CSV convertido com sucesso para {novo_arquivo}"
            except Exception as e:
                return f"Error ao converter .csv para .xlsx: {e}"

    except Exception as e:
        return f"Erro ao converter arquivo: {e}"
