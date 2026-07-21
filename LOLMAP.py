
"""
Autor: SKULL
Uso: python3 LOLMAP.py
Descricao: search for vulnerabilities
"""
import subprocess
import socket
import sys
import ipaddress
import time
import os
import platform
import dns.resolver
import dns.rdatatype
from concurrent.futures import ThreadPoolExecutor
from scapy.all import Ether, ARP, srp1

os.system("cls" if os.name == "nt" else "clear")

flag = b"""
000       0000000   000      
000      000   000  000      
000      000   000  000      
000      000   000  000      
000      000   000  000      
000      000   000  000      
0000000   0000000   0000000  
"""
print("\033[91m" + flag.decode() + "\033[0m")

time.sleep(0.5)

print("Plataforma:", platform.system())
print("Release:", platform.release())
print("Version:", platform.version())
print("Arquitetura:", platform.architecture()[0])

print()
time.sleep(0.4)

def validador(ip):
    try:
        ipaddress.ip_address(ip)
        sys.audit("### [IP VALIDO] ###", ip)
        return True
    except ValueError:
        sys.audit("### [IP INVALIDO] ###", ip)
        return False

def resolver_dominio(dominio):
    try:
        resultado = dns.resolver.resolve(dominio, dns.rdatatype.A)
        ip = str(resultado[0])
        sys.audit("### [RESOLUCAO DE DOMINIOS] ###", dominio, ip)
        print(f"Dominio resolvido: {dominio} -> {ip}")
        return ip
    except dns.resolver.NXDOMAIN:
        sys.audit("### [RESOLUCAO DE DOMINIOS FALHOU] ###", dominio)
        print("O dominio nao existe!")
        return None
    except dns.resolver.NoAnswer:
        sys.audit("### [RESOLUCAO DE DOMINIOS FALHOU] ###", dominio)
        print("O dominio nao possui registro A!")
        return None
    except Exception as e:
        sys.audit("### [RESOLUCAO DE DOMINIOS FALHOU] ###", dominio)
        print(f"Erro: {e}")
        return None

def arping(ip_alvo):
    pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip_alvo)
    
    resposta = srp1(pacote, timeout=2, verbose=1)
    
    if resposta is None:
        print(f"O IP: {ip_alvo} não respondeu (timeout ou offline).")
    
    if resposta:
        print(f"O IP: {ip} está no MAC: {mac}")
        print(f"Resumo:", resposta.summary())
        return mac
    else:
        print("Recebeu um pacote, mas não é uma resposta ARP esperada.")

def detectar_os(ip):
    try:
        ping = subprocess.run(["ping", "-c", "1", "-W", "1", ip],
                              capture_output=True, text=True)
        for linha in ping.stdout.split("\n"):
            if "ttl=" in linha.lower():
                ttl_valor = int(linha.lower().split("ttl=")[1].split()[0])
                if ttl_valor <= 64:
                    return f"Linux/Unix (TTL={ttl_valor})"
                elif ttl_valor <= 128:
                    return f"Windows (TTL={ttl_valor})"
                elif ttl_valor <= 255:
                    print(f"Roteadores/Dispositivos de Rede (TTL={ttl_valor})")
                else:
                    return f"Cisco/Network (TTL={ttl_valor})"
    except Exception:
        pass
    return "Desconhecido"


portas_abertas = []
lock_lista = __import__('threading').Lock()
os_detectado = detectar_os  

def scan_port(ip, port):
    global portas_abertas
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            result = s.connect_ex((ip, port))
        except Exception:
            return
        if result == 0:
            try:
                servico = socket.getservbyport(port)
            except OSError:
                servico = "desconhecido"
            print(f"Porta {port} aberta - {servico}")
            with lock_lista:
                portas_abertas.append((port, servico))

if __name__ == "__main__":
    alvo = input("Digite o IP ou dominio: ").strip()

    if validador(alvo):
        ip = alvo
        print(f"IP valido: {ip}")
    else:
        print("Tentando resolver como dominio...")
        ip = resolver_dominio(alvo)
        if not ip:
            print("Nao foi possivel resolver. Encerrando.")
            sys.exit()

    escolha = input("Quer resolver MAC? (S/N): ")
    if escolha.upper() == "N".upper():
        pass
    elif escolha .upper() == "S".upper():
        ip_alvo = ip
        mac = arping(ip_alvo)
    else:
        mac = "Não consultado!"

    OS = detectar_os(ip)
    print(f"OS detectado: {OS}")

    port_inicial = int(input("Porta inicial: "))
    port_final = int(input("Porta final: "))
    threads = int(input("Threads: "))

    print(f"\n### [ESCANEANDO] {ip} [PORTAS] {port_inicial}-{port_final} ###\n")
    start_time = time.perf_counter()

    with ThreadPoolExecutor(max_workers=threads) as executor:
        for port in range(port_inicial, port_final + 1):
            executor.submit(scan_port, ip, port)

    end_time = time.perf_counter()
    print(f"\n### [RESULTADO] ###")
    print(f"Alvo: {alvo} ({ip}) | OS: {OS}")
    print(f"Portas abertas: {len(portas_abertas)}")
    for porta, servico in sorted(portas_abertas):
        print(f"  {porta} - {servico}")
    print(f"Tempo: {end_time - start_time:.2f}s")
