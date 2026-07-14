"""
Fight LSTM Model Evaluation Module

This module evaluates the trained LSTM-based violence
recognition model using a separate test dataset.

Purpose:
    - Load the prepared pose sequence dataset.
    - Split data into training and testing subsets.
    - Load the trained LSTM model weights.
    - Perform inference on test samples.
    - Calculate evaluation metrics.
    - Generate confusion matrix.


Evaluation Metrics:

    Accuracy:
        Overall percentage of correct predictions.


    Precision:
        How many predicted fights were actually fights.


    Recall:
        How many actual fights were detected.


    F1 Score:
        Balance between precision and recall.


    Confusion Matrix:
        Shows correct and incorrect classifications.



Pipeline:

Pose Dataset
      |
      ↓
FightDataset
      |
      ↓
Train/Test Split
      |
      ↓
Load Trained LSTM Model
      |
      ↓
Test Prediction
      |
      ↓
Performance Evaluation



Model:

Input:

    Pose Sequence

    Shape:

        (30,132)


Output:

    Two classes:

        0 → NonFight

        1 → Fight

"""



from pathlib import Path


import torch

from torch.utils.data import random_split
from torch.utils.data import DataLoader



# Evaluation metrics

from sklearn.metrics import (

    accuracy_score,

    precision_score,

    recall_score,

    f1_score,

    confusion_matrix

)



# Custom dataset and model

from dataset import FightDataset

from model import FightLSTM





# --------------------------------------------------
# Load Dataset
# --------------------------------------------------
#
# Dataset contains:
#
#   Fight/
#   NonFight/
#
# Each sample:
#
#   (30,132) pose sequence
#
# --------------------------------------------------


dataset = FightDataset(

    "../data/pose_sequences"

)





# --------------------------------------------------
# Create Test Split
# --------------------------------------------------
#
# 80% training
#
# 20% testing
#
# The test data is used only for evaluation.
#
# --------------------------------------------------


train_size = int(

    0.8 * len(dataset)

)


test_size = (

    len(dataset)

    -

    train_size

)




train_dataset, test_dataset = random_split(

    dataset,

    [

        train_size,

        test_size

    ]

)





# DataLoader provides batches during inference

test_loader = DataLoader(

    test_dataset,

    batch_size=16,

    shuffle=False

)





# --------------------------------------------------
# Select Computing Device
# --------------------------------------------------
#
# Use GPU if available,
# otherwise CPU.
#
# --------------------------------------------------


device = (

    "cuda"

    if torch.cuda.is_available()

    else

    "cpu"

)





# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------
#
# The trained LSTM weights are loaded from:
#
# models/fight_lstm.pth
#
# --------------------------------------------------


model = FightLSTM().to(device)



model.load_state_dict(

    torch.load(

        "../models/fight_lstm.pth",

        map_location=device

    )

)




# Switch model to evaluation mode

# Disables training-specific operations

model.eval()





# Storage for actual and predicted labels

y_true = []

y_pred = []





# --------------------------------------------------
# Model Inference
# --------------------------------------------------
#
# No gradient calculation is required during testing.
#
# --------------------------------------------------


with torch.no_grad():


    for x, y in test_loader:



        # Move input to selected device

        x = x.to(device)



        # Model prediction

        output = model(x)



        # Select class with highest probability

        preds = torch.argmax(

            output,

            dim=1

        )



        # Store actual labels

        y_true.extend(

            y.numpy()

        )



        # Store predicted labels

        y_pred.extend(

            preds.cpu().numpy()

        )





# --------------------------------------------------
# Calculate Evaluation Metrics
# --------------------------------------------------


print(

    "\nAccuracy:",

    accuracy_score(

        y_true,

        y_pred

    )

)



print(

    "Precision:",

    precision_score(

        y_true,

        y_pred

    )

)



print(

    "Recall:",

    recall_score(

        y_true,

        y_pred

    )

)



print(

    "F1:",

    f1_score(

        y_true,

        y_pred

    )

)





# --------------------------------------------------
# Confusion Matrix
# --------------------------------------------------
#
# Format:
#
#                 Predicted
#
#                 0       1
#
# Actual 0       TN      FP
#
# Actual 1       FN      TP
#
# --------------------------------------------------


print(

    "\nConfusion Matrix:"

)



print(

    confusion_matrix(

        y_true,

        y_pred

    )

)