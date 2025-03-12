from pulp import LpMaximize, LpProblem, LpVariable,LpMinimize

# 1️ Définition du problème de minimisation
model = LpProblem(name="Minimisation_Z", sense=LpMinimize)

# 2️ Déclaration des variables de décision (X, Y, Z Le nombre d'unité de métal de 1000, 800 et 550 qui seront utilisés)
# x1 = LpVariable(name="x1", lowBound=0)  nombre de métal de 1000 qui seront coupé en 450
# x2 = LpVariable(name="x2", lowBound=0)  nombre de métal de 1000 qui seront coupé en 300
# x3 = LpVariable(name="x3", lowBound=0)  nombre de métal de 1000 qui seront coupé en 180
# y1 = LpVariable(name="y1", lowBound=0)  nombre de métal de 800 qui seront coupé en 450
# y2 = LpVariable(name="y2", lowBound=0)  nombre de métal de 800 qui seront coupé en 300
# y3 = LpVariable(name="y3", lowBound=0)  nombre de métal de 800 qui seront coupé en 180
# z1 = LpVariable(name="z1", lowBound=0)  nombre de métal de 550 qui seront coupé en 450
# z2 = LpVariable(name="z2", lowBound=0)  nombre de métal de 550 qui seront coupé en 300
# z3 = LpVariable(name="z3", lowBound=0)  nombre de métal de 550 qui seront coupé en 180

# # 9 solutions entieres

x1 = LpVariable(name="x1", lowBound=0, cat="Integer")
x2 = LpVariable(name="x2", lowBound=0, cat="Integer")
x3 = LpVariable(name="x3", lowBound=0, cat="Integer")
x4 = LpVariable(name="x4", lowBound=0, cat="Integer")
x5 = LpVariable(name="x5", lowBound=0, cat="Integer")
x6 = LpVariable(name="x6", lowBound=0, cat="Integer")
x7 = LpVariable(name="x7", lowBound=0, cat="Integer")

y1 = LpVariable(name="y1", lowBound=0, cat="Integer")
y2 = LpVariable(name="y2", lowBound=0, cat="Integer")
y3 = LpVariable(name="y3", lowBound=0, cat="Integer")
y4 = LpVariable(name="y4", lowBound=0, cat="Integer")
y5 = LpVariable(name="y5", lowBound=0, cat="Integer")

z1 = LpVariable(name="z1", lowBound=0, cat="Integer")
z2 = LpVariable(name="z2", lowBound=0, cat="Integer")
z3 = LpVariable(name="z3", lowBound=0, cat="Integer")

# 3️ Ajout de la fonction objectif : Max Z = 3x1 + 2x2
model += (100 * (x1 + x2 + x3 + z1) + 70 * x4 + 10 * x5 + 40 * x6 + 160 * x7 + 50 * y1 + 170 * y2 + 80 * y3 + 20 * y4 + 140 * y5 + 70 * z2 +
          10 * z3) * 1.9 , "Objectif"


# 4️ Ajout des contraintes
model += ( x1 + x2 + x3 + x4 + x5 + x6 + x7 <= 82 , "Contrainte_1")
model += ( y1 + y2 + y3 + y4 + y5 <= 73 , "Contrainte_2")
model += ( z1 + z2 + z3 <= 124, "Contrainte_3")

model += ( 2 * x1 + x4 + x5 + y1 + y2 + z1 >= 162 , "Contrainte_4")
model += ( 3 * x2 + x4 + 2 * x6 + x7 + y1 + 2 * y4 + y5 + z2 >= 204 , "Contrainte_5")
model += ( 5 * x3 + x4 + 3 * x5 + 2 * x6 + 3 * x7 + y2 + 4 * y3 + y4 + 2 * y5 + z2 + 3 * z3 >= 192 , "Contrainte_6")

# 5️ Résolution du problème
model.solve()

# 6️ Affichage des résultats
print("Statut :", model.status)  # Optimal ?
print("Solution optimale :")
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"x3 = {x3.varValue}")
print(f"x4 = {x4.varValue}")
print(f"x5 = {x5.varValue}")
print(f"x6 = {x6.varValue}")
print(f"x7 = {x7.varValue}")
print(f"y1 = {y1.varValue}")
print(f"y2 = {y2.varValue}")
print(f"y3 = {y3.varValue}")
print(f"y4 = {y4.varValue}")
print(f"y5 = {y5.varValue}")
print(f"z1 = {z1.varValue}")
print(f"z2 = {z2.varValue}")
print(f"z3 = {z3.varValue}")

print(f"Valeur optimale de Z = {model.objective.value()}")
