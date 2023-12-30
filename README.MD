
#  ChatGPT Data Crawling Tool

This project constitutes a tool for extracting ChatGPT data through an automated clicker approach.

## Table of Contents

- [About](#about)
- [Key Features](#key-features)
- [Why Use This Tool?](#why-use-this-tool)
- [Approach Explanation](#approach-explanation)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
    - [data_loader_config.json](#data_loader_config.json)
    - [clicker_config.json](#clicker_config.json)
    - [window_config.json](#window_config.json)
    - [Setup video](#setup-video)
- [Usage](#usage)

    

## About
The ChatGPT Data Crawling Tool is a utility designed to automate the process of gathering data from the OpenAI ChatGPT web application using an automated clicker. It simplifies the task of interacting with the ChatGPT interface and collecting conversations for research, analysis, or any other purpose.

## Key Features

- **Automated Clicker:** The tool leverages an automated clicker to simulate user interactions with the ChatGPT interface, making it efficient to collect large datasets.

- **Configurable Settings:** Users can customize various settings such as conversation length, interaction frequency, and more to tailor the data collection process to their specific needs.

- **Data Export:** Collected conversations can be easily exported in common formats (e.g., CSV, JSON), facilitating seamless integration with downstream analysis tools.

## Why Use This Tool?

- **Research:** Ideal for researchers and data scientists looking to gather conversational data from ChatGPT for studies and experiments.

- **Training Data:** Useful for obtaining diverse training data for training and fine-tuning natural language processing models.

- **Customization:** Offers flexibility with configurable settings, allowing users to adapt the tool to different use cases and scenarios.

## Approach Explanation

Navigating the landscape of alternative approaches, such as employing Selenium, presents challenges encompassing encounters with CAPTCHA systems, firewalls, and associated complexities. Furthermore, even if one successfully circumvents these obstacles, the sustainability of the methodology in the face of future updates remains uncertain. In contrast, the utilization of a web interface for automation affords a more streamlined approach, requiring minimal adjustments for seamless adaptation to subsequent updates.

## Getting Started

### Prerequisites

Before you begin, ensure that your environment meets the following prerequisites:

- **Python:** The project requires Python to be installed on your system. We recommend using Python 3.8 or later.
- **Pip**: The project uses Pip, the Python package installer, to manage dependencies.

### Installation

Follow these steps to set up the ChatGPT Data Crawling Tool on your system:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/hungluu6453/ChatGPT-Data-Crawling.git
   cd ChatGPT-Data-Crawling
2. **Install Dependencies**
    ```bash
    pip install -r requirements.txt

## Project Structure

The project is organized in a structured manner to enhance clarity and maintainability. Below is an overview of the main directories and files within the repository:

- **`/src`**: This directory houses the source code of the ChatGPT Data Crawling Tool.

  - **`data_loader.py`**: A GUI for loading and saving data.
  - **`clicker.py`**: An automated clicker.
  - **`setup.py`**: A GUI for setting up automated coordinate.
  - **`/config`**: A subdirectory containing config files.
  - **`/input`**: A subdirectory containing input csv files.
  - **`/prompt`**: A subdirectory containing prompt templates
  - **`/result`**: A subdirectory containing output csv files

- **`requirements.txt`**: Lists all the dependencies required for the project. Install these dependencies using `pip install -r requirements.txt`.

- **`.gitignore`**: Specifies files and directories that should be ignored by version control.

- **`/tutorial video`**: This directory contains a video showing setup process.

## Configuration

### data_loader_config.json

The `data_loader_config.json` file contains various parameters that allow users to customize input data, prompting template and output file path:

| Parameter            | Description                                                 |  
|----------------------|-------------------------------------------------------------|
| `INPUT_PATH`         | The path for input csv file.        |
| `PROMPT_PATH`        | The path for prompting template.|
| `RESULT_PATH`        | The path to save generated results.        |

### clicker_config.json

The `clicker_config.json` file contains parameters that allow users to customize automated procedures:

| Parameter            | Description                                                 |  Example |
|----------------------|-------------------------------------------------------------|----------|
| `REQUEST_WAITING_INTERVAL`| How long should we wait for ChatGPT to generate te response in seconds. This value should be adjust to the length of the output for each usage.         | 15 |
| `SLEEP_TIME`        | After waiting for `REQUEST_WAITING_INTERVAL`, the system will sleep for `SLEEP_TIME` and retry for `ERROR_LIMIT` times| 5 |
| `ERROR_LIMIT` | The number of retries | 3 |

### window_config.json

In our experiment, we use 3 ChatGPT accounts for crawling process. Therefore, the `clicker_config.json` contains a list of configuration for each ChatGPT window. Specify the coordinates for each parameters can be done using `setup.py` file, which opens a GUI that make select the coordinates easier. As this is the main process when apply the Automation Tool for a new system, we will provide detailed descriptions for each coordinate, and also a video for the setup process.

| Parameter            | Description                                                 |  
|----------------------|-------------------------------------------------------------|
| `COPY_COOR`         | This is the coordinate of the 'Copy Data' button in data_loader GUI.       |
| `PASTE_COOR`        | This is the coordinate of the 'Paste Result' button in data_loader GUI. |
| `CHATBOX_COOR`        | This is the coordinate of the chatbox in ChatGPT window.        |
|  `SUBMIT_COOR` | This is the coordinate of the submit button in ChatGPT window. |
| `SUBMIT_COOR`| This is the coordinate of the submit button in ChatGPT window. |
| `SCROLL_COOR`| As ChatGPT sometimes dont scroll to the bottom when generating results, which we cannot copy the output, this is the coordinate of the scroll down button in ChatGPT window.|
| `GET_COOR`| This is the coordinate of the copy button in ChatGPT window. |
| `SUB_GET_COOR`| As ChatGPT sometimes will generate more than 1 results, therefore we need another coordinate for the copy button in ChatGPT window. |
| `CLOSE_REVIEW_COOR`| This is the coordinate for closing review popups of ChatGPT. |
| `NEW_CHAT_COOR`| This is the coordinate to open new chat window, which helps reduce the execution time of each response after a period of using 1 window. |

### Setup Video 
To see the tutorial, please go to `./tutorial_video/config_tutorial.mp4`

## Usage
In order use the tool, please follow these steps: 
1. Add data to `\input` folder
2. Add prompt to `prompt` folder
3. Config `\src\config\data_loader_config.json` file
4. cd to `\src` folder
5. Run `data_loader.py`
6. Run `setup.py` in a different terminal
7. Follow the tutorial in [Setup video](#setup-video), apply for all 3 window, then save new config and close the setup GUI.
8. Config `src\config\clicker_config.json` file
9. Run `clicker.py`
    