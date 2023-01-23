from transformers import BertTokenizer
##files from git
from model import BertForMultiLabelClassification
from multilabel_pipeline import MultiLabelPipeline
from pprint import pprint
import torch
tokenizer = BertTokenizer.from_pretrained("monologg/bert-base-cased-goemotions-original")
model = BertForMultiLabelClassification.from_pretrained("monologg/bert-base-cased-goemotions-original")

activation = {}
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook

model.bert.register_forward_hook(get_activation('bert')) #layer problem
x = #input problem
output = model(x)
print(activation['bert'])


#output_attention = True
  ->
