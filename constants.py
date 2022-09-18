from os import environ as env
from random import choice

#! REVISADO
#! REVISADO
#! REVISADO

TIME_BETWEEN_LIKES_ON_COMMENTS = 1
TIME_BETWEEN_LIKE_AND_COMMENT_VIDEO = 0 # tempo entre interação no video, ou seja, tempo que vai esperar após deixar uma curtida e um comentário
TIME_BETWEEN_THE_LIKE_AND_COMMENT = 0 # tempo que vai esperar entre uma curtida e um comentário
MAX_LIKES_ON_COMMENTS = 31

DOMINIO = env["DOMINIO"]
MY_API_URL = env["MY_API_URL"]
MY_API_URL_UPDATE = env["MY_API_URL_UPDATE"]
MY_YT_API_KEY = env["MY_YT_API_KEY"]

class URL:

    SITE = f"https://{DOMINIO}/"
    SITE_UPLOAD = f'https://{DOMINIO}/studio/upload/select'
    MY_VIDEOS = f'https://{DOMINIO}/studio/my_videos'
    MY_DASHBOARD = f'https://{DOMINIO}/v2/personal-center/dashboard'


class CSS_ELEMENT:

    # DOMINIO
    UPLOAD_INPUT = 'input.video-input' # <input data-v-df377040="" type="file" accept="video/mp4,video/MP2T,video/x-flv,video/x-ms-wmv,video/ms-asf,application/vnd.rn-realmedia-vbr,video/mpeg,video/3gpp,video/webm,video/x-matroska,video/quicktime,video/avi" class="video-input">
    UPLOAD_PROGRESS = 'div.process-value-text' # <div data-v-7802f6e4="" class="process-value-text">100%</div>
    VIDEO_TITLE = 'input#video-name' # <input data-v-2398d312="" id="video-name" type="text" autocomplete="off" placeholder="Digite o título do vídeo" class="input-text">
    VIDEO_THUMB = 'div.cover-item-wrapper'
    THUMB_LOADING = 'div.cover-item-wrapper > img.no-img' # <img data-v-6e6ca63f="" src="" class="no-img">
    SEND_VIDEO_BUTTON = 'div.wrap > form.form > div.form-item > button[type="submit"]' # <button data-v-2398d312="" type="submit" class="">Envio confirmado</button>
    LAST_VIDEO_THUMB = 'ul.list-ul > li.list-item > div.img-out'
    APPROVED = 'ul.list-ul > li.list-item > div.video-info > span.review'
    UPLOAD_SUCCESS = 'div.vue-easily-notify'
    NO_DATA = 'div.list-out > div > div.no-data'

    # RECAPTCHA
    DESAFIO_DE_AUDIO = "button[title='Receber um desafio de áudio']"
    RECAPTCHA = "iframe[title='recaptcha challenge expires in two minutes']"
    TYPE_CHALENGE = 'div.rc-imageselect-desc-wrapper'
    OBJECT_TO_FIND = 'div#rc-imageselect > div.rc-imageselect-payload > div > div > div > strong'
    IMG = "div.rc-image-tile-wrapper > img"
    RELOAD = 'button#recaptcha-reload-button' # <button class="rc-button goog-inline-block rc-button-reload" title="Receber outro desafio" value="" id="recaptcha-reload-button" tabindex="3"></button>
    VERIFY = 'button#recaptcha-verify-button' # <button class="rc-button-default goog-inline-block" title="" value="" id="recaptcha-verify-button" tabindex="0">Verificar</button>
    TABLE_4 = 'table.rc-imageselect-table-44'
    TABLE_3 = 'table.rc-imageselect-table-33'
    # TABLE_4 = 'table.rc-imageselect-table-44'

    # GOOGLE
    PESQUISAR_POR_IMG = "div[aria-label='Pesquisa por imagem']"
    UPLOAD_IMG = "form[method='GET'] > div > div > a"
    CHOOSE_FILE = "input[type='file']"
    INPUT_URL_IMG = "input#Ycyxxc"
    BUTTON_PESQUISAR = 'input#RZJ9Ub'
    BARRA_PESQUISA_VALUE = "input[aria-label='Pesquisar']"
    IMG_SEMELHANTES = "title-with-lhs-icon > a"
    IMGS_GRID = "div#islmp"

    # YOUTUBE
    FILTER_BUTTON = 'a.yt-simple-endpoint'
    LAST_HOUR = 'a#endpoint > div#label > yt-formatted-string'



