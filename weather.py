import subprocess
import sys
import tkinter as tk #this is a GUI kit for window and widgets
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
    #im using my own API and if it doesn't show, then the free trial ended... it is what it is!
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

# initiating the window
window = tk.Tk() 
#making the window size
window.geometry("1920x1080")
window.title("Natalies Weather App")

#asinging variable to a font to make it easier to just plug in
f = ("poppins", 15, "bold") 
t = ("poppins", 35, "bold")

#making the textfield widget with working typing feature
textfield = tk.Entry(window, font = t)
#Padding around the text field
textfield.pack(pady = 20)
#the program starts, and the user can start typing immediately without needing to click on the widget first, FOCUSSS
textfield.focus()
#Whenver you hit RETURN on your keyboard, it starts up the getWeather with the value in the textfield
textfield.bind("<Return>", getWeather)


#these are label widgets to display text, for the humidty and sunrise and such
label1 = tk.Label(window,font = t) 
label1.pack()

label2 = tk.Label(window,font = f)
label2.pack()

label3 = tk.Label(window,text="I don't know why am I here...")
label3.pack(side="left")

window.mainloop()#this runs the window itself or making it loop itself forever until you exits
