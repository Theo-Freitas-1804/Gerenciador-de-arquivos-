import os

#Caminhos padrão do Android (ajustados para Pydroid 3 no Samsung)

caminhos_padrao = {
"Downloads": "/storage/emulated/0/Download",
"Imagens": "/storage/emulated/0/DCIM",
"Documentos": "/storage/emulated/0/Documents",
"Músicas": "/storage/emulated/0/Music",
"Vídeos": "/storage/emulated/0/Movies",
"WhatsApp": "/storage/emulated/0/WhatsApp/Media",
"Raiz": "/storage/emulated/0"
}

#Dicionário de extensões por categoria

extensoes = {
"imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
"documentos": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".odt"],
"áudio": [".mp3", ".wav", ".ogg", ".m4a", ".flac"],
"vídeo": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
"compactados": [".zip", ".rar", ".7z", ".tar"],
"executáveis": [".apk", ".exe", ".sh", ".py"],
"outros": []  # Caso não caia em nenhuma das categorias acima
}

#Pasta onde os logs do sistema serão armazenados

PASTA_LOGS = os.path.join(caminhos_padrao["Documentos"], "Logs_Gerenciador")

#Entrada de diretório usada para o menu ou input dinâmico

entrada_padrao = caminhos_padrao["Downloads"]