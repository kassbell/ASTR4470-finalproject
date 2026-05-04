from src.forces import compute_accs

def step_euler(x, v, m, dt):
    acc = compute_accs(x, m)

    vel_new = v + acc * dt
    x_new = x + v * dt

    return x_new, vel_new


def step_leapfrog(x, v, m, dt):
    acc = compute_accs(x, m)
    
    v_half = v + 0.5 * acc * dt
    
    x_new = x + v_half * dt
    
    acc_new = compute_accs(x_new, m)
    
    v_new = v_half + 0.5 * acc_new * dt
    
    return x_new, v_new