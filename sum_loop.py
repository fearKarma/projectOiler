def arrayadd():

    x = [508666,700834,694948, 909834, 806321,353078,155717]
    y = [758945, 758163, 774003, 306528, 739785, 376882, 809934]
    z = []
    for j in range(0,len(x)):
        z.append(x[j] + y[j])
    return z

print(arrayadd())
