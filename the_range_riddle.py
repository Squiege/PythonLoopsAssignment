#Task 1 - Range Riddle
import random

moods = [ "Happy", "Sad", "Energetic", "Calm" ]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

i = 0

for i in days:
    selected_day = [i]
    for mood in moods:
        select_mood = random.choice(moods)
    print("On", i, "you were feeling", select_mood)

