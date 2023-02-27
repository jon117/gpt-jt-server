
from transformers import pipeline

pipe = pipeline(model='togethercomputer/GPT-JT-6B-v1')

while True:
    
    data = input('Ask GPT a question: ')

    if data == 'exit':
        break

    result = pipe(data)
    print(result)