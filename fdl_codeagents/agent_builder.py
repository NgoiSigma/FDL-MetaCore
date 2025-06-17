# FDL Code Agent Constructor for OpenAI Integrations
from fdl_agent_kernel.fdl_navigator import FDLNavigator
import openai

class FDLCodeAgent:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.navigator = FDLNavigator()

    def run_dialogue(self, statement_a: str, statement_b: str):
        syn = self.navigator.navigate(statement_a, statement_b)
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "FDL Agent Initiated"},
                {"role": "user", "content": syn}
            ]
        )
        return response['choices'][0]['message']['content']
