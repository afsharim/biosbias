from datasets import load_dataset, concatenate_datasets
import datasets
import pickle

print(datasets.__version__)

try:
    dataset = load_dataset("LabHC/bias_in_bios", use_auth_token="?")
    all_data = concatenate_datasets([dataset['train'], dataset['test'], dataset['dev']])

    # Define the filename
    filename = 'BIOS.pkl'

    # Open a file in write-binary mode
    with open(filename, 'wb') as file:
        pickle.dump(all_data, file)
    print("Dataset downloaded and saved successfully!")
except Exception as e:
    print("An error occurred:", str(e))
