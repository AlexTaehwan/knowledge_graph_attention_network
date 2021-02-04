from collections import Counter
from pathlib import Path



def read_user_items(path):
    user_items = dict()
    num_lines = 0
    with open(path, 'r') as f:
        for line in f:
            num_lines += 1
            tokens = line.split()
            user = tokens[0]
            items = tokens[1:]
            items = [int(x) for x in items]
            user_items[str(user)] = items
    print(f"num_lines: {num_lines}")
    return user_items


def dump_user_items(path, user_items):
    print(f"Dumping {len(user_items)} users to {path}")
    with open(path, 'w') as f:
        for user, user_items in user_items.items():
            user_items = [str(x) for x in user_items]
            user_items_str = " ".join(user_items)
            write_str = f"{user} {user_items_str}"
            f.write(f"{write_str}\n")

def filter_out_test_items(train_data, test_data):
    clean_train_data = dict()
    c = Counter()
    # iterate over training data user items
    for user in train_data.keys():
        train_items = set(train_data[user])
        test_items = set(test_data[user])
        clean_train_items = train_items.difference(test_items)
        if len(clean_train_items) < len(train_items):
            print(f"Duplicates found for user: {user}")
            c['removed_items'] += 1
            #import pdb;pdb.set_trace()
        else:
            c['kept_items'] += 1
        clean_train_data[user] = clean_train_items

    print(c)
    return clean_train_data


def main():
    repo_dir = "/people/hamc649/recommendation/knowledge_graph_attention_network"
    data_dir = f"{repo_dir}/Data"
    dataset = 'amazon-book'
    dataset_dir = f"{data_dir}/{dataset}"
    clean_data_dir = f"{repo_dir}/clean_data"
    output_dir = f"{clean_data_dir}/{dataset}"
    print(f"Making sure output_dir: {output_dir} exists")
    Path(output_dir).mkdir(parents=True, exist_ok=True)


    # Read in input train data
    train_data_path = f"{dataset_dir}/train.txt"
    train_data = read_user_items(train_data_path)

    # Read in input test data
    test_data_path = f"{dataset_dir}/test.txt"
    test_data = read_user_items(test_data_path)

    # Filter out items from train that are in test
    clean_train_data = filter_out_test_items(train_data, test_data)
    #import pdb;pdb.set_trace()
    
    # Dump train.txt
    clean_train_data_path = f"{output_dir}/train_filtered.txt"
    dump_user_items(clean_train_data_path, clean_train_data)



if __name__ == "__main__":
    main()
