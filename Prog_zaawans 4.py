import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization

#Zdefiniowanie macierzy
macierz_dec = np.array([
    [5000, 0.2, 3, 7],
    [7000, 0.5, 5, 5],
    [6000, 0.3, 4, 6]
])

#Określenie wag
wagi = np.array([0.4, 0.3, 0.2, 0.1])

#Określenie typów kryteriów
typy_kryteriow = [False, True, True, False] 

#Normalizacja danych
macierz_norm = minmax_normalization(macierz_dec, typy_kryteriow)

#TOPSIS
topsis = TOPSIS()
ranking_topsis = topsis(macierz_norm, wagi, typy_kryteriow)

#SPOTIS
spotis = SPOTIS()
ranking_spotis = spotis(macierz_dec, wagi, typy_kryteriow)

wyniki = [
    ("A1", ranking_topsis[0], ranking_spotis[0]),
    ("A2", ranking_topsis[1], ranking_spotis[1]),
    ("A3", ranking_topsis[2], ranking_spotis[2])
]

for alternatywa, wynik_topsis, wynik_spotis in wyniki:
    print(f"{alternatywa}: TOPSIS = {wynik_topsis}, SPOTIS = {wynik_spotis}")
