#!/bin/bash
#SBATCH --partition=debug
#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --job-name="hello world!"
#SBATCH --output=%j_%x.out
#SBATCH --time=00:00:05

# --- Commands ---
srun echo "Hello"
srun echo $SLURM_JOB_NODELIST
srun echo $SLURM_JOB_CPUS_PER_NODE
srun sleep 10
srun echo "World!"
