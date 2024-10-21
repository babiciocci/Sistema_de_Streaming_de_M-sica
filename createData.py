# Projeto 1: Sistema de Streaming de Música
# Feito por: Gabriela Molina Ciocci 
#            Bruno Arthur Basso Silva
# RA:        22.222.032-9
#            22.123.067-5  
# Disciplina: CC5232 - Banco de Dados
# Coordenador(a): Leonardo Anjoletto Ferreira
# Ciclo: 5° Semestre. 
# Curso: Ciência da Computação
# Universidade: Centro Universitário FEI

# Para começar o projeto, primeiro precisamos importar todas as bibliotecas que iremos utilizar.

import random

# Utilizamos a biblioteca random para poder criar valores randômicos.

# Abrimos os arquivos onde contém os nomes para artistas, músicas e nomes de usuário.
# OBS: não esqueça de verificar se os arquivos estão na mesma pasta do programa!

archive_artists = open("artistas.txt", "r")
archive_artists_read = archive_artists.read()
archive_artists.close()

archive_musics = open("musicas.txt", "r")
archive_musics_read = archive_musics.read()
archive_musics.close()

archive_names = open("nomes.txt", "r")
archive_names_read = archive_names.read()
archive_names.close()

# Formatação dos arquivos para facilitar o processo de criação dos itens.

archive_artists_read = archive_artists_read.split("\n")
archive_musics_read = archive_musics_read.split("\n")
archive_names_read = archive_names_read.split("\n")

# Abrimos os arquivos onde contém os nomes personalizados para playlists.
# OBS: não esqueça de verificar se o arquivo está na mesma pasta do programa!

archive_playlist_names = open("playlist.txt", "r")
archive_playlist_names_read = archive_playlist_names.read()
archive_playlist_names.close()

# Formatação dos arquivos para facilitar o processo de criação dos itens.

archive_playlist_names_read = archive_playlist_names_read.split("\n")

# Criamos uma lista para variar os endereços de e-mail dos usuários.

emailTypes = ["@outlook.com", "@gmail.com", "@hotmail.com"]

# Lista que será responsável por armazenar os valores de ID existentes no programa.

existingID = []

# Lista que será responsável por armazenar os usuários, músicas, artistas e discos existentes no programa.

users = []
musics = []
artists = []
discs = []
playlists = []
playlist_music = []
artist_music = []

# Função responsável por criar as datas em dia, mês e ano.

def createDate(type):
    day = random.randint(1, 28)
    mounth = random.randint(1, 12)

    if day < 10:
        day = "0" + str(day)
    if mounth < 10:
        mounth = "0" + str(mounth)

    # Tipo 1: para datas de nascimento.
    if type == 1:
        year = random.randint(1950, 2010)
    
    # Tipo 2: para datas de registro ou lançamento.
    if type == 2:
        year = random.randint(2013, 2024)

    return day, mounth, year


# Aqui estão loaclizadas as funções necessárias para que o programa possa ser executado com êxito.
# createUser: Cria um usuário.
# Começamos gerando um ID de usuário aleatório. Utilizamos random para gerar um número aleatório de 0 até o comprimento do arquivo
# de usuários e fazemos a comparação com os ID's existentes para evitar IDs duplicados. Enquanto o valor do ID existir na lista de
# ID's existentes, o programa irá alterar o valor. No final, somamos 100 com o resultado apenas para padronização e identificação 
# de ID's de usuário.

def createUser(archive):
    user_id = random.randint(0, len(archive) - 1) + 100
    while user_id in existingID:
        user_id = random.randint(0, len(archive) - 1) + 100

    # Obtém o nome do usuário a partir do arquivo de nomes usando o user_id gerado.
    name = archive[user_id - 100]
    # Cria um email baseado no nome do usuário, substituindo espaços por underscores, convertendo para minúsculas e adicionando 
    # um domínio de email aleatório com base na lista de e-mails.
    email = name.replace(" ", "_").lower() + emailTypes[random.randint(0, len(emailTypes) - 1)]
    # Cria uma data de registro chamando a função createDate.
    register_date = createDate(2)

    # Adiciona o ID do usuário à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(user_id)
    # Adiciona os detalhes do usuário na lista de usuários.
    users.append([user_id, name, email, register_date])
    # Retorna o ID, nome, email e data de registro do usuário recém-criado. Não é necessário, mas foi colocado para manter 
    # formalidade no código.
    return user_id, name, email, register_date

