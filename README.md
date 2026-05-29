
<img width="1280" height="720" alt="Serial experiment_ Lane" src="https://github.com/user-attachments/assets/344736bd-adbb-4015-903d-feade58015cc" />

## LOLMAP – Scanner de Domínios e Portas
LOLMAP é uma ferramenta de segurança cibernética desenvolvida inteiramente em Python, sendo minha primeira contribuição para a área. Para utilizá-la, é necessário instalar as bibliotecas dns.resolver e dns.rdatatype, manualmente ou em um ambiente virtual. A execução se dá pelo terminal com o comando python3 LOLMAP.py. Durante a execução, o usuário informa um domínio, define a quantidade de threads (atenção: números excessivos podem interromper o funcionamento) e as portas a serem verificadas. A partir daí, a ferramenta envia datagramas com TTL progressivo para o alvo, identifica o IP correspondente, estima o sistema operacional com base nos valores de TTL retornados e exibe os serviços e portas vulneráveis que se encontram abertas.
