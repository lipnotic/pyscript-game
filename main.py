# ============================================================
# ALVORECER DOS DEUSES
# Aplicação da história ao Framework PyScript Game Jam V2
# ============================================================

from pyscript import web, when, window


# ============================================================
# CONFIGURAÇÃO GERAL
# ============================================================

CONFIG = {
    "titulo": "ALVORECER DOS DEUSES",
    "subtitulo": "Uma aventura mitológica de escolhas e múltiplos finais",
    "autor": "Felipe Garbin",
    "icone": "☀️",
    "capa": "assets/imagens/N01_silencio_antes_da_luz.svg",
    "trilha_inicial": "assets/audios/The Dawn of Aethelgard.mp3",
    "volume_inicial": 0.5,
    "vida_inicial": 3,
    "pontos_iniciais": 0,
    "cena_inicial": "N01",
}


# ============================================================
# ESTADO DO JOGO
# ============================================================

state = {
    "vida": CONFIG["vida_inicial"],
    "inventario": [],
    "pontos": CONFIG["pontos_iniciais"],
    "cena": CONFIG["cena_inicial"],

    # Variáveis narrativas sugeridas pela história
    "fe_pura": 0,
    "alianca_com_nyth": False,
    "memoria_da_mae": True,
}


# ============================================================
# CENAS / NÓS NARRATIVOS
# ============================================================

