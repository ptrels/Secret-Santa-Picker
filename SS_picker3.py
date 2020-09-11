# Secret Santa Picker

import random
from tkinter import *
from tkinter import ttk, Text, Tk, Menu, scrolledtext, messagebox, filedialog

# creates tkinter window
window = Tk()

window.title("Secret Santa Picker")


def clear_data():
    text_1.delete(0, END)
    text_2.delete(0, END)
    text_3.delete(0, END)
    text_4.delete(0, END)
    text_5.delete(0, END)
    text_6.delete(0, END)
    text_7.delete(0, END)
    text_8.delete(0, END)    

def draw():
    ## run search here
    fp = open("SS Results.txt", "w+")
    fp.write(pprint.pformat(drawing))
    fp.close()
    save_location = os.path.abspath(os.path.join("SS Results.txt"))
    messagebox.showwarning('Drawing Complete', "Drawing results saved successfully.\n\n" + "File Path:\n\n" + save_location)

def randomize():
    per_list = []
    per_dict = {}
    per_dict_1 = {}
    floaters = []
    floaters_not = []
    final_dict = {}
    num_dict = {}

    per_dict[1] = text_1.get()
    per_dict[2] = text_2.get()
    per_dict[3] = text_3.get()
    per_dict[4] = text_4.get()
    per_dict[5] = text_5.get()
    per_dict[6] = text_6.get()
    per_dict[7] = text_7.get()
    per_dict[8] = text_8.get()

    per_dict_1[text_1.get()] = 1
    per_dict_1[text_2.get()] = 2
    per_dict_1[text_3.get()] = 3
    per_dict_1[text_4.get()] = 4
    per_dict_1[text_5.get()] = 5
    per_dict_1[text_6.get()] = 6
    per_dict_1[text_7.get()] = 7
    per_dict_1[text_8.get()] = 8

    count = 1
    for k,v in per_dict.items():
        per_list.append(v)

    count_blank = per_list.count("")
    count_blank_1 = 8 - count_blank

    for i in per_list:
        if i == "":
            floaters_not.append(count)
            count +=1
        else:
            count +=1

    it = iter(per_list)
    for x in it:
        if next(it) == "":
            floaters.append(per_dict_1[x])
    
    while len(num_dict) < count_blank_1:
        for person in per_list:
            rand_num = random.randint(1, 8)

            if count_blank_1 <= 3:
                messagebox.showwarning("Warning", "Must have more than 3 people")
                return
            if rand_num in floaters_not:
                continue
            elif rand_num == int(per_dict_1[person]) + 1:
                continue
            elif rand_num == int(per_dict_1[person]) - 1:
                continue
            elif per_dict[rand_num] == person:
                continue
            elif person != "" and rand_num not in num_dict.values():
                num_dict[person] = rand_num
            else:
                continue

        for k,v in num_dict.items():
            for key,value in per_dict.items():
                if v == key:
                    final_dict[k] = value
    
    def label_active(lab):
        #lab.grid()
        lab.config(fg = "black")

    def label_inactive(lab):
        #lab.grid_forget()
        lab.config(fg = window.cget('bg'))
    
    countie = 0
    for k,v in final_dict.items():            
        label = "lab_" + str(countie)
        label = Label(bot_frame, text=k, font=("Arial Bold", 10))
        label_1 = "results_" + str(countie)
        label_1 = Label(bot3_frame, text=v, fg = window.cget('bg'), font=("Arial Bold", 10))
        buts = "but_" + str(countie)
        buts = Button(bot2_frame, text = "Show", fg = "RoyalBlue2", bg = "white", command=lambda i=label_1: label_active(i))
        buts_2 = "but_" + str(countie*2)
        buts_2 = Button(bot2_frame, text = "Hide", fg = "red", bg = "white", command=lambda i=label_1: label_inactive(i))
        buts.grid(column = 0, row = countie)
        buts_2.grid(column = 1, row = countie)
        label.grid()
        label_1.grid()
        countie +=1

    

# create frames
left_frame = Frame(window)#, width = 150, height = 200)
right_frame = Frame(window) #, width = 150, height = 200)
top_frame = Frame(window) #, width = 300, height = 100)
bot_frame = Frame(window) #, width = 100, height = 200)
bot2_frame = Frame(window) #, width = 100, height = 200)
bot3_frame = Frame(window) #, width = 100, height = 200)

# position frames
left_frame.grid(column = 0, row = 1)
right_frame.grid(column = 1, row = 1)
top_frame.grid(column = 0, row = 0, columnspan = 3)
bot_frame.grid(column = 0, row = 2)
bot3_frame.grid(column = 1, row = 2)
bot2_frame.grid(column = 2, row = 2)


## create the widget for label
lbl = Label(left_frame, text="Person 1", font=("Arial Bold", 12))

# create comboboxes
lbl_1 = Label(right_frame, text= "Person 2 / Spouse", font=("Arial Bold", 12))


# create entry boxes
text_1 = Entry(left_frame, width = 20)
text_2 = Entry(right_frame, width = 20)
text_3 = Entry(left_frame, width = 20)
text_4 = Entry(right_frame, width = 20)
text_5 = Entry(left_frame, width = 20)
text_6 = Entry(right_frame, width = 20)
text_7 = Entry(left_frame, width = 20)
text_8 = Entry(right_frame, width = 20)


# create button widgets
btn_1 = Button(top_frame, text = "Draw", fg = "green4", bg = "white", command = randomize)
btn_2 = Button(top_frame, text = "Clear Entries", fg = "RoyalBlue2", bg = "white", command = clear_data)


# layout widgets
lbl.grid(pady=3)

lbl_1.grid(pady = 3)

btn_2.grid(pady = (5, 3))
btn_1.grid(pady = (3, 5))

text_1.grid(pady = 3)
text_2.grid(pady = 3)
text_3.grid(pady = 3)
text_4.grid(pady = 3)
text_5.grid(pady = 3)
text_6.grid(pady = 3)
text_7.grid(pady = 3)
text_8.grid(pady = 3)

window.mainloop()
