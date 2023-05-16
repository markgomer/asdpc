#!/usr/bin/env python3

from pika import BlockingConnection


def trata_msg(ch, method, properties, body):
    msg = body.decode().split(':')

    print('hora:')
    print('hora:')
    print('hora:')
    print('hora:')

    # ch.basic_ack(delivery_tag=method.delivery_tag) # se auto_ack = False
    conexao = BlockingConnection()
    canal = conexao.channel()
    canal.queue_declare(queue='fila')
    canal.basic_consume(queue='fila', \
                        on_message_callback=callback, auto_ack=True)
    try:
        print('Esperando mensagens... CTRL+C para sair')
        canal.start_consuming()
    except KeyboardInterrupt:
        canal.stop_consuming()
    conexao.close()