SCENES = {

    "N01": {
        "title": "N01 — O Silêncio Antes da Luz",
        "image": "assets/imagens/N01_silencio_antes_da_luz.svg",
        "text": (
            "O mundo ainda dorme sob um céu sem sol. Há mil anos, os deuses se calaram, "
            "e a humanidade aprendeu a viver na penumbra eterna. Você é Yara, guardiã de "
            "um templo em ruínas, a última que ainda escuta os sussurros das pedras antigas.\n\n"
            "Nesta noite, as pedras sussurram algo novo: um nome. Solvarah. O deus do "
            "alvorecer, que os antigos diziam ter sido aprisionado, não morto.\n\n"
            "Um mapa se forma na poeira do altar, revelando três caminhos possíveis para "
            "libertá-lo — ou impedi-lo."
        ),
        "options": [
            ("Seguir pela Trilha das Cinzas", "N02"),
            ("Descer às Catacumbas Afogadas", "N03"),
            ("Queimar o mapa e ignorar o chamado", "N04"),
        ],
    },

    "N02": {
        "title": "N02 — A Trilha das Cinzas",
        "image": "assets/imagens/N02_trilha_das_cinzas.svg",
        "text": (
            "Os hereges vivem em cavernas aquecidas por fogueiras rituais. Seu líder, o "
            "velho Kessian, reconhece Yara pelo colar que ela usa — um símbolo que ele jura "
            "ter visto no pescoço de sua própria mãe, morta há trinta anos.\n\n"
            "Kessian oferece um trato: ele revela como libertar Solvarah, mas exige que Yara "
            "carregue consigo uma relíquia amaldiçoada, capaz de aprisionar qualquer deus — "
            "inclusive o que ela vier a libertar."
        ),
        "options": [
            ("Aceitar a Corrente do Silêncio", "aceitar_corrente"),
            ("Recusar e confiar apenas na fé", "fe_pura"),
        ],
    },

    "N03": {
        "title": "N03 — As Catacumbas Afogadas",
        "image": "assets/imagens/N03_catacumbas_afogadas.svg",
        "text": (
            "A água sobe até os joelhos. Nas paredes, murais mostram os deuses sendo "
            "arrastados por correntes de luz negra — não mortos, mas presos por outra coisa. "
            "No centro da câmara, um espelho d'água reflete não o teto, mas um céu estrelado "
            "que não existe mais.\n\n"
            "Do espelho emerge uma voz: Nyth, deusa do esquecimento, irmã de Solvarah. Ela "
            "afirma que foi ela mesma quem os aprisionou a todos — para proteger o mundo do "
            "que aconteceria se eles despertassem com raiva."
        ),
        "options": [
            ("Confiar em Nyth e pedir sua ajuda", "aliar_nyth"),
            ("Desconfiar e libertar Solvarah sozinha", "N07"),
        ],
    },

    "N04": {
        "title": "FINAL — O Guardião do Silêncio",
        "image": "assets/imagens/N04_mapa_em_cinzas_FIM.svg",
        "text": (
            "Yara joga o mapa nas chamas do altar. A fumaça sobe e, por um instante, forma "
            "um rosto — o de um homem sorrindo com tristeza — antes de se dissipar.\n\n"
            "Nada acontece. Nenhum trovão, nenhuma punição. Apenas o mundo continuando na "
            "penumbra, exatamente como antes. Yara envelhece guardando o templo, e a história "
            "de Solvarah se torna apenas mais uma lenda perdida.\n\n"
            "Um final tranquilo, mas incompleto: o mistério nunca é resolvido, e o mundo "
            "permanece como estava."
        ),
        "options": [],
    },

    "N05": {
        "title": "N05 — O Coração da Montanha",
        "image": "assets/imagens/N05_coracao_da_montanha.svg",
        "text": (
            "O caminho leva a uma fenda na Montanha Cinza, onde Solvarah está selado sob "
            "uma laje de luz solidificada — a última luz do sol antes do silêncio. Para "
            "quebrá-la, é preciso um sacrifício: um pedaço da própria memória de quem a quebra."
        ),
        "options": [
            ("Sacrificar a lembrança da mãe", "sacrificar_memoria"),
            ("Usar a Corrente do Silêncio", "usar_corrente"),
            ("Recuar e buscar mais informação", "N03"),
        ],
    },

    "N06": {
        "title": "N06 — Aliança com Nyth",
        "image": "assets/imagens/N06_alianca_com_nyth.svg",
        "text": (
            "Nyth revela a verdade: Solvarah não foi aprisionado por punição, mas por "
            "misericórdia. Ele havia decidido incendiar o mundo com um novo amanhecer tão "
            "intenso que apagaria toda vida — não por maldade, mas por acreditar que era hora "
            "de recomeçar tudo.\n\n"
            "Com a ajuda de Nyth, é possível libertá-lo de forma controlada, mantendo parte "
            "de seu poder selado."
        ),
        "options": [
            ("Libertá-lo mantendo o selo parcial", "N10"),
            ("Pedir a Nyth que remova todo o selo", "N11"),
        ],
    },

    "N07": {
        "title": "FINAL — O Amanhecer Que Consome",
        "image": "assets/imagens/N07_amanhecer_que_consome_FIM.svg",
        "text": (
            "Yara ignora os avisos de Nyth e quebra o selo sozinha, usando apenas sua fé. "
            "A câmara treme. A água das catacumbas evapora instantaneamente, e uma figura "
            "de luz pura emerge — imensa, radiante, sem controle algum.\n\n"
            "Solvarah desperta livre e absoluto. O primeiro raio de sol em mil anos incendeia "
            "o horizonte — bonito, terrível e imparável. O mundo terá um novo amanhecer, mas "
            "talvez nenhum entardecer."
        ),
        "options": [],
    },

    "N08": {
        "title": "N08 — O Preço da Memória",
        "image": "assets/imagens/N08_preco_da_memoria.svg",
        "text": (
            "Yara entrega sua lembrança mais preciosa. A laje racha como vidro, e a luz que "
            "escapa não é ofuscante, mas dourada e quente — como um abraço esquecido. Solvarah "
            "desperta, mas Yara já não se lembra por que chorou ao libertá-lo.\n\n"
            "Solvarah, grato e lúcido, pergunta seu nome. Ela não sabe mais dizer."
        ),
        "options": [
            ("Pedir que Solvarah devolva sua memória", "recuperar_memoria"),
            ("Aceitar o esquecimento como preço", "N13"),
        ],
    },

    "N09": {
        "title": "N09 — Libertação Parcial",
        "image": "assets/imagens/N09_libertacao_parcial.svg",
        "text": (
            "A Corrente do Silêncio absorve o excesso de poder no momento da libertação. "
            "Solvarah desperta contido, quase humano em sua forma — um deus diminuído, mas "
            "consciente e grato por ainda existir.\n\n"
            "Ele oferece a Yara uma escolha final: usar o restante de seu poder para trazer "
            "de volta o sol de vez, ou usá-lo para reviver os outros deuses adormecidos, um "
            "a um, ao longo dos séculos."
        ),
        "options": [
            ("Pedir o retorno definitivo do sol", "N14"),
            ("Despertar os outros deuses lentamente", "N15"),
        ],
    },

    "N10": {
        "title": "FINAL — O Equilíbrio Restaurado",
        "image": "assets/imagens/N10_equilibrio_restaurado_FIM.svg",
        "text": (
            "Solvarah desperta com metade de seu poder ainda contido por Nyth. Ele não se "
            "opõe — reconhece que talvez não estivesse pronto para tanta liberdade.\n\n"
            "Juntos, Solvarah e Nyth decidem governar o ciclo dia/noite em equilíbrio, pela "
            "primeira vez em mil anos. O mundo ganha de volta o ciclo do sol e da lua, "
            "comedido e estável. Yara se torna a primeira sacerdotisa de uma nova era."
        ),
        "options": [],
    },

    "N11": {
        "title": "FINAL — O Deus Que Aprendeu a Esperar",
        "image": "assets/imagens/N11_deus_que_aprendeu_a_esperar_FIM.svg",
        "text": (
            "Nyth relutantemente remove o selo por completo, confiando no julgamento de Yara. "
            "Solvarah desperta inteiro — e, para surpresa de todos, ele chora. Mil anos de "
            "solidão o mudaram mais do que o poder jamais poderia.\n\n"
            "Solvarah devolve o sol ao mundo, mas com moderação — nascer e pôr-do-sol, como "
            "deveria ser desde sempre. Um final de esperança conquistada, não dada de graça."
        ),
        "options": [],
    },

    "N12": {
        "title": "FINAL — Duas Perdas, Um Ganho",
        "image": "assets/imagens/N12_duas_perdas_um_ganho_FIM.svg",
        "text": (
            "Solvarah aceita o pedido. Para devolver a memória de Yara, ele abre mão de parte "
            "de seu poder recém-recuperado — o suficiente para nunca mais conseguir apagar "
            "um amanhecer inteiro, apenas iluminá-lo.\n\n"
            "Yara recupera a lembrança da mãe, mas Solvarah permanece para sempre diminuído. "
            "O mundo ganha sóis suaves, nunca mais ofuscantes."
        ),
        "options": [],
    },

    "N13": {
        "title": "FINAL — O Amanhecer Sem Nome",
        "image": "assets/imagens/N13_amanhecer_sem_nome_FIM.svg",
        "text": (
            "Yara aceita viver sem aquela lembrança. Ela nunca saberá o rosto da própria mãe "
            "outra vez — mas o mundo desperta, dourado e vivo, pela primeira vez em mil anos.\n\n"
            "Ela se torna lenda: a guardiã que esqueceu para que todos pudessem lembrar de "
            "novo o que era o sol."
        ),
        "options": [],
    },

    "N14": {
        "title": "FINAL — Luz Eterna",
        "image": "assets/imagens/N14_luz_eterna_FIM.svg",
        "text": (
            "Solvarah usa o que resta de seu poder para acender o sol permanentemente. O céu "
            "nunca mais escurecerá por completo.\n\n"
            "Um mundo sem noite é deslumbrante a princípio, mas as plantas noturnas morrem, "
            "os animais da escuridão desaparecem, e o equilíbrio do mundo se rompe de um "
            "jeito novo. Nem toda luz é bênção sem sombra."
        ),
        "options": [],
    },

    "N15": {
        "title": "FINAL — A Semente do Amanhecer",
        "image": "assets/imagens/N15_semente_do_amanhecer_FIM.svg",
        "text": (
            "Solvarah escolhe reviver os outros deuses aos poucos, ao longo de gerações. "
            "Yara não viverá para ver o fim dessa jornada, mas planta a primeira semente de "
            "um mundo que voltará, devagar, a ter todos os seus deuses de volta.\n\n"
            "Nada se resolve de imediato, mas tudo começa a se curar."
        ),
        "options": [],
    },

    # Cena de consequência para tentativa inválida de usar a Corrente.
    "corrente_ausente": {
        "title": "A Relíquia que Você Não Possui",
        "image": "assets/imagens/N05_coracao_da_montanha.svg",
        "text": (
            "Yara procura pela Corrente do Silêncio, mas nunca aceitou a relíquia de Kessian.\n\n"
            "A única opção é escolher outro caminho."
        ),
        "options": [
            ("Voltar à laje", "N05"),
        ],
    },
}


