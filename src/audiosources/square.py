from dataclasses import dataclass, field
from typing import List
from scipy.io.wavfile import write
import numpy as np

@dataclass
class Square:
    f: float = 440.0 # Frequency
    rate: int = 44100 # Sampling rate (Hz)
    d : int = 2 # Duration of sample (s)
    a : float = 1.0 # Amplitude of the sample
    data : List[float] = field(init=False)

    def __post_init__(self):
        phase = 0
        self.data = []
        for x in range(0, self.d * self.rate):
            phase += 2*np.pi*self.f/self.rate
            if int(phase / np.pi) % 2 == 0:
                self.data.append(self.a)
            else:
                self.data.append(-self.a)

    def save(self, path : str = 'test.wav'):
        scaled = np.int16(self.data / np.max(np.abs(self.data)) * 32767)
        write(path, self.rate, scaled)

