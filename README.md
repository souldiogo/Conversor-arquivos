# 🧠 Conversor de Arquivos Leve e Prático

Este projeto foi criado com um propósito simples e importante: oferecer uma ferramenta de conversão de arquivos que funcione bem em **notebooks lentos**, 
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

## 🚀 Como Instalar e Usar
1 - Já com o codigo no vscode, instale o `pyinstaller`:
    pip install pyinstaller
    
2 - Gere o arquivo .exe:
    pyinstaller --onefile --paths=. converter.py
    "Vai cria uma pasta chamada `dist/` dentro do projeto. Lá estará o arquivo .exe.
    
3 - Adicione o caminho comepleto do `dist/` ao PATH do sistema:
    1.Vá em Configurações Avançadas do Sistema
    2. Clique em Váriaveis de Ambiente
    3. Na seção Path, clique em Novo
    4. Adicione o caminho completo da pasta `dist/`, por exemplo:
        C:\Users\souldiogo\Downloads\minha_pasta\convert\dist
        
4 - Por fim, abra o terminal e digite:
    converter

### 1. Clone o repositório

```bash
git clone https://github.com/souldiogo/Conversor-arquivos.git
cd Conversor-arquivos


