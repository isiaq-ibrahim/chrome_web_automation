Here is the source code of the Python program. Help mr to write a README for my GitHub repo.

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
        print("opening :"+ url)
        wb.get(chrome_path).open(url)

web_auto()