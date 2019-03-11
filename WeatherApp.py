import tkinter as tk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600


def get_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humid = weather['main']['humidity']
        final_str = 'City: %s\nConditions: %s\nTemperature: %s°C\nHumidity: %s' %(name, desc, temp, humid)
    except:
        final_str = 'there is problem in retrieving this information'

    return final_str


def get_weather(city):
    weather_key = '296094de8054f7317e134b00466e194b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = get_response(weather)

    # print(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


# background_image = tk.PhotoImage(file='landscape.png')
# background_label = tk.Label(root, image=background_image)
# background_label.place(relwidth=1, relheight=1)
bg_color = tk.Label(bg='#59606b')
bg_color.place(relwidth=1, relheight=1)

frame1 = tk.Frame(root, bg='#88c6e2', bd=5) # just added the cursor for fun
frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry = tk.Entry(frame1, font=('courier', 18))
entry.place(relwidth=0.65, relheight=1)
button = tk.Button(frame1, text='Check Weather', font=('courier', 11), command=lambda : get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1.0)


frame2 = tk.Frame(root, bg='#88c6e2', bd=5)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(frame2, font=('courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)


root.mainloop()