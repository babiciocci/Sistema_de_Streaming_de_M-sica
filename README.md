# Projeto 1: Sistema de Streaming de Música

Feito por: Bruno Arthur Basso Silva | Gabriela Molina Ciocci 
<br>
RA: 22.123.067-5 | 22.222.032-9 
<br>
Disciplina: CC5232 - Banco de Dados
<br>
Coordenador(a): Leonardo Anjoletto Ferreira
<br>
Ciclo: 5° Semestre. 
<br>
Curso: Ciência da Computação
<br>
Universidade: Centro Universitário FEI

======================================================================================================================================================

Certifique-se de criar o Banco de Dados e respectivas tabelas antes de utilizar o código.
<br>
O arquivo que contém as Queries de criação de tabelas no Banco de Dados chama-se "Queries SQL para Criação de Tabelas.txt".
<br>
O arquivo que contém as Queries para as 20 questões de Álgebra Relacional chama-se "Queries SQL para Álgebra Relacional.txt".

======================================================================================================================================================

CÓDIGO PARA CRIAÇÃO DE DADOS ALEATÓRIOS:

Para utilizar o código, é obrigatório que os arquivos de texto estejam na mesma pasta que o programa em Python, são eles:

   -> usuarios.txt
   <br>
   -> artistas.txt
   <br>
   -> musicas.txt
   <br>
   -> playlists.txt

Ao baixar todos os arquivos e colocá-los no mesmo local, então você poderá executar o código.
<br>
Para definir a quantidade de cada item que será gerado, você precisará descer até as últimas linhas do código onde estão localizadas as variáveis que armazenam o valor de cada item que será gerado.
<br>
Após definir os valores desejados, você poderá rodar o programa.
<br>
Neste momento, será mostrado um menu contendo todas as informações dos alunos envolvidos e da disciplina.
<br>
Ao apertar enter, o programa irá gerar dados aleatórios e criará um novo arquivo de texto contendo todos os itens gerados:

   -> codeSQL.txt

Você poderá fechar o programa após a criação do arquivo.
<br>
Neste arquivo contém as Queries para adição dos dados no banco de dados.
<br>
Para adicioná-las, basta abrir o arquivo "codeSQL.txt", copiar todo seu conteúdo e colar no terminal do SQL.

======================================================================================================================================================

MODELO ENTIDADE RELACIONAL (MER):

<img src="Modelo Entidade Relacional.jpg">

======================================================================================================================================================

MODELO RELACIONAL (3FN):

Com base nos atributos e relacionamentos, temos o seguinte modelo relacional:

Musica

    ID_Música (PK)
    Título
    Duração
    ID_Disco (FK)

Artista

    ID_Artista (PK)
    Nome
    Data_Nascimento

Disco

    ID_Disco (PK)
    Título
    Data_Lancamento
    ID_Artista (FK)

Usuário

    ID_Usuário (PK)
    Nome
    Email
    Data_Registro

Playlist

    ID_Playlist (PK)
    Título
    ID_Usuário (FK)

Playlist_Música

    ID_Playlist (FK)
    ID_Música (FK)

Artista_Música

    ID_Artista (FK)
    ID_Música (FK)

Observações sobre a normalização
<br>
1NF (Primeira Forma Normal): Todos os atributos devem ter valores atômicos, e as tabelas devem ter uma chave primária definida.
<br>
2NF (Segunda Forma Normal): Todos os atributos não-chave devem depender completamente da chave primária, não apenas de parte dela.
<br>
3NF (Terceira Forma Normal): Não deve haver dependências transitivas, ou seja, atributos não-chave devem depender apenas da chave primária e não de outros atributos não-chave.
<br>

```mermaid 
erDiagram

   ARTISTA{
      int ID_Artista PK
      string Nome
      date Data_Nascimento
   }
   DISCO{
        int ID_Disco PK
        string Titulo
        date Data_Lancamento
        int ID_Artista FK
   }
   USUARIO{
        int ID_Usuario PK
        string Nome
        string Email
        date Data_Registro
    }
   MUSICA{
        int ID_Musica PK
        string Titulo
        int Duracao
        int ID_Disco FK
    }
    PLAYLIST{
        int ID_Playlist PK
        string Titulo
        int ID_Usuario FK
    }
    PLAYLIST_MUSICA{
        int ID_Playlist FK
        int ID_Musica FK
    }
   ARTISTA_MUSICA{
        int ID_Artista FK
        int ID_Musica FK
    }

    MUSICA ||--o| DISCO: "pertence_a"
    DISCO ||--o| ARTISTA: "criado_por"
    PLAYLIST ||--o| USUARIO: "criada_por"
    PLAYLIST_MUSICA ||--|| PLAYLIST: "contém"
    PLAYLIST_MUSICA ||--|| MUSICA: "contém"
    ARTISTA_MUSICA ||--|| ARTISTA: "interpreta"
    ARTISTA_MUSICA ||--|| MUSICA: "é_interpretada_por"
```
