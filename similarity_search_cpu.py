import faiss
import gensim

model = gensim.models.KeyedVectors.load("data/chive-1.2-mc5_gensim/chive-1.2-mc5.kv")
vectors  = model.vectors

d = vectors.shape[1]  # 300
k = 10

index = faiss.IndexFlatL2(d)
index.add(vectors)

D, I = index.search(vectors, k)
print(I)