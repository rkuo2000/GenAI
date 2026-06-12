import lmstudio as lms

model = lms.llm("google/gemma-4-31b-qat")
result = model.respond("What is the meaning of life?")

print(result)
