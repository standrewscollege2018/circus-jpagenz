from tkinter import *

# define ticket class
class Ticket:

    def __init__(self, times, capacity, price):
        self._times = times
        self._capacity = capacity
        self._price = price
        tickets.append(self)
        ticket_times.append(self._times)

tickets = []
ticket_times = []

Ticket("10am", 150, 5)
Ticket("3pm", 150, 5)
Ticket("8pm", 250, 12)

root = Tk()
root.title("Pizza label")
root.geometry('400x400')

def update_label():
    ticket_info.set("")
    for t in Times:
        time_info.set(time_info.get() + t._times + "   $" + str(t._price) + "\n")

# set up the label
ticket_info = StringVar()

ticket_lbl = Label(root, textvariable=ticket_info, justify='left')
ticket_lbl.grid(row=0, sticky=W)


#  create the option menu
selected_ticket = StringVar()
selected_ticket.set(ticket_names[0])
# three parameters: location, selected item, list of all items
selected_ticket = OptionMenu(root, selected_pizza, *pizza_names)
selected_ticket.grid(row = 1)


update_label()
root.mainloop()


