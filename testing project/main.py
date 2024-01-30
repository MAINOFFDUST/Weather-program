import requests
import customtkinter




def get_weather():
    city = cityField.get()

    key = '965863e1ab87fbadd137be58a7b3b6e7'
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    info['text'] = f'{str(weather["name"])}: {weather['main']['temp']}'

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.title('WeatheR')
app.geometry('300x250')



frame_top = customtkinter.CTkFrame(master=app)
frame_top.pack(pady=20, padx=60, fill="both", expand=True)

# frame_bottom = customtkinter.CTkFrame(master=app)
# frame_bottom.pack(pady=0.15, padx=0.15)

cityField = customtkinter.CTkEntry(master=frame_top)
cityField.pack(pady=15)

info = customtkinter.CTkLabel(master=frame_top, text='Введите название города')
info.pack(pady=30)

btn = customtkinter.CTkButton(master=frame_top, text='Узнать погоду!', command=get_weather, border_color="white")
btn.pack()

app.mainloop()