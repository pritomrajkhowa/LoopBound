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
	break_3_flag1=Function('break_3_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_1_flag10=Function('break_1_flag10',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_12_flag60=Function('break_12_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_9_flag47=Function('break_9_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	a60=Function('a60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_3_flag26=Function('break_3_flag26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	b1=Function('b1',IntSort(),IntSort())
	break_11_flag60=Function('break_11_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_n4=Int('_n4')
	break_4_flag47=Function('break_4_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d1=Function('d1',IntSort(),IntSort(),IntSort(),IntSort())
	break_3_flag60=Function('break_3_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_4_flag60=Function('break_4_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_2_flag10=Function('break_2_flag10',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d10=Function('d10',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_6_flag1=Function('break_6_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_7_flag47=Function('break_7_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	e10=Function('e10',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_11_flag1=Function('break_11_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_4_flag26=Function('break_4_flag26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_N2=Function('_N2',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_6_flag60=Function('break_6_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_9_flag60=Function('break_9_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_N3=Function('_N3',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_2_flag1=Function('break_2_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_8_flag1=Function('break_8_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_9_flag1=Function('break_9_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_5_flag60=Function('break_5_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_3_flag47=Function('break_3_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_5_flag26=Function('break_5_flag26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_7_flag60=Function('break_7_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_N1=Function('_N1',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_1_flag26=Function('break_1_flag26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	e26=Function('e26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_N4=Function('_N4',IntSort(),IntSort(),IntSort(),IntSort())
	a1=Function('a1',IntSort(),IntSort(),IntSort(),IntSort())
	break_10_flag60=Function('break_10_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_5_flag47=Function('break_5_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	c47=Function('c47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_1_flag60=Function('break_1_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_1_flag47=Function('break_1_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	c26=Function('c26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	c1=Function('c1',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	e1=Function('e1',IntSort(),IntSort(),IntSort(),IntSort())
	break_2_flag26=Function('break_2_flag26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_5_flag1=Function('break_5_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	e47=Function('e47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_8_flag47=Function('break_8_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_12_flag1=Function('break_12_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	c=Int('c')
	b=Int('b')
	e=Int('e')
	d=Int('d')
	break_2_flag60=Function('break_2_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_n2=Int('_n2')
	_n3=Int('_n3')
	break_2_flag47=Function('break_2_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_n1=Int('_n1')
	break_7_flag1=Function('break_7_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_8_flag60=Function('break_8_flag60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	c60=Function('c60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d26=Function('d26',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	a47=Function('a47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_1_flag1=Function('break_1_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	break_10_flag1=Function('break_10_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	e60=Function('e60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d47=Function('d47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d60=Function('d60',IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_6_flag47=Function('break_6_flag47',IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	break_4_flag1=Function('break_4_flag1',IntSort(),IntSort(),IntSort(),IntSort())
	ex03=Function('ex03',RealSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",500)
	_s.add(ForAll([_n4],Implies(_n4>=0,a60(_n4 + 1,b,e,d) == a47(_N3(_n4,b,e,d),_n4,b,e,d))))
	_s.add(ForAll([_n4],Implies(_n4>=0,c60(_n4 + 1,c,b,e,d) == c47(_N3(_n4,b,e,d),_n4,b,e,d))))
	_s.add(ForAll([_n4],Implies(_n4>=0,e60(_n4 + 1,e,b,d) == e47(_N3(_n4,b,e,d),_n4,b,e,d))))
	_s.add(ForAll([_n4],Implies(_n4>=0,d60(_n4 + 1,d,b,e) == d47(_N3(_n4,b,e,d),_n4,b,d,e))))
	_s.add(a60(0,b,e,d) == 1)
	_s.add(c60(0,c,b,e,d) == c)
	_s.add(e60(0,e,b,d) == e)
	_s.add(d60(0,d,b,e) == d)
	_s.add(Not(((b)<(((_N4(b,e,d))+(1))))))

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
