import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import index

def openfileEnc():
    filename = filedialog.askopenfilename(initialdir="D:/", title="Select file",
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    fileToEncrptyEntryUpdate(filename)

def opendirectoryEnc():
    directory = filedialog.askdirectory(initialdir="D:/", title="Select directory")
    destinationFolderEncEntryUpdate(directory)

def openfileDec():
    filename = filedialog.askopenfilename(initialdir="D:/", title="Select file",
                                          filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    fileToDecryptEntryUpdate(filename)

def opendirectoryDec():
    directory = filedialog.askdirectory(initialdir="D:/", title="Select directory")
    destinationFolderDecEntryUpdate(directory)

def sendfilepage():
    webbrowser.open_new(r"http://127.0.0.1:5000/upload-file")

def recievefilepage():
    webbrowser.open_new(r"http://127.0.0.1:5000/file-directory")

def opengithub(event):
    webbrowser.open_new(r"https://github.com/Paras-Verma-2531/CipherConnect")

def fileToEncrptyEntryUpdate(filename):
    inputEncFileEntry.delete(0, tk.END)
    inputEncFileEntry.insert(0, filename)

def destinationFolderEncEntryUpdate(directory):
    inputEncDirEntry.delete(0, tk.END)
    inputEncDirEntry.insert(0, directory)

def fileToDecryptEntryUpdate(filename):
    outputDecFileEntry.delete(0, tk.END)
    outputDecFileEntry.insert(0, filename)

def destinationFolderDecEntryUpdate(directory):
    outputDecDirEntry.delete(0, tk.END)
    outputDecDirEntry.insert(0, directory)

def encryptor():
    EncryptBTN.config(state="disabled")
    public_key = publicKeyOfRecieverEntry.get()
    private_key = privateKeyOfSenderEntry.get()
    directory = inputEncDirEntry.get()
    filename = inputEncFileEntry.get()
    index.encrypt(filename, directory, public_key, private_key)

def decryptor():
    DecryptBTN.config(state="disabled")
    public_key = publicKeyOfSenderEntry.get()
    private_key = privateKeyOfRecieverEntry.get()
    directory = outputDecDirEntry.get()
    filename = outputDecFileEntry.get()
    index.decrypt(filename, directory, public_key, private_key)

def main():
    global form
    form = tk.Tk()
    form.wm_title('CipherConnect')

    style = ttk.Style()
    style.theme_use('clam')  # You can choose different themes here
    style.configure('Bold.TLabel', font=('Arial', 10, 'bold'))
    style.configure('Highlight.TButton', foreground='white', background='#4CAF50', font=('Arial', 10, 'bold'))

    EncryptStep = ttk.LabelFrame(form, text=" 1. File Encryption: ")
    EncryptStep.grid(row=0, columnspan=7, sticky='W', padx=10, pady=10, ipadx=5, ipady=5)

    DecryptStep = ttk.LabelFrame(form, text=" 2. File Decryption: ")
    DecryptStep.grid(row=2, columnspan=7, sticky='W', padx=10, pady=10, ipadx=5, ipady=5)

    Aboutus = ttk.LabelFrame(form, text=" About ")
    Aboutus.grid(row=0, column=9, columnspan=2, rowspan=8, sticky='NS', padx=10, pady=10)

    menu = tk.Menu(form)
    form.config(menu=menu)

    menufile = tk.Menu(menu)
    menufile.add_command(label='Send file', command=lambda: sendfilepage())
    menufile.add_command(label='Recieve file', command=lambda: recievefilepage())
    menufile.add_command(label='Exit', command=lambda: exit())
    menu.add_cascade(label='Menu', menu=menufile)

    global inputEncFileEntry
    global inputEncDirEntry
    global publicKeyOfRecieverEntry
    global privateKeyOfSenderEntry
    global EncryptBTN

    inputEncFile = ttk.Label(EncryptStep, text="Select the File:", style='Bold.TLabel')
    inputEncFile.grid(row=0, column=0, padx=5, pady=5, sticky='W')

    inputEncFileEntry = ttk.Entry(EncryptStep)
    inputEncFileEntry.grid(row=0, column=1, columnspan=7, padx=5, pady=5, sticky="WE")

    inputEncBtn = ttk.Button(EncryptStep, text="Browse ...", command=openfileEnc, style='Highlight.TButton')
    inputEncBtn.grid(row=0, column=8, padx=5, pady=5, sticky='W')

    inputEncDir = ttk.Label(EncryptStep, text="Save File to:", style='Bold.TLabel')
    inputEncDir.grid(row=1, column=0, padx=5, pady=5, sticky='W')

    inputEncDirEntry = ttk.Entry(EncryptStep)
    inputEncDirEntry.grid(row=1, column=1, columnspan=7, padx=5, pady=5, sticky="WE")

    inputEncDirBtn = ttk.Button(EncryptStep, text="Browse ...", command=opendirectoryEnc, style='Highlight.TButton')
    inputEncDirBtn.grid(row=1, column=8, padx=5, pady=5, sticky='W')

    publicKeyOfReciever = ttk.Label(EncryptStep, text="Public-Key of reciever:", style='Bold.TLabel')
    publicKeyOfReciever.grid(row=2, column=0, padx=5, pady=5, sticky='W')

    publicKeyOfRecieverEntry = ttk.Entry(EncryptStep)
    publicKeyOfRecieverEntry.grid(row=2, column=1, padx=5, pady=5, sticky='WE')

    privateKeyOfSender = ttk.Label(EncryptStep, text="Private-Key of sender:", style='Bold.TLabel')
    privateKeyOfSender.grid(row=2, column=5, padx=5, pady=5, sticky='W')

    privateKeyOfSenderEntry = ttk.Entry(EncryptStep)
    privateKeyOfSenderEntry.grid(row=2, column=7, padx=5, pady=5, sticky='WE')

    EncryptBTN = ttk.Button(EncryptStep, text="Encrypt", command=encryptor, style='Highlight.TButton')
    EncryptBTN.grid(row=2, column=8, padx=5, pady=5, sticky='W')

    global outputDecFileEntry
    global outputDecDirEntry
    global publicKeyOfSenderEntry
    global privateKeyOfRecieverEntry
    global DecryptBTN

    outputDecFile = ttk.Label(DecryptStep, text="Select the File:", style='Bold.TLabel')
    outputDecFile.grid(row=0, column=0, padx=5, pady=5, sticky='W')

    outputDecFileEntry = ttk.Entry(DecryptStep)
    outputDecFileEntry.grid(row=0, column=1, columnspan=7, padx=5, pady=5, sticky="WE")

    outputDecBtn = ttk.Button(DecryptStep, text="Browse ...", command=openfileDec, style='Highlight.TButton')
    outputDecBtn.grid(row=0, column=8, padx=5, pady=5, sticky='W')

    outputDecDir = ttk.Label(DecryptStep, text="Save File to:", style='Bold.TLabel')
    outputDecDir.grid(row=1, column=0, padx=5, pady=5, sticky='W')

    outputDecDirEntry = ttk.Entry(DecryptStep)
    outputDecDirEntry.grid(row=1, column=1, columnspan=7, padx=5, pady=5, sticky="WE")

    outputDecDirBtn = ttk.Button(DecryptStep, text="Browse ...", command=opendirectoryDec, style='Highlight.TButton')
    outputDecDirBtn.grid(row=1, column=8, padx=5, pady=5, sticky='W')

    publicKeyOfSender = ttk.Label(DecryptStep, text="Public-Key of sender:", style='Bold.TLabel')
    publicKeyOfSender.grid(row=2, column=0, padx=5, pady=5, sticky='W')

    publicKeyOfSenderEntry = ttk.Entry(DecryptStep)
    publicKeyOfSenderEntry.grid(row=2, column=1, padx=5, pady=5, sticky='WE')

    privateKeyOfReciever = ttk.Label(DecryptStep, text="Private-Key of reciever:", style='Bold.TLabel')
    privateKeyOfReciever.grid(row=2, column=5, padx=5, pady=5, sticky='W')

    privateKeyOfRecieverEntry = ttk.Entry(DecryptStep)
    privateKeyOfRecieverEntry.grid(row=2, column=7, padx=5, pady=5, sticky='WE')

    DecryptBTN = ttk.Button(DecryptStep, text="Decrypt", command=decryptor, style='Highlight.TButton')
    DecryptBTN.grid(row=2, column=8, padx=5, pady=5, sticky='W')

    intro = ttk.Label(Aboutus, text="\nCipherConnect - A Fortified Data Exchange System", style='Bold.TLabel')
    intro.grid(row=0)

    text1 = ttk.Label(Aboutus, text="\nCipherConnect enables its users to securely\ntransfer files in 'txt' format without\n"
                                "any third party eavesdropping\n")
    text1.grid(row=1)

    githublink = ttk.Label(Aboutus, text="Know More", foreground="blue", cursor="hand2")
    githublink.bind("<Button-1>", opengithub)
    githublink.grid(row=2)

    padding = ttk.Label(Aboutus, text="\n\n\n\n")
    padding.grid(row=3)

    form.mainloop()

if __name__ == "__main__":
    main()