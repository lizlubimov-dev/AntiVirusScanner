import tkinter
from tkinter import DISABLED, NORMAL, filedialog
import yara

g_filepath = ""

def main():
    rules = yara.compile(filepaths={
                                   "namespace1": "C:\\LizProjects\\PhytonLearning\\Yara_Rules_Set\\EK_Angler.yar",
                                   "namespace2": "C:\\LizProjects\\PhytonLearning\\Yara_Rules_Set\\EK_Blackhole.yar",
                                   "namespace3": "C:\\LizProjects\\PhytonLearning\\Yara_Rules_Set\\EK_BleedingLife.yar",
                                   "namespace4": "C:\\LizProjects\\PhytonLearning\\Yara_Rules_Set\\EK_Crimepack.yar",
                                   "namespace5": "C:\\LizProjects\\PhytonLearning\\Yara_Rules_Set\\EK_Eleonore.yar"
                                   })

    matches = rules.match(g_filepath)

    if len(matches) == 0:
        label_result_string.set("No viruses found")
    else:
        result_string = "Be careful! A virus detected! \r\n matches list: \r\n"
        for match in matches:
            result_string = result_string + match + "\r\n"
        label_result_string.set(result_string)


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
