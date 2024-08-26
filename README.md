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
