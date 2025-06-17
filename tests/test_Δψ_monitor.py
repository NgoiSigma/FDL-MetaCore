import unittest
from modules.Δψ_monitor.lie_tension_analyzer import analyze_lie_tension

class TestLieTensionAnalyzer(unittest.TestCase):
    def test_simple_case(self):
        text = "Заявление о мире сопровождается поставками оружия."
        result = analyze_lie_tension(text)
        self.assertIsInstance(result, dict)
        self.assertIn("tension_score", result)
        self.assertGreaterEqual(result["tension_score"], 0.0)
        self.assertLessEqual(result["tension_score"], 1.0)

    def test_empty_input(self):
        result = analyze_lie_tension("")
        self.assertEqual(result["tension_score"], 0.0)

if __name__ == '__main__':
    unittest.main()
