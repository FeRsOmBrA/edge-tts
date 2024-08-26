# Text-to-Speech App with Edge TTS

This application provides a simple and user-friendly interface for converting text to speech using Microsoft Edge's TTS engine. It offers a variety of voices and languages to choose from, making it a versatile tool for various purposes.

## Features

* **Multiple Voices:** Choose from a wide selection of voices, each with its unique characteristics.
* **Language Support:** Supports various languages, including English, French, Spanish, German, and more.
* **Hotkey Support:** Trigger the text-to-speech functionality with a customizable hotkey (Ctrl+Alt+S by default).
* **User-Friendly Interface:** A clean and intuitive interface makes it easy to use for users of all levels.
* **Customizable Theme:** Choose between light and dark themes to personalize your experience.

## Requirements

* **Python 3.7 or higher:** You can download the latest version from [https://www.python.org/downloads/](https://www.python.org/downloads/).
* **Required Packages:** Install the necessary packages by running `pip install -r requirements.txt`.

## Installation

1. Clone this repository: `git clone https://github.com/your-username/your-repository-name.git`
2. Navigate to the project directory: `cd your-repository-name`
3. Install the required packages: `pip install -r requirements.txt`

## Usage

1. Run the application: `python tts_app.py`
2. Select your desired language and voice from the dropdown menus.
3. Enter the text you want to convert to speech in the text box.
4. Click the "🔊" button or press Ctrl+Alt+S to start the speech synthesis.

## Generating the Voices File

The `voices_file_generator.py` script fetches the available voices from the Edge TTS engine and saves them to a CSV file (`output.csv`). This file is used by the main application to populate the voice selection dropdown.

To regenerate the voices file, run the following command:

```bash
python voices_file_generator.py
```


<hr>  
By:
<div align="center">
    <img src="https://i.ibb.co/DVCbGKp/1694197931620-e-1700697600-v-beta-t-V9i-TOhf-Pk-Vf-Bh4-QQxt-QPBVvs-Uyi-c-Emms-Qlh9d-C8p-UA.jpg" alt="hero" style="width: 200px; height: auto; border-radius: 50%;">
    <h3>Andres Castaño</h3>
    <p>Data Scientist | Geological Engineer</p>
    <a href="https://github.com/FeRsOmBrA" target="_blank">
        <img alt="GitHub" src="https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github" />
    </a>
    <a href="https://www.linkedin.com/in/ferney-castano/" target="_blank">
        <img alt="LinkedIn" src="https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=linkedin" />
    </a>
</div>
