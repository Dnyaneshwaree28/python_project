




from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("C:/Users/sansk/Downloads/water_sound.wav", "stop")
    init_water = time()
    init_break = time()
    init_exercise = time()
    watersecs = 3
    exsecs = 10
    breaksec = 20

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('C:/Users/sansk/Downloads/water_sound.wav', 'drank')
            init_water = time()
            log_now("Drank Water at")

        if time() -init_exercise >exsecs :
            print("Exercise time. Enter 'donex' to stop the alarm.")
            musiconloop('C:/Users/sansk/Downloads/count_down.wav', 'donex')
            init_eyes = time()
            log_now("Relaxed at")

        if time() - init_break > breaksec :
            print("Other Activity Time. Enter 'done' to stop the alarm.")
            musiconloop('C:/Users/sansk/Downloads/alarm.wav', 'done')
            init_exercise = time()
            log_now("Break done at")









    




