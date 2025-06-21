import os
import webbrowser
import time

cold="https://c.tenor.com/8UJ-00rQuAwAAAAd/tenor.gif"
hot= "https://thebulletin.org/wp-content/uploads/2022/10/blast-wave.2022-10-19-13_46_33.gif"

uwu=input("do you like the heat or the cold better?: ")

def response():
    if "cold" in uwu:
        print(" ")
        print("you're a reasonable person! i think you're great :D")
        print(" ")
        time.sleep(7)
        webbrowser.open(cold)
        
        
    elif "heat" in uwu:
        print(" ")
        print("you're mean, get what u deserve :/")
        print(" ")
        time.sleep(10)
        webbrowser.open(hot)
        
        
        try:       
            time.sleep(6)
            os.system("shutdown -h now")
        finally:
            time.sleep(6)
            os.system("shutdown /s /t 0")

response()
    
