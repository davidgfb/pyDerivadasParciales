def menosGradiente(z): # decreciente
    if z in ("x*y", "xy", "x *y", "x * y", "x* y"):
        return ("(-y, -x, 0)")

    elif z in ("x+y", "x + y", "x+ y", "x +y"):
        return ("(-1, -1, 0)")

#PROBADOR
'''
z, z1 = "xy", "x+y"

print(menosGradiente(z), "debe ser (-y, -x, 0)\n\n",

      menosGradiente(z1), "debe ser (-1, -1, 0)")
'''

def d(z, P):
    menosGradienteZ = menosGradiente(z)
    
    esProducto = menosGradienteZ == "(-y, -x, 0)"
    
    if len(P) == 2:
        x, y = P  
        
    elif len(P) == 3:
        x, y, z = P
        
        if esProducto:
            if not z == x*y:
                z = x*y
                print("z debe ser", z)
              
    if esProducto:
        return (-y, -x, 0)
    
#PROBADOR
z, P = "xy", (0, 0, 1)

print(d(z, P), "debe ser (0, 0, 0)")
