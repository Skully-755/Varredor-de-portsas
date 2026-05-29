
<img width="694" height="358" alt="Captura_de_tela_de_2026-05-29_15-37-333" src="https://github.com/user-attachments/assets/72b33dfa-4797-476b-9b28-eb2c00ecfabd" />


## LOLMAP – Scanner de Domínios e Portas
LOLMAP é uma ferramenta de segurança cibernética desenvolvida inteiramente em Python, sendo minha primeira contribuição para a área. Para utilizá-la, é necessário instalar as bibliotecas dns.resolver e dns.rdatatype, manualmente ou em um ambiente virtual. A execução se dá pelo terminal com o comando python3 LOLMAP.py. Durante a execução, o usuário informa um domínio, define a quantidade de threads (atenção: números excessivos podem interromper o funcionamento) e as portas a serem verificadas. A partir daí, a ferramenta envia datagramas com TTL progressivo para o alvo, identifica o IP correspondente, estima o sistema operacional com base nos valores de TTL retornados e exibe os serviços e portas vulneráveis que se encontram abertas.
