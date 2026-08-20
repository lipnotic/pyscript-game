# ============================================================
# FRAMEWORK PYSCRIPT GAME JAM - V2
# ============================================================
#
# Estrutura orientada a:
# - cenas;
# - estado;
# - botões;
# - imagens;
# - vídeos;
# - trilha sonora;
# - vida;
# - inventário;
# - pontuação;
# - múltiplos finais.
#
# O aluno altera principalmente:
# 1. CONFIG
# 2. SCENES
# 3. executar_acao()
#
# ============================================================

from pyscript import web, when, window


# ============================================================
# CONFIGURAÇÃO GERAL DO JOGO
# ============================================================

CONFIG = {
    "titulo": "ALVORECER DOS DEUSES",
    "subtitulo": "Uma aventura mitológica interativa",
    "autor": "Felipe Garbin",
    "icone": "⚔️",

    # OPCIONAL:
    # coloque None para não usar capa.
    "capa": None,
    # Exemplo:
    # "capa": "assets/imagens/capa.jpg",

    # Trilha iniciada pelo botão grande INICIAR JOGO.
    # Coloque None para não usar música inicial.
    "trilha_inicial": "assets/audios/The Dawn of Aethelgard.mp3",

    # Volume entre 0.0 e 1.0.
    "volume_inicial": 0.5,

    "vida_inicial": 3,
    "pontos_iniciais": 0,

    # Cena que aparece ao iniciar/reiniciar.
    "cena_inicial": "inicio",
}


# ============================================================
# ESTADO DO JOGADOR
# ============================================================

state = {
    "vida": CONFIG["vida_inicial"],
    "inventario": [],
    "pontos": CONFIG["pontos_iniciais"],
    "cena": CONFIG["cena_inicial"],
}


# ============================================================
# CENAS
# ============================================================
#
# CAMPOS SUPORTADOS:
#
# "title"  -> título da cena
# "text"   -> narrativa
# "image"  -> imagem opcional
# "video"  -> vídeo opcional
# "video_autoplay" -> True/False
# "audio"  -> áudio opcional para TROCAR a trilha
# "stop_audio" -> True para parar a trilha
# "options" -> até 4 opções:
#              ("Texto do botão", "acao")
#
# Se "audio" não existir, a música atual continua tocando.
# Se "video" existir, ele substitui a imagem naquela cena.
#
# ============================================================

