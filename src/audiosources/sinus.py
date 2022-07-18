from dataclasses import dataclass, field
from typing import List
from scipy.io.wavfile import write
import numpy as np

@dataclass
class Sinus:
    f: float = 440.0 # Frequency
    rate: int = 44100 # Sampling rate (Hz)
    d : int = 2 # Duration of sample (s)
    a : float = 1.0 # Amplitude of the sample
    data : List[float] = field(init=False)

    def __post_init__(self):
        self.data = [self.a*np.sin(2*np.pi*self.f*x/self.rate) for x in range(self.d*self.rate)]

    def save(self, path : str = 'test.wav'):
        scaled = np.int16(self.data / np.max(np.abs(self.data)) * 32767)
        write(path, self.rate, scaled)

