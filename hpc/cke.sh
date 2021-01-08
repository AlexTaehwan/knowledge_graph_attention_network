#!/usr/bin/bash

#SBATCH --job-name=cke
#SBATCH --output=logs/%x-%j.out
#SBATCH -A ST_GRAPHS
#SBATCH -p shared_dlt
#SBATCH -N 1
#SBATCH --ntasks-per-node=4
#SBATCH --gres=gpu:1
#SBATCH -t 5-23:59:00

module purge
module load cuda/9.2.148 
module load python/anaconda3.2019.3
module load gcc/5.2.0
source /share/apps/python/anaconda3.2019.3/etc/profile.d/conda.sh
source activate kgat

model_type=cke
datasets=("amazon_book" "last-fm" "yelp2018")

REPO_DIR=~/recommendation/knowledge_graph_attention_network
MODEL_DIR=${REPO_DIR}/Model
cd $MODEL_DIR

printf "Running model_type=${model_type} on all datasets"
for dataset in ${datasets[*]}
do
    date
    printf "Running model_type=${model_type} on dataset=${dataset}\n"
    python Main.py \
        --model_type $model_type \
        --alg_type bi \
        --dataset $dataset \
        --regs [1e-5,1e-5] \
        --layer_size [64,32,16] \
        --embed_size 64 \
        --lr 0.0001 \
        --epoch 1000 \
        --verbose 50 \
        --save_flag 1 \
        --pretrain -1 \
        --batch_size 1024 \
        --node_dropout [0.1] \
        --mess_dropout [0.1,0.1,0.1] \
        --use_att True \
        --use_kge True
done
printf "Finished"
