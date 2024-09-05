from transformers import pipeline
classifier = pipeline("sentiment-analysis")
res = classifier("I cant bear it anymore.")
print(res)
