"""
n = 3
  *   2 espaçamento 1 *
 ***  1 espaçamento 3 *
***** 0 espaçamento 5 *

n = 4
   *    3 espaçamento 1 *
  ***   2 espaçamento 3 * 
 *****  1 espaçamento 5 *
******* 0 espaçamento 7 *

n = 5
    *     4 espaçamento 1 *
   ***    3 espaçamento 3 *
  *****   2 espaçamento 5 *
 *******  1 espaçamento 7 *
********* 0 espaçamento 9 *    
   
"""


def christmas_tree(n):
    for x in range(n):
        print(" "*(n-x-1) + "*" * (2*x+1))


christmas_tree(5)
# Desafio Completo-> ZNO
