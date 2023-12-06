from PIL import Image as img
import numpy as np
 
# Recuperation des donnees du fichier
#photo = img.open("img/IMG_2908.JPG")
#contour = img.open("template.png")
photo = img.open("img/graphe.png")
photo = np.array(photo)
#contour = np.array(contour)
#print(contour.shape, photo.shape)
#print(contour[5][700][3])


def scale_img(photo, taille = 1580):
    print(photo.shape)
    hauteur_b = photo.shape[0]
    largeur_b = photo.shape[1]
    largeur_f = taille
    hauteur_f = hauteur_b*largeur_f/largeur_b
    rapport = largeur_b/largeur_f
    image_scale = np.zeros((int(hauteur_f), int(largeur_f), 3))
    print(image_scale.shape)
    for color in range(3) :
        for y in range(largeur_b) :
            for x in range(hauteur_b) :
                for angle_v in range(2) :
                    for angle_h in range(2) :
                        if angle_v == 1 :
                            if int((x+angle_v)*rapport) != int(x*rapport) :
                                continue
                        if angle_h == 1 :
                            if int((y+angle_h)*rapport) != int(x*rapport) :
                                continue
                        current_pixel = photo[x][y][color]
                        a = (x+angle_v) * rapport
                        b = (y+angle_h) * rapport
                        common_area = min((2*angle_v-1)*(a%1)+1-angle_v, rapport)*min((2*angle_h-1)*(b%1)+1-angle_h, rapport)
                        a = a//1
                        b = b//1
                        #image_scale[a][b][color] += common_area*current_pixel
    return image_scale
                        
new_p = img.fromarray(scale_img(photo))

if new_p.mode != 'RGB':
    new_p = new_p.convert('RGB')
new_p.save("tmp.jpg")