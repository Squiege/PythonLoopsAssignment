#Task 1 - Double Scoop with Nested Loops
import random

moods = ["Happy", "Sad", "Angry", "Frustrated"]
tod = ["Morning", "Afternoon", "Evening"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in days:
    for a in tod:
        for mood in moods:
            chosen_mood = random.choice(moods)
        print("On", i, a, "you were feeling", chosen_mood)