volar=input("puede volar? ")
humano=input("es humano? ")
mascara=input("tiene mascara? ")
if volar=="si":
    if humano=="si":
        if mascara=="si":
            print("es ironman")
        else: print("es capitan Marvel")
    else: 
        if mascara=="no":
            print("vision")
        else: print("ronal")
else: 
    if humano=="si":
        if mascara=="si":
            print("spider")
        else: print("hulk")
    else: 
        if mascara=="si":
            print("black bolt")
        else: print("thanos")
   