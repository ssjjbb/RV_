import tkinter as tk
import time
import random


def temp1():
    rand_temp1 = random.randint(10, 40)
    return rand_temp1


def temp2():
    rand_temp2 = random.randint(-2, 8)
    return rand_temp2


def hatch_state(n):
    hatch1 = random.randint(0, 1)
    hatch2 = random.randint(0, 1)
    hatch3 = random.randint(0, 1)
    hatch4 = random.randint(0, 1)
    hatch5 = random.randint(0, 1)
    if n == 1:
        if hatch1 == 0:
            return "green"
        else:
            return "red"
    elif n == 2:
        if hatch2 == 0:
            return "green"
        else:
            return "red"
    elif n == 3:
        if hatch3 == 0:
            return "green"
        else:
            return "red"
    elif n == 4:
        if hatch4 == 0:
            return "green"
        else:
            return "red"
    elif n == 5:
        if hatch5 == 0:
            return "green"
        else:
            return "red"
    else:
        return 0


width = 300
height = 25

window = tk.Tk()
while True:
    try:

        """
        Block for temperature values and their visuals
        ---------------------------------------------------------------------------------------------------------------
        """
        temperature_frame1 = tk.Frame(master=window, width=width, height=height, bg="red", borderwidth=3)
        temperature_frame1.pack()
        temperature_frame2 = tk.Frame(master=window, width=width, height=height, bg="blue", borderwidth=3)
        temperature_frame2.pack()
        title1 = tk.Label(master=temperature_frame1, text="Temperature:", bg="red")
        title1.place(x=0, y=0)
        title2 = tk.Label(master=temperature_frame2, text="Temperature 2:", bg="blue")
        title2.place(x=0, y=0)
        value1 = tk.Message(master=temperature_frame1, text=temp1(), bg="red")
        value1.place(x=120, y=0)
        value2 = tk.Message(master=temperature_frame2, text=temp2(), bg="blue")
        value2.place(x=120, y=0)
        """
        Block for temperature values and their visuals ends
        ---------------------------------------------------------------------------------------------------------------
        Block for hatch state values and their visuals 
        """
#Frames
        hatch1_frame = tk.Frame(master=window, width=width, height=height, borderwidth=3)
        hatch1_frame.pack()
        hatch2_frame = tk.Frame(master=window, width=width, height=height, borderwidth=3)
        hatch2_frame.pack()
        hatch3_frame = tk.Frame(master=window, width=width, height=height, borderwidth=3)
        hatch3_frame.pack()
        hatch4_frame = tk.Frame(master=window, width=width, height=height, borderwidth=3)
        hatch4_frame.pack()
        hatch5_frame = tk.Frame(master=window, width=width, height=height, borderwidth=3)
        hatch5_frame.pack()

#Labels
        h_title1 = tk.Label(master=hatch1_frame, text="Hatch 1 state: ", borderwidth=3)
        h_title1.place(x=0, y=0)
        h_title2 = tk.Label(master=hatch2_frame, text="Hatch 2 state: ", borderwidth=3)
        h_title2.place(x=0, y=0)
        h_title3 = tk.Label(master=hatch3_frame, text="Hatch 3 state: ", borderwidth=3)
        h_title3.place(x=0, y=0)
        h_title4 = tk.Label(master=hatch4_frame, text="Hatch 4 state: ", borderwidth=3)
        h_title4.place(x=0, y=0)
        h_title5 = tk.Label(master=hatch5_frame, text="Hatch 5 state: ", borderwidth=3)
        h_title5.place(x=0, y=0)

#Hatches
        h_state1 = tk.Message(master=hatch1_frame, text="", bg=hatch_state(1))
        h_state1.place(x=125, y=0)
        h_state2 = tk.Message(master=hatch2_frame, text="", bg=hatch_state(2))
        h_state2.place(x=125, y=0)
        h_state3 = tk.Message(master=hatch3_frame, text="", bg=hatch_state(3))
        h_state3.place(x=125, y=0)
        h_state4 = tk.Message(master=hatch4_frame, text="", bg=hatch_state(4))
        h_state4.place(x=125, y=0)
        h_state5 = tk.Message(master=hatch5_frame, text="", bg=hatch_state(5))
        h_state5.place(x=125, y=0)


        """
        Block for hatch state values and their visuals ends
        ---------------------------------------------------------------------------------------------------------------
        """
        window.update()

        """
        ---------------------------------------------------------------------------------------------------------------
        """
#Mass destruction below
        title1.destroy()
        title2.destroy()

        value1.destroy()
        value2.destroy()

        temperature_frame1.destroy()
        temperature_frame2.destroy()

        hatch1_frame.destroy()
        hatch2_frame.destroy()
        hatch3_frame.destroy()
        hatch4_frame.destroy()
        hatch5_frame.destroy()

        h_title1.destroy()
        h_title2.destroy()
        h_title3.destroy()
        h_title4.destroy()
        h_title5.destroy()

        h_state1.destroy()
        h_state2.destroy()
        h_state3.destroy()
        h_state4.destroy()
        h_state5.destroy()

        time.sleep(1)

    except Exception:
        window.destroy()
