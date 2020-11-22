plateau = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

possible = [[True, True, True],
           [True, True, True],
           [True, True, True]]

game_over = False

#boucle du jeu
while game_over == False:

    #pion du joueur a qui c'est le tour
    for pion in ['X', 'O']:

        if pion == "X":
            print("tour du bg (X)")
        if pion == "O":
            print("tour du pd (O)")
        
        #affichage du plateau
        print(" 1   2   3")
        print("-----------")       
        for i in range(3):
            ligne = plateau[i]
            print(f" {ligne[0]} | {ligne[1]} | {ligne[2]}  {i+1}")
            print("-----------")
        ajoue = False

        #choix du placement du pion 
        while ajoue == False:
            xvalid = False
            yvalid = False

            #choix d'un x valide
            while xvalid == False:
                x = int(input("x?")) - 1
                if x not in [0,1,2]:
                    print(f"mais où est ce que tu vois une case n°{x+1} ಠ_ಠ")
                else:
                    xvalid = True

            #choix d'un y valide
            while yvalid == False:
                y = int(input("y?")) - 1
                if y not in [0,1,2]:
                    print(f"mais où est ce que tu vois une case n°{y+1} ಠ_ಠ")
                else:
                    yvalid = True
            
            #placement du pion 
            if possible[y][x] == True:
                plateau[y][x] = pion
                possible[y][x] = False
                ajoue = True
            else:
                print("pas possible, reessaie fdp")
            
            #verifier si quelqu'un a gagné
            plateau_gagnants = [[pion, pion, pion],[],[]]



    