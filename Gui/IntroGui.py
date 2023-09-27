import tkinter as a
r = a.Tk()
r.title('Counting Seconds')
button = a.Button(r, text='Stop', width=25, command=r.destroy)
button.pack()
co = a.Canvas(r, width=800, height=400, bg='blue')
co.pack()
r.mainloop()
