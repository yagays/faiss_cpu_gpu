# Faiss CPU vs. GPU

## Benchmark

### GPU
```shell
$ time poetry run python similarity_search_gpu.py
[[      0       1       7 ...      15       4      13]
 [      1      10       0 ...      13       5       2]
 [      2       5       3 ...       1       6      13]
 ...
 [3197453 3195315 3195856 ... 3180839 1817620 1549199]
 [3197454 3195644 3196672 ... 2462337 3029141 2637080]
 [3197455 3194839 3195101 ... 2402276 3195618 3195049]]
poetry run python similarity_search_gpu.py  281.09s user 168.50s system 100% cpu 7:26.23 total
```

### CPU
```shell
$ time poetry run python similarity_search_cpu.py
[[      0       1       7 ...      15       4      13]
 [      1      10       0 ...      13       5       2]
 [      2       5       3 ...       1       6      13]
 ...
 [3197453 3195315 3195856 ... 3180839 1817620 1549199]
 [3197454 3195644 3196672 ... 2462337 3029141 2637080]
 [3197455 3194839 3195101 ... 2402276 3195618 3195049]]
poetry run python similarity_search_cpu.py  752784.61s user 132.06s system 1124% cpu 18:36:19.62 total
```

### Results

| Method | Device | Time (hh:mm:ss) | 
| --- | ---|  -- | 
| GPU |GTX 3090 (Mem:24GB) | 00:07:26 | 
| CPU| Ryzen 9 5900 (12core/24thread)| 18:36:19| 

## Spec

- Ubuntu 22.04
- CUDA: 11.8
