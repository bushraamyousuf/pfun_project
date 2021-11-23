username=input("Hi, I am ploo, your personal mental health assistant. What can i call you?")

emotions_1=["anxious","angry","happy","sad","frustated","calm"]

emotion = input('How are you feeling today? \n Choose one of the following emotions: \n Anxious \n Angry \n Happy \n Sad \n Frustrated \n Pensive ')

user_emotions = emotion.lower()
#print(x)

if user_emotions in emotions_1:
    a = input("why are you feeling this way?")
    
    if user_emotions == "anxious":
        print("I am so sorry to hear that",username)
        print(input("Am you worrying just to worry?"))
        print(input("Are you fears based in reality?"))
        print(input(""))
        print('Try to take deep breaths')
    