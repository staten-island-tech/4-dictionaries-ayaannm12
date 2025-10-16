def spaces(n,y,t):
    occupied = 0
    for i in range(n):
         if y[i] == "C" and t[1] == "C":
              occupied += 1
    return (occupied)

print(spaces(5, "CCC...", "C.C.C."))
