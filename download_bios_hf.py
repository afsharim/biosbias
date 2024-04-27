from datasets import load_dataset
import datasets
print(datasets.__version__)

dataset = load_dataset("LabHC/bias_in_bios",use_auth_token="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")

# Combining the train, test, and dev splits
all_data = dataset['train'].concatenate(dataset['test'], dataset['dev'])

import pickle

# Define the filename
filename = 'BIOS.pkl'

# Open a file in write-binary mode
with open(filename, 'wb') as file:
    pickle.dump(all_data, file)