# createArtist: Cria um artista.
# Iniciamos novamente a geração de um ID de artista aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor. 
# Não foi somado nenhum valor com o resultado pois a padronização e identificação de ID's de artistas será de valores menores que 100.

def createArtist(archive):
    artist_id = random.randint(0, len(archive) - 1)
    while artist_id in existingID:
        artist_id = random.randint(0, len(archive) - 1)

    # Obtém o nome do artista a partir do arquivo de artistas usando o artist_id gerado.
    name = archive[artist_id]
    # Cria uma data de nascimento chamando a função createDate.
    born_date = createDate(1)

    # Adiciona o ID do artista à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(artist_id)
    # Adiciona os detalhes do artista na lista de artistas. A lista vazia no final irá conter o id das músicas que pertencem ao
    # artista.
    artists.append([artist_id, name, born_date, []])
    # Retorna o ID, nome e data de nascimento do artista recém-criado. Não é necessário, mas foi colocado para manter formalidade 
    # no código.
    return artist_id, name, born_date

# createMusic: Cria uma música.
# Iniciamos novamente a geração de um ID de música aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para músicas são de valores maiores que 500.

def createMusic(archive):
    music_id = random.randint(0, len(archive) - 1) + 500
    while music_id in existingID:
        music_id = random.randint(0, len(archive) - 1) + 500
    
    # Obtém o título da música a partir do arquivo de músicas usando o music_id gerado.
    title = archive[music_id - 500]
    # Cria uma data de lançamento chamando a função createDate.
    release_date = createDate(2)
    # Cria o valor de duração da música.
    duration = random.randint(120, 360)

    # Adiciona o ID da música à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(music_id)
    # Adiciona os detalhes da música na lista de músicas.
    musics.append([music_id, title, release_date, duration])
    # Retorna o ID, título, data de lançamento e duração da música recém-criada.
    return music_id, title, release_date, duration

# createDisc: Cria um disco.
# Iniciamos novamente a geração de um ID de disco aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para discos são de valores maiores que 1000.

def createDisc(archive):
    disc_id = random.randint(0, len(archive) - 1) + 1000
    while disc_id in existingID:
        disc_id = random.randint(0, len(archive) - 1) + 1000

    # Obtém o título do disco a partir do arquivo de músicas usando o disc_id gerado.
    title = musics[random.randint(0, len(musics) - 1)][1]
    # Adiciona um artista para o álbum.
    artist_id = artists[random.randint(0, len(artists) - 1)][0]
    # Cria uma data de lançamento chamando a função createDate.
    release_date = createDate(2)

    # Adiciona o ID do disco à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(disc_id)
    # Adiciona os detalhes do disco na lista de discos.
    discs.append([disc_id, title, release_date, artist_id])
    # Retorna o ID, título, data de lançamento e artista do disco recém-criado.
    return disc_id, title, release_date, artist_id

# createPlaylist: Cria uma playlist.
# Iniciamos novamente a geração de um ID de playlist aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para playlists são de valores maiores que 2000 e menores que 2500.

def createPlaylist():
    playlist_id = random.randint(2000, 2500)
    while playlist_id in existingID:
        playlist_id = random.randint(2000, 2500)
    
    # Obtém o título da playlist a partir da lista archive_playlist_names_read.
    title = archive_playlist_names_read[random.randint(0, len(archive_playlist_names_read) - 1)]
    # Adiciona um dono para a playlist.
    user_id = users[random.randint(0, len(users) - 1)][0]

    # Adiciona o ID da playlist à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(playlist_id)
    # Adiciona os detalhes da playlist na lista de playlists. A lista vazia no final irá conter o id das músicas que pertencem a
    # playlist.
    playlists.append([playlist_id, title, user_id, []])
    # Retorna o ID, título e usuário da playlist recém-criada.
    return playlist_id, title, user_id

