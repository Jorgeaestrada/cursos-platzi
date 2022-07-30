from typing import Tuple, Dict, List
# Lista de diccionarios, cuyas llaves son strings
# y cuyos valores son tuplas de dos enteros
CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
	{
		'coord1': (1,2),
		'coord2': (3,4),
	},
	{
		'coord1': (0,1),
		'coord2': (2,5)
	}
]

print("coordinates:    {}".format(coordinates))