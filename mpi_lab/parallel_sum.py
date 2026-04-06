from mpi4py import MPI
import numpy as np

def simple_sum(N):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        data = np.arange(1, N + 1, dtype=np.int64)
        chunks = np.array_split(data, size) 
    else:
        chunks = None

    # precomputes the distributed sum
    local_chunk = comm.scatter(chunks, root=0)
    local_sum = np.sum(local_chunk, dtype=np.int64)
    distributed_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    if rank == 0:
        check = N * (N + 1) // 2
        print(f"The sum of 1-{N} is {distributed_sum} == {check}.")


for N in (10, 1000, 10000):
    simple_sum(N)