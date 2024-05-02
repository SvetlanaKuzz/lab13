import tkinter as tk
import requests
class Joke:
    def __init__(self, root):
        self.root = root
        self.root.title("Английские анекдоты") #Устанавливаем заголовок главного окна
        self.root.geometry("400x200")  # Задаем размер окна
        self.root.minsize(400, 200)  # Задаем минимальный размер окна
        self.root.configure(bg='lavender') #Фон
        self.joke_label = tk.Label(self.root, text="", font=("Arial", 14), bg='lavender', wraplength=350, justify="center") #определяет максимальную ширину текста
        self.joke_label.pack(pady=20)
        self.get_joke_button = tk.Button(self.root, text="Получить анекдот", command=self.get_joke)
        self.get_joke_button.pack()
    def get_joke(self):
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        joke_data = response.json()
        joke = f"{joke_data['setup']}\n{joke_data['punchline']}"
        self.joke_label.config(text=joke)
def main():
    root = tk.Tk()
    app = Joke(root)
    root.mainloop()
if __name__ == "__main__": #запуск функции main в случае, если файл запускается как основная программа
    main()