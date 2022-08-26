# -*- coding: utf-8 -*-
"""
Autor: Carlos Santana

Atividade 3 - calculo de endereço IPv4
O seguinte algoritmo calcula a subrede e o broadcast de um endereço IPv4.
A metodologia é a seguinte:
1. O usuário deve digitar o endereço IPv4.
2. O algoritmo deve separar o endereço em seus componentes (IPv4) e converter cada um deles para binário.
3. O algoritmo deve calcular a subrede e o broadcast do endereço IPv4.
4. O algoritmo deve imprimir o endereço IPv4, o endereço da subrede e o endereço do broadcast.
"""

# A seguinte função converte um endereço IP para binário.
def bin_ip(ip_address):
    binary_ip = ''
    for octet in ip_address.split('.'):
        binary_ip += bin(int(octet))[2:].zfill(8)
    # Separate the binary string into a list of 8-bit binary strings.
    binary_ip_list = [binary_ip[i:i+8] for i in range(0, len(binary_ip), 8)]
    
    return binary_ip_list

print(bin_ip('192.168.0.1'))

# Calcular endereço de rede.
# Pega como argumento o endereço binário e a máscara.
def net_address(binary_address, net_mask):
    # Converte o endereço binário como string
    binary_address = ''.join(binary_address)
    binary_address = binary_address[:net_mask]

    net_address = ''
    for i in range(32 - net_mask):
        net_address = binary_address + "0"
    
    # Completa os 0s do endereço até chegar na máscara.
    while len(net_address) < 32:
        net_address += "0"
    # Converte o endereço binário para decimal.
    ipStr = str(int(net_address[:8],2)) +"."+ str(int(net_address[8:16],2)) +"."+ str(int(net_address[16:24],2)) +"."+ str(int(net_address[24:],2)) # Converte o ip em decimal (achei a expressão aqui, linha 56: https://gist.github.com/windard/6bc7bfa7013aafb1239faab2050a9fda)
   
    # Adiciona os pontos divisores de octetos
    net_address = net_address[:8] + "." + net_address[8:16] + "." + net_address[16:24] + "." + net_address[24:]

    return net_address, ipStr

# Calcular endereço de broadcast.
# Pega como argumento o endereço binário e a máscara.
def broadcast_address(binary_address, net_mask):
    # Converte o endereço binário como string
    binary_address = ''.join(binary_address)
    binary_address = binary_address[:net_mask]

    broadcast_address = ''
    for i in range(32 - net_mask):
        broadcast_address = binary_address + "1"  

    # Completa os 1s do endereço até chegar na máscara.
    while len(broadcast_address) < 32:
        broadcast_address += "1"
   
    # Converte o endereço binário para decimal.
    ipStr = str(int(broadcast_address[:8],2)) +"."+ str(int(broadcast_address[8:16],2)) +"."+ str(int(broadcast_address[16:24],2)) +"."+ str(int(broadcast_address[24:],2)) # Converte o ip em decimal (achei a expressão aqui, linha 56: https://gist.github.com/windard/6bc7bfa7013aafb1239faab2050a9fda)
    
    # Adiciona os pontos divisores de octetos
    broadcast_address = broadcast_address[:8] + "." + broadcast_address[8:16] + "." + broadcast_address[16:24] + "." + broadcast_address[24:]

    return broadcast_address, ipStr

# Execução do algoritmo
print(net_address(bin_ip('183.244.34.32'), 28))
print(broadcast_address(bin_ip('183.244.34.32'), 28))