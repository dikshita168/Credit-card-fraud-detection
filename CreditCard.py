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

def on_svm_click():
    accuracy_value.config(text=str(get_accuracy("SVM")), fg="white", bg="#4CAF50")

def on_random_forest_click():
    accuracy_value.config(text=str(get_accuracy("Random Forest")), fg="white", bg="#2196F3")

def on_adaboost_click():
    accuracy_value.config(text=str(get_accuracy("AdaBoost")), fg="white", bg="#FF9800")

window = tk.Tk()
window.geometry("600x400")
window.title("Credit Card Fraud Detection System")

left_frame = tk.Frame(window,  bg="#f2f2f2")
left_frame.pack(side=tk.LEFT, padx=20)


svm_button = tk.Button(left_frame, text="SVM", width=15, command=on_svm_click, bg="#4CAF50", fg="white")
svm_button.pack(pady=10)

random_forest_button = tk.Button(left_frame, text="Random Forest", width=12, command=on_random_forest_click, bg="#2196F3", fg="white")
random_forest_button.pack(pady=10)

adaboost_button = tk.Button(left_frame, text="AdaBoost", width=10, command=on_adaboost_click, bg="#FF9800", fg="white")
adaboost_button.pack(pady=10)

center_frame = tk.Frame(window, bg="white")
center_frame.pack(side=tk.LEFT)

label = tk.Label(center_frame, text="Credit Card Fraud Detection System", font=("Arial", 16), bg="white")
label.pack(pady=(50, 20))

accuracy_label = tk.Label(center_frame, text="Accuracy: ", font=("Arial", 12), bg="white")
accuracy_label.pack()

accuracy_value = tk.Label(center_frame, text="0.00", font=("Arial", 12, "bold"), bg="white")
accuracy_value.pack()

button = tk.Button(center_frame, text="Run Colab (Link)", width=20, command=run_colab, bg="#4CAF50", fg="white")
button.pack(pady=20)

right_frame = tk.Frame(window, bg="#f2f2f2")
right_frame.pack(side=tk.RIGHT, padx=20)

window.mainloop()
