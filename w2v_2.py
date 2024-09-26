from w2v_1 import text
from janome.tokenizer import Tokenizer

t = Tokenizer()
text = text

def extract_words(text:str) -> list[str]:
    tokens = t.tokenize(text)
    return [token.base_form for token in tokens
            if token.part_of_speech.split(",")[0] in ["名詞","動詞"]]

sentences = text.split("。")
word_list = [extract_words(sentence) for sentence in sentences]

for word in word_list[0]:
    print(word)