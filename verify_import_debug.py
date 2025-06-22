# Minimal import test for question_generator
import sys
print('sys.path:', sys.path)
try:
    from question_generator import QuestionGenerator
    print('✅ Import succeeded: QuestionGenerator is available.')
except Exception as e:
    print('❌ Import failed:', e)