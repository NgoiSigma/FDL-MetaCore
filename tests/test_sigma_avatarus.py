import unittest
from sigma_avatarus.sigma_avatarus import SigmaAvatarus

class TestSigmaAvatarus(unittest.TestCase):
    def setUp(self):
        self.avatar = SigmaAvatarus()

    def test_awaken(self):
        response = self.avatar.awaken()
        self.assertIn("пробуждён", response)

    def test_process_input_logical(self):
        phrase = "Свет возникает из тьмы как противоположность, но не враг."
        output = self.avatar.process_input(phrase)
        self.assertIn("interpretation", output)
        self.assertIn("resonance", output)

    def test_empty_input(self):
        output = self.avatar.process_input("")
        self.assertIsInstance(output, dict)
        self.assertTrue(len(output["interpretation"]) == 0)

if __name__ == "__main__":
    unittest.main()
