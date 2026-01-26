# pip install google.genai

from google import genai
client = genai.Client(http_options={'api_version': 'v1beta'})

response = client.models.generate_content(
#    model="gemini-3-flash-preview",
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words"
)

print(response.text)
