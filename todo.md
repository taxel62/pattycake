# TODO
- Implement methods that add tile genes and glue genes to the organism.
	- Be sure to add constraints for adding the genes. For example, we don't want redefinitions of glues, we don't want to add tiles if we are already at a max, etc.
- Implement the general algorithm evolving the organisms.
- Easier way to create seed assembly.
- Easier way to define an organism.
	- Can probably just use a simple "SYMBOL NORTH_GLUE EAST_GLUE SOUTH_GLUE WEST_GLUE" per line in a file.