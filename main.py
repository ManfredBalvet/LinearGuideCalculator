from config_for_length import config_for_length
import tkinter as tk


def main():
    length = answer.get()
    lbl_output1["text"] = ""
    lbl_output2["text"] = ""
    if length.isdigit():
        output = config_for_length(int(length))
        lbl_output1["text"] = f"\nFor a {length}mm shaft you need:\n\n" + output
    else:
        lbl_output2["text"] = "\nYour length needs to be a number"


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Long Shafts Configurations")
    window.resizable(width=True, height=True)

    question = tk.Label(master=window, text="What length you want to build?", width=60)
    answer = tk.Entry(master=window, width=30)
    button = tk.Button(master=window, text="Calculate!", command=main)
    lbl_output1 = tk.Label(master=window)
    lbl_output2 = tk.Label(master=window, fg="red")

    question.grid(row=0, column=0)
    answer.grid(row=1, column=0)
    button.grid(row=2, column=0, sticky="ns")
    lbl_output1.grid(row=3, column=0, sticky="nw")
    lbl_output2.grid(row=3, column=0, sticky="nw")

    window.mainloop()
