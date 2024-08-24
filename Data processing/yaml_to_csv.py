import os
import yaml
import pandas as pd

def yaml_to_csv(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.yaml'):
            file_path = os.path.join(input_folder, filename)

            with open(file_path, 'r') as yaml_file:
                try:
                    data = yaml.safe_load(yaml_file)
                except yaml.YAMLError as e:
                    print(f"Error reading {filename}: {e}")
                    continue

            if isinstance(data, list):
                df = pd.DataFrame(data)
            elif isinstance(data, dict):
                df = pd.json_normalize(data)
            else:
                print(f"Skipping {filename}: Unsupported data structure.")
                continue

            
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.csv")
            df.to_csv(output_file, index=False)
            print(f"Converted {filename} to {output_file}")


input_folder = "t20s"  
output_folder = "t20s_csv_files"  

yaml_to_csv(input_folder, output_folder)
