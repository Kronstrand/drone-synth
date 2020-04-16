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

from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import time

waveforms = []

# waveform values
n_samples = 4410
hz = 50
t = np.linspace(0, 1, n_samples)

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

# play waveform
sd.play(waveform, sps, loop=True)
time.sleep(2)
sd.stop()        




