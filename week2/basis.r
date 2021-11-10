source ('physical_constants.r')

get_gamma <- function(m=mp, beta=0, t=0) {
  if (beta == 0 & t != 0) {
    return (1. + t / m)
  } else if (beta != 0 & t == 0) {
    return (1. / sqrt(1. - beta^2))
  } else if (beta != 0 & t !=0) {
    gamma_from_t <- 1. + t/m
    gamma_from_beta <- 1. / sqrt(1. - beta^2)
    if (gamma_from_t == gamma_from_beta) {
      return (gamma_from_t)
    } else {
      stop("beta does not match to the kinetic energy")
    }
  } else{
    stop("either beta or T should be non-zero value")
  }
}

get_beta <- function(m=mp, gamma=0, t=0){
  if (gamma == 0 & t != 0) {
    gamma <- get_gamma(m=m, t=t)
    return (sqrt(1. - 1./gamma^2))
  } else if (gamma != 0 | t == 0) {
    return (sqrt(1. - 1./gamma^2))
  } else if (gamma != 0 & t !=0) {
    gamma_from_t <- get_gamma(m=m, t=t)
    if (gamma == gamma_from_t) {
      return (gamma)
    } else {
      stop("gamma does not match to the kinetic energy")
    }
  } else {
    stop("either gamma or T should be non-zero value")
  }
}

get_kinetic_energy <- function(m=mp, gamma=0, beta=0) {
  if (gamma != 0 & beta == 0) {
    return ((gamma - 1.)*m)
  } else if (gamma == 0 & beta != 0) {
    return ((get_gamma(m=m, beta=beta) - 1.)*m)
  } else if (gamma != 0 & beta != 0) {
    E_from_gamma <- (gamma - 1.)*m
    E_from_beta <- (get_gamma(m=m, beta=beta) - 1.)*m
    if (E_from_gamma == E_from_beat) {
      return (E_from_gamma)
    } else {
      stop("gamma and beta do not match for calculating the kinetic energy")
    }
  }
}

get_momentum <- function(m=mp, gamma) {
  return(sqrt(gamma^2-1)*m)
}
