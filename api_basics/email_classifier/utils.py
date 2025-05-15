import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification



# create a function for getting the model and tokenizer

def get_artifacts():
    model_uri = "muyiiwaa/distilbert-email-model"
    # get the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_uri)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = AutoModelForSequenceClassification.from_pretrained(model_uri, 
                                                            num_labels = 2).to(device)
    return model, tokenizer, device


def check_email(email_text: str):
  model, tokenizer, device = get_artifacts()
  encoding = tokenizer.encode_plus(
        email_text,
        padding = 'max_length',
        truncation = True,
        return_tensors = 'pt',
        add_special_tokens = True)

  input_ids = encoding['input_ids']
  attention_mask = encoding['attention_mask']
  softmax = torch.nn.Softmax(dim=1)

  with torch.no_grad():
    model.eval()
    input_ids = input_ids.to(device)
    attention_mask = attention_mask.to(device)
    outputs = model(input_ids = input_ids, attention_mask = attention_mask)
    probs, preds = torch.max(softmax(outputs.logits), 1)


  decision = ['Real Email', 'Spam Email']
  return decision[preds.item()], round(probs.item(), 4)


DESCRIPTION = """

This application contains a suite of endpoints for checking 
if an email is real or a junk. It interfaces a fine tuned distil bert
model trained on 1k samples of real and junk email.
"""

def get_description(desc=DESCRIPTION):
   return desc


if __name__ == "__main__":
  print(check_email(email_text= "Hello how are you? Are you available for a lunch!"))