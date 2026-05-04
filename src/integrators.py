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

def step_rk4(x, v, m, dt):
    def acc(x):
        return compute_accs(x, m)
    
    k1_v = acc(x)
    k1_x = v

    k2_v = acc(x + 0.5 * k1_x * dt)
    k2_x = v + 0.5 * k1_v * dt

    k3_v = acc(x + 0.5 * k2_x * dt)
    k3_x = v + 0.5 * k2_v * dt

    k4_v = acc(x + k3_x * dt)
    k4_x = v + k3_v * dt

    x_new = x + (dt / 6.0) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
    v_new = v + (dt / 6.0) * (k1_v + 2*k2_v + 2*k3_v + k4_v)

    return x_new, v_new