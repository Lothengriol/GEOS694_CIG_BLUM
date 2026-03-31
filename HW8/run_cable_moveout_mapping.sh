#!/bin/bash
#SBATCH --job-name=cable_moveout_mapping
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --time=00:10:00
#SBATCH --output=cable_moveout_mapping_%j.out


source ~/.bashrc
conda activate GEOS694
python cable_moveout_mapping.py

