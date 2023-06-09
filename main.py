import os
from pytube import YouTube

# Defina o caminho do arquivo que contém os links dos vídeos e músicas
file_path_mp4 = "urls_mp4.txt"
file_path_mp3 = "urls_mp3.txt"

# Crie a lista para armazenar os nomes dos vídeos e músicas que deram erro
videos_que_deram_erro = []
musicas_que_deram_erro = []

# Abra o arquivo em modo de leitura e escrita
with open(file_path_mp4, "r+") as file:
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

# Atualize os arquivos de URLs com a lista atualizada
with open(file_path_mp4, "w") as file:
    file.writelines(urls)

# Baixe as músicas em MP3
with open(file_path_mp3, "r") as file:
    urls = file.readlines()

    for url in urls:
        yt = YouTube(url)

        try:
            # Selecione o áudio em MP3 com a maior qualidade
            ys = yt.streams.filter(only_audio=True).first()

            # Defina o caminho de saída do arquivo
            output_path = "./musicas_baixadas/"

            # Faça o download da música
            ys.download(output_path)

            print(f"Download da música '{yt.title}' completo!")
            # Se o download for bem-sucedido, remova a linha correspondente do arquivo
            urls.remove(url)
        except:
            # Se a exceção for lançada, adicione o nome da música à lista de erros
            musicas_que_deram_erro.append(yt.title)
            print(f"Erro ao baixar a música '{yt.title}'")

# Atualize os arquivos de URLs com a lista atualizada
with open(file_path_mp3, "w") as file:
    file.writelines(urls)

# Imprima os nomes dos vídeos que deram erro
if videos_que_deram_erro:
    print("Vídeos que deram erro:") 
    for video in videos_que_deram_erro:
        print(video)

if musicas_que_deram_erro:
    print("Músicas que deram erro:") 
    for musica in musicas_que_deram_erro:
        print(musica)