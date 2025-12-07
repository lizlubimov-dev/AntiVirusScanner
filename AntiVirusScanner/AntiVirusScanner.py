from encodings import undefined
import requests
import tkinter
from tkinter import DISABLED, NORMAL, filedialog

def main():
    url = "https://www.virustotal.com/vtapi/v2/file/scan"
    
    params = {"apikey": "5f889b7566fb64af84c36cf53c01897e00952a9b7805aec049f9b4b72a15c27d"}

    files = {"file": ("Petra.jpg", open("C:\Liz\Petra.jpg", "rb"))}

    response = requests.post(url, files=files, params=params).json()
    print(response)

    scan_id = response["scan_id"]

    response_code = int(response["response_code"])

    if response_code != 1:
        label_result_string.set("Oops! Something has gone wrong!")
        return

    response_code = 0

    while(response_code != 1):
        reporturl = "https://www.virustotal.com/vtapi/v2/file/report?resource=" + scan_id

        no_content_in_response = 204
        response = requests.get(reporturl, params=params)
        if response.status_code != no_content_in_response:
            response = response.json()
            response_code = response["response_code"]

    result = response["positives"]
    
    virus_list = []

    
    if result == 0:
        label_result_string.set("No viruses found")
    else:
        for scan in response["scans"]:
            if response["scans"][scan]["detected"] == True:
                virus_list.append(response["scans"][scan]["result"])
        result_string = str(result) + " viruses found, please be careful! \r\n List of viruses found:"
        for virus in virus_list:
            result_string = result_string + "\r\n " + virus
        
        label_result_string.set(result_string)
    print()
    

def file_search():
    filename = tkinter.filedialog.askopenfilename(initialdir = "/",
											  title = "Select a File",
											  filetypes = (("all files",
															"*.*"),
															("Text files",
															"*.txt*")))

    label_file_name.set("The file choosen is: " + filename)
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