# ============================================================
# ACESSO AO HTML
# ============================================================

def el(id_elemento):
    return web.page[id_elemento]


# ============================================================
# IDENTIDADE VISUAL
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
    audio.dataset.inicial = trilha if trilha else ""
    audio.dataset.volume = str(CONFIG.get("volume_inicial", 0.5))


# ============================================================
# STATUS
# ============================================================

def atualizar_status():
    vida = state["vida"]
    if vida > 0:
        el("vida").innerText = " ".join(["❤️"] * vida)
        el("vida").classList.remove("danger")
    else:
        el("vida").innerText = "💀"
        el("vida").classList.add("danger")

    if state["inventario"]:
        el("inventario").innerText = ", ".join(state["inventario"])
    else:
        el("inventario").innerText = "Vazio"

    el("pontos").innerText = str(state["pontos"])


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
    window.frameworkVideo.play(caminho, autoplay)


def trocar_audio(caminho):
    if caminho:
        window.frameworkAudio.play(
            caminho,
            CONFIG.get("volume_inicial", 0.5),
            True,
        )


def parar_audio():
    window.frameworkAudio.stop()


# ============================================================
# BOTÕES
# ============================================================

def configurar_botao(numero, texto="", ativo=False):
    botao = el(f"opcao{numero}")
    botao.innerText = texto
    botao.disabled = not ativo
    botao.style.display = "block" if ativo else "none"


