import customtkinter as ct
from ctk_widget import CTkMeter

root = ct.CTk()
ct.set_appearance_mode("White")
root.minsize(height=500, width=550)
root.configure(bg_color='#fafafa')


# Function for testing command
def change_it(value):
    meter.set(value)
    meter.textvariable.set(f'{int((value / 360) * 100)}%')  # To set the text

meter = CTkMeter(root,padding=19, background='#242424',foreground='#ffffff', troughcolor='#b6b6de', font='Calibri 14 bold',indicatorcolor='#0f1273')
meter.pack(pady=5)

meter.set(360)  # Value must be between 0 and 360

meter.textvariable.set(f'{int((meter.arcvariable.get() / 360) * 100)}%')  # To set the text

slider = ct.CTkSlider(root, from_=0, to=2000, number_of_steps=100, width=245, command=lambda value: change_it(value))
slider.pack(anchor="center")
root.mainloop()