# Modern-Text-to-Speech-Converter
A modern, user-friendly Text-to-Speech application built with Python and tkinter. Convert text to speech in multiple languages with customizable speed settings.
# Modern Text-to-Speech Converter

A modern, user-friendly Text-to-Speech application built with Python and tkinter. Convert text to speech in multiple languages with customizable speed settings.

![Text to Speech Converter](https://raw.githubusercontent.com/username/repo-name/main/screenshots/app-screenshot.png)

## Features

- Clean, modern UI built with ttkbootstrap
- Support for multiple languages (powered by gTTS)
- Adjustable speech speed
- Real-time character count
- Progress indication during conversion
- Automatic file saving with unique identifiers
- Threaded processing to prevent UI freezing

## Requirements

```
Python 3.7+
tkinter
ttkbootstrap
gTTS
```

## Installation

1. Clone the repository:
```bash
git clone [https://github.com/iamliaqateagle/Modern-Text-to-Speech-Converter.git]
cd text-to-speech-converter
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the application:
```bash
python modrentts.py
```

1. Select your desired language from the dropdown menu
2. Toggle slow mode if needed
3. Enter or paste your text in the text area
4. Click "Convert to Speech" to generate the audio file
5. The generated MP3 file will be saved in the `output` directory

## Project Structure

```
text-to-speech-converter/
│
├── modrentts.py          # Main application file
├── requirements.txt      # Project dependencies
├── README.md            # Project documentation
├── LICENSE              # Project license
└── output/             # Directory for generated audio files
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [gTTS](https://github.com/pndurette/gTTS) for text-to-speech conversion
- [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) for modern UI widgets

## Author

LiaqatEagle

## Support

If you found this project helpful, please give it a ⭐️!
