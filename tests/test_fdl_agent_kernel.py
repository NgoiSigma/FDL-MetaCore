import unittest
from fdl_agent_kernel.contradiction_solver import ContradictionSolver
from fdl_agent_kernel.dialectical_flow import DialecticalFlow

class TestFDLAgentKernel(unittest.TestCase):
    def setUp(self):
        self.solver = ContradictionSolver()
        self.flow = DialecticalFlow()

    def test_resolve_contradiction(self):
        thesis = "Индивидуум важен"
        antithesis = "Коллектив важнее"
        result = self.solver.resolve(thesis, antithesis)
        self.assertIn("синтез", result.lower())

    def test_generate_flow(self):
        context = "Украина, самоуправление, ресурсная автономия"
        result = self.flow.generate(context)
        self.assertIsInstance(result, dict)
        self.assertIn("тезис", result)
        self.assertIn("антитезис", result)
        self.assertIn("синтез", result)

if __name__ == '__main__':
    unittest.main()
