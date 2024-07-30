from DatasetPreparor import PreProcessDataset
from train import TrainLlama2

PreProcessDataset().read_csv_chunk("medquad.csv",3)
TrainLlama2().train()