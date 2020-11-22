# Aula 16 (Tuplas)

times = ('Atlético-MG', 'Internacional', 'São Paulo', 'Palmeiras', 'Vasco', 'Flamengo', 'Fluminense',
         'Sport', 'Santos', 'Fortaleza', 'Athletico-PR', 'Ceará', 'Atlético-GO', 'Corinthians', 'Grêmio',
         'Bahia', 'Coritiba', 'Bragantino', 'Botafogo', 'Goiás')

print('Os 5 Primeiros: {}'.format(times[0:5]))
print('Os 4 Últimos: {}'.format(times[-4:]))
print('Em Ordem: {}'.format(sorted(times)))
print('Posição do Sport: {}'.format(times.index('Sport')+1))
