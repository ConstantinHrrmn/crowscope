from constants import Adafruit_DHT,temp,temp_sensor_type

def Start():
    humidity, temperature = Adafruit_DHT.read_retry(temp_sensor_type,temp)

    while humidity < 80:
        humidity, temperature = Adafruit_DHT.read_retry(temp_sensor_type,temp)
        
    print("Humidité au dessus de 80")
    
def Enigme():
    return "Quand le thé est chaud, il faut souffler sur la boite bleue."
    