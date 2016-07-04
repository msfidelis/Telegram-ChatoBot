#!/usr/bin/python
# -*- coding: utf-8 -*-

from twx.botapi import TelegramBot
from random import randint
import pickle
import sqlite3
from os import path
import sys
import datetime

CURR_PATH = path.dirname(path.realpath(__file__))
DUMP_FILE = path.join(CURR_PATH, "data.pkl")

BOTAPI = ''
bot = TelegramBot(BOTAPI)
bot.update_bot_info().wait()


###### MODELS ######

# Grava a mensagem no banco name, sobnome, username, update.message.text, bot_message
def setmessage(nome, sobrenome, username, message, response):
    try:
        data = datetime.datetime.now().date().isoformat()
        con = sqlite3.connect('botchato.db')
        cur = con.cursor()
        dados = [
            (nome, sobrenome, username, message, response, data)
        ]
        # Insere os registros
        insert = "INSERT INTO messages (name, sobname, username, message, response, data) values (?,?,?,?,?,?)"
        cur.executemany(insert, dados)
        con.commit()
    except:
        print "DATABASE ERROR"
        pass


# Função de "Aprendizado"
def learn():
    hoje = datetime.datetime.now().date().isoformat()
    con = sqlite3.connect('botchato.db')
    cur = con.cursor()
    # PEGA AS 3 FRASES MAIS UTILIZADAS DO DIA
    query = "SELECT COUNT(*) as qtd, message FROM messages GROUP BY message LIMIT 3 WHERE data = "


def crentemessages():
    num = randint(1, 3)
    
    if num == 1:
        return "Vaza daqui seu crente Agenor duque. Vai fazer milagres na pqp..."
    elif num == 2:
        return "Seu crente crentão..."
    elif num == 3:
        return "Odeio crente"
    elif num == 4: 
        return ""
    
	
    
# Query de xingamentos
def xingamentosearch():
    try:
        con = sqlite3.connect('botchato.db')
        cur = con.cursor()
        query = "SELECT COUNT(*) as qtd FROM ofensas"
        cur.execute(query)

        recset = cur.fetchall()
        for rec in recset:
            for reg in rec:
                qtd = reg
        con.close()

        con = sqlite3.connect('botchato.db')
        cur = con.cursor()

        # Pega um numero aleatório dentro do range da quantidade de ofensas registradas
        num = randint(1, qtd)

        # Procura na base a ofensa aprendida de id X
        query_xingamento = "SELECT ofensa FROM ofensas WHERE id = %s" % num
        cur.execute(query_xingamento)
        xingamento = cur.fetchall()

        for message in xingamento:
            for resposta in message:
                return resposta

    except:
        pass

# Piadas de mãe gorda
def suamaesearch():
    try:
        con = sqlite3.connect('botchato.db')
        cur = con.cursor()
        query = "SELECT COUNT(*) as qtd FROM suamae"
        cur.execute(query)

        recset = cur.fetchall()
        for rec in recset:
            for reg in rec:
                qtd = reg
        con.close()

        con = sqlite3.connect('botchato.db')
        cur = con.cursor()

        # Pega um numero aleatório dentro do range da quantidade de ofensas registradas
        num = randint(1, qtd)

        # Procura na base a ofensa aprendida de id X
        query_xingamento = "SELECT message FROM suamae WHERE id = %s" % num
        cur.execute(query_xingamento)
        xingamento = cur.fetchall()

        for message in xingamento:
            for resposta in message:
                return resposta
    except:
        pass
    
# Piadas de mãe gorda
def bomdiasearch():
    try:
        con = sqlite3.connect('botchato.db')
        cur = con.cursor()
        query = "SELECT COUNT(*) as qtd FROM bomdia"
        cur.execute(query)

        recset = cur.fetchall()
        for rec in recset:
            for reg in rec:
                qtd = reg
        con.close()

        con = sqlite3.connect('botchato.db')
        cur = con.cursor()

        # Pega um numero aleatório dentro do range da quantidade de ofensas registradas
        num = randint(1, qtd)

        # Procura na base a ofensa aprendida de id X
        query_xingamento = "SELECT message FROM bomdia WHERE id = %s" % num
        cur.execute(query_xingamento)
        xingamento = cur.fetchall()

        for message in xingamento:
            for resposta in message:
                return resposta
    except:
        pass    

def trylearn():
    date = now()
    print date
    
    
# Se existe, carregar a lista de mensagens respondidas
if path.exists(DUMP_FILE):
    pkl_file = open(DUMP_FILE)
    answered_messages = pickle.load(pkl_file)
else:
    answered_messages = []

offset = None

while (True):
    try:
	trylearn()
        bot_message = False
        print ("Verificando o Web Service".center(50, '-'))
        updates = bot.get_updates(offset=offset).wait()

        for pos, update in enumerate(updates):
            offset = update.update_id + 1
            print(str(pos) + " " + str(update) + "n")
            update_id = update.update_id
            
            crenteTest = int(update.message.text.find('crente'))

            # Se a mensagem não foi respondida, responda o usuário
            if update_id not in answered_messages:
                sender_id = update.message.sender.id

                #Metodos default
                if update.message.text == "/suamae":
                    bot_message = suamaesearch()
                elif update.message.text == "/bomdia":
                    bot_message = bomdiasearch()
                elif update.message.text == "/about":
                    bot_message = "O Matheus Fidelis é lindo pra caralho. Senhor Deus do Universo!!"
                elif update.message.text == "/start":
                    bot_message = "Oi, eu sou o ChatoBot. Não gostou pau no seu cu."

                #Algumas mensagens customizadas
                elif update.message.text.upper() == "OI":
                    bot_message = "Fala aí otário"
                elif update.message.text.upper() == "OLÁ":
                    bot_message = "Fala aí otário"
                elif update.message.text.upper() == "DUVIDO":
                    bot_message = "Meu pau no seu ouvido"
                elif update.message.text.upper() == "CALA A BOCA":
                    bot_message = "Cala a boca morreu, quem manda na minha boca sou eu"
                elif update.message.text.upper() == "CALA BOCA":
                    bot_message = "Cala a boca morreu, quem manda na minha boca sou eu"
                elif update.message.text.upper() == "VIADO":
                    bot_message = "Viado é rolimã, como tu e tua irmã"
                    
                #metodos customizados
                
                #Zoa crente
                elif crenteTeste >= 0:
                    bot_message = crentemessages()
                    print bot_bot_message
                    print "Deu certo"
                        
                #Ofensa aleatória
                else:
                    name = update.message.sender.first_name
                    sobnome = update.message.sender.last_name
                    username = update.message.sender.username
                    bot_message = xingamentosearch()

                #Responde ao usuário solicitante
                if bot_message:
                    result = bot.send_message(sender_id, bot_message)
                    bot_message = False

                    # Grava o log da mensagem
                    setmessage(name, sobnome, username, update.message.text, bot_message)
                    if result:
                        answered_messages.append(update_id)

                output = open(DUMP_FILE, 'wb')
                pickle.dump(answered_messages, output)  # persiste a lista de mensagens respondidas


    except:
        pass

    output = open(DUMP_FILE, 'wb')
    pickle.dump(answered_messages, output)  # persiste a lista de mensagens respondidas
