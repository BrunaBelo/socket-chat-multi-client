O projeto consiste em um chat assíncrono que permite a conexão com vários clientes, foi desenvolvido na linguagem python 
utilizando conceitos de socket e threading, onde, os clientes se comunicam
com um servidor principal que replica as mensagens enviadas para todos os clientes
conectados via socket, cada conexão socket trabalha diretamente em um thread possibilitando desta forma a sincronicidade do chat.
Quando o cliente digita "see ya" sua conexão é fechada.

# Como utilizar:

Basta executar os scripts:

server$ python server.py
client$ python client.py