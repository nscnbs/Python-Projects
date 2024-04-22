import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf

def simulate_random_walk(N, num_samples=1000000):
    counts = np.zeros(2 * N + 1)

    for _ in range(num_samples):
        random_values = np.random.choice([-1, 1], size=N)
        random_walk_sum = np.sum(random_values)
        counts[random_walk_sum + N] += 1

    empirical_distribution = np.cumsum(counts) / num_samples
    return empirical_distribution

def plot_distribution(N, empirical_distribution, normal_distribution):
    x_values = np.arange(-N, N + 1)
    plt.plot(x_values, empirical_distribution, label=f'Empiryczna S_{N}', color='green')
    plt.plot(x_values, normal_distribution, label=f'Normalne S_{N} Aproksymacja', color='red')
    plt.xlabel('Suma')
    plt.ylabel('Skumulowana Prawdopodobieństwo')
    plt.legend()
    plt.title(f'Porównanie Rozkładu Błądzenia Losowego dla N = {N}')
    plt.grid(True)
    plt.show()

def main():
    N_values = [5, 10, 15, 20, 25, 30, 100]

    for N in N_values:
        empirical_distribution = simulate_random_walk(N)
        normal_distribution = 0.5 * (1 + erf(np.arange(-N, N + 1) / (np.sqrt(2) * np.sqrt(N))))
        print(f'Dystrybuanta S({N}): {empirical_distribution}')
        
        print('Roznica:')
        for i in range(len(normal_distribution)):
            diff = np.abs(empirical_distribution[i] - normal_distribution[i])
            print(f'x = {i - N}: {diff}')

        plot_distribution(N, empirical_distribution, normal_distribution)

if __name__ == "__main__":
    main()
