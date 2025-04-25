# Chrome Web Automation

This repository contains a simple Python automation program that opens multiple URLs in the Google Chrome browser with a single click, saving you time and effort.

## 🚀 About the Project

The `Chrome Automation` script automatically launches a list of my favorite and frequently visited websites without the need to manually type them one by one.

This is particularly useful for:

- Starting your work or study session quickly
- Opening daily tools and resources with ease
- Automating your browsing workflow

## 🛠️ How It Works
- The program uses Python's built-in `webbrowser` module.
- A list of URLs is defined in the `URLS` variable.
- Each URL is opened in Chrome using the specified Chrome executable path.

## 📄 Source Code
```bash
import webbrowser as wb

def web_auto():
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    URLS = (
        "stackoverflow.com",
        "gmail.com",
        "youtube.com",
        "outlook.com",
        "linkedin.com",
        "udemy.com",
        "https://github.com/isiaq-ibrahim"
    )

    for url in URLS:
        print("opening :" + url)
        wb.get(chrome_path).open(url)

web_auto()
```

### 🖥️ Requirements

- Python 3.x installed on your system
- Google Chrome browser installed
- Adjust the chrome_path variable if Chrome is installed in a different location

### 🔧 How to Run

- Clone or download this repository.
- Open the project folder in your terminal or command prompt.
- Run the script:
```bash
python filename.py
```
(Replace filename.py with the name of your Python file.)
- Watch as multiple tabs open automatically in Chrome!

### ✨ Customization

You can easily customize the script by:

- Adding or removing URLs from the URLS tuple.
- Changing the browser path if you want to use a different browser.

### 📚 License

This project is licensed under the MIT License — feel free to use, modify, and share it!
