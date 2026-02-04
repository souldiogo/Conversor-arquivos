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


