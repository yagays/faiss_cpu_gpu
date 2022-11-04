import faiss
import gensim

model = gensim.models.KeyedVectors.load("data/chive-1.2-mc5_gensim/chive-1.2-mc5.kv")
vectors  = model.vectors

d = vectors.shape[1]  # 300
k = 10

gpu_resource = faiss.StandardGpuResources()
cpu_index = faiss.IndexFlatL2(d)
gpu_index = faiss.index_cpu_to_gpu(gpu_resource, 0, cpu_index)
gpu_index.add(vectors)

D, I = gpu_index.search(vectors, k)
print(I)