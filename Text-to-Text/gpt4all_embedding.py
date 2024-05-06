from gpt4all import Embed4All
text = 'Who is Laurens van der Maaten?'
embedder = Embed4All('nomic-embed-text-v1.f16.gguf')
output = embedder.embed(text, prefix='search_query')
print(output)
