# AI-Mastermind
Solving Mastermind using genetic algorithms

## Description

The Mastermind is a board game for two players. One plays the master and the other guesses the associations of pawns the master has set using clues given by the other player.   

To modelise the Mastermind, the colors are represented with numbers from 1 to 8 and the associations of pawns with an array.  
The score is set according to the rank of the comparaison :
```
([[0,0], [0,1], [1,0], [0,2], [1,1], [2,0], [0,3],[1,2], [2,1], [3,0], [0,4], [1,3], [2,2],[4,0]])
```
 the first value being the number of paws with the right color and the second the number of paws in the right plan and with the right color.
 
The goal is to minimize the fitness function the compares associations with previous questions/answers.   

The roulette Wheel selection was used to solve the game.  
Part of the heuristic hill climbing algorithm has also been implemented.

## Getting Started

### Executing program

```
python3 genetique.py
```

## Authors

Claire, Noélie, Elise

## Acknowledgments

* Images des mathématiques, [Optimisation Inspirée par la Nature](images.math.cnrs.fr/Optimisation-Inspiree-par-la-Nature.html), Carola Doerr, October 9 2018 (visited on April 14, 2021)
* [A heuristic hill climbing algorithm for Mastermind](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.1.2546&rep=rep1&type=pdf), Alexandre Temporel, (visited on April 14, 2021)
