import tkinter
import hashlib
from tkinter import DISABLED, NORMAL, filedialog
import requests

g_filepath = "";

def file_Hash(filepath):
    algoritm = "MD5"
    hash_func = hashlib.new(algoritm)
    
    with open(filepath, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def main():
    virus_hash_list_url = "https://virusshare.com/hashfiles/VirusShare_00000.md5"
    virus_hash_list = requests.get(virus_hash_list_url)
    virus_hash_list = virus_hash_list.content.decode()
    virus_hash_list= virus_hash_list[virus_hash_list.rindex("#") + 2:]
    
    global g_filepath
    file_hush = file_Hash(g_filepath)

    if virus_hash_list.find(file_hush) != -1:
        label_result_string.set("Be careful! This file is a virus!")
    else:
        label_result_string.set("No viruses found")

def file_search():
    global g_filepath;
    g_filepath = tkinter.filedialog.askopenfilename(initialdir = "/",
											  title = "Select a File",
											  filetypes = (("all files",
															"*.*"),
															("Text files",
															"*.txt*")))

    label_file_name.set("The file choosen is: " + g_filepath)
    label_result_string.set("Is this the correct file name?")
    start_checking_button["state"] = NORMAL
    start_checking_button.configure(background="gold")



root = tkinter.Tk()
root.geometry("500x250")
root.winfo_height = 100
root.configure(background="#C8E9F2")
label_file_name = tkinter.StringVar()
label_for_file_name = tkinter.Label(root, textvariable=label_file_name)
label_for_file_name.configure(background="#C8E9F2")
label_for_file_name.configure(font=("Arial", 14))
label_for_file_name.pack()

label_result_string = tkinter.StringVar()
label_result = tkinter.Label(root, textvariable=label_result_string)
label_result.configure(background="#C8E9F2")
label_result.configure(font=("Arial", 14))
label_result.pack()

choose_file_button = tkinter.Button(root,
						            text = "Choose file",
						            command=file_search,
                                    anchor="center",
                                    bd=3,
                                    cursor="hand2",
                                    disabledforeground="gray",
                                    font=("Arial", 14),
                                    height=2,
                                    justify="center",
                                    padx=10,
                                    pady=5,
                                    width=15,
                                    wraplength=100,
                                    background="gold")
choose_file_button.pack()

start_checking_button = tkinter.Button(root,
						               text = "Yes! Check it",
						               command=main,
                                       anchor="center",
                                       bd=3,
                                       cursor="hand2",
                                       disabledforeground="gray",
                                       font=("Arial", 14),
                                       height=2,
                                       justify="center",
                                       padx=10,
                                       pady=5,
                                       width=15,
                                       wraplength=100,
                                       background="light grey")
start_checking_button.pack()
start_checking_button["state"] = DISABLED

root.mainloop()
