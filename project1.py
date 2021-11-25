import time

# countdown timer 

def meditation_timer(t):
    t = 60
    while t > 0: # while t > 0 for clarity 
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r")
      time.sleep(1)
      t -= 1
    print('Well Done!')



username=input("Hi, I am ploo, your personal mental health assistant. What can i call you?")

emotions_1=["anxious","angry","happy","sad","frustated","calm"]

emotion = input('How are you feeling today? \n Choose one of the following emotions: \n Anxious \n Angry \n Happy \n Sad \n Frustrated \n Pensive ')

user_emotions = emotion.lower()

if user_emotions in emotions_1:
    a = input("why are you feeling this way?")
    
    if user_emotions == "anxious":
        print("I am so sorry to hear that",username)
        print(input("Am you worrying just to worry?"))
        print(input("Are you fears based in reality?"))
        print(input(""))
        print('Try to take deep breaths')
        meditation_timer(t)
    
