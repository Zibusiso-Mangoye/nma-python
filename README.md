 # `nma-python`

Python implementation of numerical method algorithms. Numerical analysis is the study of algorithms that use numerical approximation for the problems of mathematical analysis. The algorithms implemeted are taken from [Numerical Analysis](https://www.amazon.com/Numerical-Analysis-Richard-L-Burden/dp/0538733519) 9th Edition by [Richard L. Burden](https://www.amazon.com/Richard-L-Burden/e/B001IQZIR0/ref=dp_byline_cont_book_1) and [J. Douglas Faires](https://www.amazon.com/s/ref=dp_byline_sr_book_2?ie=UTF8&field-author=J.+Douglas+Faires&text=J.+Douglas+Faires&sort=relevancerank&search-alias=books).

### Structure of the Project

For each major topic there is :

- a python notebook that explains sections of that topic and how to use the algorithm in question.
- a python file for that same topic for use in solving problems.

For example, chapter two in the 9th edition is "Solutions of Equations in One Variable", in the repository it has the name "one_var_equations" and has a .py and .ipynb file: one_var_equations.ipynb and one_var_equations.py

Also included are img, test folders that contain any images used in the notebooks and markdown files and tests for every algorithms. The tests are proven examples that are in the book.

### Installation Guide

To download the repository:

```
git clone <https://github.com/NumericalMethodsAlgorithms/nma-python.git>
```

Then you need to install the basic dependencies to run the project on your system:

```
cd nma-python
pip install -r requirements.txt
```

And you are good to go!

### Index of Algorithms

| **Algorithm** | **Name (in 9<sup>th</sup> edition)** | **Name (in repository)**      | **File**                                                 | **Tests** | **Notebook**
|:--------------|:-------------------------------------|:------------------------------|:---------------------------------------------------------|:----------|:------------|
| 2.1           | Bisection                            | `bisection`                   | [`one_var_equations.py`](ivp_4_ode.py)           |       |     |
| 5.1           | Runge-Kutta (Order Four)                              | `runge_kutta_o4`                | [`ivp_4_ode.py`](ivp_4_ode.py)                              |   yes   |     |

### Acknowledgements

Many thanks for all the [contributions](https://github.com/NumericalMethodsAlgorithms/nma-python/graphs/contributors)
