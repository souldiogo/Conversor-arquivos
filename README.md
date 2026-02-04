# 🧠 Conversor de Arquivos Leve e Prático

Este projeto foi criado com um propósito simples e importante: oferecer uma ferramenta de conversão de arquivos, 
especialmente útil para **professores** e usuários que não querem (ou não podem) instalar programas pesados.

O conversor é leve, direto ao ponto e roda via **linha de comando (CMD)**, usando a biblioteca `pyinstaller` para gerar um executável simples e portátil.

---

## 🔄 Tipos de Arquivos Suportados

O programa consegue converter entre os seguintes formatos:

### 🖼️ Imagens
- `JPEG`
- `PNG`
- `BMP`
- `GIF`

### 📄 Documentos
- `DOCX`
- `PDF`

### 📊 Planilhas
- `XLSX`
- `CSV`

---

## 📌Como instalar e usar se foi baixado o arquivo em winrar
1 - Extraia o arquivo  > Conversor-arquivos-main
2 - Abra à pasta ja extraida no vscode 
3 - Com o código aberto, abra o terminal e digite para instalar o pyinstaller:
        pip install pyinstaller

4 - Gerando o arquivo .exe:
        pyinstaller --onefile --paths=. converter.py
        "Criara uma pasta chamada `dist/` dentro do projeto esse é o arquivo .exe

5 - Adicione o caminho completo do `dist/` ao PATH do sistema:
        1. Entre nas configurações avançadas do sistema
        2. Na seção Path, clique em novo
        3. Adicione o caminho completo da pasta do `dist/`
                por exemplo: C:\Users\souldiogo\Dowlaods\minha_pasta\convert\dist

6 - Por fim, abra o terminal (cmd) e digite:
        converter
        

    
📝 Observação: Sempre que for converter um arquivo, informe o formato original dele. 
Por exemplo, se o arquivo se chama notas_do_ano.pdf, o sistema vai entender que ele é um PDF e vai convertê-lo para .docx automaticamente.

Se o seu arquivo estiver em um pendrive, o caminho pode variar dependendo da letra atribuída ao dispositivo. Aqui vão dois exemplos:
Quando o arquivo estiver diretamente no pendrive (sem estar em uma pasta):
    D:\Documento.docx
Quando o arquivo estiver dentro de uma pasta no pendrive:
    D:\MeusArquivos\PDFs\relatorio.pdf

### 1. Clone o repositório

```bash
git clone https://github.com/souldiogo/Conversor-arquivos.git
cd Conversor-arquivos


