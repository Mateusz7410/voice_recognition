__author__ = 'mateu'


from scipy.signal import decimate
from scipy import *
import scipy.io.wavfile
import numpy as np

if __name__ == "__main__":
    filenames = ["train/026_M.wav", "train/004_M.wav","train/005_M.wav","train/007_M.wav","train/023_M.wav","train/011_M.wav","train/013_M.wav","train/027_M.wav","train/019_M.wav","train/020_M.wav",
                "train/003_K.wav", "train/006_K.wav","train/008_K.wav","train/009_K.wav","train/012_K.wav","train/014_K.wav","train/025_K.wav","train/028_K.wav","train/018_K.wav","train/022_K.wav"]

    for filename in filenames:
        w, signal = scipy.io.wavfile.read(filename)
        if signal.ndim > 1:
            signal = [i[1] for i in signal]
        #fig = plt.figure(figsize=(15, 6), dpi=80)
        signal = signal * np.kaiser(len(signal), 100)
        fftSig = abs(fft(signal))
        #ax = fig.add_subplot("611")
        #ax.set_xlim(0,1000)
        #ax.plot(fftSig)

        '''for i in range(2,7):
            #yo = 610 + i
            #ax = plt.subplot(yo)
            tmp = copy(fftSig)
            d = decimate(tmp, int(i))
            tmp[:len(d)] = d
            #ax.set_xlim(0,1000)
            #ax.plot(tmp)'''
        d = decimate(fftSig, 6)
        fftSig[:len(d)] = d

        fftSig = fftSig[80:260]
        #print(np.argmax(tmp) + 80)
        if(np.argmax(fftSig) + 80) > 85 and (np.argmax(fftSig) + 80) < 155:
            print('M')
        else:
            print("K")

        #show()