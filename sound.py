import sys, csv, os

import essentia
import essentia.standard
import essentia.streaming

from pylab import plt, plot, tight_layout, savefig, show, np
from numpy import nan, Infinity


class Song:
    notes = [
        600,
        660,
        740,
        805,
        880,
        1000
    ]

    def __init__(self, filename):
        self.fs = 44100
        self.H = 128
        self.M = 2048

        predominantMelody = essentia.standard.PredominantPitchMelodia(frameSize=self.M, hopSize=self.H)
        self.x = essentia.standard.MonoLoader(filename=filename, sampleRate=self.fs)()

        self.pitch, self.pitchConfidence = predominantMelody(self.x)

    def get_note(self, time):
        """
        return the predominant note in the song at the given time
        :param time: in ms
        :return: note index
        """
        pitchIndex = time * self.fs / 1000 / self.H
        if not 0 < pitchIndex < len(self.pitch) - 1:
            return None
        frequency = self.pitch[pitchIndex]
        if frequency:
            return self.translate_frequency_to_note(frequency)
        return None

    def get_duration(self):
        """
        :return: song duration in ms
        """
        return (len(self.x) * 1000) / self.fs

    @staticmethod
    def translate_frequency_to_note(frequency):
        closestNote = None
        offset = Infinity
        for i in range(0, len(Song.notes)):
            if i == 0:
                if frequency < Song.notes[i + 1]:
                    closestNote = i
                    offset = abs(frequency - Song.notes[i])
            elif i < len(Song.notes) - 1:
                if Song.notes[i - 1] < frequency < Song.notes[i + 1] and offset > abs(frequency - Song.notes[i]):
                    closestNote = i
                    offset = abs(frequency - Song.notes[i])
            elif i == len(Song.notes) - 1:
                if Song.notes[i - 1] < frequency and offset > abs(frequency - Song.notes[i]):
                    closestNote = i
                    offset = abs(frequency - Song.notes[i])
        return closestNote

    def plot_frequencies(self):
        plt.figure(1, figsize=(9.5, 4))
        plt.subplot(2, 1, 1)

        plt.plot(np.arange(self.x.size) / float(self.fs), self.x)
        plt.axis([0, self.x.size / float(self.fs), min(self.x), max(self.x)])
        plt.ylabel('amplitude')
        plt.title('x (carnatic.wav)')

        plt.subplot(2, 1, 2)
        frmTime = self.H * np.arange(self.pitch.size) / float(self.fs)
        self.pitch[self.pitch == 0] = nan
        plot(frmTime, self.pitch, color='g', linewidth=1.5)
        plt.axis([0, self.x.size / float(self.fs), 500, 1200])
        plt.title('prominent melody')

        tight_layout()
        savefig('predominantMelody.png')

        show()
