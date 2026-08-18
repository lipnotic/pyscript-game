# pyscript-game
Framework para criação de jogos e histórias com alternativas de enrredo guidas pelo jogador.
IT PYSCRIPT - JOGO DE AVENTURA / VISUAL NOVEL

ESTRUTURA
---------
index.html
jogo.py
assets/

IMAGEM POR CENA
---------------
Use no jogo.py:
    mostrar_imagem("assets/floresta.jpg")

ÁUDIO DE FUNDO
--------------
Use:
    tocar_audio("assets/trilha.mp3")

Para parar:
    parar_audio()

Observação: navegadores podem bloquear autoplay.
Nesse caso, o jogador pode clicar no controle de áudio.

VÍDEO
-----
Use:
    mostrar_video("assets/introducao.mp4")

Para esconder:
    esconder_video()

TESTE LOCAL
-----------
Execute nesta pasta:
    python -m http.server 8000

Depois abra:
    http://localhost:8000

MIDIAS SUGERIDAS
----------------
assets/inicio.jpg
assets/cena_a.jpg
assets/cena_b.jpg
assets/cena_c.jpg
assets/cena_d.jpg
assets/final_bom.jpg
assets/final_ruim.jpg
assets/trilha.mp3
assets/introducao.mp4

IMPORTANTE - WORKER + IMAGENS/VIDEO/AUDIO
----------------------------------------
Este kit usa um Web Worker para permitir input() sem travar a pagina.
Como o Python tambem altera elementos HTML (imagem, audio e video), o servidor
precisa habilitar Cross-Origin Isolation.

Por isso, para testar localmente, use:
    INICIAR_JOGO.bat

ou, manualmente:
    python servidor.py

Nao use mais:
    python -m http.server 8000

porque esse servidor simples nao envia os cabecalhos necessarios para o worker
acessar document/window.
