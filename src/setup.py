import json
import time
from customtkinter import *
from pynput import mouse



global current_mouse_position
global clickcount
global config_file
global config_raw
global value_list

config_file = './config/window_config.json'
config_raw = json.load(open(config_file))
current_mouse_position = (0, 0)
clickcount = 0

def on_move(x, y):
    global current_mouse_position
    current_mouse_position = (x,y)

def on_click(x, y, button, pressed):
    global current_mouse_position
    global clickcount
    if button == mouse.Button.left:
        current_mouse_position = (x,y)
        clickcount += 1
        
listener = mouse.Listener(on_move=on_move, on_click=on_click)
listener.start()

set_appearance_mode("dark")

root = CTk()
root.geometry("600x670")
root.title("Setup tool")
root.grid_columnconfigure(0, weight=1)

def choose_coordinate(label):
    def call():
        global current_mouse_position
        global clickcount
        global listener
        clickcount = 0
        while clickcount<2:
            time.sleep(0.001)
        label.configure(text=f"[{current_mouse_position[0]}, {current_mouse_position[1]}]")
        clickcount = 0
    
    return call
            
frame = CTkFrame(
    master=root,
    width=580,
    height=650, 
    fg_color="#ECEFF4",
)
frame.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="e")
frame.pack_propagate(False)

right_label = CTkLabel(
    master=frame, 
    text='CONFIGURATION',
    fg_color='transparent',
    pady=10,
    corner_radius=20,
    text_color='#2E3440',
    font=('Roboto', 36),
    )
right_label.pack(expand=True, anchor='n')

tabview = CTkTabview(
    master=frame,
    height=450,
    width=500,
    fg_color='#D8DEE9'
    )
tabview.pack(padx=20, pady=20)
value_list = [[] for x in range(len(config_raw))]
function_list = [[] for x in range(len(config_raw))]

for window_id, window in enumerate(config_raw):
    tabview.add(str(window_id))
    for value_id, key in enumerate(config_raw[window_id].keys()):
        temp_label = CTkLabel(
            master=tabview.tab(str(window_id)),
            justify='center',
            padx=30,
            text_color='#2E3440',
            font=('Roboto',18),
            text=f"[{config_raw[window_id][key][0]}, {config_raw[window_id][key][1]}]"
            )
        value_list[window_id].append(temp_label)
    
    function_list[window_id] = [choose_coordinate(x) for x in value_list[window_id]]
    
    for value_id, key in enumerate(config_raw[window_id].keys()):
        value_list[window_id][value_id].grid(row=value_id, column=1, padx=5, pady=5)
        CTkButton(
            master=tabview.tab(str(window_id)),
            text=key,
            command=function_list[window_id][value_id],
            width=250,
            compound='left',
            fg_color='#2E3440',
            text_color='#ECEFF4',
            font=('Roboto',16),
            ).grid(row=value_id, column=0, padx=5, pady=5)

def parse_string_to_list(value):
    value = value[1: -1]
    value = [int(v) for v in value.split(', ')]
    return (value[0], value[1])

def save_config():
    global config_raw
    global value_list
    global config_file
    
    for window_id, window in enumerate(config_raw):
        for value_id, key in enumerate(config_raw[window_id].keys()):
            config_raw[window_id][key] = parse_string_to_list(value_list[window_id][value_id].cget("text"))
    
    with open(config_file, 'w') as f:
        json.dump(config_raw, f)
    

save_new_config_btn = CTkButton(
    master=frame,
    text='Save new config',
    width=200,
    height=50,
    font=('Roboto', 18),
    fg_color='#2E3440',
    text_color='#ECEFF4',
    command=save_config,
    corner_radius=5,
)

save_new_config_btn.pack(anchor='n')

empty_frame = CTkFrame(
    master=frame,
    fg_color='transparent',
    height=20
)

empty_frame.pack()

root.mainloop()
listener.stop()