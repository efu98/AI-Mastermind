import random

jeu = [];
M = 50;   # nombre de parents séléctionnés pour produire la génération suivante
N = 4;    # nombre de pions de la combinaison


def get_score(prop):
    for i in jeu:
        if i[0] == prop:
            return i[1];
    return -1;

def compare(solution, proposition):
    comp=[0,0] #[nb de pions bonne couleur + bon placement ; nb de pions de bonne couleur]
    for i in range(len(proposition)):
        if proposition[i] == solution[i]:
            comp[0] +=1
            solution[i] = 0
        if proposition[i] in solution:
            comp[1]+=1
    return comp

def score(comp):
    res_score = 0;
    tab= [[0,0], [0,1], [1,0], [0,2], [1,1], [2,0], [0,3],[1,2], [2,1], [3,0], [0,4], [1,3], [2,2],[4,0]]
    for i in range(len(tab)):
        if comp == tab[i]:
            res_score = i
    return res_score

def eval(c,c_j):
    sc_j = get_score(c_j);
    score_virtuel = score(compare(c, c_j));
    return abs(score_virtuel - sc_j)

def fitness(c):
    somme = 0;
    for i in range(len(jeu)):
        somme += eval(c, jeu[i][0])
    return somme/len(jeu)

def tirage_roulette(candidats):
    roulette_res = []
    roulette = []
    sum_f = 0;
    sum_p = 0;
    f_max = 0;
    fc = 0;
    global f_min
    f_min=9999;
    global best_candidat
    best_candidat=[];

    #trouve f_max pour le calcul des p et le meilleur candidat
    for c in candidats:
        fc = fitness(c)
        if f_max < fc:
            f_max = fc;
        if f_min > fc:
            f_min = fc;
            best_candidat = c

        sum_f+= fc;
        roulette.append([c, fc]);

    #crée la roulette en aditionnant les 'cases' de taille proportionelle au fitness de chaque dandidat
    for i in range(len(roulette)):
        p=(f_max-roulette[i][1])/sum_f;
        roulette[i].append(p)
        sum_p += p;

    # tire au sort 49 candidats
    for tirage in range(M-1):
        v = random.random() * sum_p;
        #print("v=", v);
        index = 0;
        t=0;

        while t < v:
            #print("index=", index);
            t += roulette[index][2];
            #print("t=", t);
            index += 1;
        roulette_res.append(roulette[index-1][0])

    #ajoute le meilleur candidats
    roulette_res.append(best_candidat)

    return roulette_res;

def init_candidats():

    return [[random.randrange(1, 9) for _ in range(N)] for _ in range(100)]

def mutation_swap(candidat):
    prob = random.random();
    if prob < 0.1:
        i1 = random.randrange(N);
        i2 = random.randrange(N);
        temp = candidat[i1];
        candidat[i1]=candidat[i2];
        candidat[i2]=temp;

    return candidat;

def croisement(candidat1, candidat2):
    c1=candidat1
    c2=candidat2
    cut= random.randrange(N);
    for i in range(0,cut):
        temp = c1[i];
        c1[i]=c2[i];
        c2[i]=temp;

    return c1, c2;

def genetique():
    new_generation=[];
    #on créé une population de 100 individus
    candidats = init_candidats();

    for i in range(1):

        #on selectionne 50 individus
        selection = tirage_roulette(candidats);
        parents = selection.copy()

        #on croise la selection
        while len(selection) > 0:
              s = random.randrange(len(selection))-1;
              x = random.randrange(len(selection))-1;

              croisement1, croisement2 = croisement(selection[s], selection[x]);
              new_generation.append(croisement1);
              new_generation.append(croisement2);
              del(selection[s]);
              del(selection[x]);

        #on mute la nouvelle generation
        for i in range(len(new_generation)):
            new_generation[i] = mutation_swap(new_generation[i]);

        candidat = new_generation + parents
        i+=1

    f_min=9999;
    for c in candidat:
        fc = fitness(c)
        if f_min > fc:
            f_min = fc;
            best_candidat = c

    return best_candidat;


def un_jeu():
    solution=[random.randrange(1, 9) for _ in range(N)]


    #premier tour
    premier_candidat = [random.randrange(1, 9) for _ in range(N)];
    jeu.append((premier_candidat, score(compare(solution, premier_candidat))));
    i =0;
    candidat=genetique()
    while solution != candidat:
        jeu.append((candidat, score(compare(solution, candidat))));
        i += 1
        if i > 99:
            break
        candidat=genetique()

    return i

def main():
    print(un_jeu())


if __name__ == "__main__":
    main()

#tester si on créé à partir des parents 100 croisements ou si la nouvelle généreation est le somme des 50 parents et des 50 enfants
#tester si on fait 1 ou plusieurs générations entre chaque tour de jeux
