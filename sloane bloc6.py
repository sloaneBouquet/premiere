devoir=15
if devoir>=10:
    print("BRAVO MEC")
    
nom=Alice
if nom>=18:
   print("elle a 18 ans ")
   
#exercice 2
def bac (prenom, nom, moyenne):
    if moyenne >= 10:
       texte= ("Congratulation tu as eu ton bac")
    else:
        texte= ("Dommage tu as pas eu ton bac finalement")
    return texte

print(bac("Alice", "Dupon", 18))

print(bac("Bob", "Martin", 9))

