# RandomWalk
Random walk on 2d grid with contaminants

Suppose a random walker moves in a grid of size 100 x 100 cell. The walker will start position 50 x 50
and will make 1000 moves. Randomly distributed in the grid are n (n= 1, 5, 50) contaminants or sources
of infectious material. Whenever the random walker reaches a grid position with such a contaminant it
is marked as infected and will stay infected for the remainder of the walk (so you could actually
terminate the walk at this point). Conduct computational experiments to explore the following:

a) The probability of the walker to become infected as a function of the number of contaminants in
the grid.

b) The probability of the walker to become infected as a function of the length (i.e., number of steps)
of the random walk.

c) The probability of the walker to become infested as a function of “average step-size”. For this you
need to alter the average distance covered by each step the walker makes. The actual step size of
each step must be an integer and is chosen from a distribution

![Picture1](https://user-images.githubusercontent.com/77468658/192350405-f72fdddc-8e64-4857-be55-425bdd9e7d6f.png)

![Picture2](https://user-images.githubusercontent.com/77468658/192350415-9c4a426f-fbde-4597-a096-1827fd4602e3.png)

![A9vmnk6u_mmmuoz_96o](https://user-images.githubusercontent.com/77468658/192350425-63a17bd2-dbbe-4b91-ad3b-0577f53a4f06.png)
