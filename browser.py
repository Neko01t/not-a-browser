import requests
from bs4 import BeautifulSoup
import tkinter as tk
window = tk.Tk()

def getWeb(urlm):
    data = requests.get(urlm).text
    soup = BeautifulSoup(data, "html.parser")
    title = soup.find("title")
    para1 = soup.find("p")
    return [title,para1]

window.title("browser")
window.geometry("600x400")

tktitle = tk.Label(window, text="browser")
tktitle.pack()
entry = tk.Entry(window, width=30)
entry.pack()
tkpara1 = tk.Text(window, height = 5, width = 52)
tkpara1.pack()
def get_input():
    tkpara1.delete("1.0", tk.END)
    user_input = entry.get()
    print("User input:", user_input)
    weburl= "https://"+user_input
    [title,para1] = getWeb(weburl)
    print(para1.text)
    tktitle.config(text=title.text)
    tkpara1.insert(tk.END, para1.text)


button = tk.Button(window, text="go to link website", command=get_input)
button.pack()
 

window.mainloop()