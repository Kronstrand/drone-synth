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

controls_margin = 10

font = pygame.font.Font('fonts/manaspc.ttf', 10) # font by codeman38
font_symbols = pygame.font.Font('freesansbold.ttf', 10)
text = font.render('The moonstone synth is here', True, green)

  
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (width // 2, height // 2) 

vol_text = font.render('Volumne', True, green)
vol_text_rect = vol_text.get_rect()
vol_text_rect.right = width - 70
vol_text_rect.top = height - 30

vol_text_bar = font_symbols.render("||||||", True, green)
vol_text_bar_rect = vol_text.get_rect()
vol_text_bar_rect.left = vol_text_rect.right + controls_margin # set relative to volume text
vol_text_bar_rect.top = height - 30

waveforms = []

# waveform values
n_samples = 4410
hz = 50
t = np.linspace(0, 1, n_samples)
volume = 0.1

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

key_sensitivity = 0.3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if volume + key_sensitivity > 1:
                    volume = 1
                else:
                    volume += key_sensitivity
            if event.key == pygame.K_DOWN:
                if volume - key_sensitivity < 0:
                    volume = 0
                else:
                    volume -= key_sensitivity
    
    #render visuals
    screen.blit(text, textRect)
    screen.blit(vol_text, vol_text_rect)
    screen.blit(vol_text_bar, vol_text_bar_rect)

    pygame.display.update()
sd.stop()        




