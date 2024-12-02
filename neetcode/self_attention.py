import torch
import torch.nn as nn
from torchtyping import TensorType
import numpy as np

# 0. Instantiate the linear layers in the following order: Key, Query, Value.
# 1. Biases are not used in Attention, so for all 3 nn.Linear() instances, pass in bias=False.
# 2. torch.transpose(tensor, 1, 2) returns a B x T x A tensor as a B x A x T tensor.
# 3. This function is useful:
#    https://pytorch.org/docs/stable/generated/torch.nn.functional.softmax.html
# 4. Apply the masking to the TxT scores BEFORE calling softmax() so that the future
#    tokens don't get factored in at all.
#    To do this, set the "future" indices to float('-inf') since e^(-infinity) is 0.
# 5. To implement masking, note that in PyTorch, tensor == 0 returns a same-shape tensor 
#    of booleans. Also look into utilizing torch.ones(), torch.tril(), and tensor.masked_fill(),
#    in that order.
class SingleHeadAttention(nn.Module):
    
    def __init__(self, embedding_dim: int, attention_dim: int):
        super().__init__()
        torch.manual_seed(0)
        self.key_layer = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.query_layer = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.value_layer = nn.Linear(embedding_dim, attention_dim, bias=False)
        self.softmax_layer = nn.Softmax(2)
        self.attention_dim = attention_dim

    def forward(self, embedded: TensorType[float]) -> TensorType[float]:
        num_tokens = embedded.shape[1]
        mask = torch.ones([num_tokens, num_tokens], dtype=bool)
        mask = ~torch.tril(mask)
        mask = mask[None,:,:]

        key = self.key_layer(embedded)
        query = self.query_layer(embedded)
        value = self.value_layer(embedded)
        weights = (query @ torch.transpose(key, 1, 2))/(self.attention_dim**0.5)
        weights.masked_fill_(mask,float("-inf"))
        weights = self.softmax_layer(weights)
        output = weights @ value
        return torch.round(output, decimals=4)



embedding_dim = 2
attention_dim = 3
embedded = [
  [[-1.4381, 0.1232],
   [-0.1080, 0.3458]],
  [[0.1929, -0.8567],
   [-0.1160, 1.2547]]
]

output =[[[ 9.1380e-01,  4.2240e-01, -3.4970e-01],
         [ 4.1830e-01,  2.3370e-01, -1.1930e-01]],

        [[ 2.7090e-01, -7.8700e-02, -3.0960e-01],
         [-1.4960e-01, -3.0000e-04,  1.2680e-01]]]

self_attention = SingleHeadAttention(embedding_dim, attention_dim)
assert torch.equal(self_attention(torch.Tensor(embedded)), torch.Tensor(output))




