import random

jeu = [];
N = 4;    # nombre de pions de la combinaison
solution = [random.randrange(1, 9) for _ in range(N)]
print(solution)


def compare(solution, proposition):
    comp=[0,0] #[nb de pions bonne couleur + bon placement ; nb de pions de bonne couleur]
    s=solution.copy();
    p=proposition.copy();
    #recherche des pions ayant la bonne couleur et le bon placement
    for i in range(len(proposition)):
        if p[i] == s[i]:
            comp[0] +=1
            s[i] = 0
            p[i]=-1;
    #recherche de pions ayant la bonne couleur mais pas le bon placement
    for j in range(len(proposition)):
        for k in range(len(proposition)):
            if p[j]==s[k]:
                comp[1]+=1
                s[k]=0;
                p[j]=-1
    return comp

def score(comp):
    res_score = 0;
    #N étant la taille de la solution
    tab= [[0,0], [0,1], [1,0], [0,2], [1,1], [2,0], [0,3],[1,2], [2,1], [3,0], [0,4], [1,3], [2,2],[4,0]]
    for i in range(len(tab)):
        if comp == tab[i]:
            res_score = i
    return res_score

def new_guess():
    while True:
        #step 1 : on recupere m le nombre de pions bien places et on fixe m pions du candidat au hasard
        position=[0,1,2,3];
        i=0;
        precedent = jeu[-1];
        comparaison= compare(solution, precedent[0]);
        print("comparaison=", comparaison);
        new_candidat = [0,0,0,0];
        last_candidat = precedent[0];
        print("last_candidat=", last_candidat);

        while i < comparaison[0]:
            x = random.randrange(0, 4)
            if new_candidat[x] == 0:
                new_candidat[x] = last_candidat[x]
                position.remove(x)
                i+=1
        print("new_candidat", new_candidat);

        #step 2 : on recupere p le nombre de pions de bonne couleur mais mal placés et on permute p pions du candidat au hasard
        j = comparaison[1];
        while j > 0:
            if len(position) >= 2 :
                u = random.randrange(0, len(position))
                v = random.randrange(0, len(position))
                while u == v:
                    v = random.randrange(0, len(position))
                y = position[u]
                z = position[v]
                new_candidat[y] = last_candidat[z]
                new_candidat[z] = last_candidat[y]
                position.remove(y)
                position.remove(z)
                j-=2
            if (len(position)==1) :
                for m in range(len(new_candidat)):
                    if new_candidat[m] == 0:
                        new_candidat[m] = last_candidat[position[0]];
                        position.remove(position[0])
                j-=1

        #step 3 : s'il reste des pions à completer on leur donne une couleur au hasard
        for l in range(len(new_candidat)):
            if new_candidat[l] == 0:
                new_candidat[l] = random.randrange(1,9)
        if(new_candidat!=last_candidat):
            break;
    return new_candidat

def un_jeu():

    i=0

    #premier tour
    candidat = [random.randrange(1, 9) for _ in range(N)];
    jeu.append((candidat, score(compare(solution, candidat))));

    #tours suivants

    while solution != candidat:
        candidat = new_guess()
        jeu.append((candidat, score(compare(solution, candidat))));
        i += 1
    return i

def main():
    print(un_jeu())


if __name__ == "__main__":
    main()


#tester si on créé à partir des parents 100 croisements ou si la nouvelle généreation est le somme des 50 parents et des 50 enfants
#tester si on fait 1 ou plusieurs générations entre chaque tour de jeux
