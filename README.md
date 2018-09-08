# LoopBoundTool

We present a new algorithm for computing upper bounds on the number of executions of each program instruction during any single program run. The upper bounds are expressed as functions of program input values. Experimental results show that the algorithm implemented
in a prototype tool LoopBoundTool often produces tighter bounds than current tools like Looperman, Loopus, KoAT, PUBS and Rank for loop bound analysis.

The goal of loop bound analysis is to derive for each loop in a given program
an upper bound on the number of its iterations during any execution of the
program. These bounds can be parametrized by the program input. The loop
bound analysis is an active research area with two prominent applications: 
program
complexity analysis and worst case execution time (WCET) analysis.
The aim of program complexity analysis is to derive an asymptotic complexity
of a given program. The complexity is commonly considered by programmers
in their everyday work and it is also used in specifications of programming languages.(This para is copied from a paper)


### Awards & Achievements

## Publications


# See below for system requirements, installation, usage, and everything else.

### Support

* If something is not working or missing, open an [issue](https://github.com/VerifierIntegerAssignment/VerifierIntegerAssignment.github.io/issues).

* As a last resort, send mail to 
  [Pritom Rajkhowa](mailto:pritom.rajkhowa@gmail.com), [Fangzhen Lin](mailto:flin@cs.ust.hk), or both.





### System Requirements and Installation

In practice we have run recSolver on standard Ubuntu 16.04 LTS distribution. LoopBoundTool is provided as a set of binaries and libraries for
Ubuntu 16.04 LTS distribution. 

#### Download 


##### Clone over HTTPS:

 $ git clone https://github.com/VerifierIntegerAssignment/LoopBoundTool.git
 
 #### Running LoopBoundTool


LoopBoundTool framework is run by using the `viap_tool_bound.py` tool in the LoopBoundTool directory.
For a given input recurrence equations, the tool tried to find the closed from solution(s). 

#### Running Command

PATH_TO_LoopBoundTool/viap_tool_bound.py sourcefile



#### Output :
```
-DISPLAY DETAIL BOUND ANALYSIS OF INPUT PROGRAM
```

### Using The LoopBoundTool

Next, we illustrate how to use LoopBoundTool 

#### How to run this Example 



```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();

void ex01(int a, int b) {
      while (a >= b) {
          b = b + 1;
      }
          return;
}

```

#### How to run above Example 


#### Example 1

$../viap_tool_bound.py ../benchmark/ABC_ex01.c

#### Output 

```python
Program Body
{
  while (a >= b)
  {
    b = b + 1;
  }

}

Function Name:
ex01
Return Type:
void
Input Variables:
{ a:int b:int}
Local Variables:
{}

Output in normal notation:
1. Frame axioms:
a1(a) = a

2. Output equations:
b1(b,a) = (_N1(a,b)+b)

3. Other axioms:
(a<(_N1(a,b)+b))
(_n1<_N1(a,b)) -> (a>=(_n1+b))

4. Assumption :

5. Assertion :


Bound - O(_n) of the loop corresponds to loop constant_N1(a,b)

((-(1)+b)-a)

Final Complexity ---- O(_n)
```



#### Example 2


```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();
int main() {
int v1 = __VERIFIER_nondet_int();
int v2 = __VERIFIER_nondet_int();
goto loc2;
loc2:
 if (__VERIFIER_nondet_int()) {
  goto loc0;
 }
 goto end;
loc0:
 if (__VERIFIER_nondet_int()) {
  v1 = __VERIFIER_nondet_int();
  v2 = __VERIFIER_nondet_int();
  goto loc1;
 }
 goto end;
loc1:
end:
;
}

```

#### How to run above Example 



$../viap_tool_bound.py ../benchmark/dsa_test1.t2.c

#### Output 

```python
Program Body
{
  int v1_var;
  v1_var = __VERIFIER_nondet_int();
  int v2_var;
  v2_var = __VERIFIER_nondet_int();
  if (__VERIFIER_nondet_int() > 0)
  {
    if (__VERIFIER_nondet_int() > 0)
    {
      v1_var = __VERIFIER_nondet_int();
      v2_var = __VERIFIER_nondet_int();
    }

  }

}

Function Name:
main
Return Type:
int
Input Variables:
{}
Local Variables:
{ v1_var:int v2_var:int}

Output in normal notation:
1. Frame axioms:

2. Output equations:
v1_var1 = ite((__VERIFIER_nondet_int7>0),ite((__VERIFIER_nondet_int6>0),__VERIFIER_nondet_int4,__VERIFIER_nondet_int2),__VERIFIER_nondet_int2)
v2_var1 = ite((__VERIFIER_nondet_int7>0),ite((__VERIFIER_nondet_int6>0),__VERIFIER_nondet_int5,__VERIFIER_nondet_int3),__VERIFIER_nondet_int3)

3. Other axioms:

4. Assumption :

5. Assertion :


Final Complexity ---- O(1)
```



#### Example 3


```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();

void ex02(int a,int b) {
    int i = 1;
      while (i-b<a) {
	i=i/2;
      }

}
```

#### How to run above Example 



$../viap_tool_bound.py ../benchmark/simple1.c

#### Output 

```python
Program Body
{
  int i;
  i = 1;
  while ((i - b) < a)
  {
    i = i / 2;
  }

}

Function Name:
ex02
Return Type:
void
Input Variables:
{ a:int b:int}
Local Variables:
{ i:int}

Output in normal notation:
1. Frame axioms:
a1(a) = a
b1(b) = b

2. Output equations:
i1(b,a) = ((2**-(_N1(b,a)))*1)

3. Other axioms:
((((2**-(_N1(b,a)))*1)-b)>=a)
(_n1<_N1(b,a)) -> ((((2**-(_n1))*1)-b)<a)

4. Assumption :

5. Assertion :


Bound - O(log(_n)/log(2))

log(1/(a + b))/log(2)

Final Complexity ---- O(log(_n)/log(2))

```



#### Example 4


```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();

void ex02(int a, int b, int c) {
    a = 0;
      while (b >= 1 + a) {
        c = 0;
          while (1) {
            if (a >= c) {
              c = c + 1;
            }
            else if (c >= a + 1) {
              a = a + 1;
                break;
            }
            else if (1) {
              c = 1;
              a = 1;
              b = 1;
              break;
            }
            else
              return;
          }
      }
          return;
}```

#### How to run above Example 



$../viap_tool_bound.py ../benchmark/ABC_ex02.i

#### Output 

```python
Program Body
{
  int n;
  int i;
  i = 0;
  while (i <= (n * n))
  {
    i = i + 1;
  }

}

Function Name:
main
Return Type:
int
Input Variables:
{}
Local Variables:
{ i:int n:int}

Output in normal notation:
1. Frame axioms:
n1 = n

2. Output equations:
i1 = (_N1+0)

3. Other axioms:
((_N1+0)>(n*n))
(_n1<_N1) -> ((_n1+0)<=(n*n))

4. Assumption :

5. Assertion :


Bound - O(_n**2) of the loop corresponds to loop constant_N1

((n*n)+1)

Final Complexity ---- O(_n**2)

```



#### Example 4


```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();
void ex15(int m, int n, int p, int q) {

        __VERIFIER_assume(m >= 0 && n >=0 && p>=0 && q>=0);
	for (int i = 1; i <= n; i = i + 1)
		for (int j = 1; j <= m; j = j + 1)
			for (int k = i; k <= p; k = k + 1)
				for (int l = q; l <= j; l = l + 1)
					;
}```

#### How to run above Example 



$../viap_tool_bound.py ../benchmark/ABC_ex15.c

#### Output 

```python
Program Body
{
  int _1_ASSUME;
  _1_ASSUME = 0;
  _1_ASSUME = (((m >= 0) && (n >= 0)) && (p >= 0)) && (q >= 0);
  int i;
  i = 1;
  while (i <= n)
  {
    int j;
    j = 1;
    while (j <= m)
    {
      int k;
      k = i;
      while (k <= p)
      {
        int l;
        l = q;
        while (l <= j)
        {
          l = l + 1;
        }

        k = k + 1;
      }

      j = j + 1;
    }

    i = i + 1;
  }

}

Function Name:
ex15
Return Type:
void
Input Variables:
{ q:int p:int m:int n:int}
Local Variables:
{ _1_ASSUME:int i:int k:int j:int l:int}

Output in normal notation:
1. Frame axioms:
q1(q) = q
p1(p) = p
m1(m) = m
n1(n) = n

2. Output equations:
i1(n) = (_N4(n)+1)
k1(n,m,p) = k10(_N4(n),m,p)
j1(n,m) = j10(_N4(n),m)
l1(n,m,q,p) = l10(_N4(n),m,q,p)

3. Other axioms:
((_N1(_n2,_n3,_n4,q)+q)>(_n3+1))
(_n1<_N1(_n2,_n3,_n4,q)) -> ((_n1+q)<=(_n3+1))
l4((_n2+1),_n3,_n4,q,p,m) = (_N1(_n2,_n3,_n4,q)+q)
l4(0,_n3,_n4,q,p,m) = l7(_n3,_n4,q,p,m)
((_N2(_n3,_n4,p)+(_n4+1))>p)
(_n2<_N2(_n3,_n4,p)) -> ((_n2+(_n4+1))<=p)
k7((_n3+1),_n4,p,m) = (_N2(_n3,_n4,p)+(_n4+1))
l7((_n3+1),_n4,q,p,m) = l4(_N2(_n3,_n4,p),_n3,_n4,q,p,m)
k7(0,_n4,p,m) = k10(_n4,m,p)
l7(0,_n4,q,p,m) = l10(_n4,m,q,p)
((_N3(_n4,m)+1)>m)
(_n3<_N3(_n4,m)) -> ((_n3+1)<=m)
k10((_n4+1),m,p) = k7(_N3(_n4,m),_n4,p,m)
j10((_n4+1),m) = (_N3(_n4,m)+1)
l10((_n4+1),m,q,p) = l7(_N3(_n4,m),_n4,q,p,m)
k10(0,m,p) = k
j10(0,m) = j
l10(0,m,q,p) = l
((_N4(n)+1)>n)
(_n4<_N4(n)) -> ((_n4+1)<=n)

4. Assumption :
((((m>=0) and (n>=0)) and (p>=0)) and (q>=0))

5. Assertion :


Bound - O(_n) of the loop corresponds to loop constant_N1(_n2,_n3,_n4,q)

ForAll(_n3,Implies(And(_n3>=0,_n3<((m+1)-1)),(((_n3+1)+1)-q)))

Bound - O(_n) of the loop corresponds to loop constant_N2(_n3,_n4,p)

ForAll(_n4,Implies(And(_n4>=0,_n4<((n+1)-1)),(((p+1)-_n4)-1)))

Bound - O(_n) of the loop corresponds to loop constant_N3(_n4,m)

((m+1)-1)

Bound - O(_n) of the loop corresponds to loop constant_N4(n)

((n+1)-1)

Final Complexity ---- O(_n**4)


```



#### Example 5


```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();
void ex02(int a, int b, int c) {
    a = 0;
      while (b >= 1 + a) {
        c = 0;
          while (1) {
            if (a >= c) {
              c = c + 1;
            }
            else if (c >= a + 1) {
              a = a + 1;
                break;
            }
            else if (1) {
              c = 1;
              a = 1;
              b = 1;
              break;
            }
            else
              return;
          }
      }
          return;
}```

#### How to run above Example 



$../viap_tool_bound.py ../benchmark/ABC_ex02.c

#### Output 

```python
Program Body
{
  int break_3_flag;
  break_3_flag = 0;
  int break_2_flag;
  break_2_flag = 0;
  int break_4_flag;
  break_4_flag = 0;
  int break_1_flag;
  break_1_flag = 0;
  a = 0;
  while ((b >= (1 + a)) && (break_4_flag == 0))
  {
    break_4_flag = 0;
    c = 0;
    while ((((1 > 0) && (break_3_flag == 0)) && (break_2_flag == 0)) && (break_1_flag == 0))
    {
      break_3_flag = 0;
      break_2_flag = 0;
      break_1_flag = 0;
      if (a >= c)
      {
        c = c + 1;
      }
      else
        if (c >= (a + 1))
      {
        a = a + 1;
        break_1_flag = 1;
      }
      else
        if (1 > 0)
      {
        c = 1;
        a = 1;
        b = 1;
        break_2_flag = 1;
      }



      if ((break_2_flag == 0) && (break_1_flag == 0))
      {
        if (((1 <= 0) && (c < (a + 1))) && (a < c))
        {
          break_3_flag = 1;
        }

      }

    }

    if (((1 <= 0) && (c < (a + 1))) && (a < c))
    {
      break_4_flag = 1;
    }

  }

}

Function Name:
ex02
Return Type:
void
Input Variables:
{ a:int c:int b:int}
Local Variables:
{ break_3_flag:int break_2_flag:int break_4_flag:int break_1_flag:int}

Output in normal notation:
1. Frame axioms:

2. Output equations:
a1(b) = a21(_N2(b))
c1(c,b) = c21(_N2(b),c)
b1(b) = b21(_N2(b),b)
break_4_flag1(b) = break_4_flag21(_N2(b))
break_1_flag1(b) = break_1_flag21(_N2(b))
break_3_flag1(b) = break_3_flag21(_N2(b))
break_2_flag1(b) = break_2_flag21(_N2(b))

3. Other axioms:
a16((_n1+1),_n2) = ite((a16(_n1,_n2)>=c16(_n1,_n2)),a16(_n1,_n2),ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),(a16(_n1,_n2)+1),ite((1>0),1,a16(_n1,_n2))))
c16((_n1+1),_n2) = ite((a16(_n1,_n2)>=c16(_n1,_n2)),(c16(_n1,_n2)+1),ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),c16(_n1,_n2),ite((1>0),1,c16(_n1,_n2))))
b16((_n1+1),_n2,b) = ite((a16(_n1,_n2)>=c16(_n1,_n2)),b16(_n1,_n2,b),ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),b16(_n1,_n2,b),ite((1>0),1,b16(_n1,_n2,b))))
break_1_flag16((_n1+1),_n2) = ite((a16(_n1,_n2)>=c16(_n1,_n2)),0,ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),1,0))
break_3_flag16((_n1+1),_n2) = ite(((ite((a16(_n1,_n2)>=c16(_n1,_n2)),0,ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),0,ite((1>0),1,0)))==0) and (ite((a16(_n1,_n2)>=c16(_n1,_n2)),0,ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),1,0))==0)),ite((((1<=0) and (ite((a16(_n1,_n2)>=c16(_n1,_n2)),(c16(_n1,_n2)+1),ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),c16(_n1,_n2),ite((1>0),1,c16(_n1,_n2))))<(ite((a16(_n1,_n2)>=c16(_n1,_n2)),a16(_n1,_n2),ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),(a16(_n1,_n2)+1),ite((1>0),1,a16(_n1,_n2))))+1))) and (ite((a16(_n1,_n2)>=c16(_n1,_n2)),a16(_n1,_n2),ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),(a16(_n1,_n2)+1),ite((1>0),1,a16(_n1,_n2))))<ite((a16(_n1,_n2)>=c16(_n1,_n2)),(c16(_n1,_n2)+1),ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),c16(_n1,_n2),ite((1>0),1,c16(_n1,_n2)))))),1,0),0)
break_2_flag16((_n1+1),_n2) = ite((a16(_n1,_n2)>=c16(_n1,_n2)),0,ite((c16(_n1,_n2)>=(a16(_n1,_n2)+1)),0,ite((1>0),1,0)))
a16(0,_n2) = a21(_n2)
c16(0,_n2) = 0
b16(0,_n2,b) = b21(_n2,b)
break_1_flag16(0,_n2) = break_1_flag21(_n2)
break_3_flag16(0,_n2) = break_3_flag21(_n2)
break_2_flag16(0,_n2) = break_2_flag21(_n2)
((((1<=0) or (break_3_flag16(_N1(_n2),_n2)!=0)) or (break_2_flag16(_N1(_n2),_n2)!=0)) or (break_1_flag16(_N1(_n2),_n2)!=0))
(_n1<_N1(_n2)) -> ((((1>0) and (break_3_flag16(_n1,_n2)==0)) and (break_2_flag16(_n1,_n2)==0)) and (break_1_flag16(_n1,_n2)==0))
a21((_n2+1)) = a16(_N1(_n2),_n2)
c21((_n2+1),c) = c16(_N1(_n2),_n2)
b21((_n2+1),b) = b16(_N1(_n2),_n2,b)
break_4_flag21((_n2+1)) = ite((((1<=0) and (c16(_N1(_n2),_n2)<(a16(_N1(_n2),_n2)+1))) and (a16(_N1(_n2),_n2)<c16(_N1(_n2),_n2))),1,0)
break_1_flag21((_n2+1)) = break_1_flag16(_N1(_n2),_n2)
break_3_flag21((_n2+1)) = break_3_flag16(_N1(_n2),_n2)
break_2_flag21((_n2+1)) = break_2_flag16(_N1(_n2),_n2)
a21(0) = 0
c21(0,c) = c
b21(0,b) = b
break_4_flag21(0) = 0
break_1_flag21(0) = 0
break_3_flag21(0) = 0
break_2_flag21(0) = 0
((b21(_N2(b),b)<(1+a21(_N2(b)))) or (break_4_flag21(_N2(b))!=0))
(_n2<_N2(b)) -> ((b21(_n2,b)>=(1+a21(_n2))) and (break_4_flag21(_n2)==0))

4. Assumption :

5. Assertion :


Bound - O(_n) of the loop corresponds to loop constant_N1(_n2)

Bound - O(_n) of the loop corresponds to loop constant_N2(b)


Detected Scenario is as follows-
((0<=_n1) and (_n1<_CE1(_n2))) -> (a16(_n1,_n2)>=c16(_n1,_n2))
(a16(_CE1(_n2),_n2)<c16(_CE1(_n2),_n2))
(c16(_CE1(_n2),_n2)>=(a16(_CE1(_n2),_n2)+1))
(_N1(_n2)==(_CE1(_n2)+1))
c16(_N1(_n2),_n2)=_CE1(_n2)
a16(_N1(_n2),_n2)=(1+a21(_n2))
b16(_N1(_n2),_n2,b)=b21(_n2,b)
b21(_N2(b),b)=b
c21(_N2(b),c)=_CE1(_N2(b))
a21(_N2(b))=_N2(b)
a1(b) = _N2(b)
c1(c,b) = _CE1(_N2(b))
b1(b) = b
break_1_flag1(b) = 1

Final Complexity ---- O(n**2)
```



#### Example 6


```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();
void ex03(int a, int b, int c, int d, int e) {
    a = 1;
      while (b >= a) {
        c = 1;
          while (1) {
            if (a >= c) {
              d = a + 1;
              while (1) {
                if (b >= d) {
                  e = 1;
                  while (1) {
                    if (d >= e) {
                      e = e + 1;
                    }
                    else if (e >= d + 1) {
                      d = d + 1;
                        break;
                    }
                    else
                      return;
                  }
                }
                else if (d >= b + 1) {
                  c = c + 1;
                    break;
                }
                else
                  return;
              }
            }
            else if (c >= a + 1) {
              a = a + 1;
              break;
            }
            else
              return;
          }
      }
          return;
}```

#### How to run above Example 



$../viap_tool_bound.py ../benchmark/ABC_ex03.c

#### Output 

```python
Program Body
{
  int break_8_flag;
  break_8_flag = 0;
  int break_12_flag;
  break_12_flag = 0;
  int break_10_flag;
  break_10_flag = 0;
  int break_11_flag;
  break_11_flag = 0;
  int break_4_flag;
  break_4_flag = 0;
  int break_1_flag;
  break_1_flag = 0;
  int break_3_flag;
  break_3_flag = 0;
  int break_5_flag;
  break_5_flag = 0;
  int break_2_flag;
  break_2_flag = 0;
  int break_7_flag;
  break_7_flag = 0;
  int break_9_flag;
  break_9_flag = 0;
  int break_6_flag;
  break_6_flag = 0;
  a = 1;
  while ((((b >= a) && (break_10_flag == 0)) && (break_11_flag == 0)) && (break_12_flag == 0))
  {
    break_10_flag = 0;
    break_11_flag = 0;
    break_12_flag = 0;
    c = 1;
    while (((((1 > 0) && (break_8_flag == 0)) && (break_7_flag == 0)) && (break_9_flag == 0)) && (break_6_flag == 0))
    {
      break_8_flag = 0;
      break_7_flag = 0;
      break_9_flag = 0;
      break_6_flag = 0;
      if (a >= c)
      {
        d = a + 1;
        while ((((1 > 0) && (break_3_flag == 0)) && (break_5_flag == 0)) && (break_4_flag == 0))
        {
          break_3_flag = 0;
          break_5_flag = 0;
          break_4_flag = 0;
          if (b >= d)
          {
            e = 1;
            while (((1 > 0) && (break_2_flag == 0)) && (break_1_flag == 0))
            {
              break_2_flag = 0;
              break_1_flag = 0;
              if (d >= e)
              {
                e = e + 1;
              }
              else
                if (e >= (d + 1))
              {
                d = d + 1;
                break_1_flag = 1;
              }


              if (break_1_flag == 0)
              {
                if ((e < (d + 1)) && (d < e))
                {
                  break_2_flag = 1;
                }

              }

            }

          }
          else
            if (d >= (b + 1))
          {
            c = c + 1;
            break_3_flag = 1;
          }


          if (break_3_flag == 0)
          {
            if ((d >= (b + 1)) || (b >= d))
            {
              if ((e < (d + 1)) && (d < e))
              {
                break_4_flag = 1;
              }

            }

            if (break_4_flag == 0)
            {
              if ((d < (b + 1)) && (b < d))
              {
                break_5_flag = 1;
              }

            }

          }

        }

      }
      else
        if (c >= (a + 1))
      {
        a = a + 1;
        break_6_flag = 1;
      }


      if (break_6_flag == 0)
      {
        if ((c >= (a + 1)) || (a >= c))
        {
          if ((d >= (b + 1)) || (b >= d))
          {
            if ((e < (d + 1)) && (d < e))
            {
              break_7_flag = 1;
            }

          }

          if (break_7_flag == 0)
          {
            if ((d < (b + 1)) && (b < d))
            {
              break_8_flag = 1;
            }

          }

        }

        if ((break_8_flag == 0) && (break_7_flag == 0))
        {
          if ((c < (a + 1)) && (a < c))
          {
            break_9_flag = 1;
          }

        }

      }

    }

    if ((e < (d + 1)) && (d < e))
    {
      break_10_flag = 1;
    }

    if (break_10_flag == 0)
    {
      if ((d < (b + 1)) && (b < d))
      {
        break_11_flag = 1;
      }

      if (break_11_flag == 0)
      {
        if ((c < (a + 1)) && (a < c))
        {
          break_12_flag = 1;
        }

      }

    }

  }

}

Function Name:
ex03
Return Type:
void
Input Variables:
{ a:int c:int b:int e:int d:int}
Local Variables:
{ break_8_flag:int break_12_flag:int break_10_flag:int break_11_flag:int break_4_flag:int break_1_flag:int break_3_flag:int break_5_flag:int break_2_flag:int break_7_flag:int break_9_flag:int break_6_flag:int}

Output in normal notation:
1. Frame axioms:
b1(b) = b

2. Output equations:
a1(b,e,d) = a60(_N4(b,e,d),b,e,d)
break_8_flag1(b,e,d) = break_8_flag60(_N4(b,e,d),b,e,d)
c1(c,b,e,d) = c60(_N4(b,e,d),c,b,e,d)
e1(e,b,d) = e60(_N4(b,e,d),e,b,d)
d1(d,b,e) = d60(_N4(b,e,d),d,b,e)
break_12_flag1(b,e,d) = break_12_flag60(_N4(b,e,d),b,e,d)
break_10_flag1(b,e,d) = break_10_flag60(_N4(b,e,d),b,e,d)
break_11_flag1(b,e,d) = break_11_flag60(_N4(b,e,d),b,e,d)
break_4_flag1(b,e,d) = break_4_flag60(_N4(b,e,d),b,e,d)
break_1_flag1(b,e,d) = break_1_flag60(_N4(b,e,d),b,e,d)
break_3_flag1(b,e,d) = break_3_flag60(_N4(b,e,d),b,e,d)
break_5_flag1(b,e,d) = break_5_flag60(_N4(b,e,d),b,e,d)
break_2_flag1(b,e,d) = break_2_flag60(_N4(b,e,d),b,e,d)
break_7_flag1(b,e,d) = break_7_flag60(_N4(b,e,d),b,e,d)
break_9_flag1(b,e,d) = break_9_flag60(_N4(b,e,d),b,e,d)
break_6_flag1(b,e,d) = break_6_flag60(_N4(b,e,d),b,e,d)

3. Other axioms:
break_2_flag10((_n1+1),_n2,_n3,_n4,b,e,d) = ite((ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),0,ite((e10(_n1,_n2,_n3,_n4,b,e,d)>=(d10(_n1,_n2,_n3,_n4,b,e,d)+1)),1,0))==0),ite(((ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),(e10(_n1,_n2,_n3,_n4,b,e,d)+1),e10(_n1,_n2,_n3,_n4,b,e,d))<(ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),d10(_n1,_n2,_n3,_n4,b,e,d),ite((e10(_n1,_n2,_n3,_n4,b,e,d)>=(d10(_n1,_n2,_n3,_n4,b,e,d)+1)),(d10(_n1,_n2,_n3,_n4,b,e,d)+1),d10(_n1,_n2,_n3,_n4,b,e,d)))+1)) and (ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),d10(_n1,_n2,_n3,_n4,b,e,d),ite((e10(_n1,_n2,_n3,_n4,b,e,d)>=(d10(_n1,_n2,_n3,_n4,b,e,d)+1)),(d10(_n1,_n2,_n3,_n4,b,e,d)+1),d10(_n1,_n2,_n3,_n4,b,e,d)))<ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),(e10(_n1,_n2,_n3,_n4,b,e,d)+1),e10(_n1,_n2,_n3,_n4,b,e,d)))),1,0),0)
e10((_n1+1),_n2,_n3,_n4,b,e,d) = ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),(e10(_n1,_n2,_n3,_n4,b,e,d)+1),e10(_n1,_n2,_n3,_n4,b,e,d))
d10((_n1+1),_n2,_n3,_n4,b,e,d) = ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),d10(_n1,_n2,_n3,_n4,b,e,d),ite((e10(_n1,_n2,_n3,_n4,b,e,d)>=(d10(_n1,_n2,_n3,_n4,b,e,d)+1)),(d10(_n1,_n2,_n3,_n4,b,e,d)+1),d10(_n1,_n2,_n3,_n4,b,e,d)))
break_1_flag10((_n1+1),_n2,_n3,_n4,b,e,d) = ite((d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d)),0,ite((e10(_n1,_n2,_n3,_n4,b,e,d)>=(d10(_n1,_n2,_n3,_n4,b,e,d)+1)),1,0))
break_2_flag10(0,_n2,_n3,_n4,b,e,d) = break_2_flag26(_n2,_n3,_n4,b,e,d)
e10(0,_n2,_n3,_n4,b,e,d) = 1
d10(0,_n2,_n3,_n4,b,e,d) = d26(_n2,_n3,_n4,b,e,d)
break_1_flag10(0,_n2,_n3,_n4,b,e,d) = break_1_flag26(_n2,_n3,_n4,b,e,d)
(((1<=0) or (break_2_flag10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d)!=0)) or (break_1_flag10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d)!=0))
(_n1<_N1(_n2,_n3,_n4,b,e,d)) -> (((1>0) and (break_2_flag10(_n1,_n2,_n3,_n4,b,e,d)==0)) and (break_1_flag10(_n1,_n2,_n3,_n4,b,e,d)==0))
c26((_n2+1),_n3,_n4,b,e,d) = ite((b>=d26(_n2,_n3,_n4,b,e,d)),c26(_n2,_n3,_n4,b,e,d),ite((d26(_n2,_n3,_n4,b,e,d)>=(b+1)),(c26(_n2,_n3,_n4,b,e,d)+1),c26(_n2,_n3,_n4,b,e,d)))
e26((_n2+1),_n3,_n4,b,e,d) = ite((b>=d26(_n2,_n3,_n4,b,e,d)),e10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),e26(_n2,_n3,_n4,b,e,d))
d26((_n2+1),_n3,_n4,b,e,d) = ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))
break_4_flag26((_n2+1),_n3,_n4,b,e,d) = ite((ite((b>=d26(_n2,_n3,_n4,b,e,d)),0,ite((d26(_n2,_n3,_n4,b,e,d)>=(b+1)),1,0))==0),ite(((ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))>=(b+1)) or (b>=ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d)))),ite(((ite((b>=d26(_n2,_n3,_n4,b,e,d)),e10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),e26(_n2,_n3,_n4,b,e,d))<(ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))+1)) and (ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))<ite((b>=d26(_n2,_n3,_n4,b,e,d)),e10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),e26(_n2,_n3,_n4,b,e,d)))),1,0),0),0)
break_1_flag26((_n2+1),_n3,_n4,b,e,d) = ite((b>=d26(_n2,_n3,_n4,b,e,d)),break_1_flag10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),break_1_flag26(_n2,_n3,_n4,b,e,d))
break_3_flag26((_n2+1),_n3,_n4,b,e,d) = ite((b>=d26(_n2,_n3,_n4,b,e,d)),0,ite((d26(_n2,_n3,_n4,b,e,d)>=(b+1)),1,0))
break_5_flag26((_n2+1),_n3,_n4,b,e,d) = ite((ite((b>=d26(_n2,_n3,_n4,b,e,d)),0,ite((d26(_n2,_n3,_n4,b,e,d)>=(b+1)),1,0))==0),ite((ite(((ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))>=(b+1)) or (b>=ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d)))),ite(((ite((b>=d26(_n2,_n3,_n4,b,e,d)),e10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),e26(_n2,_n3,_n4,b,e,d))<(ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))+1)) and (ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))<ite((b>=d26(_n2,_n3,_n4,b,e,d)),e10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),e26(_n2,_n3,_n4,b,e,d)))),1,0),0)==0),ite(((ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d))<(b+1)) and (b<ite((b>=d26(_n2,_n3,_n4,b,e,d)),d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),d26(_n2,_n3,_n4,b,e,d)))),1,0),0),0)
break_2_flag26((_n2+1),_n3,_n4,b,e,d) = ite((b>=d26(_n2,_n3,_n4,b,e,d)),break_2_flag10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d),break_2_flag26(_n2,_n3,_n4,b,e,d))
c26(0,_n3,_n4,b,e,d) = c47(_n3,_n4,b,e,d)
e26(0,_n3,_n4,b,e,d) = e47(_n3,_n4,b,e,d)
d26(0,_n3,_n4,b,e,d) = (a47(_n3,_n4,b,e,d)+1)
break_4_flag26(0,_n3,_n4,b,e,d) = break_4_flag47(_n3,_n4,b,e,d)
break_1_flag26(0,_n3,_n4,b,e,d) = break_1_flag47(_n3,_n4,b,e,d)
break_3_flag26(0,_n3,_n4,b,e,d) = break_3_flag47(_n3,_n4,b,e,d)
break_5_flag26(0,_n3,_n4,b,e,d) = break_5_flag47(_n3,_n4,b,e,d)
break_2_flag26(0,_n3,_n4,b,e,d) = break_2_flag47(_n3,_n4,b,e,d)
((((1<=0) or (break_3_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)!=0)) or (break_5_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)!=0)) or (break_4_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)!=0))
(_n2<_N2(_n3,_n4,b,e,d)) -> ((((1>0) and (break_3_flag26(_n2,_n3,_n4,b,e,d)==0)) and (break_5_flag26(_n2,_n3,_n4,b,e,d)==0)) and (break_4_flag26(_n2,_n3,_n4,b,e,d)==0))
a47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))
break_8_flag47((_n3+1),_n4,b,e,d) = ite((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),0,ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),1,0))==0),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d))>=(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))+1)) or (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d)))),ite((ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))>=(b+1)) or (b>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e)))),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d))<(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))+1)) and (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))<ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d)))),1,0),0)==0),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))<(b+1)) and (b<ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e)))),1,0),0),0),0)
c47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d))
e47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d))
d47((_n3+1),_n4,b,d,e) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))
break_4_flag47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),break_4_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),break_4_flag47(_n3,_n4,b,e,d))
break_1_flag47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),break_1_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),break_1_flag47(_n3,_n4,b,e,d))
break_3_flag47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),break_3_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),break_3_flag47(_n3,_n4,b,e,d))
break_5_flag47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),break_5_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),break_5_flag47(_n3,_n4,b,e,d))
break_2_flag47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),break_2_flag26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),break_2_flag47(_n3,_n4,b,e,d))
break_7_flag47((_n3+1),_n4,b,e,d) = ite((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),0,ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),1,0))==0),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d))>=(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))+1)) or (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d)))),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))>=(b+1)) or (b>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e)))),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d))<(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))+1)) and (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))<ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d)))),1,0),0),0),0)
break_9_flag47((_n3+1),_n4,b,e,d) = ite((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),0,ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),1,0))==0),ite(((ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d))>=(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))+1)) or (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d)))),ite((ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))>=(b+1)) or (b>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e)))),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d))<(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))+1)) and (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))<ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d)))),1,0),0)==0),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))<(b+1)) and (b<ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e)))),1,0),0),0)==0) and (ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d))>=(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))+1)) or (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d)))),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))>=(b+1)) or (b>=ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e)))),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d))<(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))+1)) and (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),d47(_n3,_n4,b,d,e))<ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),e47(_n3,_n4,b,e,d)))),1,0),0),0)==0)),ite(((ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d))<(ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))+1)) and (ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),a47(_n3,_n4,b,e,d),ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),(a47(_n3,_n4,b,e,d)+1),a47(_n3,_n4,b,e,d)))<ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d),c47(_n3,_n4,b,e,d)))),1,0),0),0)
break_6_flag47((_n3+1),_n4,b,e,d) = ite((a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d)),0,ite((c47(_n3,_n4,b,e,d)>=(a47(_n3,_n4,b,e,d)+1)),1,0))
a47(0,_n4,b,e,d) = a60(_n4,b,e,d)
break_8_flag47(0,_n4,b,e,d) = break_8_flag60(_n4,b,e,d)
c47(0,_n4,b,e,d) = 1
e47(0,_n4,b,e,d) = e60(_n4,e,b,d)
d47(0,_n4,b,d,e) = d60(_n4,d,b,e)
break_4_flag47(0,_n4,b,e,d) = break_4_flag60(_n4,b,e,d)
break_1_flag47(0,_n4,b,e,d) = break_1_flag60(_n4,b,e,d)
break_3_flag47(0,_n4,b,e,d) = break_3_flag60(_n4,b,e,d)
break_5_flag47(0,_n4,b,e,d) = break_5_flag60(_n4,b,e,d)
break_2_flag47(0,_n4,b,e,d) = break_2_flag60(_n4,b,e,d)
break_7_flag47(0,_n4,b,e,d) = break_7_flag60(_n4,b,e,d)
break_9_flag47(0,_n4,b,e,d) = break_9_flag60(_n4,b,e,d)
break_6_flag47(0,_n4,b,e,d) = break_6_flag60(_n4,b,e,d)
(((((1<=0) or (break_8_flag47(_N3(_n4,b,e,d),_n4,b,e,d)!=0)) or (break_7_flag47(_N3(_n4,b,e,d),_n4,b,e,d)!=0)) or (break_9_flag47(_N3(_n4,b,e,d),_n4,b,e,d)!=0)) or (break_6_flag47(_N3(_n4,b,e,d),_n4,b,e,d)!=0))
(_n3<_N3(_n4,b,e,d)) -> (((((1>0) and (break_8_flag47(_n3,_n4,b,e,d)==0)) and (break_7_flag47(_n3,_n4,b,e,d)==0)) and (break_9_flag47(_n3,_n4,b,e,d)==0)) and (break_6_flag47(_n3,_n4,b,e,d)==0))
a60((_n4+1),b,e,d) = a47(_N3(_n4,b,e,d),_n4,b,e,d)
break_8_flag60((_n4+1),b,e,d) = break_8_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
c60((_n4+1),c,b,e,d) = c47(_N3(_n4,b,e,d),_n4,b,e,d)
e60((_n4+1),e,b,d) = e47(_N3(_n4,b,e,d),_n4,b,e,d)
d60((_n4+1),d,b,e) = d47(_N3(_n4,b,e,d),_n4,b,d,e)
break_12_flag60((_n4+1),b,e,d) = ite((ite(((e47(_N3(_n4,b,e,d),_n4,b,e,d)<(d47(_N3(_n4,b,e,d),_n4,b,d,e)+1)) and (d47(_N3(_n4,b,e,d),_n4,b,d,e)<e47(_N3(_n4,b,e,d),_n4,b,e,d))),1,0)==0),ite((ite(((d47(_N3(_n4,b,e,d),_n4,b,d,e)<(b+1)) and (b<d47(_N3(_n4,b,e,d),_n4,b,d,e))),1,0)==0),ite(((c47(_N3(_n4,b,e,d),_n4,b,e,d)<(a47(_N3(_n4,b,e,d),_n4,b,e,d)+1)) and (a47(_N3(_n4,b,e,d),_n4,b,e,d)<c47(_N3(_n4,b,e,d),_n4,b,e,d))),1,0),0),0)
break_10_flag60((_n4+1),b,e,d) = ite(((e47(_N3(_n4,b,e,d),_n4,b,e,d)<(d47(_N3(_n4,b,e,d),_n4,b,d,e)+1)) and (d47(_N3(_n4,b,e,d),_n4,b,d,e)<e47(_N3(_n4,b,e,d),_n4,b,e,d))),1,0)
break_11_flag60((_n4+1),b,e,d) = ite((ite(((e47(_N3(_n4,b,e,d),_n4,b,e,d)<(d47(_N3(_n4,b,e,d),_n4,b,d,e)+1)) and (d47(_N3(_n4,b,e,d),_n4,b,d,e)<e47(_N3(_n4,b,e,d),_n4,b,e,d))),1,0)==0),ite(((d47(_N3(_n4,b,e,d),_n4,b,d,e)<(b+1)) and (b<d47(_N3(_n4,b,e,d),_n4,b,d,e))),1,0),0)
break_4_flag60((_n4+1),b,e,d) = break_4_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
break_1_flag60((_n4+1),b,e,d) = break_1_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
break_3_flag60((_n4+1),b,e,d) = break_3_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
break_5_flag60((_n4+1),b,e,d) = break_5_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
break_2_flag60((_n4+1),b,e,d) = break_2_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
break_7_flag60((_n4+1),b,e,d) = break_7_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
break_9_flag60((_n4+1),b,e,d) = break_9_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
break_6_flag60((_n4+1),b,e,d) = break_6_flag47(_N3(_n4,b,e,d),_n4,b,e,d)
a60(0,b,e,d) = 1
break_8_flag60(0,b,e,d) = 0
c60(0,c,b,e,d) = c
e60(0,e,b,d) = e
d60(0,d,b,e) = d
break_12_flag60(0,b,e,d) = 0
break_10_flag60(0,b,e,d) = 0
break_11_flag60(0,b,e,d) = 0
break_4_flag60(0,b,e,d) = 0
break_1_flag60(0,b,e,d) = 0
break_3_flag60(0,b,e,d) = 0
break_5_flag60(0,b,e,d) = 0
break_2_flag60(0,b,e,d) = 0
break_7_flag60(0,b,e,d) = 0
break_9_flag60(0,b,e,d) = 0
break_6_flag60(0,b,e,d) = 0
((((b<a60(_N4(b,e,d),b,e,d)) or (break_10_flag60(_N4(b,e,d),b,e,d)!=0)) or (break_11_flag60(_N4(b,e,d),b,e,d)!=0)) or (break_12_flag60(_N4(b,e,d),b,e,d)!=0))
(_n4<_N4(b,e,d)) -> ((((b>=a60(_n4,b,e,d)) and (break_10_flag60(_n4,b,e,d)==0)) and (break_11_flag60(_n4,b,e,d)==0)) and (break_12_flag60(_n4,b,e,d)==0))

4. Assumption :

5. Assertion :


Bound - O(_n) of the loop corresponds to loop constant_N3(_n4, b, e, d)
Bound - O(_n) of the loop corresponds to loop constant_N2(_n3, _n4, b, e, d)
Bound - O(_n) of the loop corresponds to loop constant_N1(_n2, _n3, _n4, b, e, d)
Bound - O(_n) of the loop corresponds to loop constant_N4(b, e, d)


Detected Scenario is as follows-
((0<=_n3) and (_n3<_CE3(_n4,b,e,d))) -> (a47(_n3,_n4,b,e,d)>=c47(_n3,_n4,b,e,d))
(a47(_CE3(_n4,b,e,d),_n4,b,e,d)<c47(_CE3(_n4,b,e,d),_n4,b,e,d))
(c47(_CE3(_n4,b,e,d),_n4,b,e,d)>=(a47(_CE3(_n4,b,e,d),_n4,b,e,d)+1))
(_N3(_n4,b,e,d)==(_CE3(_n4,b,e,d)+1))
((0<=_n2) and (_n2<_CE2(_n3,_n4,b,e,d))) -> (b>=d26(_n2,_n3,_n4,b,e,d))
(b<d26(_CE2(_n3,_n4,b,e,d),_n3,_n4,b,e,d))
(d26(_CE2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)>=(b+1))
(_N2(_n3,_n4,b,e,d)==(_CE2(_n3,_n4,b,e,d)+1))
((0<=_n1) and (_n1<_CE1(_n2,_n3,_n4,b,e,d))) -> (d10(_n1,_n2,_n3,_n4,b,e,d)>=e10(_n1,_n2,_n3,_n4,b,e,d))
(d10(_CE1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d)<e10(_CE1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d))
(e10(_CE1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d)>=(d10(_CE1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d)+1))
(_N1(_n2,_n3,_n4,b,e,d)==(_CE1(_n2,_n3,_n4,b,e,d)+1))
d10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d)=(1+d26(_n2,_n3,_n4,b,e,d))
e10(_N1(_n2,_n3,_n4,b,e,d),_n2,_n3,_n4,b,e,d)=(_CE1(_n2,_n3,_n4,b,e,d)+1)
c26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)=(1+c47(_n3,_n4,b,e,d))
e26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)=(_CE1(_CE2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)+1)
d26(_N2(_n3,_n4,b,e,d),_n3,_n4,b,e,d)=((_CE2(_n3,_n4,b,e,d)+a47(_n3,_n4,b,e,d))+1)
d47(_N3(_n4,b,e,d),_n4,b,d,e)=((_CE2(_CE3(_n4,b,e,d),_n4,b,e,d)+a60(_n4,b,e,d))+1)
a47(_N3(_n4,b,e,d),_n4,b,e,d)=(1+a60(_n4,b,e,d))
c47(_N3(_n4,b,e,d),_n4,b,e,d)=(_CE3(_n4,b,e,d)+1)
e47(_N3(_n4,b,e,d),_n4,b,e,d)=(_CE1(_CE2(_CE3(_n4,b,e,d),_n4,b,e,d),_CE3(_n4,b,e,d),_n4,b,e,d)+1)
d60(_N4(b,e,d),d,b,e)=((_CE2(_CE3(_N4(b,e,d),b,e,d),_N4(b,e,d),b,e,d)+(_N4(b,e,d)+1))+1)
e60(_N4(b,e,d),e,b,d)=(_CE1(_CE2(_CE3(_N4(b,e,d),b,e,d),_N4(b,e,d),b,e,d),_CE3(_N4(b,e,d),b,e,d),_N4(b,e,d),b,e,d)+1)
c60(_N4(b,e,d),c,b,e,d)=(_CE3(_N4(b,e,d),b,e,d)+1)
a60(_N4(b,e,d),b,e,d)=(_N4(b,e,d)+1)
a1(b,e,d) = (_N4(b,e,d)+1)
c1(c,b,e,d) = (_CE3(_N4(b,e,d),b,e,d)+1)
e1(e,b,d) = (_CE1(_CE2(_CE3(_N4(b,e,d),b,e,d),_N4(b,e,d),b,e,d),_CE3(_N4(b,e,d),b,e,d),_N4(b,e,d),b,e,d)+1)
d1(d,b,e) = ((_CE2(_CE3(_N4(b,e,d),b,e,d),_N4(b,e,d),b,e,d)+(_N4(b,e,d)+1))+1)
break_1_flag1(b,e,d) = 1
break_3_flag1(b,e,d) = 1
break_6_flag1(b,e,d) = 1

Final Complexity ---- O(n**4)
```


#### Example 7


```C
// benchmarks/ABC_ex01.c
extern void __VERIFIER_error() __attribute__ ((__noreturn__));
void __VERIFIER_assert(int cond) { if(!(cond)) { ERROR: __VERIFIER_error(); } }
int __VERIFIER_nondet_int();
int BinarySearch(int arr[], int n,int size) { 

    int fst = 0;
    int lst = size - 1; 
    while (fst <= lst) { 
        int mid = (fst + lst) / 2;
        if (arr[mid] < n) fst = mid + 1; 
        else if (arr[mid] == n) break; 
        else lst = mid - 1; } 
    return mid; 
}```

#### How to run above Example 



$../viap_tool_bound.py ../benchmark/binary_seach.i

#### Output 

```python
Program Body
{
  int break_1_flag;
  break_1_flag = 0;
  int RET;
  RET = 0;
  int fst;
  fst = 0;
  int lst;
  lst = size - 1;
  while ((fst <= lst) && (break_1_flag == 0))
  {
    break_1_flag = 0;
    int mid;
    mid = (fst + lst) / 2;
    if (arr[mid] < n)
    {
      fst = mid + 1;
    }
    else
      if (arr[mid] == n)
    {
      break_1_flag = 1;
    }
    else
    {
      lst = mid - 1;
    }


  }

  RET = mid;
}

Function Name:
BinarySearch
Return Type:
int
Input Variables:
{ arr:int size:int n:int}
Local Variables:
{ lst:int fst:int RET:int break_1_flag:int mid:int}

Output in normal notation:
1. Frame axioms:
arr1(arr) = arr
size1(size) = size
n1(n) = n

2. Output equations:
lst1(arr,n,size) = lst7(_N1(arr,n,size),arr,n,size)
fst1(arr,n,size) = fst7(_N1(arr,n,size),arr,n,size)
mid1(arr,n,size) = mid7(_N1(arr,n,size),arr,n,size)
break_1_flag1(arr,n,size) = break_1_flag7(_N1(arr,n,size),arr,n,size)
BinarySearch(n,size,arr) = mid7(_N1(arr,n,size),arr,n,size)

3. Other axioms:
lst7((_n1+1),arr,n,size) = ite((d1array(arr,((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2))<n),lst7(_n1,arr,n,size),ite((d1array(arr,((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2))==n),lst7(_n1,arr,n,size),(((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2)-1)))
fst7((_n1+1),arr,n,size) = ite((d1array(arr,((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2))<n),(((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2)+1),fst7(_n1,arr,n,size))
mid7((_n1+1),arr,n,size) = ((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2)
break_1_flag7((_n1+1),arr,n,size) = ite((d1array(arr,((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2))<n),0,ite((d1array(arr,((fst7(_n1,arr,n,size)+lst7(_n1,arr,n,size))/2))==n),1,0))
lst7(0,arr,n,size) = (size-1)
fst7(0,arr,n,size) = 0
mid7(0,arr,n,size) = mid
break_1_flag7(0,arr,n,size) = 0
((fst7(_N1(arr,n,size),arr,n,size)>lst7(_N1(arr,n,size),arr,n,size)) or (break_1_flag7(_N1(arr,n,size),arr,n,size)!=0))
(_n1<_N1(arr,n,size)) -> ((fst7(_n1,arr,n,size)<=lst7(_n1,arr,n,size)) and (break_1_flag7(_n1,arr,n,size)==0))

4. Assumption :

5. Assertion :


Case
ForAll([_n1],Implies(_n1>=0,((d1array(arr,((((fst7(_n1,arr,n,size))+(lst7(_n1,arr,n,size))))/(2))))<(n))))
Bound - O(log(_n)/log(2)) of the loop corresponds to loop constant_N1(arr,n,size)

log(size + 1)/log(2)

Case
ForAll([_n1],Implies(_n1>=0,And(((d1array(arr,((((fst7(_n1,arr,n,size))+(lst7(_n1,arr,n,size))))/(2))))==(n)),Not(((d1array(arr,((((fst7(_n1,arr,n,size))+(lst7(_n1,arr,n,size))))/(2))))<(n))))))
Bound - O(log(_n)/log(2)) of the loop corresponds to loop constant_N1(arr,n,size)

log(size + 1)/log(2)

Final Complexity ---- O(log(_n)/log(2))
```

