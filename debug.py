from tessaract import Tessaract
import math

tessaract = Tessaract([[-1,-1,-1,-1],[1,1,1,1]])
print(tessaract.vertcies)
tessaract.rotate(math.pi*2)
print(tessaract.vertcies)