from morse_converter import MorseConverter
import tkinter

#________________Create morse converter object____________________#
converter = MorseConverter()

#_____Function takes app input, converts to morse and updates the output label______#
def convert():
    message = entry.get().lower()
    print(message)
    message_chars = converter.string_to_list(message)
    converter.to_morse(message_chars)
    morse_output = converter.to_string()
    morse_out_label['text'] = f'Morse Code: {morse_output}'



#____________________________TKinter GUI Setup_________________________#
window = tkinter.Tk()
window.config(padx=30, pady=50)
window.title('Morse Converter')
window.minsize(width=350, height=500)

morse_image = tkinter.PhotoImage(file='morse.png')
canvas = tkinter.Canvas(width=250, height=150, bg='blue', highlightthickness=0)
canvas.create_image(125, 75, image=morse_image)
canvas.grid(row=1, column=1)

heading_label = tkinter.Label(text='Morse Converter')
heading_label.config(font=('Arial', 30, 'bold'), fg='blue', padx=20)
heading_label.grid(row=0, column=1)

input_label = tkinter.Label(text="Write something and I'll convert it into morse code")
input_label.config(pady=10)
input_label.grid(row=2, column=1)

entry = tkinter.Entry(width=30)
entry.insert(tkinter.END, string='Write here')
entry.grid(row=3, column=1)

text_input = entry.get()

button = tkinter.Button(text='Convert', command=convert)
button.grid(row=4, column=1)

morse_out_label = tkinter.Label(text='Morse Code: ')
morse_out_label.grid(row=5, column=1)


window.mainloop()