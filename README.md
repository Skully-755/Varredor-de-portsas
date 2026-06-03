![demonstração da ferramenta](img/file_000000007490720ebcc5088761516350.png)

## LOLMAP – Scanner de Domínios e Portas
LOLMAP é uma ferramenta de segurança cibernética desenvolvida inteiramente em Python, sendo minha primeira contribuição para a área. Para utilizá-la, é necessário instalar as bibliotecas dns.resolver, dns.rdatatype e scapy, manualmente ou em um ambiente virtual. A execução se dá pelo terminal com o comando python3 LOLMAP.py. Durante a execução, o usuário informa um domínio, define a quantidade de threads (atenção: números excessivos podem interromper o funcionamento) e as portas a serem verificadas. A partir daí, a ferramenta envia datagramas com TTL progressivo para o alvo, identifica o IP correspondente, estima o sistema operacional com base nos valores de TTL retornados, realiza um ARP scan para obter exclusivamente o endereço MAC do servidor e, por fim, exibe os serviços e portas vulneráveis que se encontram abertas.

## Instalação
1. Clone este repositório.
2. Crie um ambiente virtual: `python3 -m venv venv && source venv/bin/activate`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute: `python3 LOLMAP.py`

## Aviso Legal

Esta ferramenta foi desenvolvida exclusivamente para fins educacionais e de pesquisa em segurança cibernética, com o objetivo de auxiliar profissionais e estudantes a compreenderem técnicas de varredura de rede.

O autor não se responsabiliza pelo uso indevido desta ferramenta. É estritamente proibido utilizá-la contra sistemas sem a autorização prévia e por escrito do proprietário. O usuário é o único responsável por quaisquer consequências legais decorrentes do uso indevido.

