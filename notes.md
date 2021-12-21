# Notes

## TODO
- Add methods that can modify the genes of an organism. Could start with just the basic mutations outlined in the notes.
	- Worrying about this later, but we need to have some constraints on mutations so that dumb stuff doesn't happen and break a decent system or not change anything at all. For example, no redefining glues, making sure the tileset remains deterministic, etc.
- Evolutionary algorithm.
	- Setup.
	- Simulate on all organisms.
	- Find best via reward function.
	- Breed.
	- Mutate.
	- Repeat for G generations.
- File input and output should be moved to Tools.py and made more general.

## Questions
- How best to setup a neural network? One large one or multiple small ones?
- Best ways to mutate?
- Best ways to reproduce?
- How many of these questions are normal and won't ever have a 'right' answer just better answers?

## Resources
- [NEAT paper](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf)
- [Evolutionary Cellular Automata](https://arxiv.org/pdf/1508.05752.pdf)
- [Neural Cellular Automata](https://distill.pub/2020/growing-ca/)

## Optimizations
- Assembly currently looks through the tileset, but since we want deterministic tilesets, the South and West glues of each location in the assembly must be unique. 