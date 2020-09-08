import numpy as np
import pandas as pd

class Levee:

    def __init__(self, length, width = 2, height = 1):
        self.length = length
        self.width = width
        self.height = height

    def cross_area(self, shape = 'triangle'):
        """Calculates crossectional area.

        Parameters
        ----------
        shape (str)
            Shape of the levee.

        Returns
        -------
        Crossectional area
        """
        if shape.lower() == 'triangle':
            return 0.5*self.width*self.height
        elif shape.lower() == 'rectangle':
            return self.width * self.height
        else:
            raise ValueError("'shape'  should be either triangle or rectangle")

    