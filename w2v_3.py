from gensim.models import word2vec
from w2v_2 import word_list

model = word2vec.Word2Vec(word_list, vector_size=100, window=5, min_count=5, workers=4)
model.save("gingatetsudo.model")

#ベクトルの表示がうまくいかない
print(model.wv["みなさん"])