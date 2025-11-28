import torch
import json
import torch.nn.functional as F

model = torch.load('lambda_inference/global_model.pt', map_location='cpu', weights_only=False)

model.eval()

def lambda_handler(event, context):
    try:
        input_data = json.loads(event['body']) 
        x = torch.tensor(input_data['features']).float().unsqueeze(0)


        print(x.shape)

        with torch.no_grad():
            output = model(x)
            print("Raw output:", output) 
            probs = torch.sigmoid(output)
            print("Softmax probabilities:", probs)
            predicted_class = (probs >= 0.5).long()
            is_fraud = predicted_class

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediction": int(is_fraud.item()),  
                "probability": float(probs.item()),
                "meaning": "0 = Not Fraud, 1 = Fraud"
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }