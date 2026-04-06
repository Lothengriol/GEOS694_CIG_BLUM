import sys
import random
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size == 1:
    n = random.randint(1, 10)
    
    message = {'parts': ['hello world!', n], 'current': n}
    message['parts'].append('goodbye world!')

    print(' '.join(str(x) for x in message['parts']))
    sys.exit(0)

if rank == 0:
    n = random.randint(1, 10)
    
    message = {'parts': ['hello world!', n], 'current': n}
    comm.send(message, dest=1, tag=10)
    
    final_message = comm.recv(source=size - 1, tag=11)
    print(' '.join(str(x) for x in final_message['parts']))

elif 1 <= rank <= size - 2:
    message = comm.recv(source=rank - 1, tag=10)
    next_value = message['current'] * rank

    message['parts'].append(next_value)
    message['current'] = next_value 

    comm.send(message, dest=rank + 1, tag=10)

elif rank == size - 1:
    message = comm.recv(source=rank - 1, tag=10)
    next_value = message['current'] * rank

    message['parts'].append(next_value)
    message['current'] = next_value 
    message['parts'].append('goodbye world!')

    comm.send(message, dest=0, tag=11)