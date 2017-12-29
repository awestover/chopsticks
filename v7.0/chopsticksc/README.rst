This module allows a human to play chopsticks against either another human or a computer.
In the game chopsticks both the user and the human start out with 1 finger on each hand.
The goal of the game is to reduce the other players hand to a 0 in modulus 5, although the game can be played in different moduli.
Valid moves include redistributing your own hands so that you preserve the total number of fingers. This is called a switch.
ex: 1 1 1 1 -> 2 0 1 1
ex: 3 1 1 1 -> 2 2 1 1
Another valid move is called a hit. With a hit you add the value of one of your hands to the value of the opponents hands (modulus 5).
ex: 1 3 1 3 -> 1 3 2 3
ex: 3 3 3 3 -> 3 3 1 3

The computer has a lookup table already coded in that was formed by playing
against initially random opponents and evolving with a genetic algorithm.

Good Luck!
