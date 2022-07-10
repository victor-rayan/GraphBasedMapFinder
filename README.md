**Grafos2_MapFinder.** 

Temas:
 - Grafos2

# MapFinder

**Trabalho**: Grafos 2<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 18/0024868  |  Mateus Moreira Lima |
| 19/0044390  |  Victor Rayan Adriano Ferreira  |

## Sobre 
Nosso trabalho utiliza o algoritmo de dijikstra para traçar o menor caminho sobre o mapa da cidade de Las Venturas do jogo Grand Theft Auto San Andreas, ele tem como objetivo mostrar as localizações das ferraduras do jogo, que são colecionáveis, e estabelecer um ponto de menor caminho entre a origem e o destino, que são as ferraduras.

O mapa utiliza duas formas de traçar os objetivos, uma por carro outra por jetpack, com carro ele respeita as regras da via, com jetpack ele tenta traçar o caminho com a menor distância sem considerar as vias.

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

Tela do menu inicial:
![Tela menu inicial](./assets/menuInicial.png)

Mapa do jogo.

![Mapa do jogo](./assets/mapaJogo.png)

Tela com objetivos traçados utilizando o carro:

![Mapa com carro](./assets/mapaJogoCarro.png)

Tela com objetivos traçados utilizando jetpack:

![Mapa com jetpack](./assets/mapaJogoJetpack.png)


## Instalação 
**Linguagem**: Python<br>
**Biblioteca**: Pygame<br>

Para rodar a aplicação é necessário ter instalado em sua máquina o python 3 e o pygame.

### Rode o comando a seguir para baixar o pygame:
```
$ pip install pygame
```
ou
```
$ pip3 install pygame
```

### Para rodar a aplicação certifique se estar dentro da pasta Mapfinder:

Para entrar dentro da pasta Mapfinder

```
$ cd Mapfinder
```

### Rodar a aplicação:
```
$ python controler.py
```
ou
```
$ python3 controler.py
```


## Uso 
Selecione o botão com o método desejado para traçar a rota, Carro ou Jetpack, utilize o botão esquerdo do mouse para selecionar a sua posição de origem, e o botão direito como destino. Para retornar ao menu pressione a tecla C.

!! Caso esteja de carro utilize as vias como origem do destino. !!

!! O seu destino deve sempre ser uma ferradura espalhada pelo mapa. !!



