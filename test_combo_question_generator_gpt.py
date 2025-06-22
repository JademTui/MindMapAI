import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from modules.combo_question_generator import ComboQuestionGenerator

def test_gpt4mini_filter():
    # Ensure the API key is set
    api_key = os.getenv("OPENAI_API_KEY")
    assert api_key, "OPENAI_API_KEY environment variable must be set for this test."
    
    # Simple educational context
    context = "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods from carbon dioxide and water."
    
    # Instantiate with GPT-4.1 mini filtering enabled
    generator = ComboQuestionGenerator(use_gpt_filter=True)
    questions = generator.generate(context)
    print("Filtered questions by GPT-4.1 mini:")
    for q in questions:
        print("-", q)
    # Basic sanity check: should return a list of strings
    assert isinstance(questions, list)
    assert all(isinstance(q, str) for q in questions)
    assert len(questions) > 0

if __name__ == "__main__":
    test_gpt4mini_filter()
