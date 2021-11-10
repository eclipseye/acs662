import numpy as np
import physical_constants as pc

def get_gamma(m=pc.mp, beta=0, t=0):
    if (beta == 0 and t != 0):
        return (1. + t / m)
    elif (beta != 0 and t == 0):
        return (1. / np.sqrt(1. - beta**2))
    elif (beta != 0 and t !=0):
        gamma_from_t = 1. + t / m
        gamma_from_beta = 1. / np.sqrt(1. - beta**2)
        if (gamma_from_t == gamma_from_beta):
            return (gamma_from_t)
        else:
            print("beta does not match to the kinetic energy")
    else:
        print("either beta or T should be non-zero value")

def get_beta(m=pc.mp, gamma=0, t=0):
    if (gamma == 0 and t != 0):
        gamma = get_gamma(m=m, t=t)
        return (np.sqrt(1. - 1. / gamma**2))
    elif (gamma != 0 or t == 0):
        return (np.sqrt(1. - 1./gamma**2))
    elif (gamma != 0 and t !=0):
        gamma_from_t = get_gamma(m=m, t=t)
        if (gamma == gamma_from_t):
            return (gamma)
        else:
            print("gamma does not match to the kinetic energy")
    else:
        print("either gamma or T should be non-zero value")

def get_kinetic_energy(m=pc.mp, gamma=0, beta=0):
    if (gamma != 0 and beta == 0):
        return ((gamma - 1.)*m)
    elif (gamma == 0 and beta != 0):
        return ((get_gamma(m=m, beta=beta) - 1.)*m)
    elif (gamma != 0 and beta != 0):
        E_from_gamma = (gamma - 1.)*m
        E_from_beta = (get_gamma(m=m, beta=beta) - 1.)*m
        if (E_from_gamma == E_from_beat):
            return (E_from_gamma)
        else:
            print("gamma and beta do not match for calculating the kinetic energy")

def get_momentum(m=pc.mp, gamma=0):
    return(np.sqrt(gamma**2-1)*m)