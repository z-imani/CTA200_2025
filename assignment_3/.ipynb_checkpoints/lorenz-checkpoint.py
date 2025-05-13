def lorenz(t, W, sigma=10.0, r=28.0, b=8.0/3.0):
    """
    Defines the Lorenz system of ODEs.

    Parameters:
    - t (float): Current time (required by solve_ivp, but not used directly).
    - W (list or array): Current values of X, Y, Z.
    - sigma (float): Prandtl number.
    - r (float): Rayleigh number.
    - b (float): Geometric parameter.

    Returns:
    - dWdt (list): Time derivatives [dX/dt, dY/dt, dZ/dt].
    """
    X, Y, Z = W
    dXdt = sigma * (Y - X)
    dYdt = r * X - Y - X * Z
    dZdt = -b * Z + X * Y
    return [dXdt, dYdt, dZdt]