SCENES = {

    "inicio": {
        "title": "O chamado",
        "image": "assets/imagens/inicio.png",
        "text": (
            "O céu se parte em luz enquanto antigos símbolos "
            "surgem nas pedras diante de você.\n\n"
            "Duas rotas conduzem ao templo."
        ),
        "options": [
            ("Seguir pela floresta", "floresta"),
            ("Entrar pelas ruínas", "ruinas"),
        ],
    },


    "floresta": {
        "title": "Floresta antiga",
        "image": "assets/imagens/floresta.jpg",
        "text": (
            "A floresta parece observar cada passo.\n\n"
            "Sob uma árvore você encontra uma pequena lanterna."
        ),
        "options": [
            ("Pegar a lanterna", "pegar_lanterna"),
            ("Ignorar e continuar", "portao"),
        ],
    },


    "ruinas": {
        "title": "Ruínas",
        "image": "assets/imagens/ruinas.jpg",
        "text": (
            "Entre colunas destruídas existe uma chave marcada "
            "com o símbolo dos deuses."
        ),
        "options": [
            ("Pegar a chave", "pegar_chave"),
            ("Seguir sem a chave", "portao"),
        ],
    },


    "portao": {
        "title": "O portão",
        "image": "assets/imagens/portao.jpg",
        "text": (
            "Um enorme portão bloqueia o caminho.\n\n"
            "Uma passagem escura também desce sob o templo."
        ),
        "options": [
            ("Tentar abrir o portão", "testar_portao"),
            ("Descer pela passagem", "testar_passagem"),
        ],
    },


    # Consequência explícita: evita que a mensagem seja
    # sobrescrita imediatamente por outra cena.
    "porta_falha": {
        "title": "O selo reage",
        "image": "assets/imagens/portao.jpg",
        "text": (
            "Sem a chave, o selo do portão libera uma descarga.\n\n"
            "Você perde uma vida."
        ),
        "options": [
            ("Recuperar-se e voltar", "portao"),
        ],
    },


    "passagem_falha": {
        "title": "Escuridão",
        "image": "assets/imagens/passagem.jpg",
        "text": (
            "Sem luz, você pisa em falso na passagem.\n\n"
            "Você perde uma vida."
        ),
        "options": [
            ("Levantar e voltar", "portao"),
        ],
    },


    "santuario": {
        "title": "Santuário",
        "image": "assets/imagens/santuario.jpg",

        # Exemplo de troca de música por cena:
        # "audio": "assets/audios/santuario.mp3",

        "text": (
            "Você chega ao santuário.\n\n"
            "No altar há um fragmento luminoso. "
            "Talvez seja importante para o final da jornada."
        ),
        "options": [
            ("Pegar o fragmento", "pegar_fragmento"),
            ("Deixá-lo e seguir", "oraculo"),
        ],
    },


    "oraculo": {
        "title": "A mensagem",
        "image": "assets/imagens/oraculo.jpg",

        # Exemplo de vídeo por cena:
        # "video": "assets/videos/oraculo.mp4",
        # "video_autoplay": False,

        "text": (
            "Uma voz ecoa pelo salão:\n\n"
            "\"Somente quem reuniu os sinais poderá escolher "
            "o destino deste mundo.\""
        ),
        "options": [
            ("Aceitar o poder dos deuses", "decidir_final"),
            ("Rejeitar o chamado", "fim_neutro"),
        ],
    },


    "fim_bom": {
        "title": "FINAL: ALVORECER",
        "image": "assets/imagens/final_bom.jpg",
        "text": (
            "A chave, a luz e o fragmento respondem ao mesmo tempo.\n\n"
            "Você compreende o verdadeiro propósito do templo "
            "e restaura o equilíbrio."
        ),
        "options": [],
    },


    "fim_alternativo": {
        "title": "FINAL: PODER INCOMPLETO",
        "image": "assets/imagens/final_alternativo.jpg",
        "text": (
            "Você aceita o poder, mas algo está faltando.\n\n"
            "O templo desperta sem revelar todos os seus segredos."
        ),
        "options": [],
    },


    "fim_neutro": {
        "title": "FINAL: O RETORNO",
        "image": "assets/imagens/final_neutro.jpg",
        "text": (
            "Você decide não interferir.\n\n"
            "Ao sair, o templo volta ao silêncio, "
            "como se estivesse esperando outro escolhido."
        ),
        "options": [],
    },


    "fim_ruim": {
        "title": "FINAL: QUEDA",
        "image": "assets/imagens/final_ruim.jpg",
        "stop_audio": True,
        "text": (
            "Suas forças chegam ao fim.\n\n"
            "As antigas portas se fecham e a jornada termina aqui."
        ),
        "options": [],
    },
}


# ============================================================
# ACESSO AOS ELEMENTOS DO HTML
# ============================================================

def el(id_elemento):
    return web.page[id_elemento]


# ============================================================
# CONFIGURAR IDENTIDADE VISUAL
# ============================================================

def configurar_identidade():

    titulo = CONFIG["titulo"]
    autor = CONFIG["autor"]
    subtitulo = CONFIG["subtitulo"]

    window.document.title = titulo

    el("titulo-jogo").innerText = titulo
    el("autor-jogo").innerText = f"Autor: {autor}"

    el("titulo-abertura").innerText = titulo
    el("subtitulo-abertura").innerText = subtitulo
    el("autor-abertura").innerText = f"Criado por {autor}"
    el("icone-abertura").innerText = CONFIG["icone"]

    capa = CONFIG.get("capa")

    if capa:
        el("capa-jogo").src = capa
        el("capa-jogo").style.display = "block"
        el("icone-abertura").style.display = "none"
    else:
        el("capa-jogo").style.display = "none"
        el("icone-abertura").style.display = "block"

    audio = el("audio-fundo")

    trilha = CONFIG.get("trilha_inicial")

    if trilha:
        audio.dataset.inicial = trilha
    else:
        audio.dataset.inicial = ""

    audio.dataset.volume = str(
        CONFIG.get("volume_inicial", 0.5)
    )


