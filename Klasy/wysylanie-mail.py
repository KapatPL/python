'''
pip3 install pandas
pip3 install xlwt
'''

import os
import pandas as pd
import email, smtplib, ssl

from email.utils import formatdate
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


''' Klasa do generowania mail dla po??cze? TLS,
    Zmodyfikowany kod dla SSL ze strony 
    https://realpython.com/python-send-email/
    
    TODO: je?eli po??czenie ma by? realizowane przez SSL co? bedzie trzeba dopisa?. 
        Na dzie? pisania kodu Funkcja jest nie potrzebna
    
    TODO: Nale?y zmodyfikowa? tak klas? aby da?o si? wysy?a? wi?cej ni? jednego maila.
        na dzie? obecny jednen obiekt jeden mail
    
    TODO: Dopisa? wczytywanie konfiguracji z pliku :)
    
    TODO: Zrobi? kreator konfiguracji w trybie graficznym dla consoli.
    TODO: Wygenerowa? raport w HTML :D
'''
class SendMail():
    '''
    subject     --> Tytu? wiadomo?ci
    body        --> Wiadomo??
    account     --> Konto za pomoc? kt�rego b?dziemy si? logowa?
    password    --> has?o do konta
    port        --> port po kt�rym bedziemy si? ??czy?
    host        --> adres serwera pocztowego
    sender      --> Nazwa wy?wietlana sk?d przyszla wiadomo??
    '''
    def __init__ (self, subject, body,  
            receiver,
            account, 
            password, 
            port=587, 
            host="",
            sender = None
            ):
        # Iniciowanie potrzebnych zmiennych
        self.__account = account
        self.__subject = subject
        self.__body = body
        if sender is None:
            self.__sender_email = account
        else:
            self.__sender_email = sender
        self.__receiver_email = receiver
        self.__password = password
        self.host = host 
        self.port = port

    '''
    Generuje i wysy?a wiadomo?? 
    '''
    def generate_mail(self, filename):
        
        # Nag?owki wiadomosci
        message = MIMEMultipart()
        message["From"] = self.__sender_email
        message["To"] = self.__receiver_email
        message["Subject"] = self.__subject
        message["Bcc"] = self.__receiver_email
        message["Date"] = formatdate(localtime=True)

        message.attach(MIMEText(self.__body, "plain"))

        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
            )

        ''' Dodawanie zalacznika, i konversja na stringa '''
        message.attach(part)
        text = message.as_string()

        # Log in to server using secure context and send email
        with smtplib.SMTP(self.host, self.port) as server:
            # server.set_debuglevel(True)
            server.starttls()
            server.login(self.__account, self.__password)
            server.sendmail(self.__sender_email, self.__receiver_email, text)
            # print(server.)

''' TODO: Nale?a?o by poprawi? po??czenia, na t? chwil? brak czasu.
        Pami?ta? o tym w kolejnych implementacjach

    TODO: Napisa? generator 
'''
