import os
from pytube import YouTube

# Defina o caminho do arquivo que contém os links dos vídeos
file_path = "urls.txt"

# Crie a lista para armazenar os nomes dos vídeos que deram erro
videos_que_deram_erro = []

# Abra o arquivo em modo de leitura e escrita
with open(file_path, "r+") as file:
    # Leia todas as linhas do arquivo em uma lista
    urls = file.readlines()

    # Percorra cada link e faça o download do vídeo
    for url in urls:
        # Crie um objeto da classe YouTube
        yt = YouTube(url)

        try:
            # Selecione a maior resolução possível do vídeo MP4
            ys = yt.streams.get_highest_resolution()

            # Defina o caminho de saída do arquivo
            output_path = "./videos_baixados/"

            # Faça o download do vídeo
            ys.download(output_path)

            print(f"Download do vídeo '{yt.title}' completo!")
            # Se o download for bem-sucedido, remova a linha correspondente do arquivo
            urls.remove(url)
        except:
            # Se a exceção for lançada, adicione o nome do vídeo à lista de erros
            videos_que_deram_erro.append(url)
            print(f"Erro ao baixar o vídeo '{url.strip()}'")

    # Reescreva todo o conteúdo do arquivo com a lista atualizada de links
    file.seek(0)
    file.writelines(urls)
    file.truncate()

# Imprima os nomes dos vídeos que deram erro
if videos_que_deram_erro:
    print("Vídeos que deram erro:") 
    for video in videos_que_deram_erro:
        print(video)
