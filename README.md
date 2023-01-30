# bert-goemotions-upgrade diary

This is a bert-based classification model on goemotions dateset- with a downstream task model added to bert.

## Goal： 
I want to extract the activation of neurons in the hidden layer in bert part mainly in this model and perform a analysis based on the activated and inactivated neurons.

## Anticipated approach: 
Since the activation function used is known, for a neuron with an output value greater than a threshold —— it is activated and can be judged and filtered according to the output value obtained for each neuron.

## Attempt：
1.Use hook to get (mimic getting intermediate feature values in image recognition)
2.Add print the output value directly into the code
