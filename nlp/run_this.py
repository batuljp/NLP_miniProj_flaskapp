from summarize import summarize

text = "Alice and Bob are friends. Alice is fun and cuddly. Bob is cute and quirky. Together they go on wonderful adventures in the land of tomorrow. Alice's cuddliness and Bob's cuteness allow them to reach their goals. But before they get to them, they have to go past their mortal enemy — Mr. Boredom. He is ugly and mean. They will surely defeat him. He is no match for their abilities."
sentence_count = 2
language = 'english'
summary = summarize(text, sentence_count, language='english')

print(summary)