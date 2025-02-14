import os

def block_ip(ip_address):
    """
    Função para bloquear um IP usando o iptables.
    :param ip_address: Endereço IP que será bloqueado
    :return: None
    """
    os.system(f"sudo iptables -A INPUT -s {ip_address} -j DROP")
    print(f"IP {ip_address} bloqueado com sucesso!")

# Exemplo de uso
block_ip("192.168.1.100")  # Substitua pelo IP que deseja bloquear
