a=35
b=94
def solve(numh, numl):
    rabbits=0.5*numl-numh
    chickens=2*numh-0.5*numl
    return(rabbits, chickens)
c=solve(a,b)
print(f'chickens {c[0]}, rabbits {c[1]}')