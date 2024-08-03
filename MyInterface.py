import webbrowser
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def run_colab():
    url = 'https://colab.research.google.com/drive/1feznbus5tYZEnUibeUD7E-QYwCeTwlUv#scrollTo=N6euJuhNWl83'
    webbrowser.open_new_tab(url)

def get_accuracy(model_name):
    if model_name == "SVM":
        accuracy = 0.9392251
    elif model_name == "Random Forest":
        accuracy =  0.9494089
    elif model_name == "AdaBoost":
        accuracy = 0.9241703
    else:
        accuracy = 0
    return accuracy


window = tk.Tk()
window.geometry("600x400")
window.title("Credit Card Fraud Detection System")


left_frame = tk.Frame(window, bg="#f2f2f2")
left_frame.pack(side=tk.LEFT, padx=20)

svm_button = tk.Button(left_frame, text="SVM", width=15, command=on_svm_click, bg="#4CAF50", fg="white")
svm_button.pack(pady=10)

window.mainloop()