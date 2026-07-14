"""
Fight LSTM Model Training Module

This module trains the LSTM-based violence recognition model
using extracted human pose sequences.

Purpose:

    - Load prepared pose sequence dataset.
    - Create training batches.
    - Perform forward propagation.
    - Calculate classification loss.
    - Update model parameters using backpropagation.
    - Monitor training accuracy.
    - Save trained model weights.



Task:

Binary Classification:

    0 → NonFight

    1 → Fight



Training Pipeline:


Pose Sequences
      |
      ↓
FightDataset
      |
      ↓
DataLoader
      |
      ↓
FightLSTM Model
      |
      ↓
Loss Calculation
      |
      ↓
Backpropagation
      |
      ↓
Updated Model Weights
      |
      ↓
fight_lstm.pth



Input:

Pose sequence:

    Shape:

        (30,132)


Where:

    30  → Number of frames

    132 → Pose features per frame



Training Configuration:

    Batch Size:
        16

    Learning Rate:
        0.001

    Optimizer:
        Adam

    Loss Function:
        CrossEntropyLoss

    Epochs:
        20



Output:

Saved trained model:

    models/fight_lstm.pth

"""



import torch


from torch.utils.data import DataLoader

from torch.optim import Adam



# Custom dataset and model

from dataset import FightDataset

from model import FightLSTM





# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
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
# -------------------------------------------------


dataset = FightDataset(

    "../data/pose_sequences"

)



print(

    "Dataset Size:",

    len(dataset)

)





# -------------------------------------------------
# Create DataLoader
# -------------------------------------------------
#
# DataLoader:
#
#   - Creates mini batches.
#   - Randomizes training samples.
#
# -------------------------------------------------


loader = DataLoader(

    dataset,

    batch_size=16,

    shuffle=True

)





# -------------------------------------------------
# Select Computing Device
# -------------------------------------------------
#
# Uses GPU if available.
# Otherwise CPU.
#
# -------------------------------------------------


device = (

    "cuda"

    if torch.cuda.is_available()

    else "cpu"

)



print(

    "Device:",

    device

)





# -------------------------------------------------
# Initialize Model
# -------------------------------------------------
#
# Creates LSTM violence classifier.
#
# -------------------------------------------------


model = FightLSTM().to(device)





# -------------------------------------------------
# Optimizer
# -------------------------------------------------
#
# Adam updates model parameters by using
# gradients calculated during backpropagation.
#
# Learning rate controls update size.
#
# -------------------------------------------------


optimizer = Adam(

    model.parameters(),

    lr=0.001

)





# -------------------------------------------------
# Loss Function
# -------------------------------------------------
#
# CrossEntropyLoss is used for
# multi-class classification.
#
# Here:
#
#   Class 0 → NonFight
#
#   Class 1 → Fight
#
# -------------------------------------------------


criterion = torch.nn.CrossEntropyLoss()





# Number of complete passes through dataset

epochs = 20





# -------------------------------------------------
# Training Loop
# -------------------------------------------------

for epoch in range(epochs):


    # Enable training mode

    model.train()



    total_loss = 0

    correct = 0

    total = 0




    # Process mini batches

    for x, y in loader:



        # Move data to CPU/GPU

        x = x.to(device)

        y = y.to(device)




        # Remove previous gradients

        optimizer.zero_grad()




        # Forward pass

        output = model(x)




        # Calculate prediction error

        loss = criterion(

            output,

            y

        )




        # Backpropagation

        loss.backward()




        # Update weights

        optimizer.step()




        # Track loss

        total_loss += loss.item()




        # Convert scores into predicted classes

        predictions = output.argmax(

            dim=1

        )




        # Count correct predictions

        correct += (

            predictions == y

        ).sum().item()




        # Count total samples

        total += y.size(0)





    # Calculate epoch accuracy

    accuracy = (

        100 * correct / total

    )





    # Display training progress

    print(

        f"Epoch {epoch+1}/{epochs} "

        f"Loss={total_loss:.4f} "

        f"Accuracy={accuracy:.2f}%"

    )





# -------------------------------------------------
# Save Trained Model
# -------------------------------------------------
#
# Only model parameters are saved.
#
# These weights can later be loaded
# for inference.
#
# -------------------------------------------------


torch.save(

    model.state_dict(),

    "../models/fight_lstm.pth"

)




print(

    "\nTraining Complete"

)



print(

    "Saved:",

    "../models/fight_lstm.pth"

)