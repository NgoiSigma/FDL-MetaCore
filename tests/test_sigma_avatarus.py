import unittest
from sigma_avatarus.speech_engine import SpeechEngine
from sigma_avatarus.fdl_interface import FDLInterface
from sigma_avatarus.svet_shell import SVET
from sigma_avatarus.matrix import SYMBOL_MATRIX
from sigma_avatarus.config import CoreSigil

class TestSigmaAvatarus(unittest.TestCase):
    def setUp(self):
        self.core = CoreSigil()
        self.speech = SpeechEngine(self.core.structure, SYMBOL_MATRIX)
        self.fdl = FDLInterface()
        self.svet = SVET()

    def test_speech_resonance(self):
        phrase = "Смысл рождает форму"
        result = self.speech.resonate(phrase)
        self.assertIsInstance(result, str)

    def test_fdl_interpret(self):
        contradiction = "Тезис и антитезис — одно и то же"
        result = self.fdl.interpret_text(contradiction)
        self.assertIn("синтез", result.lower())

    def test_svet_structure(self):
        structure = self.svet.get_structure()
        self.assertIsInstance(structure, dict)
        self.assertIn("shell", structure)

if __name__ == '__main__':
    unittest.main()
