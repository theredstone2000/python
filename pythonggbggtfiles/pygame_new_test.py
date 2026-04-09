from my_modules.useful_variables import letter_list
from my_modules import filter_recreation
from my_modules import range_recreation
import typing
import typing_extensions
import threading
import collections
import pynput
import pygame
import tkinter as TK
import tk

tasks = {}
for ch in letter_list:
    tasks[ch] = ""
letter_list.reverse()
a = letter_list
letter_list.reverse()
for ch in letter_list:
    for hc in a:
        tasks[ch] = hc
print(tasks)
for ch in letter_list:
    print(tasks[ch])
print(tasks.keys())
print(tasks.items())
print(tasks.values())

for ch in (letter_list):
    task = tasks[ch]
    task = 1
    tasks[ch] = task
print(tasks)

def test(a):
    return(a)

print(filter_recreation.filter(test, [True,False]))

import modulefinder
print(f"this is supposed to give [2,4,6,8] : {range_recreation.range(2,9,2)}")

d = {
    "block.minecraft.waxed_chiseled_copper": "Cuivre sculpté ciré",
    "block.minecraft.waxed_copper_bars": "Barreaux de cuivre ciré",
    "block.minecraft.waxed_copper_block": "Bloc de cuivre ciré",
    "block.minecraft.waxed_copper_bulb": "Ampoule en cuivre ciré",
    "block.minecraft.waxed_copper_chain": "Chaîne en cuivre ciré",
    "block.minecraft.waxed_copper_chest": "Coffre en cuivre ciré",
    "block.minecraft.waxed_copper_door": "Porte en cuivre ciré",
    "block.minecraft.waxed_copper_golem_statue": "Statue de golem de cuivre ciré",
    "block.minecraft.waxed_copper_grate": "Grille en cuivre ciré",
    "block.minecraft.waxed_copper_lantern": "Lanterne en cuivre ciré",
    "block.minecraft.waxed_copper_trapdoor": "Trappe en cuivre ciré",
    "block.minecraft.waxed_cut_copper": "Cuivre taillé ciré",
    "block.minecraft.waxed_cut_copper_slab": "Dalle de cuivre taillé ciré",
    "block.minecraft.waxed_cut_copper_stairs": "Escalier en cuivre taillé ciré",
    "block.minecraft.waxed_exposed_chiseled_copper": "Cuivre sculpté exposé ciré",
    "block.minecraft.waxed_exposed_copper": "Cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_bars": "Barreaux de cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_bulb": "Ampoule en cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_chain": "Chaîne en cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_chest": "Coffre en cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_door": "Porte en cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_golem_statue": "Statue de golem de cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_grate": "Grille en cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_lantern": "Lanterne en cuivre exposé ciré",
    "block.minecraft.waxed_exposed_copper_trapdoor": "Trappe en cuivre exposé ciré",
    "block.minecraft.waxed_exposed_cut_copper": "Cuivre taillé exposé ciré",
    "block.minecraft.waxed_exposed_cut_copper_slab": "Dalle de cuivre taillé exposé ciré",
    "block.minecraft.waxed_exposed_cut_copper_stairs": "Escalier en cuivre taillé exposé ciré",
    "block.minecraft.waxed_exposed_lightning_rod": "Paratonnerre exposé ciré",
    "block.minecraft.waxed_lightning_rod": "Paratonnerre ciré",
    "block.minecraft.waxed_oxidized_chiseled_copper": "Cuivre sculpté oxydé ciré",
    "block.minecraft.waxed_oxidized_copper": "Cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_bars": "Barreaux de cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_bulb": "Ampoule en cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_chain": "Chaîne en cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_chest": "Coffre en cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_door": "Porte en cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_golem_statue": "Statue de golem de cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_grate": "Grille en cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_lantern": "Lanterne en cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_copper_trapdoor": "Trappe en cuivre oxydé ciré",
    "block.minecraft.waxed_oxidized_cut_copper": "Cuivre taillé oxydé ciré",
    "block.minecraft.waxed_oxidized_cut_copper_slab": "Dalle de cuivre taillé oxydé ciré",
    "block.minecraft.waxed_oxidized_cut_copper_stairs": "Escalier en cuivre taillé oxydé ciré",
    "block.minecraft.waxed_oxidized_lightning_rod": "Paratonnerre oxydé ciré",
    "block.minecraft.waxed_weathered_chiseled_copper": "Cuivre sculpté érodé ciré",
    "block.minecraft.waxed_weathered_copper": "Cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_bars": "Barreaux de cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_bulb": "Ampoule en cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_chain": "Chaîne en cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_chest": "Coffre en cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_door": "Porte en cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_golem_statue": "Statue de golem de cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_grate": "Grille en cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_lantern": "Lanterne en cuivre érodé ciré",
    "block.minecraft.waxed_weathered_copper_trapdoor": "Trappe en cuivre érodé ciré",
    "block.minecraft.waxed_weathered_cut_copper": "Cuivre taillé érodé ciré",
    "block.minecraft.waxed_weathered_cut_copper_slab": "Dalle de cuivre taillé érodé ciré",
    "block.minecraft.waxed_weathered_cut_copper_stairs": "Escalier en cuivre taillé érodé ciré",
    "block.minecraft.waxed_weathered_lightning_rod": "Paratonnerre érodé ciré",
    "block.minecraft.weathered_chiseled_copper": "Cuivre sculpté érodé",
    "block.minecraft.weathered_copper": "Cuivre érodé",
    "block.minecraft.weathered_copper_bars": "Barreaux de cuivre érodé",
    "block.minecraft.weathered_copper_bulb": "Ampoule en cuivre érodé",
    "block.minecraft.weathered_copper_chain": "Chaîne en cuivre érodé",
    "block.minecraft.weathered_copper_chest": "Coffre en cuivre érodé",
    "block.minecraft.weathered_copper_door": "Porte en cuivre érodé",
    "block.minecraft.weathered_copper_golem_statue": "Statue de golem de cuivre érodé",
    "block.minecraft.weathered_copper_grate": "Grille en cuivre érodé",
    "block.minecraft.weathered_copper_lantern": "Lanterne en cuivre érodé",
    "block.minecraft.weathered_copper_trapdoor": "Trappe en cuivre érodé",
    "block.minecraft.weathered_cut_copper": "Cuivre taillé érodé",
    "block.minecraft.weathered_cut_copper_slab": "Dalle de cuivre taillé érodé",
    "block.minecraft.weathered_cut_copper_stairs": "Escalier en cuivre taillé érodé",
    "block.minecraft.weathered_lightning_rod": "Paratonnerre érodé",
}

for ch in d.keys():
    d[ch]="c'est tous les cuivre cirées puis un certain niveau d'oxidation je sais pas quoi je vais pas tout écrire j'ai la flemme"

for ch in d.items():
    ch1 = ch.__getitem__(0)
    ch2 = ch.__getitem__(1)
    ch3 = "    \"" + ch1 + "\" : \"" + ch2 + "\","
    print(ch3)

