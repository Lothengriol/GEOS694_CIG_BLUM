#!/bin/bash
#SBATCH --job-name=dem_check
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:05:00
#SBATCH --output=dem_check_%j.out
#SBATCH --error=dem_check_%j.err

python checks.py

echo "DEM check complete!"
