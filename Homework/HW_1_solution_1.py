# HW 1 solution

from scipy.optimize import minimize

fun = lambda x: (x[0]-x[1])**2 + (x[1] + x[2] - 2)**2 + (x[3] - 1)**2 + (x[4] - 1)**2

cons = ({})
