from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

## operational functions
def change_label(dist_in_km):
    km_value.config(text=dist_in_km)

def calculate_distance():
    distance_miles=dist_in_miles.get()
    distance_km=float(distance_miles)*1.60934
    change_label(str(distance_km))
    dist_in_miles.delete(0, END)



## Layouts
dist_in_miles=Entry(width=10)
dist_in_miles.grid(column=1,row=0,padx=5,pady=5)

is_equal_to=Label(text="is equal to")
is_equal_to.grid(column=0,row=1,padx=5,pady=5)

km_value=Label(text='0')
km_value.grid(column=1,row=1,padx=5,pady=5)

miles_label=Label(text="Miles")
miles_label.grid(column=2,row=0,padx=5,pady=5)

km_label=Label(text="Km")
km_label.grid(column=2,row=1,padx=5,pady=5)

calculate_button=Button(text="Calculate",command=calculate_distance)
calculate_button.grid(column=1,row=2,padx=5,pady=5)







window.mainloop()



