import requests
from bs4 import BeautifulSoup
import tkinter as tk

window = tk.Tk()

def getWeb(urlm):
    try:
        data = requests.get(urlm, timeout=5)
        soup = BeautifulSoup(data.text, "html.parser")
        title = soup.find("title")
        para1 = soup.find("p")
        return title.text if title else "No Title", para1.text if para1 else "No paragraph found."
    except Exception as e:
        return "Error", f"Could not fetch the website: {e}"

window.title("browser")
window.geometry("600x400")

tktitle = tk.Label(window, text="browser", font=('Arial', 16))
tktitle.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack()

tkpara1 = tk.Text(window, height=10, width=60, wrap='word')
tkpara1.pack(pady=10)

def get_input():
    tkpara1.delete("1.0", tk.END)
    user_input = entry.get().strip()
    if not user_input:
        tktitle.config(text="Invalid URL")
        tkpara1.insert(tk.END, "Please enter a valid URL.")
        return
    if not user_input.startswith("http"):
        user_input = "https://" + user_input
    title, para1 = getWeb(user_input)
    tktitle.config(text=title)
    tkpara1.insert(tk.END, para1)

button = tk.Button(window, text="Go to website", command=get_input)
button.pack(pady=5)

window.mainloop()
