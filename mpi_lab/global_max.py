from mpi4py import MPI
import random

def global_max():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    local_value = random.randint(0, 1000)
    global_max_root = comm.reduce(local_value, op=MPI.MAX, root=0)
    global_max = comm.bcast(global_max_root, root=0)

    if local_value == global_max:
            print(f"Rank {rank} has value {local_value} which is the global max {global_max}")
    else:
            print(f"Rank {rank} has value {local_value} which is less than global max {global_max}")

global_max()