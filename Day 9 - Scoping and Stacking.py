#-----------
# #Scoping
#------------
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("Inner:", x)  # Local

    inner()
    print("Outer:", x)  # Enclosing

outer()
print("Global:", x)  # Global

#-----------
#Stacking
#-----------
def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(f"Entering level {n}")
        countdown(n - 1)
        print(f"Returning from level {n}")

countdown(3)
