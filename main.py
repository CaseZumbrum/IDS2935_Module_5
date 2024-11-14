import speech_recognition as sr

from transformers import pipeline
import pygame

# Other options for the LLM, the 135m and 360m are much smaller (faster), but do not reliably produce a parsable output

#pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct", device="cuda")
#pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M-Instruct", device="cuda")
pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct", device="cuda")

# Initialize the recognizer 
r = sr.Recognizer() 

messages = [
{"role": "system", "content": "Whatever a user says to you, provide a list of three possible responses to their sentence following standard python list syntax."},
]
    
# Loop infinitely for user to
# speak
print("ready")
pygame.init()

screen = pygame.display.set_mode((1920, 1200))
pygame.display.set_caption("Design Challenge")
screen.fill((255,255,255))
pygame.display.flip()

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
