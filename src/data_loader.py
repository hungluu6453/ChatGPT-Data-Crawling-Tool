import json
import pandas as pd
import logging
from datetime import datetime
from customtkinter import *

set_appearance_mode("dark")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    # filename='logs/clicker.log',
    # filemode='w',
)

global data
global start_index
global cur_index
global end_index

config = json.load(open("./config/data_loader_config.json"))

prompt = open(config['PROMPT_PATH'], "r", encoding='utf8').read()
data = pd.read_csv(config['INPUT_PATH'])
input_field = data.columns

start_index = 0
cur_index = start_index
end_index = data.index[-1]

root = CTk()
root.geometry("200x100+650+0")
root.title("Data Automation Tool")


def copy_input():
    global data
    global cur_index
    text = prompt.format(**data.loc[cur_index])
    root.clipboard_clear()
    root.clipboard_append(text)


def paste_result():
    global data
    global cur_index
    global end_index
    
    data.loc[cur_index, ['result']] = [root.clipboard_get()]
    logging.info(f"Finished Index: {cur_index}/{end_index} at {datetime.now()}")
    data.to_csv(config['RESULT_PATH'], index=False)
    if cur_index == end_index:
        logging.info(f"-----------Finished at {datetime.now()}-------------")
        root.destroy()
        
    cur_index +=1


copy_run_button = CTkButton(
    master=root,
    text ="Copy Data",
    command=copy_input,
    width=200,
    height=50,
    font=("Roboto", 18),
    corner_radius=5,
    fg_color='#2E3440',
    text_color='#ECEFF4',
    )

paste_button = CTkButton(
    master=root,
    text ="Paste Result",
    command=paste_result,
    width=200,
    height=50,
    font=("Roboto", 18),
    corner_radius=5,
    fg_color='#2E3440',
    text_color='#ECEFF4',
    )

copy_run_button.pack()
paste_button.pack()
root.mainloop()

