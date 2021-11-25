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



username=input("Hi, I am ploo, your personal mental health assistant. What can I call you?")

emotions_1=["anxious","angry","happy","sad","frustated"]

emotion = input('Hi '+username+', How are you feeling today? \n Choose one of the following emotions: \n Anxious \n Angry \n Happy \n Sad \n Frustrated')

user_emotions = emotion.lower()

if user_emotions in emotions_1:
    a = input("why are you feeling this way?")
    
    if user_emotions == "anxious":
        print("I am so sorry to hear that",username)
        print(input("Are you worrying just to worry?"))
        print(input("How do you know your thoughts are true?"))
        print(input("What are the chances the thing you are worrying about will actually happen?"))
        print(input("What can be the worst possible outcome?"))
        print('Try to take deep breaths')
        meditation_timer(t)
    elif user_emotions=="angry":
        print("I am so sorry to hear that",username)
        print(input("Does this feeling make your situation better?"))
        print(input(""))
        print(input(""))
        print(input(""))
        print('Try to take deep breaths')
        meditation_timer(t)

    elif user_emotions=="happy":
        print("Thats good to hear!")
        print(input(""))
        print(input(""))
        print(input(""))
        print(input(""))
        print("Have a great day!")
    elif user_emotions=="sad":
        print("I am so sorry to hear that",username)
        print(input(""))
        print(input(""))
        print(input(""))
        print(input(""))
        print("I hope this makes you feel refresehed!")
    elif user_emotions=="frustated":
        print("I am so sorry to hear that",username)
        print(input(""))
        print(input(""))
        print(input(""))
        print(input(""))
        print('Try to take deep breaths')
        meditation_timer(t)

    
