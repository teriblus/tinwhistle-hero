import unittest
import sound

song = sound.Song('/home/lecorgnt/Bureau/perso/tinwhistlehero/doremi.mp3')

class sound_test(unittest.TestCase):
    def translate_frequency_to_note_test(self):
        self.assertEqual(song.translate_frequency_to_note(500), 0)
        self.assertEqual(song.translate_frequency_to_note(620), 0)
        self.assertEqual(song.translate_frequency_to_note(800), 3)
        self.assertEqual(song.translate_frequency_to_note(810), 3)
        self.assertEqual(song.translate_frequency_to_note(990), 5)
        self.assertEqual(song.translate_frequency_to_note(1200), 5)

    def get_note_test(self):
        self.assertEqual(song.get_note(5000),0)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
