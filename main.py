from config_for_length import config_for_length
import tkinter as tk
from shaft import Shaft
from scraper import get_live_price


def main():
    target_length = answer.get()
    configurations["text"] = ""
    warning["text"] = ""
    # Scrap price to get live price when login won't be required
    shafts = [
        Shaft("MO-LM-014-2295__2", length=2295, price=539.18),
        Shaft("MO-LM-014-1530__2", length=1530, price=357.68),
        Shaft("MO-LM-014-0855__2", length=855, price=292.66),
        Shaft("MO-LM-014-0585__2", length=585, price=232.54),
    ]

    if target_length.isdigit():
        current_pricing = "Using those shafts and price:"
        for shaft in shafts:
            current_pricing += f"\n{shaft.name} at ${shaft.price}USD"
        warning["text"] = current_pricing
        configurations["text"] = config_for_length(int(target_length), shafts)

    else:
        warning["text"] = "Don't be a Terry, your target_length needs to be a number"


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Long Shafts Configurations")
    window.resizable(width=True, height=True)

    question = tk.Label(master=window, text="How long do you need you shaft to be? (mm)", width=60)
    answer = tk.Entry(master=window, width=30)
    button = tk.Button(master=window, text="Calculate!", command=main)
    configurations = tk.Label(master=window, justify="left")
    warning = tk.Label(master=window, fg="red")

    question.grid(row=0, column=0)
    answer.grid(row=1, column=0)
    button.grid(row=2, column=0)
    warning.grid(row=3, column=0)
    configurations.grid(row=4, column=0)

    window.mainloop()
