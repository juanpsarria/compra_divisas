def compra_divisas(monto_ars, cotizacion_usd):
    # Monto que se podría comprar
    max_dolares = monto_ars / cotizacion_usd
    print(f'El monto que se podría comprar es {max_dolares:.2f}.')
    
    # Cantidad de billetes de cada nominación
    billetes_100 = int(max_dolares // 100)
    resto = max_dolares - (billetes_100 * 100)
    
    billetes_20 = int(resto // 20)
    resto -= billetes_20 * 20
    
    billetes_10 = int(resto // 10)
    resto -= billetes_10 * 10
    
    # Monto realmente comprado
    dolares_comprados = (billetes_100 * 100) + (billetes_20 * 20) + (billetes_10 * 10)
    print(f'El monto comprado es {dolares_comprados}. Recibe {billetes_100} billetes de 100, {billetes_20} billetes de 20 y {billetes_10} billetes de 10')
    
    # Dinero sin gastar
    dinero_sin_gastar = (max_dolares - dolares_comprados) * cotizacion_usd
    print(f'Su vuelto es ${dinero_sin_gastar:.2f}.')
    
    #Se retornan los valores en caso de necesitar usarlos
    return {
        "max_dolares": max_dolares,
        "dolares_comprados": dolares_comprados,
        "billetes_100": billetes_100,
        "billetes_20": billetes_20,
        "billetes_10": billetes_10,
        "dinero_sin_gastar": dinero_sin_gastar
    }


compra_divisas(2050000, 1030)