def midpoint(f, a, b, n):
    h = (b - a) / n
    f_sum = 0
    for i in range(1, n):
        x = (a + h/2.0) + i*h
        f_sum = f_sum + f(x)
    return h*f_sum


def application():
    from math import exp
    v = lambda t: 3*(t**2)*exp(t**3)
    n = int(input('n: '))
    numerical = midpoint(v, 0, 1, n)

    # Comparing with exact result
    V = lambda t: exp(t**3)  # derived by hand
    exact = V(1) - V(0)
    error = abs(exact - numerical)
    print('n={:d}: {:.16f}, error: {:g}'.format(n, numerical, error))

if __name__ == '__main__':
    application()