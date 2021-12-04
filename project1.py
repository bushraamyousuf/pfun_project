import time

# countdown timer 
t = 10
def meditation_timer(t):
    t = 10
    while t > 0: # while t > 0 for clarity 
      mins = t // 60
      secs = t % 60
      timer = '{:02d}:{:02d}'.format(mins, secs)
      print(timer, end="\r")
      time.sleep(1)
      t -= 1
    print('Well Done!')



username=input("Hi, I am ploo, your personal mental health assistant. What can I call you?")

emotions_1=["anxious","angry","confused","sad","frustated"]

emotion = input('Hi '+username+', How are you feeling today? \n Choose one of the following emotions: \n Anxious \n Angry \n confused \n Sad \n Frustrated')

user_emotions = emotion.lower()

if user_emotions in emotions_1:
    a = input("why are you feeling this way?")
    
    if user_emotions == "anxious":
        print("I am so sorry to hear that",username)
        input("Are you worrying just to worry?")
        input("How do you know your thoughts are true?")
        input("What are the chances the thing you are worrying about will actually happen?")
        input("What can be the worst possible outcome?")
        print('Try to take deep breaths')
        meditation_timer(t)
    elif user_emotions=="angry":
        print("I am so sorry to hear that",username)
        input("Does this feeling make your situation better?")
        input("Are you truely understanding the other person?")
        input("Are your expectations reasonable?")
        input("Is your anger getting you what you want?")
        input("Is your anger out of proportion to the offense?")
        print('Try to take deep breaths')
        meditation_timer(t)

    elif user_emotions=="confused":
        print("Hope you find clarity soon!",username)
        input("What is right with me?")
        input("What’s worse – Failing or never trying, never knowing?")
        input("What expectation do I have from people around me?")
        input("Do I hear my inner voice and listen to my intuition?")
        print("If you can’t get a good grip on life, relax. Be gentle with yourself. You are doing your best!")
        print("Take deep breath")
        meditation_timer(t)      
    elif user_emotions=="sad":
        print("I am so sorry to hear that",username)
        input("Why are you down?")
        input("what positive encounter you had today?")
        input("Is this the hardest thing you have faced today?")
        input("What is the worst that could happen?")
        print("I hope this makes you feel better!")
    elif user_emotions=="frustated":
        print("I am so sorry to hear that",username)
        input("Are you frustrated because you don’t want to admit that you miscalculated, or you didn’t know the answer, or you couldn’t do what you thought you could, etc.?")
        input("What else is possible? How can you change your approach? ")
        input("Will what happened matter in a week? A month? A year?")
        input("Are you as interested in seeing the situation for what it is as you are, in being “right”?")
        print('Try to take deep breaths')
        meditation_timer(t)

    
