import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk

def getWeb(urlm):
    try:
        data = requests.get(urlm, timeout=5)
        soup = BeautifulSoup(data.text, "html.parser")
        title = soup.find("title").text if soup.find("title") else "No Title"

        paragraphs = soup.find_all("p")
        para_texts = [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
        content = "\n\n".join(para_texts) if para_texts else "No paragraphs found."
        return title, content
    except Exception as e:
        return "Error", f"Could not fetch website: {e}"

window = tk.Tk()
window.title("Mini Paragraph Browser")
window.geometry("700x500")

title_label = tk.Label(window, text="Mini Paragraph Browser", font=("Arial", 18))
title_label.pack(pady=10)

entry = tk.Entry(window, width=50)
entry.pack(pady=5)

text_frame = tk.Frame(window)
text_frame.pack(expand=True, fill='both', padx=10, pady=10)

scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

text_widget = tk.Text(text_frame, wrap="word", yscrollcommand=scrollbar.set, state="disabled")
text_widget.pack(side="left", fill="both", expand=True)

scrollbar.config(command=text_widget.yview)

def get_input():
    text_widget.config(state="normal")
    text_widget.delete("1.0", tk.END)
    user_input = entry.get().strip()
    if not user_input:
        title_label.config(text="Invalid URL")
        text_widget.insert(tk.END, "Please enter a valid URL.")
    else:
        if not user_input.startswith("http"):
            user_input = "https://" + user_input
        title, content = getWeb(user_input)
        title_label.config(text=title)
        text_widget.insert(tk.END, content)
    text_widget.config(state="disabled")

button = tk.Button(window, text="Fetch Website Content", command=get_input)
button.pack(pady=5)

window.mainloop()
