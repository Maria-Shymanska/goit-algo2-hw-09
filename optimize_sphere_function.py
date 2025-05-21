import random
import math

# Sphere function definition
def sphere_function(x):
    return sum(xi ** 2 for xi in x)

# Helper function: generate a random solution within given bounds
def random_solution(bounds):
    return [random.uniform(bound[0], bound[1]) for bound in bounds]

# Helper function: generate a neighbor solution by small perturbation
def neighbor(x, bounds, step_size=0.1):
    return [max(min(xi + random.uniform(-step_size, step_size), bound[1]), bound[0])
            for xi, bound in zip(x, bounds)]

# Hill Climbing algorithm
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    current = random_solution(bounds)
    current_value = func(current)

    for _ in range(iterations):
        candidate = neighbor(current, bounds)
        candidate_value = func(candidate)

        if abs(candidate_value - current_value) < epsilon:
            break

        if candidate_value < current_value:
            current, current_value = candidate, candidate_value

    return current, current_value

# Random Local Search algorithm
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    best = random_solution(bounds)
    best_value = func(best)

    for _ in range(iterations):
        candidate = random_solution(bounds)
        candidate_value = func(candidate)

        if abs(candidate_value - best_value) < epsilon:
            break

        if candidate_value < best_value:
            best, best_value = candidate, candidate_value

    return best, best_value

# Simulated Annealing algorithm
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    current = random_solution(bounds)
    current_value = func(current)
    best, best_value = current, current_value

    for _ in range(iterations):
        if temp < epsilon:
            break

        candidate = neighbor(current, bounds)
        candidate_value = func(candidate)
        delta = candidate_value - current_value

        # Accept worse solution with a probability based on temperature
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current, current_value = candidate, candidate_value

            if current_value < best_value:
                best, best_value = current, current_value

        temp *= cooling_rate  # Decrease temperature

    return best, best_value

# Main block to run all algorithms
if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]  # Search space bounds for each dimension

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Solution:", hc_solution, "Value:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Solution:", rls_solution, "Value:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Solution:", sa_solution, "Value:", sa_value)
