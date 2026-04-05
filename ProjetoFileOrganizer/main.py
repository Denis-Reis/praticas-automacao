import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title ="Selecione uma pasta")

lista_arquivos = os.listdir(caminho)

print(lista_arquivos)

locais = {
    "imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "planilhas": [".xlsx", ".csv"],
    "documentos": [".docx", ".txt", ".odt"],
    "pdfs": [".pdf"],
    "videos": [".mp4", ".avi", ".mkv"],
    "audios": [".mp3", ".wav"],
    "compactados": [".zip", ".rar", ".7z"],
    "instaladores": [".exe", ".msi"],
}

for arquivo in lista_arquivos:
    # 01. Arquivo.pdf
    nome, extencao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extencao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
               os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}",f"{caminho}/{pasta}/{arquivo}")  
