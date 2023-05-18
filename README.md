# TicTacToe
Sovling Tic-Tac-Toe with Minimax

The idea is simple; create code that can use Minimax to "solve" Tic-Tac-Toe. We'll start with some board (either empty, or for testing a user generated one) and it will be up to the code to determine whose turn 
it is, and what that player's best move is. 

Version 1 appears to be effective at finding winning moves and tying moves. However, if the game state is such that a player is doomed to lose, they will not choose the sequence that delays this outcome as long
as possible. In principle this isn't a problem, as it does not change the end result (win-tie-lose), but in terms of trying to model "optimal" play, it would be better to prolong the game and create more 
opportunities for the opponent to make a mistake. Could be corrected by adding a "depth" variable that counts how deep Minimax has to go to find the end state, and in the even a loss is inevitable, preferring
moves that have a greater depth than those with shorter.