class COMMENT:

    def GetRandom():
        return choice([
            "gostei do vídeo",
            "booa",
            "ai sim",
            "alguém dá like no meu comentário pfv :)",
            "KKKKKKKKK",
            "cara que massa",
            "oxe top demais",
            "já deixei meu like",
            "curte aqui",
            "gostei demais",
            "opa alguém curte aqui",
            "Deus te ama",
            "Deus é fiel",
            "CAVALO",
            "me dá like",
            "HEHEHEHE",
            "Passando aqui para deixaer o meu like .",
            "Deixando o likee",
            "ótimo parabéns.",
            "NOVO ASSINANTE. Convido você a crescer junto. Bençãos.",
            "Adorei",
            "Excelente",
            "passando deixar meu apoio",
            "LIKE PFVVV",
            "Olá!!!!",
            "bora curtir pessoal e não esqueçam de deixar o comentário",
            "dando like nesse comentrio vc ganha e eu tbm, vamo se ajudar",
            "Inscrito e liked!!!",
            "Maneiro",
            "kkkk",
            "caraaaaaa",
            "nani???",
            "agora me ajuda curtindo meu comentátio obg",
            "Passando pra apoiar o canal tmj sucesso meu amigo se puder visitar meu Canal e deixar seu like no meu último vídeo",
            "Excelente video, espero que você cresça muito e alcance seus objetivos.\nDeixei aqui minha humilde inscrição e um like.\nConsegue dar uma força no meu canal tambem?",
            "Adoro ver seus vídeos amigo, sucesso",
            "Top parabéns",
            "Deixando meu apoio e meu pequeno super like família",
            "#Like",
            "Aquele like juntos somos mais fortes",
            "Top D+",
            "OI, PASSANDO PRA DEIXAR MEU APOIO!! PARABENS!!",
            "Buen video",
            "Bom video",
            "Borá deixar o LIKEZAO e COMENTARIO ",
            "tmj",
            "Tome lake",
            "muito massa!!.",
            "nice video",
            "espero que você cresça,Top parabéns",
            "AJUDINHA",
            "aqui deixando .meu apoio",
            "Likezão pra fortalecer",
            "DEIXANDO AQUELE LIKE PRA FORTALECER O CANAL TAMO JUNTO IRMAO SALVE SALVE A {DOMINIO}",
            "Canal com conteúdo legal",
            "Esse vídeo é muito bom!!!!",
            "pariu lake",
            "Deixando o meu like. Ajude meu canal se inscrevendo dando o like e comentando. TMJ",
            "Ola bom dia pessoal, sou novo por aqui e venho pedir um like para cada um de vocês, que Deus possa derramar chuva de bençãos sobre a vida de todos, amém?",
            "Passando pra poiar tmj susseço",
            "Olá, estou muito feliz em conhecê-lo, vamos SEGUIR e DESENVOLVER juntos. Obrigado meus amigos",
            "Arretadooo",
            "saudações bom conteúdo apoiando como sempre obrigado",
            "Regalando Like",
            "vem comigo",
            "Se inscreva no canal",
            "Apoiando",
            "blzz",
            "Deixando o meu apoio com like , desejando sucesso e prosperidade ao canal. Aceito a sua RETRIBUIÇÃO, com muito carinho e gratidão. Abraços",
            "passando para deixar aquele like maroto!",
            "Suporte para a Alegria!",
            "big like",
            "passando e contribuindo pra fortalecer o canal, like de força",
            "Ótimo conteúdo",
            "Fortalecer é o Segredo",
            "Deixando meu like de sempre",
            "Fortalecendo para Valorizar seu Trabalho",
            "Pas passando para conferir seu belo Trabalho",
            "já deixando o criptolike",
            "Muito legal, já me inscrevi no seu canal",
            "Parabéns pelo canal..Likes e inscrição com sucesso !",
            "Que Deus nos abençoe!",
            "vamos ajudar uns aos outros",
            "muito bom, fortalecendo z",
            "Estou sem energia para deixar like",
            "muito bom sucesso",
            "like from me",
            "Todos os likes serão bem vindos e retribuídos também!",
            "#juntossomosmaisfortes",
            "Como sempre, um ótimo vídeo.  Parabens pelo canal",
            "Vamos todos crescer juntos!",
            "Hay quá ạ, like, follow.",
            "bora lucrar aquuii",
            "muito bom seu canal parabéns me escrevendo aqui",
            "Parabés pelos vídeos, continue assim com esse mesmo engamento e produzindo vídeos de altissima qualidade.",
            "Like and follow my friend. Good luck to you",
            "heheh tmj",
            "Qtos vídeos posso assistir por dia?",
            "A persistência é o combustível da esperança , Sucesso No Canal !",
            "Ola, estou retornando a visita",
            "PASSANDO PARA DEIXAR MEU APOIO\nNÃO ESQUECE DE PASSAR NO INSCRIÇÃO MÚTUA",
            "Obrigado por seu apoio e gratidão ao nosso canal",
            "parabéns, seu Canal é muito didático! já merecia estar nos TOP!",
            "Demorei para te encontra. Sucesso no seu canal",
            "Like, follow, thank you for sharing this video",
            "fortalecendo o canal parabéns pelo seu vídeo parabéns",
            "Passando para dar uma força ai ao canal",
            "Tamo junto!",
            "miauau",
            "legal muito bom .....vistro o video ..retribua",
            "Passando para desejar sucesso ao canal Tmj",
            "Deixando like, passando para prestigiar o canal e o vídeo, Pessoal preciso do apoio de vocês se escrevam no meu canal e curti os meus vídeos, juntos somos mais fortes",
            "Tmj, muita sorte pra vc",
            "Meu apoio amigo",
            "Aí sim! Parabéns",
            "Aquele suporte",
            "chegando pra prestigiar o video e deixando um like pra apoiar",
            "saudações bom conteúdo apoiando como sempre obrigado",
            "Apoyando tu canal Like apóyame",
            "MUITO BOM CONTEÚDO",
            "Deixando CriptoLike para apoiar e fortalecer seu canal",
            "Falaaaa,,meuuuuu",
            "me da um like ai na namoral",
            "fala meu mano é nós Tmj sempre",
            "Un abrazo bro, pasanme por mi canal saludos",
            "Otimo video, parabens, ja deixei meu like, espero receber o seu tambem !",

        ])

class API_URL:
    LIKE = env["URL_API_LIKE"]
    COMMENT = env["URL_API_COMMENT"]