def opcoes_da_cena(nome, cena):
    """Permite adaptar opções conforme o estado sem alterar a história-base."""
    opcoes = list(cena.get("options", []))

    # Em N05, a Corrente só pode ser usada se realmente estiver no inventário.
    if nome == "N05" and not possui_item("Corrente do Silêncio"):
        opcoes = [
            ("Sacrificar a lembrança da mãe", "sacrificar_memoria"),
            ("Tentar usar a Corrente do Silêncio", "usar_corrente"),
            ("Recuar e buscar mais informação", "N03"),
        ]

    return opcoes


def atualizar_botoes(opcoes):
    for i in range(1, 5):
        if i <= len(opcoes):
            configurar_botao(i, opcoes[i - 1][0], True)
        else:
            configurar_botao(i, "", False)


# ============================================================
# MOSTRAR CENA
# ============================================================

def mostrar_cena(nome):
    if nome not in SCENES:
        el("titulo-cena").innerText = "Erro de cena"
        el("texto-cena").innerText = f"A cena '{nome}' não existe em SCENES."
        atualizar_botoes([])
        return

    state["cena"] = nome
    cena = SCENES[nome]

    el("titulo-cena").innerText = cena.get("title", nome)
    el("texto-cena").innerText = cena.get("text", "")

    video = cena.get("video")
    if video:
        mostrar_video(video, cena.get("video_autoplay", False))
    else:
        mostrar_imagem(cena.get("image"))

    if "audio" in cena:
        if cena["audio"]:
            trocar_audio(cena["audio"])
        else:
            parar_audio()

    if cena.get("stop_audio"):
        parar_audio()

    atualizar_botoes(opcoes_da_cena(nome, cena))
    atualizar_status()


# ============================================================
# FUNÇÕES DE ESTADO
# ============================================================

def adicionar_item(item, pontos=0):
    if item not in state["inventario"]:
        state["inventario"].append(item)
        state["pontos"] += pontos
    atualizar_status()


def possui_item(item):
    return item in state["inventario"]


def ganhar_pontos(quantidade):
    state["pontos"] += quantidade
    atualizar_status()


# ============================================================
# EXECUTAR AÇÃO
# ============================================================

def executar_acao(acao):

    if acao == "aceitar_corrente":
        adicionar_item("Corrente do Silêncio", pontos=15)
        mostrar_cena("N05")

    elif acao == "fe_pura":
        state["fe_pura"] += 1
        ganhar_pontos(10)
        mostrar_cena("N05")

    elif acao == "aliar_nyth":
        state["alianca_com_nyth"] = True
        ganhar_pontos(10)
        mostrar_cena("N06")

    elif acao == "sacrificar_memoria":
        state["memoria_da_mae"] = False
        ganhar_pontos(20)
        mostrar_cena("N08")

    elif acao == "usar_corrente":
        if possui_item("Corrente do Silêncio"):
            ganhar_pontos(20)
            mostrar_cena("N09")
        else:
            mostrar_cena("corrente_ausente")

    elif acao == "recuperar_memoria":
        state["memoria_da_mae"] = True
        ganhar_pontos(15)
        mostrar_cena("N12")

    elif acao in SCENES:
        mostrar_cena(acao)

    else:
        el("texto-cena").innerText = f"A ação '{acao}' não foi cadastrada."


# ============================================================
# ESCOLHER OPÇÃO
# ============================================================

def escolher_opcao(numero):
    nome = state["cena"]
    cena = SCENES[nome]
    opcoes = opcoes_da_cena(nome, cena)
    indice = numero - 1

    if indice < len(opcoes):
        executar_acao(opcoes[indice][1])


# ============================================================
# EVENTOS
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
    state["vida"] = CONFIG["vida_inicial"]
    state["inventario"] = []
    state["pontos"] = CONFIG["pontos_iniciais"]
    state["cena"] = CONFIG["cena_inicial"]
    state["fe_pura"] = 0
    state["alianca_com_nyth"] = False
    state["memoria_da_mae"] = True

    trilha = CONFIG.get("trilha_inicial")
    if trilha:
        trocar_audio(trilha)

    mostrar_cena(CONFIG["cena_inicial"])


# ============================================================
# INICIALIZAÇÃO
# ============================================================

configurar_identidade()
mostrar_cena(CONFIG["cena_inicial"])
el("botao-iniciar").disabled = False
el("botao-iniciar").innerText = "▶ INICIAR JOGO"
