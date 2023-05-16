#!/usr/bin/env python3

from pika import BlockingConnection
import time
import os

conexao = BlockingConnection()
canal = conexao.channel()

canal.exchange_declare(exchange="glog",exchange_type="fanout")

timestamp = time.time()
pid = os.getpid()
comentario = 'COMENTADO!!'

msg = f'{timestamp}:severidade:{pid}:{comentario}'

canal.basic_publish(
    exchange='glog', # default exchange
    routing_key='', # nome da fila
    body=msg)

conexao.close()