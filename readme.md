# Warzone

** Passos:

1. Um computador executará o arquivo server.py
2. Se os jogadores não estiverem no mesmo PC que o servidor, os jogadores terão que alterar o valor de self.host para o endereço IP do servidor. O endereço IP do servidor pode ser encontrado executando o comando 'ipconfig' em o prompt de comando do servidor.

Esta linha fornece o endereço IP

Endereço IPv4. . . . . . . . . . . : 192.168.0.1

Entre neste formato com as aspas, editando o arquivo network.py na LINHA 10
self.host = '192.168.0.1'

3. Jogadores executarão o arquivo game.py

NOTA: game e game2 são exatamente iguais. Você pode executar qualquer arquivo


Warzone é basicamente um jogo de Tiro Multijogador que pode ser jogado conectando 2 laptops via Socket Programming.
Este jogo tinha muitos recursos como:

O jogo (timer) não inicia até que todos participem.
Você pode pausar o jogo quando quiser.
Você pode enviar a mensagem a qualquer momento da tela do jogo para o seu oponente.
A mensagem será exibida na parte superior da tela por alguns segundos.
Você pode usar a barra de espaço para disparar.
Teclas de seta para mover para a direita/esquerda/pular.
Finalmente as pontuações serão mostradas.

