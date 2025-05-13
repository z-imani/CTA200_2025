def mandelbrot_escape_time(c, max_iter=100, escape_threshold=10):
    """
    Try to observe how quickly the sequence z_{n+1} = z_n^2 + c diverges.

    Parameters:
    - c (complex): complex number in the plane.
    - max_iter (int): max number of iterations to run.
    - escape_threshold (float): if |z| becomes larger than this, we consider it diverging.

    Returns:
    - int: how many iterations it took to escape. If it never escapes, returns max_iter.
    """
    z = 0
    for i in range(max_iter):
        z = z*z + c
        if z.real*z.real + z.imag*z.imag > escape_threshold**2:
            return i
    return max_iter
