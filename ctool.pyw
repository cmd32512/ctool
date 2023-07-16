from tkinter import *
import tkinter as tk
from tkinter import Tk, ttk, CENTER
from tkinter import ttk
from tkinter import messagebox
import platform
import win32com.client
import socket
import psutil
import cpuinfo
import requests
from ping3 import ping
import pydirectinput
import time
from time import sleep
import keyboard
import threading
    
root = Tk()
root.iconbitmap(r"/app-icon.ico")
root.geometry('500x300')
root.title("CTool+")
root.resizable(0,0)
root["bg"] = "blue"


def get_processor_name():
    try:
        info = cpuinfo.get_cpu_info()
        processor_name = info["brand_raw"]
        return processor_name
    except Exception as e:
        print("negr:", e)
        return "N/A"

    
def get_ip_address():
    try:
        host_name = socket.gethostname()
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except socket.error:
        return "N/A"

def get_public_ip():
    try:
        response = requests.get("https://api64.ipify.org?format=json")
        data = response.json()
        return data["ip"]
    except requests.exceptions.RequestException:
        return "N/A"

def get_ping(server):
    try:
        return ping(server)
    except OSError:
        return "N/A"
    
def sys_window():
    window = tk.Tk()
    window.iconbitmap(r"/app-icon.ico")
    window.title("Your system:")
    window.geometry("500x200")
    window.resizable(0,0)
    window["bg"] = "blue"
    bottomframe.pack( side = BOTTOM )
    os_name = platform.system()
    os_version = platform.version()
    wmi = win32com.client.GetObject("winmgmts:")
    query = "SELECT * FROM Win32_VideoController"
    gpu_info = wmi.ExecQuery(query)
    gpu_name = gpu_info[0].Name
    cpu_info = get_processor_name()
    network_adapters = psutil.net_if_addrs()
    network_adapter_info = ", ".join([adapter for adapter in network_adapters])
    os_label = ttk.Label(window, text=f"OS: {os_name} {os_version}", background="blue", foreground="yellow", font=("Arial", 9))
    os_label.place(relx=0.5, rely=0.2, anchor=CENTER)
    gpu_label = ttk.Label(window, text=f"GPU: {gpu_name}", background="blue", foreground="yellow", font=("Arial", 9))
    gpu_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    cpu_label = ttk.Label(window, text=f"CPU: {cpu_info}", background="blue", foreground="yellow", font=("Arial", 9))
    cpu_label.place(relx=0.5, rely=0.4, anchor=CENTER)
    network_label = ttk.Label(window, text=f"{network_adapter_info}", background="blue", foreground="yellow", font=("Arial", 8))
    network_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    alert_text = ttk.Label(window, text="More to come soon...", background="blue", foreground="yellow", font=("Arial", 9))
    alert_text.place(relx=0.5, rely=0.7, anchor=CENTER)
    
def net_window():
    window = tk.Tk()
    window.iconbitmap(r"/app-icon.ico")
    window.title("Your network:")
    window.geometry("350x255")
    window.resizable(0,0)
    window["bg"] = "blue"
    ip_address = get_ip_address()
    public_ip = get_public_ip()
    server_to_ping = "8.8.8.8"
    ping_result = get_ping(server_to_ping)
    ip_label = ttk.Label(window, text=f"IPv4: {ip_address}", background="blue", foreground="yellow", font=("Arial", 9))
    ip_label.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
    public_ip_label = ttk.Label(window, text=f"Public IP: {public_ip}", background="blue", foreground="yellow", font=("Arial", 9))
    public_ip_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
    ping_label = ttk.Label(window, text=f"Ping: {ping_result} ms", background="blue", foreground="yellow", font=("Arial", 9))
    ping_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    ping_server_label = ttk.Label(window, text=f"Server: {server_to_ping}", background="blue", foreground="yellow", font=("Arial", 9))
    ping_server_label.place(relx=0.5, rely=0.6, anchor=tk.CENTER)




    



    
frm = ttk.Frame(root)
frm.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )


style_main = ttk.Style()
style_main.configure("MainLabel.TLabel", background="blue", font=("Arial", 16), foreground="yellow", padding=(0, 5))
style_second = ttk.Style()
style_second.configure("SecondLabel.TLabel", background="blue", font=("Arial", 9), foreground="yellow", padding=(0, 0))
style_third = ttk.Style()
style_third.configure("ThirdLabel.TLabel", background="blue", font=("Arial", 9), foreground="yellow", padding=(5))
style_fourth = ttk.Style()
style_fourth.configure("FourthLabel.TLabel", background="blue", font=("Arial", 9), foreground="yellow", padding=(2))




main_text = ttk.Label(frm, text="CTool+", style="MainLabel.TLabel", anchor="center")
main_text.grid(column=0, row=0, sticky="nsew")
second_text = ttk.Label(frm, text="Utility for windows 7 and 10!", style="SecondLabel.TLabel")
second_text.grid(column=0, row=1, sticky="nsew")
third_text = ttk.Label(bottomframe, text="Made by @Comdar16", style="ThirdLabel.TLabel")
third_text.grid(column=0, row=2, sticky="nsew")
fourth_text = ttk.Label(bottomframe, text="v1.0", style="FourthLabel.TLabel", anchor="center")
fourth_text.grid(column=0, row=3, sticky="nsew")

system = Button(text="System info", command=sys_window)
system.place(relx=0.5, rely=0.5, anchor=CENTER)
network = Button(text="Network info", command=net_window)
network.place(relx=0.5, rely=0.6, anchor=CENTER)




frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)






root.mainloop()




