import tiktoken


encoder = tiktoken.encoding_for_model('gpt-4o')

print("Vocab Size", encoder.n_vocab)

text = "The cat sat on the mat"

tokens = encoder.encode(text)

print("Tokens", tokens)

decode = encoder.decode(tokens)

print("Text", decode)