import re
import keyboard
import pandas as pd
import edge_tts
import asyncio
import os
import sys
import customtkinter as ctk
from tkinter import messagebox
import threading
import pygame

# Leer las voces del archivo CSV
voices = pd.read_csv("output.csv")


async def speak(voice, text):
    base_dir = sys._MEIPASS if getattr(
        sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
    audio_path = os.path.join(base_dir, 'output.mp3')

    comm = edge_tts.Communicate(text, voice)
    await comm.save(audio_fname=audio_path)

    # Inicializar pygame para reproducir el archivo de audio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.stop()
    pygame.mixer.quit()
    os.remove(audio_path)


class TTSApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Text-to-Speech App")
        self.geometry("800x600")
        self.attributes("-topmost", True)
        self.is_speaking = False

        # Diccionario para idiomas soportados
        self.languages = {
            "French": "fr",
            "English": "en",
            "Spanish": "es",
            "Italian": "it",
            "Portuguese": "pt",
            "German": "de",
            "Korean": "ko",
            "Russian": "ru",
            "Japanese": "ja",
            "Arabic": "ar",
        }

        # Configuración del tema de la aplicación
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Configuración del marco central
        self.central_frame = ctk.CTkFrame(self)
        self.central_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Selector de Idioma
        self.label_lang = ctk.CTkLabel(
            self.central_frame, text="Select Language:")
        self.label_lang.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.lang_combobox = ctk.CTkComboBox(self.central_frame, values=list(
            self.languages.keys()), command=self.on_language_selected)
        self.lang_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        # Define en inglés como idioma predeterminado
        self.lang_combobox.set("English")

        # Selector de Voz
        self.label_voice = ctk.CTkLabel(
            self.central_frame, text="Select a Voice:")
        self.label_voice.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.voice_mapping = dict(
            zip(voices['FriendlyName'], voices['ShortName']))
        self.voices_combobox = ctk.CTkComboBox(
            self.central_frame, values=[], state="readonly")
        self.voices_combobox.grid(
            row=1, column=1, padx=10, pady=10, sticky="ew")

        # Caja de texto para introducir el texto
        self.label_text = ctk.CTkLabel(self.central_frame, text="Enter Text:")
        self.label_text.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.text_entry = ctk.CTkTextbox(
            self.central_frame, height=200, width=500)
        self.text_entry.grid(row=3, column=0, columnspan=2,
                             padx=10, pady=10, sticky="nsew")

        # Configurar las filas y columnas para que se expandan adecuadamente
        self.central_frame.grid_columnconfigure(0, weight=1)
        self.central_frame.grid_columnconfigure(1, weight=2)
        self.central_frame.grid_rowconfigure(3, weight=1)

        # Botón flotante para iniciar la conversión de texto a voz
        self.speak_button = ctk.CTkButton(
            self, text="🔊", command=self.on_speak, width=50)
        self.speak_button.configure(font=("Arial", 40, "bold"))
        self.speak_button.place(relx=0.9, rely=0.9, anchor="se")
        keyboard.add_hotkey("ctrl+alt+s", self.on_speak)

        self.on_language_selected()

    def on_language_selected(self, event=None):
        selected_language = self.languages[self.lang_combobox.get()]
        filtered_voices = voices[voices['Locale'].str.startswith(
            selected_language)]
        self.voice_mapping = dict(
            zip(filtered_voices['FriendlyName'], filtered_voices['ShortName']))
        self.voices_combobox.configure(values=list(self.voice_mapping.keys()))
        self.voices_combobox.set(
            "Microsoft Steffan Online (Natural) - English (United States)")

    def on_speak(self):
        selected_friendly_name = self.voices_combobox.get()
        voice = self.voice_mapping.get(selected_friendly_name)
        text = self.text_entry.get("1.0", "end").strip()

        if self.is_speaking:
            messagebox.showwarning(
                "Warning", "The TTS service is already speaking. Please wait.")
            return

        if not voice:
            messagebox.showerror("Error", "Please select a voice.")
            return

        if not text:
            messagebox.showerror("Error", "Please enter text.")
            return

        thread = threading.Thread(
            target=self.threaded_speak, args=(voice, text))
        thread.start()

    def threaded_speak(self, voice, text):
        self.is_speaking = True
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        try:
            loop.run_until_complete(speak(voice, text))
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            loop.close()

        self.is_speaking = False


if __name__ == "__main__":
    app = TTSApp()
    app.mainloop()
