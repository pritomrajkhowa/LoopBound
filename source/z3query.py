import sys
import os
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/setuptools/")
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/z3/python/")
from z3 import *
init(currentdirectory+"/packages/z3")
set_param(proof=True)

try:
	_p1=Int('_p1')
	_p2=Int('_p2')
	_n=Int('_n')
	_bool=Int('_bool')
	arraySort = DeclareSort('arraySort')
	_f=Function('_f',IntSort(),IntSort())
	_ToReal=Function('_ToReal',RealSort(),IntSort())
	_ToInt=Function('_ToInt',IntSort(),RealSort())
	a=Int('a')
	c=Int('c')
	b=Int('b')
	d=Int('d')
	_N1=Function('_N1',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	a1=Function('a1',IntSort(),IntSort())
	break_1_flag1=Function('break_1_flag1',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	b7=Function('b7',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_1_flag7=Function('break_1_flag7',IntSort(),IntSort(),IntSort(),IntSort())
	b1=Function('b1',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d7=Function('d7',IntSort(),IntSort(),IntSort(),IntSort())
	c1=Function('c1',IntSort(),IntSort())
	_n1=Int('_n1')
	d1=Function('d1',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	Dis1=Function('Dis1',RealSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",500)
	_s.add(ForAll([_n1],Implies(_n1>=0,b7(_n1 + 1, c, b, d) == If(c >= d7(_n1, c, d) + 1,b7(_n1, c, b, d),If(d7(_n1, c, d) >= c,b7(_n1, c, b, d) + 1,b7(_n1, c, b, d))))))
	_s.add(ForAll([_n1],Implies(_n1>=0,d7(_n1 + 1, c, d) == If(c >= d7(_n1, c, d) + 1,d7(_n1, c, d) + 1,d7(_n1, c, d)))))
	_s.add(b7(0, c, b, d) == b)
	_s.add(d7(0, c, d) == d)
	_s.add(Not(d7(0, c, d) >= c))

except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()

	sys.exit(1)

try:
	result=_s.check()
	if sat==result:
		print "Counter Example"
		print _s.model()
	elif unsat==result:
		result
		try:
			if os.path.isfile('j2llogs.logs'):
				file = open('j2llogs.logs', 'a')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
			else:
				file = open('j2llogs.logs', 'w')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
		except Exception as e:
			file = open('j2llogs.logs', 'a')
			file.write("\n**************\nProof Details\n**************\n"+"Error"+"\n")
			file.close()
		print "Successfully Proved"
	else:
		print "Failed To Prove"
except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()
