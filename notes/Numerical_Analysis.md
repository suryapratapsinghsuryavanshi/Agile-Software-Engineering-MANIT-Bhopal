# Numerical Analysis
> It is the study of numerical methods that attempt at finding approximate solutions of problems rather than the exact ones.

Numerical analysis is a branch of mathematics that uses numerical approximation to solve continuous problems. It involves designing methods that give approximate but accurate numeric solutions. These methods are useful when the exact solution is impossible or prohibitively expensive to calculate.

> Numerical analysis is applied in various fields of science, engineering, and business. Examples of numerical analysis include:

- Ordinary differential equations in celestial mechanics
- Numerical linear algebra in data analysis
- Stochastic differential equations and Markov chains for simulating living cells in medicine and biology

Numerical analysts use algorithms, software, and computer systems to perform calculations, simulations, optimization, data analysis, and modeling.

## Topics we have learn
- Solution of linear of Equation
    - Bisection Method
    - Regula Falsi
    - Iteration Method
    - Secant Method
    - Newton-Raphson Method
    - Graeffe Method
    - Graeffe method for complex root
    - Lin Bairstow Method
- Solution of System of Equation
    - Direct Methods
        - Gauss Elimination Methods
        - Gauss Jordan Method
        - Courts Method
    - Indirect Methods(Itretive)
        - Jacobi Iterative Method
        - Gauss Sidal Iterative Method
        - Relexation Method
- Interpolation
    - Equal Interval
        - Newton Froword Formula
        - Newton Backword Formula
        - Gauss Forword Formula
        - Gauss Backword Formula
        - Stirling Formula
        - Bessal's Formula
    - Unequal Interval
        - Lagrange's Interpolation Formula
        - Newton Divided Diffrence
        - Inverse Lagrange's Formula
    - Numerical Integration
        - Trapezoidal Rule
        - Simpson $\dfrac{1}{3}$ Rule
        - Simpson $\dfrac{3}{8}$ Rule
    - Numerical Diffrentiation
        - All Formula of Equal and Unqual interval can be diffrenciate, and it konown as numerical diffrenciation. For finding f'(x) or f''(x) etc.

### Bisection Method
> The bisection method is an approximation method to find the roots of the given equation by repeatedly dividing the interval. This method will divide the interval until the resulting interval is found, which is extremely small.

The bisection method is a mathematical method for finding the roots of an equation. It's also known as the interval halving method, the binary search method, or the dichotomy method.

The bisection method works by repeatedly dividing the interval until the resulting interval is extremely small. The method is based on the Bolzano's theorem for continuous functions.

The bisection method is a simple and robust method, but it's also relatively slow. It's often used to obtain a rough approximation to a solution, which is then used as a starting point for more rapidly converging methods.

#### The advantages of the bisection method are:
- It's always convergent.
- As iterations are conducted, the interval gets halved.
- You can guarantee the error in the solution of the equation.

##### Method

Let f(x) to be a continous between `a` & `b`.

let f(a) be -ve

& f(b) be +ve

Then the first approximate root is

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B150%7D%20x%20%3D%20%5Cfrac%7B%28a%20&plus;%20b%29%7D%7B2%7D)

if f(x<sub>1</sub>) is -ve then the new interval to be `b` & `x`<sub>1</sub> and if the f(x<sub>1</sub>) is +ve then the new interval should be `x`<sub>1</sub> & `a`.

Then we bisect the interval as before & continue the process until the root is found accuracy.

##### Examples
Q1. x<sup>3</sup>-2x-5=0, find the root of the given equation.

<b>Solution:</b><br>
f(x) = x<sup>3</sup>-2x-5<br>
Find the -ve to +ve transition between two diffrent numbers for this question we have f(2) is -ve and f(2.1) is +ve apply the bisection method unitl some of the digit of x<sub>i</sub> is repeate of 3 digits.

x<sub>1</sub> = (2 + 2.1) / 2 = 2.05

f(x<sub>1</sub>) = f(2.05) = -0.4848, so for now the -ve part of the interval are change to 2.05, new interval for next itration is [2.05, 2.1].

Repeate this process, unitl you get the resultent with atmost 3 repetative digits. <b>The real root of this equation is 2.095</b>.


### Regula Falsi Method
The Regula Falsi method is a numerical method for finding the approximate numerical value of a real root of an equation f(x) = 0. It is also known as the false position method. The method is a trial and error technique that uses test values for the variable and then adjusts the test value according to the outcome.

The method is similar to the bisection method algorithm. It was developed because the bisection method converges at a fairly slow speed. The Regula Falsi method requires less computational effort as it needs to evaluate only one function per iteration.

