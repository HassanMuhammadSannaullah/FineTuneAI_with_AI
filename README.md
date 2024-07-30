**Fine-Tune AI Using AI in 2 Lines of Code!**

Welcome to **"FineTuneAI_with_AI"**! This repository introduces an innovative approach to fine-tuning Large Language Models (LLMs) like LLaMA, leveraging AI to handle both preprocessing and training. With just two lines of code, you can convert raw, unprocessed data into a refined dataset ready for LLaMA training and fine-tune the model effortlessly.

## Overview

This project employs a unique method where AI generates scripts to preprocess any type of raw or jumbled data. Here’s how it works:

- **AI-Generated Preprocessing:** The system analyzes the raw dataset to identify patterns and then generates a script that transforms this data into a structured format suitable for LLaMA training. This ensures that even complex or disorganized data can be processed effectively.

- **Automated Script Monitoring:** The system continuously monitors the AI-generated preprocessing scripts. If the process fails to meet the desired goals, the system automatically restarts the process until the target is achieved, ensuring high-quality data preparation.

- **Seamless Fine-Tuning:** Once the data is processed, the fine-tuning of the LLaMA model is executed and the updated model is saved locally.

## Features

- **Dynamic Data Transformation:** Convert any raw or disorganized dataset into a well-structured format ready for LLaMA training, using AI-generated scripts that adapt to the data patterns.
- **Automatic Error Handling:** The system monitors the preprocessing process and restarts it if necessary, ensuring reliable and accurate data preparation.
- **Effortless Model Fine-Tuning:** Fine-tune the LLaMA model with minimal manual intervention and save the refined model locally.

This approach simplifies the entire workflow, making it easier to handle diverse datasets and achieve optimal results with LLaMA.


## Installation

### Using pip
  ```bash
   pip install git+https://github.com/HassanMuhammadSannaullah/FineTuneAI_with_AI.git
```

### Cloning Method
1. **Clone the Repository:**

   ```bash
   git clone https://github.com/HassanMuhammadSannaullah/FineTuneAI_with_AI.git
  
2. **Move to the directoey:**

   ```bash
   cd FineTuneAI_with_AI

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

## How To Use

### Configuration

Before running the code, you need to create and configure a `.ini` file to provide the necessary API settings. This file should be named `config.ini` and placed in the root directory of your project.

Create a file named `config.ini` in the reeot folder with the following content:

```ini
[API]
URL= Your Cloudfare API URL for CHAT Models (prefferably LLaMA 3.1)
BEARER= Your Bearer Key
```

### Running the Code

Once you have set up the configuration file and installed the package, you can run the code to preprocess your dataset and fine-tune the LLaMA model.

Here’s a simple example to get you started:

```python
from FinetuneAI_with_AI.DatasetPreparor import PreProcessDataset
from FinetuneAI_with_AI.train import TrainLlama2

# Preprocess the dataset
PreProcessDataset().read_csv_chunk("Your/raw/dataset/path", 3)

# Fine-tune the LLaMA model
TrainLlama2().train()
