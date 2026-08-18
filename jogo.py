# ============================================================
# JOGO DE AVENTURA / VISUAL NOVEL EM PYTHON + PYSCRIPT
# ============================================================

# ------------------------------------------------------------
# COMPATIBILIDADE DO input() COM PYSCRIPT
# NÃO ALTERE ESTA PARTE
# ------------------------------------------------------------
import asyncio
import builtins
import inspect

_input_original = builtins.input

def _input_compativel(prompt=""):
    resultado = _input_original(str(prompt))

    if inspect.isawaitable(resultado):
        return asyncio.run(resultado)

    return resultado

builtins.input = _input_compativel


# ------------------------------------------------------------
# ACESSO AO HTML
# NÃO ALTERE ESTA PARTE
# ------------------------------------------------------------
from pyscript import document


def definir_titulo(titulo, autor=""):

    document.querySelector(
        "#titulo-jogo"
    ).innerText = titulo

    if autor:

        document.querySelector(
            "#autor-jogo"
        ).innerText = f"Autor: {autor}"


def mostrar_imagem(caminho):

    img = document.querySelector(
        "#imagem-cena"
    )

    img.src = caminho
    img.style.display = "block"


def esconder_imagem():

    document.querySelector(
        "#imagem-cena"
    ).style.display = "none"


def tocar_audio(caminho):
    """
    Troca a trilha sonora.

    IMPORTANTE:
    Esta função apenas carrega o áudio.
    Não executa play() automaticamente.

    O áudio inicial é iniciado pelo botão
    INICIAR JOGO do index.html.
    """

    audio = document.querySelector(
        "#audio-fundo"
    )

    audio.src = caminho
    audio.load()


def parar_audio():

    audio = document.querySelector(
        "#audio-fundo"
    )

    audio.pause()
    audio.currentTime = 0


def mostrar_video(caminho):

    video = document.querySelector(
        "#video-intro"
    )

    video.src = caminho
    video.style.display = "block"
    video.load()


def esconder_video():

    video = document.querySelector(
        "#video-intro"
    )

    video.pause()
    video.style.display = "none"


# ------------------------------------------------------------
# CONFIGURAÇÃO DO JOGO
# ------------------------------------------------------------

definir_titulo(
    "ALVORECER DOS DEUSES",
    "Felipe Garbin"
)


# NÃO iniciar áudio aqui.
#
# O áudio inicial será iniciado
# pelo botão INICIAR JOGO do index.html.
#
# REMOVIDO:
#
# tocar_audio("assets/The Dawn of Aethelgard.mp3")


estado = {
    "vida": 3,
    "inventario": []
}


# ------------------------------------------------------------
# FUNÇÃO DE ESCOLHAS
# ------------------------------------------------------------

def escolher(mensagem, opcoes_validas):

    while True:

        resposta = input(
            mensagem
        ).strip().lower()

        if resposta in opcoes_validas:

            return resposta

        print(
            "⚠️ Opção inválida. Tente novamente."
        )


# ============================================================
# CENAS DO JOGO
# ============================================================

def cena_inicio():

    mostrar_imagem(
        "assets/inicio.png"
    )

    print(
        "\n" + "=" * 50
    )

    print(
        "ALVORECER DOS DEUSES"
    )

    print(
        "=" * 50
    )

    print(
        """
Escreva aqui a introdução da sua história.
O personagem precisa tomar sua primeira decisão.


1) Seguir pelo caminho A
2) Seguir pelo caminho B
"""
    )

    opcao = escolher(
        "Escolha: ",
        ["1", "2"]
    )


    if opcao == "1":  # Seguir pelo caminho A

        return "cena_a"


    return "cena_b"


def cena_a():

    mostrar_imagem(
        "assets/cena_a.png"
    )

    print(
        """
Você chegou à cena A.

Aqui você pode encontrar um item, perder vida,
conversar com um personagem ou descobrir uma pista.
"""
    )


    if "chave" not in estado["inventario"]:

        print(
            "Você encontrou uma chave."
        )

        estado[
            "inventario"
        ].append(
            "chave"
        )


    print(
        "\nInventário:",
        estado["inventario"]
    )


    print(
        """
1) Ir para a próxima cena
2) Voltar
"""
    )


    opcao = escolher(
        "Escolha: ",
        ["1", "2"]
    )


    if opcao == "1":  # Ir para próxima cena

        return "cena_c"


    return "inicio"


def cena_b():

    mostrar_imagem(
        "assets/cena_b.jpg"
    )

    print(
        """
Você escolheu o caminho B.

Crie aqui uma consequência diferente da cena A.

1) Continuar
2) Voltar
"""
    )


    opcao = escolher(
        "Escolha: ",
        ["1", "2"]
    )


    if opcao == "1":

        return "cena_d"


    return "inicio"


def cena_c():

    mostrar_imagem(
        "assets/cena_c.jpg"
    )

    print(
        "\nNesta cena você pode verificar o inventário."
    )


    if "chave" in estado["inventario"]:

        print(
            "A chave abre uma passagem secreta!"
        )

        return "final_bom"


    print(
        "Você não possui o item necessário."
    )


    return "final_ruim"


def cena_d():

    mostrar_imagem(
        "assets/cena_d.jpg"
    )

    print(
        """
Esta é outra parte da história.

1) Arriscar
2) Fugir
"""
    )


    opcao = escolher(
        "Escolha: ",
        ["1", "2"]
    )


    if opcao == "1":

        return "final_bom"


    return "final_ruim"


def final_bom():

    mostrar_imagem(
        "assets/final_bom.jpg"
    )


    print(
        """
================================
🏆 FINAL BOM
================================

Você conseguiu completar sua missão!
"""
    )


    return "fim"


def final_ruim():

    mostrar_imagem(
        "assets/final_ruim.jpg"
    )


    print(
        """
================================
💀 FINAL RUIM
================================

Algo deu errado...
"""
    )


    return "fim"


# ============================================================
# MAPA DE CENAS
# ============================================================

cenas = {

    "inicio": cena_inicio,

    "cena_a": cena_a,

    "cena_b": cena_b,

    "cena_c": cena_c,

    "cena_d": cena_d,

    "final_bom": final_bom,

    "final_ruim": final_ruim
}


# ============================================================
# MOTOR DO JOGO
# ============================================================

cena_atual = "inicio"


while cena_atual != "fim":

    cena_atual = cenas[
        cena_atual
    ]()


print(
    "\nObrigado por jogar! 🎮"
)