import magnus_model_predictions
import image_acquisition

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchsummary import summary
print(torch.cuda.is_available())

if __name__ == "__main__":
    print("Initialisation du modèle et de la caméra...")
    model, device = magnus_model_predictions.init_model("C:\\Users\\SD\\Desktop\\M1 - Q2\\Systèmes intelligents\\Magnus\\model\\Magnus_model.pth")
    image_acquisition.initialize_camera()

    try:
        while True:
            input("Appuyez sur Entrée pour calculer le prochain coup (Ctrl+C pour quitter) : ")
            Data = image_acquisition.acquire_grid_images()
            y_pred = magnus_model_predictions.model_predict(model, device, Data)
            chess_grid_predicted = magnus_model_predictions.traduce_pred(y_pred)

            # print la grille d'échec prédite
            # print le prochain coup prédit

            print(chess_grid_predicted) # ligne a supprimer

    except KeyboardInterrupt:
        print("\nArrêt du jeu.")
