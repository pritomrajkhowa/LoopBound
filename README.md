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
