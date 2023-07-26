from modelos.Figures import Circle,Rectangle,Square #apunta a archivo e importa clases
import os

os.system('clear')
#Objects
Circle(radius=5).printCalcs(units="cm", precision=5)
Rectangle(base=10, height=5).printCalcs(units="cm", precision=5)
Square(edge=10).printCalcs(units="cm", precision=5)