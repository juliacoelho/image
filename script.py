# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 05:33:38 2016

@author: Julia et Vinicius

Split & Merge
"""
from PIL import Image     #On utilise la librairie d'image PIL
from math import sqrt     #Importation de la fonction racine carrée de la librairie math

im = Image.open("Image10.bmp")    #Selection et ouverture de l'image
px = im.load()                   #Importation des pixels de l'image sous forme d'une matrice px
w,h = im.size                    #Obtentio de la taille de l'image

#a
#Ecrire une fonction permettant de lire la valeur d'un pixel.

def lirepix(x,y):
    return px[x,y]

#b
#Ecrire une fonction permettant d'affecter une couleur à un pixel.

def affpix(x,y,r,g,b):
    px[x,y] = int(r), int(g), int(b) #atribuition d'une valeur a une tuplet
    
#c    
#Ecrire une fonction permettant d'affecter une couleur à une région rectangulaire de l'image.
    
def affreg(x0,y0,x,y,r,g,b):
    for i in range(x0,x+1):
        for j in range(y0,y+1):
            affpix(i,j,r,g,b)
            
#d
#Proposez une fonction qui estime l'homogeneite des pixels s'une region retangulaire de l'image.
            
def moyenne(retx0,rety0,retx,rety):   #On va faire la fonction qui calcule la moyenne de r, g et b separament pour l'utiliser apres dans la fonction quadripartition
    rgb=[0,0,0]
    for i in range(retx0,retx+1):
        for j in range(rety0,rety+1):
            rgb[0] += px[i,j][0]
            rgb[1] += px[i,j][1]
            rgb[2] += px[i,j][2]
    return [x / ((retx-retx0+1)*(rety-rety0+1)) for x in rgb]

def homogeneite(retx0,rety0,retx,rety):   #La fonction homogeneite returne une seule valeur, la moyenne des ecarts types de r, g et b
    moy = moyenne(retx0,rety0,retx,rety)
    varr, varg, varb = 0, 0, 0
    for i in range(retx0,retx+1):
        for j in range(rety0,rety+1):
            varr += (px[i,j][0] - moy[0])**2
            varg += (px[i,j][1] - moy[1])**2
            varb += (px[i,j][2] - moy[2])**2
    ecarttr = sqrt(varr/((retx-retx0+1)*(rety-rety0+1)))
    ecarttg = sqrt(varg/((retx-retx0+1)*(rety-rety0+1)))
    ecarttb = sqrt(varb/((retx-retx0+1)*(rety-rety0+1)))
    return (ecarttr+ecarttg+ecarttb)/3

#g
#Ecrire l'algorithme de split en language python.
#Modification pour la phase merge.


def quadripartition(retx0,rety0,retx,rety,seuil):
    if retx0!=retx and rety0!=rety: 
        if homogeneite(retx0,rety0,retx,rety) < seuil:
            rgb = moyenne(retx0,rety0,retx,rety)
            affreg(retx0,rety0,retx,rety,int(rgb[0]),int(rgb[1]),int(rgb[2]))
        else:
            retxm = (retx0+retx)//2
            retym = (rety0+rety)//2
            quadripartition(retx0,rety0,retxm,retym,seuil)
            quadripartition(retxm+1,rety0,retx,retym,seuil)
            quadripartition(retx0,retym+1,retxm,rety,seuil)
            quadripartition(retxm+1,retym+1,retx,rety,seuil)

