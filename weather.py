import subprocess
import sys
import tkinter as tk #this is a GUI kit
import time
import requests

def install(package): #copied a script or function intall the Import request
    subprocess.check_call([sys.executable,"-m", "pip", "install", package])

try:
    import requests
except ImportError:
    install("requests")
    
def getWeather(window):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=880b6a7cd415b87ca46867f8df99c4a0"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main'] 
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']))

    final_info = condition + "\n" + str(temp) + "C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure" + str(pressure) + "\n" + "Humidity" + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


window = tk.Tk()
window.geometry("1920x1080")
window.title("Natalies Weather App")

f = ("poppins", 15, "bold") #asinging variable to a font to make it easier to just plug in
t = ("poppins", 35, "bold")

textfield = tk.Entry(window, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind("<Return>", getWeather)

label1 = tk.Label(window,font = t)
label1.pack()

label2 = tk.Label(window,font = f)
label2.pack()

window.mainloop()#this runs the window itself
