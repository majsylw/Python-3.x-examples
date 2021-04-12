'''
Wyobraź sobie, że w pewnej nieograniczonej dwuwymiarowej przestrzeni porusza się 
pojedyncza cząstka. Ruch ten jest podobny do błądzenia losowego, z czym nasza cząstka 
może się poruszać jedynie w 4 kierunkach o jedno oczko: w górę, w dół, w lewo i w prawo. 
Napisz program, który w każdym kroku będzie losował kolejne posunięcie cząstki 
i wyliczał jej nowe położenie. Załóżmy, że rozważamy odległość od położenia początkowego 
(punktu P0 = (0,0)) do punktu końcowego (punktu Pk = (xk, yk)) po 1000 losowań. 
Sprawdź jak będzie zachowywać się cząstka dla n powtórzeń danego eksperymentu 
(wyznacz średnią odległość dla n prób (liczbę n dopasuj eksperymentalnie) po 1000 losowań).
'''
import numpy as np
from random import randint, seed
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def Brownian_motion_MC_fors(p, n):
    distances = []
    for _ in range(n):
        x = 0
        y = 0
        xs = [x]
        ys = [y]
        for _ in range(particle):
            kierunek = randint(0, 3)
            if kierunek == 0:  # lewo
                x -= 1
            if kierunek == 1:  # prawo
                x += 1
            if kierunek == 2:  # góra
                y += 1
            if kierunek == 3:  # dół
                y -= 1
            xs.append(x)
            ys.append(y)
        distance = (x**2 + y**2)**(1/2)
        distances.append(distance)
    return np.mean(distances), xs, ys

def Brownian_motion_MC_arrays(p, n):
    xs = np.cumsum(np.random.randint(-1, 2, (p, n)), 0)
    ys = np.cumsum(np.random.randint(-1, 2, (p, n)), 0)
    distances = (xs[-1,:]**2 + ys[-1,:]**2)**(1/2)
    return np.mean(distances), xs, ys

def plot_path(x, y, r1=5):
    r2 = r1 * 2
    plt.scatter(x, y, color = "g", marker = ".")
    circle1 = plt.Circle((0, 0), r1, color='b', fill=False)
    plt.gca().add_patch(circle1)
    circle2 = plt.Circle((0, 0), r2, color='r', fill=False)
    plt.gca().add_patch(circle2)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Błądzenie losowe w 2D")
    plt.show()

if __name__ == '__main__':
    particle = int(input('liczba kroków cząstki = '))
    MCs = int(input('liczba kroków Monte Carlo = '))
    seed(1)
    np.random.seed(1)

    if MCs <= 100:
        distances, x, y = Brownian_motion_MC_fors(particle, MCs)
        print("For loops:", distances)
        plot_path(x, y)

    distances, x, y = Brownian_motion_MC_arrays(particle, MCs)
    print("Numpy array:", distances)
    plot_path(x[:,-1], y[:,-1])

    fig = plt.figure()
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)
    circle1 = plt.Circle((0, 0), 5, color='b', fill=False)
    plt.gca().add_patch(circle1)
    circle2 = plt.Circle((0, 0), 10, color='r', fill=False)
    plt.gca().add_patch(circle2)
    graph, = plt.plot([], [], 'o')

    def animate(i):
        graph.set_data(x[:i+1], y[:i+1])
        plt.title(f'Time = {i}')
        return graph

    x, y = x[:,-1], y[:,-1]
    ani = FuncAnimation(fig, animate)
    plt.show()
'''
Po uruchomieniu programu cząstka rozpoczyna błądzenie na płaszczyźnie. 
Każdy krok może z jednakowym prawdopodobieństwem odbyć się w prawo, w lewo, w górę lub w dół. 
Celem tego programu jest pokazanie, że punkt błądzący przypadkowo na płaszczyźnie przebywa 
średnio odległość proporcjonalną do pierwiastka z czasu, a nie, jak przy ruchu jednostajnym, 
proporcjonalną do czasu. Błądzący punkt przekracza okrąg o promieniu dwa po czasie średnio 
4 razy dłuższym niż czas przekroczenia okręgu o promieniu jeden.
'''
