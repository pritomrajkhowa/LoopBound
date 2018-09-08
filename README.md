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
