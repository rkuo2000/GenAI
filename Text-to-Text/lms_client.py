import lmstudio as lms

model = lms.llm("openai/gpt-oss-20b")
result = model.respond("What is the meaning of life?")

print(result)
