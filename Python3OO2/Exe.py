from modelo import Serie, Playlist
from modelo import Filme


serie = Serie('got', 2018, 8)
filme = Filme('vingadores - era de ultron ', 2015, 100)
tmep = Filme('todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 4 )

filme.dar_likes()
filme.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
serie.dar_likes()
serie.dar_likes()

print(f'Filme: {filme.nome} - {filme.duracao}   - Likes: {filme.likes}.')
print(f'Série: {serie.nome} - {serie.temporada} - Likes: {serie.likes}.')

filmes_e_series = [filme, serie, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'O tamanho da lista: {len(playlist_fim_de_semana)}.')

for programa in playlist_fim_de_semana:
    print(programa)

#perguntando se existe demolidor na lista
print(f'Existe a serie Demolidor na lista? {demolidor in playlist_fim_de_semana}.')