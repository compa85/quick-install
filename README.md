# QuickInstall

**QuickInstall** is a Python-based automation tool that simplifies the setup of a new Windows PC by installing essential software via [Chocolatey](https://chocolatey.org/).

## ⚙️ Features

- Installs a predefined list of common software (browsers, utilities, productivity tools, etc.)
- Automatically installs Chocolatey if not already present
- Simple interface, ideal for IT technicians or users setting up multiple machines
- Requires minimal user interaction

## 🚀 Requirements

- **Windows**
- **Python 3.x**
- Must be **run as Administrator**

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/compa85/quick-install.git
   cd quick-install
   ```
2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script as **Administrator**: Right-click on your terminal (e.g., Command Prompt or PowerShell) and choose "Run as administrator", then run:
   ```bash
   python3 quick-install.py
   ```

## ✏️ Customization

You can easily customize the list of software to install by modifying the software_list inside the `quick-install.py` file:

```python
software_list = [
    {"name": "Google Chrome", "package": "googlechrome"},
    {"name": "7-Zip",         "package": "7zip"},
    {"name": "Adobe Reader",  "package": "adobereader"},
    # Add or remove packages as needed
]
```

- `"name"` is for display purposes.
- `"package"` must match the exact Chocolatey package ID.

## 🛠️ Build the Executable (Optional)

To convert the script into a standalone `.exe` file (useful for easier execution on other machines), follow these steps:

### 1. Install PyInstaller

If not already installed, run:

```bash
pip install pyinstaller
```

### 2. Generate the Executable

From the project folder, run:

```bash
pyinstaller --onefile --uac-admin --icon icon.ico quick-install.py
```

### 3. Run as Administrator

To ensure the .exe has administrator privileges:

- right-click on quick-install.exe and select "**Run as administrator**"
