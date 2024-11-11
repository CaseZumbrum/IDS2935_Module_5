# Python program to translate
# speech to text and text to speech


import speech_recognition as sr

from transformers import pipeline

pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct", device="cuda")

# Initialize the recognizer 
r = sr.Recognizer() 

messages = [
{"role": "system", "content": "Whatever a user says to you, provide a list of three possible responses to their sentence following standard python list syntax."},
]
    
# Loop infinitely for user to
# speak
print("ready")
while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            messages.append({"role": "user", "content": MyText})
            print("Did you say ",MyText)
            print(pipe(messages))
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")
