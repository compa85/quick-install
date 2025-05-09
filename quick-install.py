import os
import sys
import ctypes
import questionary


# Definizione dei programmi disponibili per l'installazione
software_list = [
    {"name": "Google Chrome",   "package": "googlechrome"},
    {"name": "Google Drive",    "package": "googledrive"},
    {"name": "7-Zip",           "package": "7zip"},
    {"name": "Adobe Reader",    "package": "adobereader"},
    {"name": "LibreOffice",     "package": "libreoffice-fresh"},
    {"name": "Java Runtime",    "package": "javaruntime"},
    {"name": "FortiClient VPN", "package": "forticlientvpn"},
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


# Funzione principale
def main():
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
    else:
        print("Nessun programma selezionato.")
        
        
if __name__ == "__main__":
    main()