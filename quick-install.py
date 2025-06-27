"""
===============================================================================
 Quick Install
===============================================================================

 Author      : Davide Compagnoni
 Version     : 1.0.1
 Date        : 2025-05-10
 Description : A Chocolatey-based tool to install essential Windows software in just a few clicks.

 Features:
   - Checks if Chocolatey is installed; installs it if missing
   - Interactive menu to select which programs to install
   - Automatically installs selected programs via Chocolatey

 Resources:
   - GitHub repository: https://github.com/compa85/quick-install.git
   - Chocolatey official website: https://chocolatey.org

===============================================================================
"""


import os
import sys
import ctypes
import questionary


# Definizione dei programmi disponibili per l'installazione
software_list = [
    {"name": "Google Chrome",               "package": "googlechrome"},
    {"name": "Google Drive",                "package": "googledrive"},
    {"name": "7-Zip",                       "package": "7zip"},
    {"name": "Adobe Reader",                "package": "adobereader"},
    {"name": "LibreOffice",                 "package": "libreoffice-fresh"},
    {"name": "Java Runtime",                "package": "javaruntime"},
    {"name": "TeamViewer QuickSupport",     "package": "teamviewer-qs"},
    {"name": "FortiClient VPN",             "package": "forticlientvpn"},
]


# Funzione per installare Chocolatey
def install_chocolatey():
    powershell_command = (
        "Set-ExecutionPolicy Bypass -Scope Process -Force; "
        "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; "
        "iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    )
    os.system(f"powershell -NoProfile -ExecutionPolicy Bypass -Command {powershell_command}")


# Funzione per controllare se lo script è in esecuzione come amministratore
def is_running_as_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
    

# funzione per stampare il banner
def print_banner():
    banner = r"""
      ____  __  _____________ __  _____  _______________   __   __ 
     / __ \/ / / /  _/ ___/ //_/ /  _/ |/ / __/_  __/ _ | / /  / / 
    / /_/ / /_/ // // /__/ ,<   _/ //    /\ \  / / / __ |/ /__/ /__
    \___\_\____/___/\___/_/|_| /___/_/|_/___/ /_/ /_/ |_/____/____/
                                                                                                   
    Version 1.0.1
    by Davide Compagnoni
    
    
    """
    print(banner)


# Funzione principale
def main():
    print_banner()
    
    if not is_running_as_admin():
        print("⚠️ Il programma deve essere eseguito come amministratore.\n")
        input("Premi INVIO per uscire...")
        sys.exit(1)
    
    # Controllare se Chocolatey è installato
    isInstalled = os.system("choco -v >nul 2>&1") == 0
    if not isInstalled:
        print("Installazione di Chocolatey...")
        install_chocolatey()
        print("Chocolatey installato con successo.\n")
        print("🔁 Riavviare il programma per continuare l'installazione.\n")
        input("Premi INVIO per uscire...")
        sys.exit(0)

    # Mostrare il menu
    selected_packages = questionary.checkbox(
        "Seleziona i programmi da installare:",
        choices=[package["name"] for package in software_list]
    ).ask()

    # Installare i pacchetti selezionati
    if selected_packages:
        for package in selected_packages:
            software_package = next((p["package"] for p in software_list if p["name"] == package), None)
            if software_package:
                print(f"Installazione di {package}...")
                os.system(f"choco install {software_package} -y")
        print("Installazione completata.\n")
    else:
        print("Nessun programma selezionato.")
    
    input("Premi INVIO per uscire...")
        
        
if __name__ == "__main__":
    main()