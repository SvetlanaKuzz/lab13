import requests
import tkinter as tk

def get_weather():
    api_key = 'db0f91d6df687d044dfe0dcc944bd034'
    city = city_entry.get()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    weather_data = f'Город: {data["name"]}\nТемпература: {round(data["main"]["temp"]-273)}°C\nПогода: {data["weather"][0]["description"]}'

    weather_label.config(text=weather_data)

root = tk.Tk()
root.title("Погода")
root.geometry("600x400")
root.configure(background='lightblue')

city_label = tk.Label(root, text="Введите название города:", bg='lightblue', font=('Arial', 20), padx=10, pady=50)
city_label.pack()


city_entry = tk.Entry(root, bg='white', font=('Arial', 20))
city_entry.pack()

get_weather_button = tk.Button(root, text="OK", bg='white', font=('Arial', 15), padx=10, pady=10, command=get_weather)
get_weather_button.pack()

weather_label = tk.Label(root, text="", bg='lightblue', font=('Arial', 15), padx=10, pady=50)
weather_label.pack()

root.mainloop()