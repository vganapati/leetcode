"""
https://neetcode.io/problems/nlp-intro
"""

import torch
import torch.nn as nn
from torchtyping import TensorType
from typing import List
import numpy as np

# torch.tensor(python_list) returns a Python list as a tensor
class Solution:
    def get_dataset(self, positive: List[str], negative: List[str]) -> TensorType[float]:
       
        positive = [i.split(" ") for i in positive]
        negative = [i.split(" ") for i in negative]

        all_words = set()

        for sentence in positive:
            for word in sentence:
                all_words.add(word)
        
        for sentence in negative:
            for word in sentence:
                all_words.add(word)
        all_words = list(all_words)

        word_dict = {word: embedding for word, embedding in zip(np.sort(all_words), 1 + np.arange(len(all_words)))}

        positive_embed = [[word_dict[word] for word in phrase] for phrase in positive]
        negative_embed = [[word_dict[word] for word in phrase] for phrase in negative]


        all_phrases = positive_embed + negative_embed
        all_phrases = [torch.tensor(phrase, dtype=torch.float) for phrase in all_phrases]
        return torch.nn.utils.rnn.pad_sequence(all_phrases, batch_first=True)


solution = Solution()


positive=["Good case, Excellent value.","Great for the jawbone.","The mic is great.","If you are Razr owner...you must have this!","Highly recommend for any one who has a blue tooth phone"]
negative=["So there is no way for me to plug it in here in the US unless I go buy a converter.","Tied to charger for conversations lasting more than 45 minutes.MAJOR PROBLEMS!!","I have to jiggle the plug to get it to line up right to get decent volume.","Needless to say, I wasted my money.","What a waste of money and time!"]
output = torch.tensor([[3.0,22.0,2.0,67.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[4.0,27.0,59.0,37.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[12.0,42.0,35.0,30.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[7.0,73.0,19.0,10.0,52.0,47.0,32.0,61.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[5.0,55.0,27.0,18.0,51.0,72.0,31.0,16.0,20.0,64.0,53.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[11.0,60.0,35.0,49.0,71.0,27.0,41.0,63.0,54.0,36.0,34.0,33.0,34.0,59.0,14.0,65.0,6.0,29.0,21.0,16.0,25.0],[13.0,63.0,23.0,27.0,24.0,39.0,46.0,58.0,1.0,43.0,9.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[6.0,32.0,63.0,38.0,59.0,54.0,63.0,28.0,36.0,63.0,40.0,66.0,56.0,63.0,28.0,26.0,68.0,0.0,0.0,0.0,0.0],[8.0,63.0,57.0,6.0,70.0,48.0,45.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],[15.0,16.0,69.0,50.0,44.0,17.0,62.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]])
torch.testing.assert_close(solution.get_dataset(positive, negative), output)


positive = ["Dogecoin to the moon"]
negative = ["I will short Tesla today"]
output = [
  [1.0, 7.0, 6.0, 4.0, 0.0],
  [2.0, 9.0, 5.0, 3.0, 8.0]
]

torch.testing.assert_close(solution.get_dataset(positive, negative), torch.tensor(output))





