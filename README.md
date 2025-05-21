# Sphere Function Optimization

This project implements three local optimization algorithms to minimize the Sphere function:

\[
f(\mathbf{x}) = \sum\_{i=1}^n x_i^2
\]

where each variable \( x_i \) is within the bounds \([-5, 5]\).

---

## Algorithms Implemented

1. **Hill Climbing**  
   A greedy algorithm that iteratively moves to a better neighboring solution.

2. **Random Local Search**  
   A stochastic method that samples random points in the search space to find improvements.

3. **Simulated Annealing**  
   A probabilistic technique inspired by annealing in metallurgy, allowing occasional acceptance of worse solutions to escape local minima.

---

## Features

- Supports customizable number of iterations and precision (`epsilon`).
- Works within defined variable bounds.
- Returns the best solution found and the corresponding function value.
- Modular design for easy extension or adaptation to other functions.

---

## Usage

Run the main script to execute all three algorithms on a 2-dimensional Sphere function:

```bash
python sphere_optimization.py
```

Hill Climbing:
Solution: [0.0005, 0.0007] Value: 9.04e-07

Random Local Search:
Solution: [0.03, 0.10] Value: 0.012

Simulated Annealing:
Solution: [0.024, -0.004] Value: 0.0006
