import time
import json
import pandas as pd
import pyautogui
import pyperclip
import logging



logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%b-%y %H:%M:%S',
    # filename='logs/clicker.log',
    # filemode='w',
)

# Variable to get coordinate or run
global reload_count
global CLICKER_CONFIG

config_index = 0
reload_count = 0

WINDOW_CONFIG = json.load(open('./config/window_config.json'))
CLICKER_CONFIG = json.load(open('./config/clicker_config.json'))


########################################################################
# Utilities Function
########################################################################
def get_screen_info():
    pyautogui.mouseInfo()

def move_to(coor, duration=0.05):
    pyautogui.moveTo(coor[0], coor[1], duration=duration)

def click(coor, clicks=1, interval=0):
    pyautogui.click(coor[0], coor[1], clicks=clicks, interval=interval)

def scroll_up(pixel):
    pyautogui.scroll(pixel)
    
def scroll_down(pixel):
    pyautogui.scroll(-pixel)
    
def paste():
    pyautogui.hotkey("ctrlleft", "v")
    
def refresh_page():
    pyautogui.press('f5')

########################################################################
# Run Function
########################################################################
def run(config_dict):
    global reload_count
    global CLICKER_CONFIG
    
    current_input = ""
    error_counter = 0

    # Get new input
    click(config_dict["COPY_COOR"], clicks=3, interval=0.5)
    logging.info("Got Input")
    current_input = pyperclip.paste()
    
    # Check long conversation
    if (len(current_input.split()))> 3000:
        pyperclip.copy('Error - Long Conversation')
        click(config_dict["PASTE_COOR"])
        logging.info("Long Context Error")
        return True
    
    # Click to chatbox coordinate
    click(config_dict["CHATBOX_COOR"], clicks=2, interval=0.1)
    
    # Paste input into the chatbox
    paste()
    logging.info("Pasted Input")
    
    # Click on submit button
    click(config_dict["SUBMIT_COOR"])
    logging.info("Submitted Input")
    
    # Wait for response
    time.sleep(CLICKER_CONFIG["REQUEST_WAITING_INTERVAL"])
    
    # Wait for response to complete
    while True:
        
        # Scroll to the bottom
        click(config_dict["SCROLL_COOR"])
        scroll_down(1000)
        time.sleep(0.2)
        
        # Copy Result
        click(config_dict["GET_COOR"] , clicks=2, interval=0.1)
        logging.info("Copied Result")
        
        cur_content = pyperclip.paste()
        
        # Success at first try scenario
        if cur_content != current_input:
            click(config_dict["PASTE_COOR"])
            logging.info("====> Success")
            error_counter=0
            return True
        
        # Failed at first try scenario
        else:
            # Try sub button
            click(config_dict["SUB_GET_COOR"] , clicks=2, interval=0.1)
            cur_content = pyperclip.paste()
            # Success when trying sub button
            if cur_content != current_input:
                click(config_dict["PASTE_COOR"])
                logging.info("====> Success")
                error_counter=0
                return True
            # Generation has not finished or having review popup
            else:
                
                # Try closing popup
                click(config_dict["CLOSE_REVIEW_COOR"])
                error_counter+=1
            
                # Start new chat if reach error limit
                if error_counter==CLICKER_CONFIG["ERROR_LIMIT"]:
                    if reload_count == 1:
                        reload_count = 0
                        return False
                    reload_count+=1
                    error_counter=0
                    click(config_dict["NEW_CHAT_COOR"] , clicks=2, interval=0.1)
                    return True
                    
                # Retry
                else:
                    logging.info(f"Waiting, sleep for {CLICKER_CONFIG['SLEEP_TIME']}s")
                    time.sleep(CLICKER_CONFIG['SLEEP_TIME'])
                    continue

if __name__ == "__main__":
    while True:
        config_dict = WINDOW_CONFIG[config_index]
        if not run(config_dict):
            time.sleep(3)
            config_index = (config_index+1) % len(WINDOW_CONFIG)
            click(WINDOW_CONFIG[config_index]['NEW_CHAT_COOR'], clicks=2)
            refresh_page()
            time.sleep(1)
            refresh_page()
            time.sleep(3)
            click(WINDOW_CONFIG[config_index]["NEW_CHAT_COOR"] , clicks=2, interval=0.1)
        time.sleep(0.5)