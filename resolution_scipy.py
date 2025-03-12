from scipy.optimize import linprog

# Définition du problème de maximisation: Max Z = 20 xA1 + 35* xA2 +50 * xA3 + 18 xB1 + 32* xB2 +45 * xB3 + 22 xC1 + 38* xC2 +55 * xC3 +19 xD1 + 33* xD2 +48 * xD3, dans notre cas, il nous faut miniser le coût
# linprog minimise par défaut, donc on inverse les coefficients
c = [100, 100, 100, 70, 10, 40, 160, 50, 170, 80, 20, 140, 100, 70, 10]  # pertes

# Contraintes sous la forme Ax <= b
A = [[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 2x1 + x2 <= 6  # 2x1 + x2 <= 6
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],  # 2x1 + 3x2 <= 9
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
     [-2, 0, 0, -1, -1, 0, 0, -1, -1, 0, 0, 0, -1, 0, 0], 
     [0, -3, 0, -1, 0, -2, -1, -1, 0, 0, -2, -1, 0, -1, 0],
     [0, 0, -5, -1, -3, -2, -3, 0, -1, -4, -1, -2, 0, -1, -3]]

# eq = [[2, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0], 
#       [0, 3, 0, 1, 0, 2, 1, 1, 0, 0, 2, 1, 0, 1, 0],
#       [0, 0, 5, 1, 3, 2, 3, 0, 1, 4, 1, 2, 0, 1, 3]]
  
b = [(82),(73),(124),(- 162),(-204),(-192)]  # Second membre

# eq_resp = [(162),(204),(192)]

# Contraintes de positivité: x1, x2 >= 0 (géré automatiquement par bounds)
bounds = [(0, None), (0, None), (0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None),(0,None)]  

# Résolution avec l'algorithme du simplexe
result = linprog (c, A_ub = A, b_ub = b, bounds=bounds, method="highs", integrality = 1)
CO2 = (result.fun) * 1.9

# Affichage des résultats
if result.success:
    print("Solution optimale:", result.x)
    print("Valeur optimale des pertes:", result.fun)  # On remet le signe positif pour maximisation
    print("L'émission de CO2 : ", CO2 , "g")
else:
    print("Problème non résoluble:", result.message)
