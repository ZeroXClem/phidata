#!/bin/bash

# Activate conda
source ~/miniconda3/etc/profile.d/conda.sh

# Activate the phidata environment
conda activate phidata

# Navigate to the script directory
# Navigate to the script directory
cd /home/btw/github.com/ZeroXClem/phidata/cookbook/llms/claude

# Run the stock research automation script
python stock_research_automation.py

# Deactivate the conda environment
conda deactivate