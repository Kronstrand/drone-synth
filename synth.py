import numpy as np
import sounddevice as sd
from scipy import signal
import pygame, sys

print("")
print("")
print("      • ▌ ▄ ·.              ▐ ▄ .▄▄ · ▄▄▄▄▄       ▐ ▄ ▄▄▄ .")    
print("      ·██ ▐███▪▪     ▪     •█▌▐█▐█ ▀. •██  ▪     •█▌▐█▀▄.▀·")    
print("      ▐█ ▌▐▌▐█· ▄█▀▄  ▄█▀▄ ▐█▐▐▌▄▀▀▀█▄ ▐█.▪ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄")    
print("      ██ ██▌▐█▌▐█▌.▐▌▐█▌.▐▌██▐█▌▐█▄▪▐█ ▐█▌·▐█▌.▐▌██▐█▌▐█▄▄▌")    
print("      ▀▀  █▪▀▀▀ ▀█▄▀▪ ▀█▄▀▪▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀█▄▀▪▀▀ █▪ ▀▀▀")     
print("      .▄▄ ·  ▄· ▄▌ ▐ ▄ ▄▄▄▄▄ ▄ .▄▄▄▄ ..▄▄ · ▪  ·▄▄▄▄•▄▄▄ .▄▄▄")  
print("      ▐█ ▀. ▐█▪██▌•█▌▐█•██  ██▪▐█▀▄.▀·▐█ ▀. ██ ▪▀·.█▌▀▄.▀·▀▄ █·")
print("      ▄▀▀▀█▄▐█▌▐█▪▐█▐▐▌ ▐█.▪██▀▐█▐▀▀▪▄▄▀▀▀█▄▐█·▄█▀▀▀•▐▀▀▪▄▐▀▀▄") 
print("      ▐█▄▪▐█ ▐█▀·.██▐█▌ ▐█▌·██▌▐▀▐█▄▄▌▐█▄▪▐█▐█▌█▌▪▄█▀▐█▄▄▌▐█•█▌")
print("       ▀▀▀▀   ▀ • ▀▀ █▪ ▀▀▀ ▀▀▀ · ▀▀▀  ▀▀▀▀ ▀▀▀·▀▀▀ • ▀▀▀ .▀  ▀")
print("")
print("") 


pygame.init()
# set the pygame window name 
pygame.display.set_caption('Moonstone Synthesizer')
width = 320
height = 240
screen = pygame.display.set_mode((width, height))

white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128)
cyan = (0, 255, 255)

font = pygame.font.Font('fonts/manaspc.ttf', 10) # font by codeman38
text = font.render('The moonstone synth is here', True, green)
  
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (width // 2, height // 2) 



waveforms = []

# waveform values
n_samples = 4410
hz = 50
t = np.linspace(0, 1, n_samples)
volume = 0.4

# play values
sps = 44100 #samples per second, 44.1 khz, cd quality

# create waveforms
waveforms.append(signal.sawtooth(2 * np.pi * 15 * t)) #15 hz
waveforms.append(signal.sawtooth(2 * np.pi * 50 * t)) #50 hz
waveforms.append(signal.sawtooth(2 * np.pi * 2 * t)) #2 hz
waveforms.append(signal.sawtooth(2 * np.pi * 8 * t)) #8 hz

# combine all waveforms
def combineWaveforms(waveforms):
    waveform = waveforms[0]
    n_waveforms = len(waveforms)
    for i in range(1, n_waveforms):
        waveform += waveforms[i]
    waveform = waveform / n_waveforms
    return waveform

waveform = combineWaveforms(waveforms)
attinuated_waveform = waveform * volume

sd.play(attinuated_waveform, sps, loop=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(text, textRect)
    pygame.display.update()
sd.stop()        