The method starts by taking two guess values `a` and `b` for the root such that, ![](https://latex.codecogs.com/gif.latex?%5Cinline%20f%28a%29%20f%28b%29%20%3C%200). The iteration formula is given by:

![](https://latex.codecogs.com/gif.latex?%5Cinline%20c%20%3D%20%5Cfrac%7Ba%20*%20f%28b%29%20-%20b%20*%20f%28a%29%7D%7Bf%28b%29%20-%20f%28a%29%7D)

The iteration continues until it converges.

#### Working
i. Find the interval (a, b) s.t. f(a)f(b) < 0
<br/>
ii. Find ![](https://latex.codecogs.com/gif.latex?%5Cinline%20c%20%3D%20%5Cfrac%7Ba%20*%20f%28b%29%20-%20b%20*%20f%28a%29%7D%7Bf%28b%29%20-%20f%28a%29%7D)
<br/>
iii. f(a)f(c) < 0 root -ve in (a, c) or f(b)f(c) < 0 root +ve in (c, b)
<br/>
iv. Repeat stop i & ii until you got the real root.

### Iteration Method
Iteration method is a kind of method where we can minimize the distance from real root to proced gradualy to toward to the real root by itrating the method.

Suppose we have an equation f(x) = 0
The equation can be expressed as

x = Φ(x)

| Φ'(x) |<sub>x = x<sub>0</sub></sub> < 1

The itration method applied

The successive approximation is given by.

x<sub>n</sub> = Φ(x<sub>n-1</sub>)

x<sub>1</sub> = Φ(x<sub>0</sub>)

x<sub>2</sub> = Φ(x<sub>1</sub>)


### Secant Method | Chord Method
The secand method is same as the ragula falsi method only expected the condition of f(x<sub>0</sub>)f(x<sub>1</sub>)<0.

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B200%7D%20x_c%20%3D%20%5Cfrac%7Bx_af%28x_b%29%20-%20x_bf%28x_a%29%7D%7Bf%28x_b%29%20-%20f%28x_a%29%7D)

> This method is fail when f(x<sub>a</sub>) == f(x<sub>b</sub>), and not alwase converge.


### Newton-Raphson Method
This is one of the fastest convergence method for geting real root of quadrectic and transidental equation.

In here we use the concept of tangent.

Equation of tangent
<br/>y-y(x<sub>0</sub>)=y'(x<sub>0</sub>)(x-x<sub>0</sub>)

![graph](./newton-1.jpg)

When apply we get

![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Cdpi%7B200%7D%20x_b%20%3D%20x_a%20-%20%5Cfrac%7Bf%28x_a%29%7D%7Bf%27%28x_a%29%7D)

Only when f'(x<sub>n</sub>) != 0

### Graeffe Method
It is a fast or squrearing method and we reapate this till 3 squire digits.

x<sup>n</sup>+a<sub>1</sub>x<sup>n-1</sup>+a<sub>2</sub>x<sup>n-2</sup>+a<sub>3</sub>x<sup>n-3</sup>+.....=0

x<sup>n</sup>+a<sub>2</sub>x<sup>n-2</sup> = a<sub>1</sub>x<sup>n-1</sup>+a<sub>3</sub>x<sup>n-3</sup>

Take coman part and made squire of it and then put x<sup>2</sup> = y, and repeate till you get c'th term in coficient of U.

r<sub>1</sub> = -(c<sub>1</sub>)<sup>1/2<sup>n</sup></sup>

r<sub>2</sub> = -(c<sub>1</sub>/c<sub>2</sub>)<sup>1/2<sup>n</sup></sup>

r<sub>2</sub> = -(c<sub>2</sub>/c<sub>3</sub>)<sup>1/2<sup>n</sup></sup>

### Lin Bairstow Method
In numerical analysis, Bairstow's method is an efficient algorithm for finding the roots of a real polynomial of arbitrary degree. The algorithm first appeared in the appendix of the 1920 book Applied Aerodynamics by Leonard Bairstow. The algorithm finds the roots in complex conjugate pairs using only real arithmetic.

#### Steps of Working
1. Find p<sub>0</sub> and q<sub>0</sub> as per setisfiction of the equation or let 0, 0.
1. Senthtic division
1. Apply forumula to get p<sub>1</sub> & q<sub>1</sub>.
</br>c<sub>n-2</sub>Δp + c<sub>n-3</sub>Δq = b<sub>n-1</sub></br>
(c<sub>n-1</sub> - b<sub>n-1</sub>)Δp + c<sub>n-2</sub>Δq = b<sub>n</sub>
1. p<sub>1</sub> = p<sub>0</sub> + Δp </br>
q<sub>1</sub> = q<sub>0</sub> + Δq
1. Apply x<sup>2</sup>+p<sub>2</sub>x+q<sub>2</sub>
1. Root to be ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Calpha%5Cpm%20i%5Cbeta)
1. ![](https://latex.codecogs.com/gif.latex?%5Cinline%20-2%5Calpha%20%3D%20p)
8. ![](https://latex.codecogs.com/gif.latex?%5Cinline%20%5Calpha%5E2&plus;%5Cbeta%5E2%3Dq)

## Solution of System of Equation

### Gauss Elimination Methods
It is a direct method to solve the system of equation by the help of matrix. First form a matrix Ax=B where, A is a value of the coficient of the equation and B is a matrix of equal terms of the equation.

- $Ax=B$
- $A:B$
- Convert $A:B$ matrix into upper digonal matrix.
- And solve by puting values one by one.

### Gauss Jordan Methods
It is a direct method to solve the system of equation by the help of matrix. First form a matrix Ax=B where, A is a value of the coficient of the equation and B is a matrix of equal terms of the equation.

- $Ax=B$
- $A:B$
- Convert $A:B$ matrix into digonal matrix.
- Minimize the equation and find the value of variables.

### Courts Method
- $Ax=B$
- $A=LU$
- $U={upper-trengular-matrix}$
- $L={lower-trengular-matrix}$
- $if A=LU; then; LUx=B$
- $Let,Ux=y$
- $Ly=B$
- $A:B$
- Convert $A:B$ matrix into digonal matrix.
- Minimize the equation and find the value of variables.

## Interpolation
### Equal Interval
#### Newton Froword Formula(Bignining Diffrence)
$f(a+hu)=f(a)+\dfrac{u}{1!}\Delta f(a)+\dfrac{u(u-1)}{2!}\Delta^2 f(a)+\dfrac{u(u-1)(u-2)}{3!}\Delta^3 f(a)+\dfrac{u(u-1)(u-2)(u-3)}{4!}\Delta^4 f(a)+\ldots$

#### Newton Backword Formula(Least Diffrence)
$f(a+hu)=f(a)+\dfrac{u}{1!}\nabla f(a)+\dfrac{u(u+1)}{2!}\nabla^2 f(a)+\dfrac{u(u+1)(u+2)}{3!}\nabla^3 f(a)+\dfrac{u(u+1)(u+2)(u+3)}{4!}\nabla^4 f(a)+\ldots$

#### Gauss Froword Formula(Central Bignining Diffrence)
$f(a+hu)=y_{0}+\dfrac{u}{1!}\Delta y_{0}+\dfrac{u(u-1)}{2!}\Delta^2 y_{-1}+\dfrac{u(u-1)(u+1)}{3!}\Delta^3 y_{-1}+\dfrac{u(u-1)(u+1)(u-2)}{4!}\Delta^4 y_{-2}+\ldots$

#### Gauss Backword Formula(Central Least Diffrence)
$f(a+hu)=y_{0}+\dfrac{u}{1!}\Delta y_{-1}+\dfrac{u(u+1)}{2!}\Delta^2 y_{-1}+\dfrac{u(u+1)(u-1)}{3!}\Delta^3 y_{-2}+\dfrac{u(u+1)(u-1)(u+2)}{4!}\Delta^4 y_{-2}+\ldots$

#### Striling Central Diffrence
$f(a+hu)=y_{0}+\dfrac{u}{1!}[\dfrac{\Delta y_{0} + \Delta y_{-1}}{2}]+\dfrac{u^2}{2!}\Delta^2 y_{-1}+\dfrac{u(u^2-1)}{3!}[\dfrac{\Delta^3 y_{-1} + \Delta^3 y_{-2}}{2}]+\dfrac{u^2(u^2-1)}{4!}\Delta^4 y_{-2}+\ldots$

#### Bessal's Central Diffrence
$f(a+hu)=[\dfrac{y_{0} + y_{1}}{2}]+\dfrac{(u-1/2)}{1!}\Delta y_{0}+\dfrac{u(u-1)}{2!}[\dfrac{\Delta^2 y_{-1}+\Delta^2 y_{0}}{2}]+\dfrac{u(u-1)(u-1/2)}{3!}\Delta^3 y_{-1}+\dfrac{u(u-1)(u-2)(u+1)}{4!}[\dfrac{\Delta^4 y_{-1}+\Delta^4 y_{-2}}{2}]+\ldots$

### Unequal Interval
#### Langranges Unequal Interval Interpolation Formula
Given that a value of $x$.
| $X$ | $x_0$ | $x_1$ | $x_2$|
| --| ----| ----| ---|
| $Y$ | $y_0$ | $y_1$ | $y_2$ |

$$
f(x)=\dfrac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}*y_0+\dfrac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)}*y_1+\dfrac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}*y_2
$$

#### Newton Divided Diffrence
Form table by substractive $\dfrac{(x_{2}-x_{1})}{(y_{2}-y_{1})}$; And Apply formula.

$$
f(x)=f(x_0)+(x-x_0)\Delta f(x_0)+(x-x_0)(x-x_1)\Delta^2 f(x_0)+(x-x_0)(x-x_1)(x-x_2)\Delta^3 f(x_0)
$$
