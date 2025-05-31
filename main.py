import model_predictions
import image_acquisition
import stockfish_stockfish
import user_questions

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, Dataset
from torchsummary import summary
print(torch.cuda.is_available())

if __name__ == "__main__":
    print("Initialisation du modèle et de la caméra...")
    #model, device = magnus_model_predictions.init_model("C:\\Users\\SD\\Desktop\\M1 - Q2\\Systèmes intelligents\\Magnus\\model\\Magnus_model.pth")
    model, device = model_predictions.init_model("C:\\Projets\\Projet_Magnus\\venv\\Magnus\\model\\Magnus_model.pth")
    image_acquisition.initialize_camera()

    try:
        
        color, elo = user_questions.questions()

        while True:
            input("Appuyez sur Entrée pour calculer le prochain coup (Ctrl+C pour quitter) : ")
            Data = image_acquisition.acquire_grid_images()
            y_pred = model_predictions.model_predict(model, device, Data)
            chess_grid_predicted = model_predictions.traduce_pred(y_pred)
            meilleur_coup = stockfish_stockfish.coup_du_bot(chess_grid_predicted, "C:\\Projets\\Projet_Magnus\\stockfish_app\\stockfish-windows-x86-64-avx2.exe", elo, color)

            print("Meilleur coup prédit :", meilleur_coup)

    except KeyboardInterrupt:
        print("\nArrêt du jeu.")
