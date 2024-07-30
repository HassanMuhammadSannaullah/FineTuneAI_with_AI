import json
import csv
from FinetuneAI_with_AI.AI.queryAI import askGPT3
import re
from FinetuneAI_with_AI.variables import CODE_OUPUT_PATH
import subprocess
from os.path import exists


class PreProcessDataset:
  def __init__(self):
    self.dataset_path:str
    self.chunk:str

  def GenerateCustomScript(self):
     prompt="Now write a code that will read this file "+self.dataset_path+" and process it into a json file ready for LLAMA2 training. "+"""
      Find pattern yourself of how data relates with each other. Make a instruction answer set out of it and store in format ready for LLAMA2.
      The code should process full file. If an error occur it should handle it and keep continue with next part ofthe dataset Add functioanlity to chek the codec and use approprite one
      for reading the dataset file.

      The code should transform data to look like this
      [
        {
          "text": "<s>[INST] this is instruction  [/INST] this is response </s>"
        },
        {
          "text": "<s>[INST] this is instruction  [/INST] this is response </s>"
        }
      ]

      take care of tagging part. <s> should be beigning, [INST] before instruction and [/INST] at end of instruction and then response and in last </s?
      Do not forget to Add functioanlity to chek the codec and use approprite one
      The data which is to be transformed look like this """
     
     final_query=prompt+'\n\n'+self.chunk+"\n Keep the output file name output.json"
     return askGPT3(final_query)

  def _extract_code(self,text):
    # Match the code block within triple backticks
    code_match = re.search(r'```(?:python)?\n(.*?)```', text, re.DOTALL)
    if code_match:
        return code_match.group(1).strip()
    return None
  
  def _execute_python_file(self,filename):
    try:
        result = subprocess.run(
            ['python', filename], 
            capture_output=True, text=True, check=True
        )
        if exists('output.json'):
          print("Proccessed Dataset Created Successfully")
          return 1
        else:
           print("Processed Dataset file could not be saved.")
           return None
    except subprocess.CalledProcessError as e:
        print(f"Error executing {filename}:\n", e.stderr)
        return None
  
  def _process(self):
    while True:
      print("Trying to Generate Code using LLM API")
      response=self.GenerateCustomScript()
      if response:
        code=self._extract_code(response)
        if code:
          with open(CODE_OUPUT_PATH, 'w') as file:
            try:
              file.write(code)
              print(f"Code saved to {CODE_OUPUT_PATH}")
            except Exception as e:
               print(e)
               print("Error Occured during save of generated Code. Retrying. TO Stop Press CTRL+C")
               continue
          execution_status=self._execute_python_file(CODE_OUPUT_PATH)
          if execution_status:
            break
          else:
             print("Could not Execute LLM generated Script. Retrying by Generating New Script. To Stop Press CTRL+C")
             continue
        else:
           print("Code could not be found in Response. Retrying from Beigning. To Stop Press CTRL+C")
      else:
         print("Failed to get Response from API. Retrying. TO Stop Press CTRL+C")
         continue
      


  def read_csv_chunk(self,file_path, chunk_size):
    """
    Reads a small chunk of data from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.
    - chunk_size (int): Number of rows to read.

    Returns:
    - str: The chunk of data formatted as a string.
    """
    self.dataset_path=file_path
    chunk = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        for i, row in enumerate(csvreader):
            if i >= chunk_size:
                break
            chunk.append(row)
    self.chunk='\n'.join([','.join(map(str, row)) for row in chunk])
    self._process()

  def read_txt_chunk(self,file_path, chunk_size):
      """
      Reads a small chunk of data from a TXT file.

      Args:
      - file_path (str): Path to the TXT file.
      - chunk_size (int): Number of lines to read.

      Returns:
      - str: The chunk of data formatted as a string.
      """
      
      chunk = []
      with open(file_path, mode='r', encoding='utf-8') as txtfile:
          for i, line in enumerate(txtfile):
              if i >= chunk_size:
                  break
              chunk.append(line.strip())
      self.chunk='\n'.join(chunk)
      self._process()

  def read_json_chunk(self,file_path, chunk_size):
      """
      Reads a small chunk of data from a JSON file.

      Args:
      - file_path (str): Path to the JSON file.
      - chunk_size (int): Number of entries to read from the JSON array.

      Returns:
      - str: The chunk of data formatted as a string.
      """
      self.dataset_path=file_path
      with open(file_path, mode='r', encoding='utf-8') as jsonfile:
          data = json.load(jsonfile)
          chunk = data[:chunk_size]
      self.chunk=json.dumps(chunk, indent=4)
      self._process()

if __name__=="__main__":
   PreProcessDataset().read_csv_chunk("medquad.csv",4)