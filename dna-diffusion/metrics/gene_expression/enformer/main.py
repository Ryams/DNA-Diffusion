from enformer_inference import Enformer
from utils import inference

if __name__ == "__main__":
    data_path = "abc_data/K562.PositivePredictions.txt"
    model = Enformer(data_path)
    one_hot_seqs = model.data.fetch_sequence()  # this is a dictionary with key being Ensembl ID|Gene Name and the value
    # being the one hot encoded sequence as a torch.Tensor
    inference(one_hot_seqs, model)  # saves output to outputs folder as a pickle file

    # TODO 1: Import supplementary data table 2 from paper in order to get the cell types and genomic track type.

    # TODO 2: Perform sanity check on DNA diff test data see:
    # TODO 2: https://discord.com/channels/850068776544108564/1024646567833112656/1055581251483996210`

    # TODO 3: Transfer inference to a Colab notebook instance with a CUDA GPU