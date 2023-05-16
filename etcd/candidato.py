import threading
import etcd3 
import time
import sys

etcd = etcd3.client()
leader = None


# atualiza o lease periodicamente enquanto o cliente é o líder.
# @return void
# @client_id: nome do cliente
def keep_leadership(client_id):
    global leader
    global etcd

    while leader == client_id:
        time.sleep(3)
        etcd.put(key='/lider', value=client_id, lease=etcd.lease(10))


# Define o cliente como o líder e inicia uma thread separada para 
# atualizar a concessão.
# @client_id: nome do cliente
# @return void
def become_leader(client_id):
    global leader
    global etcd

    print(f'Sou o LÍDER!: {client_id}')
    leader = client_id
    threading.Thread(target=keep_leadership, args=(client_id,)).start()
    input('Tecle algo para terminar...')
    leader = None


# Verifica se o líder atual ainda é válido ou se um novo líder surgiu.
def check_leader_status():
    global leader
    global etcd

    while leader:
        time.sleep(5)
        resultado = etcd.get('/lider')
        if resultado[0] is None or resultado[0].decode('utf-8') != leader:
            leader = None
            break


# Contém a lógica principal e orquestra o processo de eleição do líder.
def run(client_id):
    global leader
    global etcd

    running = True

    while running:
        print(f'Tentando liderança...')
        is_leader = etcd.put_if_not_exists(key='/lider', value=client_id, lease=etcd.lease(10))

        if is_leader:
            become_leader(client_id)
            running = False         # parar o loop
            exit(0)                 # termina o programa
        # se não for o líder, perguntar quem é o líder
        else:
            leader = etcd.get('/lider')[0].decode('utf-8')
            print(f'{leader} é o líder')
            # checar se o status de líder ainda é válido
            check_leader_status()



if __name__ == "__main__":
    client_id = sys.argv[1]
    run(client_id)
