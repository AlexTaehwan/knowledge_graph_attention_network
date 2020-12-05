# Not complete, uploading to test forked repo
REPO_DIR=~/recommendation/knowledge_graph_attention_network
cd $REPO_DIR
python Main.py --model_type kgat --alg_type bi --dataset yelp2018 --regs [1e-5,1e-5] --layer_size [64,32,16] --embed_size 64 --lr 0.0001 --epoch 1000 --verbose 50 --save_flag 1 --pretrain -1 --batch_size 1024 --node_dropout [0.1] --mess_dropout [0.1,0.1,0.1] --use_att True --use_kge True