# createPlaylistMusic: Adiciona uma música em uma playlist.
# Iniciamos novamente a geração de um ID de música que contém na playlist aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para músicas em playlists são de valores maiores que 3000 e menores que 3500.

def createPlaylistMusic():
    playlistMusic_id = random.randint(3000, 3500)
    while playlistMusic_id in existingID:
        playlistMusic_id = random.randint(2000, 2500)

    # Obtemos uma playlist existente para adicionar uma música.
    playlist = playlists[random.randint(0, len(playlists) - 1)]
    # Obtemos o id dessa playlist.
    playlist_id = playlist[0]
    # Obtemos o id de uma música já existente.
    music_id = musics[random.randint(0, len(musics) - 1)][0]

    # Verificamos se a música na qual queremos adicionar já contém nessa playlist, se sim, o programa gera novamente um ID de
    # música até que encontre uma música que não contém nessa playlist.
    while music_id in playlist[3]:
        music_id = musics[random.randint(0, len(musics) - 1)][0]
    
    # Adiciona o id da música na playlist.
    playlist[3].append(music_id)
    
    # Adiciona o ID da música da playlist à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(playlistMusic_id)
    # Adiciona os detalhes da música da playlist na lista de músicas da playlists.
    playlist_music.append([playlistMusic_id, playlist_id, music_id])
    # Retorna o ID da playlist e o ID do usuário da música adicionada na playlist.
    return playlist_id, music_id

# createArtistMusic: Adiciona um artista como autor de uma música.
# Iniciamos novamente a geração de um ID de artista para a música aleatório e repetimos o processo anterior. 
# Enquanto o ID gerado já existir na lista de IDs existentes, o programa continuará a gerar um novo valor.
# O ID padronizado para músicas em playlists são de valores maiores que 4000 e menores que 4500.

def createArtistMusic():
    artistMusic_id = random.randint(4000, 4500)
    while artistMusic_id in existingID:
        artistMusic_id = artistMusic_id = random.randint(2000, 2500)

    # Obtemos um artista existente para adicionar uma música.
    artist = artists[random.randint(0, len(artists) - 1)]
    # Obtemos o id do artista.
    artist_id = artist[0]
    # Obtemos o id de uma música já existente.
    music_id = musics[random.randint(0, len(musics) - 1)][0]

    # Verificamos se a música na qual queremos adicionar o artista já pertence a esse artista, se sim, o programa gera novamente 
    # um ID de música até que encontre uma música que o artista não faça participação.
    while music_id in artist[3]:
        music_id = musics[random.randint(0, len(musics) - 1)][0]

    # Adiciona o id da música nas músicas do artista.
    artist[3].append(music_id)

    # Adiciona o ID da música do artista à lista de ID's existentes para evitar duplicatas no futuro.
    existingID.append(artistMusic_id)
    # Adiciona os detalhes da música do artista na lista de músicas do artista.
    artist_music.append([artistMusic_id, artist_id, music_id])
    # Retorna o ID do artista e o ID da música.
    return artist_id, music_id

# Função responsável por mostrar no terminal todos os itens gerados pelo programa.

def printAllItems():
    for i in users:
        print("Usuário:     ", i)
    print()
    for i in artists:
        print("Artista:     ", i)
    print()
    for i in musics:
        print("Música:      ", i)
    print()
    for i in discs:
        print("Disco:       ", i)
    print()
    for i in playlists:
        print("Playlist:    ", i)
    print()

# Função responsável por gerar o arquivo txt que contém os códigos SQL para adicionar todos os itens no banco de dados.
# O nome do arquivo gerado será "codeSQL.txt" e será encontrado na mesma pasta em que o programa está localizado.

