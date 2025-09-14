# pip install -qU dspy
# pip install datasets

import os
LLM_API_KEY = os.environ.get("GEMINI_API_KEY")

# Use Ollama local endpoint
import dspy
#lm=dspy.Ollama(model="gemma3")
lm=dspy.LM("gemini/gemini-2.5-flash",api_key=LLM_API_KEY)
dspy.settings.configure(lm=lm)

from datasets import load_dataset
def init_dataset():
    train_split = load_dataset("AI-MO/aimo-validation-aime")['train']
    train_split = [
        dspy.Example({
            "problem": x['problem'],
            'solution': x['solution'],
            'answer': x['answer'],
        }).with_inputs("problem")
        for x in train_split
    ]
    import random
    random.Random(0).shuffle(train_split)
    tot_num = len(train_split)

    test_split = load_dataset("MathArena/aime_2025")['train']
    test_split = [
        dspy.Example({
            "problem": x['problem'],
            'answer': x['answer'],
        }).with_inputs("problem")
        for x in test_split
    ]

    train_set = train_split[:int(0.5 * tot_num)]
    val_set = train_split[int(0.5 * tot_num):]
    test_set = test_split * 5

    return train_set, val_set, test_set

train_set, val_set, test_set = init_dataset()
print(len(train_set), len(val_set), len(test_set))

print("Problem:")
print(train_set[0]['problem'])
print("\n\nSolution:")
print(train_set[0]['solution'])
print("\n\nAnswer:")
print(train_set[0]['answer'])

## A simple dspy.ChainOfThought
class GenerateResponse(dspy.Signature):
    """Solve the problem and provide the answer in the correct format."""
    problem = dspy.InputField()
    answer = dspy.OutputField()

program = dspy.ChainOfThought(GenerateResponse)

### Defining the evaluation metric
def metric(example, prediction, trace=None, pred_name=None, pred_trace=None):
    correct_answer = int(example['answer'])
    try:
        llm_answer = int(prediction.answer)
    except ValueError as e:
        return 0
    return int(correct_answer == llm_answer)

### Evaluating unoptimized Chain Of Thought
evaluate = dspy.Evaluate(
    devset=test_set,
    metric=metric,
    num_threads=32,
    display_table=True,
    display_progress=True
)

evaluate(program)