# ============================================================
# STATUS
# ============================================================

def atualizar_status():

    vida = state["vida"]

    if vida > 0:
        el("vida").innerText = " ".join(
            ["❤️"] * vida
        )
        el("vida").classList.remove("danger")
    else:
        el("vida").innerText = "💀"
        el("vida").classList.add("danger")

    if state["inventario"]:
        el("inventario").innerText = ", ".join(
            state["inventario"]
        )
    else:
        el("inventario").innerText = "Vazio"

    el("pontos").innerText = str(
        state["pontos"]
    )


# ============================================================
# MULTIMÍDIA
# ============================================================

def mostrar_imagem(caminho):

    window.frameworkVideo.stop()

    imagem = el("imagem-cena")

    if not caminho:
        imagem.style.display = "none"
        return

    imagem.src = caminho
    imagem.style.display = "block"


def mostrar_video(caminho, autoplay=False):

    if not caminho:
        window.frameworkVideo.stop()
        return

    window.frameworkVideo.play(
        caminho,
        autoplay
    )


def trocar_audio(caminho):

    if not caminho:
        return

    window.frameworkAudio.play(
        caminho,
        CONFIG.get("volume_inicial", 0.5),
        True
    )


def parar_audio():

    window.frameworkAudio.stop()


# ============================================================
# BOTÕES
# ============================================================

def configurar_botao(
    numero,
    texto="",
    ativo=False
):

    botao = el(f"opcao{numero}")

    botao.innerText = texto
    botao.disabled = not ativo

    if ativo:
        botao.style.display = "block"
    else:
        botao.style.display = "none"


def atualizar_botoes(opcoes):

    for i in range(1, 5):

        if i <= len(opcoes):

            configurar_botao(
                i,
                opcoes[i - 1][0],
                True
            )

        else:

            configurar_botao(
                i,
                "",
                False
            )


# ============================================================
# MOSTRAR CENA
# ============================================================

def mostrar_cena(nome):

    if nome not in SCENES:
        el("titulo-cena").innerText = "Erro de cena"
        el("texto-cena").innerText = (
            f"A cena '{nome}' não existe em SCENES."
        )
        atualizar_botoes([])
        return

    state["cena"] = nome

    cena = SCENES[nome]

    el("titulo-cena").innerText = (
        cena.get("title", nome)
    )

    el("texto-cena").innerText = (
        cena.get("text", "")
    )

    # --------------------------------------------------------
    # MÍDIA
    # --------------------------------------------------------

    video = cena.get("video")

    if video:
        mostrar_video(
            video,
            cena.get(
                "video_autoplay",
                False
            )
        )
    else:
        mostrar_imagem(
            cena.get("image")
        )

    # Áudio é opcional.
    # Ausência da chave "audio" mantém a trilha atual.
    if "audio" in cena:

        if cena["audio"]:
            trocar_audio(
                cena["audio"]
            )
        else:
            parar_audio()

    if cena.get("stop_audio"):
        parar_audio()

    # --------------------------------------------------------
    # BOTÕES E STATUS
    # --------------------------------------------------------

    atualizar_botoes(
        cena.get("options", [])
    )

    atualizar_status()


# ============================================================
# FUNÇÕES DE ESTADO
# ============================================================

def adicionar_item(
    item,
    pontos=0
):

    if item not in state["inventario"]:

        state["inventario"].append(
            item
        )

        state["pontos"] += pontos

    atualizar_status()


def remover_item(item):

    if item in state["inventario"]:

        state["inventario"].remove(
            item
        )

    atualizar_status()


def possui_item(item):

    return item in state["inventario"]


def perder_vida(
    quantidade=1,
    cena_sem_vida="fim_ruim"
):

    state["vida"] -= quantidade

    if state["vida"] <= 0:

        state["vida"] = 0

        atualizar_status()

        mostrar_cena(
            cena_sem_vida
        )

        return True

    atualizar_status()

    return False


def ganhar_pontos(quantidade):

    state["pontos"] += quantidade

    atualizar_status()


