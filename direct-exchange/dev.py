#!/usr/bin/env python3

from pika import BlockingConnection
import time
import os

conexao = BlockingConnection()
canal = conexao.channel()
canal.queue_declare(queue='fila_marcola')

timestamp = time.time()
pid = os.getpid()
comentario = 'COMENTADO!!'

msg = f'{timestamp}:severidade:{pid}:{comentario}'

canal.basic_publish(
    exchange='', # default exchange
    routing_key='fila_marcola', # nome da fila
    body=msg)

conexao.close()
