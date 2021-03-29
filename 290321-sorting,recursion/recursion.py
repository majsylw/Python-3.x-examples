# definicja funkcji iteracyjnej
def silnia_iteracyjnie(x) :
    silnia = 1
    for i in range(1, x+1):
        silnia *= i
    return silnia

# definicja funkcji rekurencyjnej
def silnia_rekurencyjnie(x) :
    if x < 1 :
        return 1
    else :
        return x * silnia_rekurencyjnie(x - 1)

# definicja funkcji rekurencyjnej -- tail call
def silnia_ogonowa(n, accumulator=1):
  if n == 0: return accumulator
  else: return silnia_ogonowa(n-1, accumulator * n)

print(silnia_iteracyjnie(5))
print(silnia_rekurencyjnie(5))
print(silnia_ogonowa(5))