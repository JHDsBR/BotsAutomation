from os import environ as env
import smtplib

"""
    é provável que um erro irá ocorrer, então sugiro que use 
    uma senha de app no lugar da sua senha pessoal.


    você pode conseguir uma senha de app aqui 
        > https://myaccount.google.com/u/4/apppasswords?rapt=AEjHL4OlplQahPUzL9OOI9Nf_TBJLQ_HnEvBtkgJQcBwxxv85a0bzCSnGnUsIzATiOzUkpim5Gteehl_lkQK3-l3jJ2K24i7ow


    se essa opção não estiver disponível, tente ativar a 
    autenticação de dois fatores, e tente novamente.

"""


GMAIL_FROM          = str(env["GMAIL_FROM"])
GMAIL_FROM_PASSWORD = str(env["GMAIL_FROM_PASSWORD"])
GMAIL_TO            = str(env["GMAIL_TO"]).split(sep=';')


def SendEmail(assunto:str, relatorio:str, _from=None, _from_password=None, _to=None):
    
    _from = _from if _from else GMAIL_FROM
    _from_password = _from_password if _from_password else GMAIL_FROM_PASSWORD
    _to = _to if _to else GMAIL_TO

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(_from, _from_password)
            message = 'Subject: {}\n\n{}'.format(assunto, relatorio)
            server.sendmail(_from, _to, message.encode("utf8"))
            server.quit()

        print('Email enviado com sucesso\n')
        return True
    except Exception as ex:
        print('Erro ao enviar email\n')
        print(ex)
        return False 
        

