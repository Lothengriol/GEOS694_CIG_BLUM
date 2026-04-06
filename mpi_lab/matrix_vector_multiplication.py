from mpi4py import MPI
import numpy as np

def matrix_vector_mpi():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    N = size

    if rank == 0:
        A = np.random.randint(0, 10, size=(N, N)).astype(float)
        x = np.random.randint(0, 10, size=N).astype(float)
        rows = [A[i, :] for i in range(N)]
    else:
        A = None
        x = None
        rows = None

    local_row = comm.scatter(rows, root=0)
    x = comm.bcast(x, root=0)
    local_y = np.array([np.dot(local_row, x)], dtype=float)
    
    comm.Barrier()

    if rank == 0:
        y = np.empty(N, dtype=float)
        req = comm.Igather(local_y, y, root=0)
    else:
        req = comm.Igather(local_y, None, root=0)

    req.Wait()

    if rank == 0:
        for i in range(N):
            row_str = " ".join(f"{val}" for val in A[i])
            x_str = " ".join(f"{val}" for val in x)
            print(f"[{row_str}] * [{x_str}] = {y[i]}")

matrix_vector_mpi()