# ============================================================
# EXECUTAR AÇÃO
# ============================================================
#
# Regra simples:
# - se a ação tiver o mesmo nome de uma cena, abre a cena;
# - ações especiais são tratadas antes.
#
# Isso permite que a maioria das escolhas seja simples:
#
# ("Ir para a floresta", "floresta")
#
# ============================================================

def executar_acao(acao):

    # --------------------------------------------------------
    # PEGAR ITENS
    # --------------------------------------------------------

    if acao == "pegar_lanterna":

        adicionar_item(
            "lanterna",
            pontos=10
        )

        mostrar_cena(
            "portao"
        )


    elif acao == "pegar_chave":

        adicionar_item(
            "chave",
            pontos=10
        )

        mostrar_cena(
            "portao"
        )


    elif acao == "pegar_fragmento":

        adicionar_item(
            "fragmento",
            pontos=20
        )

        mostrar_cena(
            "oraculo"
        )


    # --------------------------------------------------------
    # TESTAR PORTÃO
    # --------------------------------------------------------

    elif acao == "testar_portao":

        if possui_item("chave"):

            ganhar_pontos(10)

            mostrar_cena(
                "santuario"
            )

        else:

            morreu = perder_vida()

            if not morreu:

                mostrar_cena(
                    "porta_falha"
                )


    # --------------------------------------------------------
    # TESTAR PASSAGEM
    # --------------------------------------------------------

    elif acao == "testar_passagem":

        if possui_item("lanterna"):

            ganhar_pontos(10)

            mostrar_cena(
                "santuario"
            )

        else:

            morreu = perder_vida()

            if not morreu:

                mostrar_cena(
                    "passagem_falha"
                )


    # --------------------------------------------------------
    # FINAL DEPENDENTE DO INVENTÁRIO
    # --------------------------------------------------------

    elif acao == "decidir_final":

        itens_necessarios = {
            "chave",
            "lanterna",
            "fragmento",
        }

        itens_jogador = set(
            state["inventario"]
        )

        if itens_necessarios.issubset(
            itens_jogador
        ):

            ganhar_pontos(50)

            mostrar_cena(
                "fim_bom"
            )

        else:

            mostrar_cena(
                "fim_alternativo"
            )


    # --------------------------------------------------------
    # AÇÃO NORMAL = NOME DE CENA
    # --------------------------------------------------------

    elif acao in SCENES:

        mostrar_cena(
            acao
        )


    # --------------------------------------------------------
    # AÇÃO INEXISTENTE
    # --------------------------------------------------------

    else:

        el("texto-cena").innerText = (
            f"A ação '{acao}' não foi cadastrada."
        )


# ============================================================
# ESCOLHER OPÇÃO
# ============================================================

def escolher_opcao(numero):

    cena = SCENES[
        state["cena"]
    ]

    opcoes = cena.get(
        "options",
        []
    )

    indice = numero - 1

    if indice < len(opcoes):

        acao = opcoes[
            indice
        ][1]

        executar_acao(
            acao
        )


# ============================================================
# EVENTOS DOS BOTÕES
# ============================================================

@when("click", "#opcao1")
def clicar_opcao1(event):
    escolher_opcao(1)


@when("click", "#opcao2")
def clicar_opcao2(event):
    escolher_opcao(2)


@when("click", "#opcao3")
def clicar_opcao3(event):
    escolher_opcao(3)


@when("click", "#opcao4")
def clicar_opcao4(event):
    escolher_opcao(4)


@when("click", "#reiniciar")
def reiniciar(event):

    state["vida"] = (
        CONFIG["vida_inicial"]
    )

    state["inventario"] = []

    state["pontos"] = (
        CONFIG["pontos_iniciais"]
    )

    state["cena"] = (
        CONFIG["cena_inicial"]
    )

    # Retoma a trilha inicial, se houver.
    trilha = CONFIG.get(
        "trilha_inicial"
    )

    if trilha:
        trocar_audio(trilha)

    mostrar_cena(
        CONFIG["cena_inicial"]
    )


# ============================================================
# INICIALIZAÇÃO
# ============================================================

configurar_identidade()

mostrar_cena(
    CONFIG["cena_inicial"]
)

# Somente agora libera o botão da tela inicial.
el("botao-iniciar").disabled = False
el("botao-iniciar").innerText = "▶ INICIAR JOGO"
