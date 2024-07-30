import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig
from trl import SFTTrainer

class TrainLlama2:
    def __init__(self, dataset_path=None, base_model="NousResearch/Llama-2-7b-chat-hf"):
        if not dataset_path:
            self.dataset_path='output.json'
        else:
            self.dataset_path=dataset_path
        self.base_model=base_model
        self.tokenizer = AutoTokenizer.from_pretrained(base_model)
        self.model = AutoModelForCausalLM.from_pretrained(base_model)
        self.dataset = load_dataset('json', data_files=self.dataset_path, split='train')

    def train(self):
        # Training setup
        peft_args = LoraConfig(
            lora_alpha=16,
            lora_dropout=0.1,
            r=64,
            bias="none",
            task_type="CAUSAL_LM",
        )
        training_params = TrainingArguments(
            output_dir="./results",
            num_train_epochs=1,
            per_device_train_batch_size=4,
            learning_rate=2e-4,
            # Additional parameters as needed...
        )

                # Trainer
        trainer = SFTTrainer(
            model=self.model,
            train_dataset=self.dataset,
            peft_config=peft_args,
            dataset_text_field="text",
            tokenizer=self.tokenizer,
            args=training_params,
        )

        # Train the model
        trainer.train()
