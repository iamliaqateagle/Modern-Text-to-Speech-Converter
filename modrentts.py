import tkinter as tk
from tkinter import ttk, scrolledtext
import ttkbootstrap as tb
from gtts import gTTS, lang
from threading import Thread
import os
import uuid
import time

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter By LiaqatEagle")
        self.root.geometry("1000x700")
        
        # Get available languages from gTTS
        self.languages = self.get_languages()
        
        # Create output directory
        if not os.path.exists("output"):
            os.makedirs("output")
            
        self.setup_ui()
        
    def get_languages(self):
        """Get dictionary of available languages from gTTS"""
        tts_langs = lang.tts_langs()
        # Sort languages by name
        return dict(sorted(tts_langs.items(), key=lambda x: x[1]))
        
    def setup_ui(self):
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header with title
        header = ttk.Frame(main_frame)
        header.pack(fill=tk.X, pady=(0, 20))
        
        title = ttk.Label(
            header,
            text="Text to Speech Converter",
            font=("Helvetica", 24, "bold"),
            foreground="#1e88e5"
        )
        title.pack(side=tk.LEFT)
        
        # Settings panel
        settings_frame = ttk.LabelFrame(main_frame, text="Voice Settings", padding="15")
        settings_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Create two-column layout for settings
        settings_grid = ttk.Frame(settings_frame)
        settings_grid.pack(fill=tk.X, pady=10)
        
        # Language selection
        lang_frame = ttk.Frame(settings_grid)
        lang_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        ttk.Label(
            lang_frame,
            text="Select Language",
            font=("Helvetica", 10, "bold")
        ).pack(anchor=tk.W)
        
        # Create language selection with search
        self.lang_var = tk.StringVar()
        self.lang_combo = ttk.Combobox(
            lang_frame,
            textvariable=self.lang_var,
            state="readonly",
            width=40
        )
        self.lang_combo.pack(fill=tk.X, pady=(5, 0))
        
        # Speed control
        speed_frame = ttk.Frame(settings_grid)
        speed_frame.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        ttk.Label(
            speed_frame,
            text="Speech Speed",
            font=("Helvetica", 10, "bold")
        ).pack(anchor=tk.W)
        
        self.speed_var = tk.BooleanVar(value=False)
        speed_check = ttk.Checkbutton(
            speed_frame,
            text="Slow Mode",
            variable=self.speed_var
        )
        speed_check.pack(anchor=tk.W, pady=(5, 0))
        
        # Text input area with character count
        input_frame = ttk.LabelFrame(main_frame, text="Enter Text", padding="15")
        input_frame.pack(fill=tk.BOTH, expand=True)
        
        self.text_area = scrolledtext.ScrolledText(
            input_frame,
            wrap=tk.WORD,
            font=("Helvetica", 12),
            height=12
        )
        self.text_area.pack(fill=tk.BOTH, expand=True, pady=(0, 5))
        
        # Character count label
        self.char_count_label = ttk.Label(
            input_frame,
            text="Characters: 0",
            font=("Helvetica", 9),
            foreground="#666666"
        )
        self.char_count_label.pack(anchor=tk.E, pady=(0, 10))
        
        # Bind text changes to update character count
        self.text_area.bind('<KeyRelease>', self.update_char_count)
        
        # Bottom controls
        controls_frame = ttk.Frame(input_frame)
        controls_frame.pack(fill=tk.X)
        
        # Status with loading animation
        status_frame = ttk.Frame(controls_frame)
        status_frame.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        self.status_label = ttk.Label(
            status_frame,
            text="Ready",
            font=("Helvetica", 10),
            foreground="#666666"
        )
        self.status_label.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            status_frame,
            mode='indeterminate',
            length=200
        )
        
        # Convert button with modern styling
        self.convert_btn = ttk.Button(
            controls_frame,
            text="Convert to Speech",
            style="Accent.TButton",
            command=self.start_conversion
        )
        self.convert_btn.pack(side=tk.RIGHT)
        
        # Initialize languages
        self.update_languages()
        
    def update_languages(self):
        # Create list of language names with their codes
        lang_list = [f"{name} [{code}]" for code, name in self.languages.items()]
        self.lang_combo['values'] = lang_list
        
        # Set default to English
        default_index = next(
            (i for i, lang in enumerate(lang_list) if "English" in lang),
            0
        )
        self.lang_combo.current(default_index)
    
    def update_char_count(self, event=None):
        count = len(self.text_area.get("1.0", tk.END).strip())
        self.char_count_label.config(text=f"Characters: {count}")
    
    def get_selected_language_code(self):
        selected = self.lang_combo.get()
        # Extract language code from the selection (format: "Language Name [code]")
        return selected.split('[')[1].strip(']')
    
    def convert_text_to_speech(self):
        try:
            text = self.text_area.get("1.0", tk.END).strip()
            if not text:
                self.status_label.config(
                    text="Please enter some text!",
                    foreground="#dc3545"
                )
                return
            
            # Get language code
            lang_code = self.get_selected_language_code()
            
            # Create gTTS object
            tts = gTTS(
                text=text,
                lang=lang_code,
                slow=self.speed_var.get()
            )
            
            # Generate unique filename
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"output/speech_{timestamp}_{str(uuid.uuid4())[:8]}.mp3"
            
            # Save the audio file
            tts.save(filename)
            
            self.status_label.config(
                text=f"✅ Saved as: {filename}",
                foreground="#28a745"
            )
            
        except Exception as e:
            self.status_label.config(
                text=f"❌ Error: {str(e)}",
                foreground="#dc3545"
            )
            
        finally:
            self.progress.stop()
            self.progress.pack_forget()
            self.convert_btn.config(state="normal")
    
    def start_conversion(self):
        self.convert_btn.config(state="disabled")
        self.status_label.config(
            text="Converting...",
            foreground="#1e88e5"
        )
        self.progress.pack(side=tk.LEFT, padx=20)
        self.progress.start(10)
        
        Thread(target=self.convert_text_to_speech, daemon=True).start()

if __name__ == "__main__":
    root = tb.Window(themename="cosmo")
    app = TextToSpeechApp(root)
    root.mainloop()