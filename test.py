import pandas as pd
import json
from Lambda_Inference.inference import lambda_handler

def extract_features(row, df):
    return [
        row[df.columns[0]],
        row[df.columns[1]],
        row[df.columns[2]],
        row[df.columns[3]],
        row[df.columns[4]],
        row[df.columns[5]],
        row[df.columns[6]],
        row[df.columns[7]],
        row[df.columns[8]],
        row[df.columns[9]],
        row[df.columns[10]],
        row[df.columns[11]],
        row[df.columns[12]],
        row[df.columns[13]],
        row[df.columns[14]],
        row[df.columns[15]],
        row[df.columns[16]],
        row[df.columns[17]],
        row[df.columns[18]],
        row[df.columns[19]],
        row[df.columns[20]],
        row[df.columns[22]],
    ]

def load_last_20_records(csv_path):
    df = pd.read_csv(csv_path)
    return df.tail(20)

if __name__ == "__main__":
    df = load_last_20_records("test_data.csv")

    for idx, row in df.iterrows():
        features = extract_features(row, df)
        event = {
            "body": json.dumps({"features": features})
        }

        response = lambda_handler(event, None)

        print(f"Record {idx}:")
        print(json.dumps(response, indent=2))
        print("-" * 40)

