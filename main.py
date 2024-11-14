import speech_recognition as sr
import json
from transformers import pipeline
import pygame

# Other options for the LLM, the 135m and 360m are much smaller (faster), but do not reliably produce a parsable output

#pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct", device="cuda")
#pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-360M-Instruct", device="cuda")
pipe = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct")

# Initialize the recognizer 
r = sr.Recognizer() 

messages = [
{"role": "system", "content": "Whatever a user says to you, provide a list of three possible responses to their sentence following standard python list syntax."},
]
    
# Loop infinitely for user to
# speak
print("ready")

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Design Challenge")
screen.fill((255,255,255))
img = pygame.image.load("glasses.jpg")
img = pygame.transform.scale(img, (1000,700))
screen.blit(img, (0,0))

pygame.font.init() 
my_font = pygame.font.SysFont('Times New Roman MS', 20)


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
            o = pipe(messages)
            try:
                o = json.loads(o)
                if(type(o) == list and len(o) >= 3):
                        one_surface = my_font.render('1. ' + o[0], False, (0, 0, 0))
                        screen.blit(one_surface, (175,250))
                        one_surface = my_font.render('2. ' + o[1], False, (0, 0, 0))
                        screen.blit(one_surface, (175,270))
                        one_surface = my_font.render('3. ' + o[2], False, (0, 0, 0))
                        screen.blit(one_surface, (175, 290))

                        pygame.display.flip()
            except json.JSONDecodeError:
                pass
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")
