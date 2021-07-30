def dz(z):
    if z in ("x*y", "xy", "x *y", "x * y", "x* y"):
        return ("(y, x)")

    elif z in ("x+y", "x + y", "x+ y", "x +y"):
        return ("(1, 1)")
    
#PROBADOR
z, z1 = "xy", "x+y"

print(dz(z), "debe ser (y, x)\n\n",

      dz(z1), "debe ser (1, 1)")
