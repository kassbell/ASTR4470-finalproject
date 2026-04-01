from src.forces import compute_accs

def step_euler(x, v, m, dt):
    acc = compute_accs(x, m)

    vel_new = v + acc * dt
    x_new = x + v * dt

    return x_new, vel_new