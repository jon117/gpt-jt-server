from transformers import AutoTokenizer, AutoModelForCausalLM

#load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/GPT-JT-6B-v1")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/GPT-JT-6B-v1")

#this will download the models so we don't have to do it every time :D