def createExportCode(users, artists, musics, discs, playlists, playlist_music, artist_music):
    code_archive = open("codeSQL.txt", "w")
    code_archive.write("DELETE FROM artista_musica;\n")
    code_archive.write("DELETE FROM playlist_musica;\n")
    code_archive.write("DELETE FROM disco;\n")
    code_archive.write("DELETE FROM artista;\n")
    code_archive.write("DELETE FROM playlist;\n")
    code_archive.write("DELETE FROM usuario;\n")
    code_archive.write("DELETE FROM musica;\n")


    for i in users:
        code_archive.write("INSERT INTO usuario (id, nome, email, data_registro) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + i[2] + "', '" + str(i[3][2]) + "-" + str(i[3][1]) + "-" + str(i[3][0]) + "');\n")
    
    for i in artists:
        code_archive.write("INSERT INTO artista (id, nome, data_nascimento) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2][2]) + "-" + str(i[2][1]) + "-" + str(i[2][0]) + "');\n")

    for i in musics:
        code_archive.write("INSERT INTO musica (id, titulo, duracao) VALUES (" + str(i[0]) + ", '" + i[1] + "', " + str(i[3]) + ");\n")

    for i in discs:
        code_archive.write("INSERT INTO disco (id, titulo, data_lancamento, artista_id) VALUES (" + str(i[0]) + ", '" + i[1] + "', '" + str(i[2][2]) + "-" + str(i[2][1]) + "-" + str(i[2][0]) + "', " + str(i[3]) + ");\n")

    for i in playlists:
        code_archive.write("INSERT INTO playlist (id, titulo, usuario_id) VALUES (" + str(i[0]) + ", '" + i[1] + "', " + str(i[2]) + ");\n")

    for i in playlist_music:
        code_archive.write("INSERT INTO playlist_musica (id, playlist_id, musica_id) VALUES (" + str(i[0]) + ", " + str(i[1]) + ", " + str(i[2]) + ");\n")

    for i in artist_music:
        code_archive.write("INSERT INTO artista_musica (id, artista_id, musica_id) VALUES (" + str(i[0]) + ", " + str(i[1]) + ", " + str(i[2]) + ");\n")

    code_archive.close()
    print("---> Dados gerados com sucesso!")
    print("---> Nome do arquivo: codeSQL.txt")


# Menu para o terminal. Apenas para fins estéticos do código, não altera a lógica do programa.

def menu():
    print("|=================================================|")
    print("|         Sistema de Streaming de Música          |")
    print("|=================================================|")
    print()
    print("|=====================[INFOS]=====================|")
    print("| Ciclo: 5° semestre                              |")
    print("| Curso: Ciência da Computação - FEI              |")
    print("| Disciplina: CC5232 - Banco de Dados             |")
    print("| Data: 22/10/2024                                |")
    print("|=================================================|")
    print()
    print("|================[DESENVOLVEDORES]================|")
    print("| Nomes: Gabriela Molina Ciocci                   |")
    print("|        Bruno Arthur Basso Silva                 |")
    print("| RA:    22.222.032-9                             |")
    print("|        22.123.067-5                             |")
    print("|=================================================|")
    print()
    print("|=================================================|")
    print("|            Aperte enter para iniciar!           |")
    print("|=================================================|")

# Função principal do programa.
# Aqui é onde toda a lógica é criada. 

def main():
    for _ in range(0, num_users):
        createUser(archive_names_read)
    for _ in range(0, num_artists):
        createArtist(archive_artists_read)
    for _ in range(0, num_musics):
        createMusic(archive_musics_read)
    for _ in range(0, num_discs):
        createDisc(musics)
    for _ in range(0, num_playlists):
        createPlaylist()
    for _ in range(0, num_playlistMusics):
        createPlaylistMusic()
    for _ in range(0, num_artistMusics):
        createArtistMusic()

    createExportCode(users, artists, musics, discs, playlists, playlist_music, artist_music)


# Função de início do programa
def start():

    menu()
    input()
    main()

    print("Obrigado por utilizar!")
    print()

# Variáveis responsáveis por informar a quantidade de cada item o usuário gostaria de criar.
num_users = 10
num_artists = 20
num_musics = 90
num_discs = 5
num_playlists = 10
num_playlistMusics = 50
num_artistMusics = 10

start()