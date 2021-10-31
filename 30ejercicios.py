import math

#Punto 1
def calificativo(nombre, calif): #define la funcion del punto numero 1
    return nombre+' '+calif
    
#Punto 2
def cuadrado(numero): #define la funcion del punto numero 2
    return numero**2

#Punto 3
def suma(num1,num2): #define la funcion del punto numero 3 y parte del 4
    return num1+num2

#Punto 4
def rest(num1,num2): #define las funciones del punto numero 4
    return num1-num2  
def multi (num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

#Punto 5
def parte_entera(numero:float)->int: #define la funcion del punto numero 5
    return math.trunc(numero)

#Punto 6
def valorIVA(valor_prod): #define la funcion del punto numero 6
    return valor_prod*0.19

#Punto 7
def area_perim_circ(radio): #define la funcion del punto numero 7
    area=math.pi*radio**2
    perim=math.pi*2*radio
    return area, perim
    
#Punto 8
def area_hexag(lado,apot): #define la funcion del punto numero 8
    area=lado*apot*3
    return area

#Punto 9 
def promedio(num1,num2,num3): #define la funcion del punto numero 9
    suma=num1+num2+num3
    return suma/3

#Punto 10
def intercambiar_var(var1,var2): #define la funcion del punto numero 10
    aux=var1
    var1=var2
    var2=aux
    return var1,var2

#Punto 11
def tiempo_caida(altura): #define la funcion del punto numero 11
    tiempo=math.sqrt(2*altura/9.8)
    return round(tiempo,3) #redondea a 3 decimales el retorno

#Punto 12
def distancia(acel,tiempo,velIn): #define la funcion del punto numero 12
    distancia=velIn*tiempo+(acel/2)*(tiempo**2)
    return round(distancia,3) #redondea a 3 decimales el retorno

#Punto 13
def velocidad_final(acel,velIn,tiempo): #define la funcion del punto numero 13
    vel_fin=velIn+acel*tiempo
    return round(vel_fin,3) #redondea a 3 decimales el retorno

#Punto 14
def energia(masa,vel): #define la funcion del punto numero 14
    energia=(masa*vel**2)/2
    return round(energia,3) #redondea a 3 decimales el retorno

#Punto 15
def distancia_coor(x1,y1,x2,y2): #define la funcion del punto numero 15
    distancia=math.sqrt((x2-x1)**2+(y2-y1)**2)
    return round(distancia,3) #redondea a 3 decimales el retorno

#Punto 16
def segundos_a_horas(segundos): #define la funcion del punto numero 16
    horas=(segundos/60)/60
    return round(horas,2) #redondea a 2 decimales el retorno

#Punto 17
def segundos_a_minutos(segundos): #define la funcion del punto numero 17
    minutos=segundos/60
    return round(minutos,3) #redondea a 3 decimales el retorno

#Punto 18
def segundos_a_formato(segundos): #define la funcion del punto numero 18
    hora=segundos//3600
    segundos=segundos%3600
    minuto=segundos//60
    segundos=segundos%60
    return hora,minuto,segundos

#Punto 19
def billetes(dinero_cant): #define la funcion del punto numero 19
    dicc={'100k':0,'50k':0,'20k':0,'10k':0,'5k':0,'2k':0,'1k':0} #crea un dicc con las posibilidades
    dinero_cant=dinero_cant//1000
    dicc_fin={} #crea un dicc vacio donde se almacenara la respuesta
    for x in dicc: #evalua cada elmento de dicc
        dicc[x]=dinero_cant//int(x[0:-1])
        
        dinero_cant=dinero_cant%int(x[0:-1])
    for x in dicc: #evalua cada elemento de dicc modificado
        if dicc[x]!=0:  #si el elemento se modifico es agregado al dicc vacio
            dicc_fin[x]=dicc[x]
        
    return dicc_fin

#Punto 20
def inverso(numero): #define la funcion del punto numero 20
    prim=numero//1000
    numero=numero%1000
    seg=numero//100
    numero=numero%100
    terc=numero//10
    cuart=numero%10
    numero=cuart*1000+terc*100+seg*10+prim 
    if len(str(numero))==3: #si el invertido tiene 3 digitos porque no toma en cuenta el 0 a la izq, se agrega un 0
        numero='0'+str(numero)
    elif len(str(numero))==2: #si el invertido tiene 2 digitos por la misma razon se agregan dos 0: '00'
        numero='00'+str(numero)
    elif len(str(numero))==1: #si el invertido tiene 1 digito por la misma razon se agregan tres 0: '000'
        numero='000'+str(numero)
    return numero

#Punto 21
def par_impar(numero): #define la funcion del punto numero 21
    respuesta=0
    if numero%2==0:
        respuesta='Par'
    else:
        respuesta='Impar'
    return respuesta

#Punto 22
def positivo_negativo(numero): #define la funcion del punto numero 22
    respuesta=0
    if numero>=0:
        respuesta='Positivo'
    else:
        respuesta='Negativo'
    return respuesta

#Punto 23
def pos_neg_par_impar(numero): #define la funcion del punto numero 23
    par_o_impar=par_impar(numero) #invoca la funcion del punto 21
    signo=positivo_negativo(numero) #invoca la funcion del punto 22
    return par_o_impar+'-'+signo
  
#Punto 24  
def descuento_5porc(valor_prod): #define la funcion del punto numero 24
    iva=valorIVA(valor_prod)
    valor_prod+=iva
    if iva>=150000:
        valor_prod*=0.95
    return valor_prod

#Punto 25
def punto25(numero): #define la funcion del punto numero 25
    if numero>=10:
        numero*=3
    else:
        numero/=4
    return numero

#Punto 26
def nota_final(n1,n2,n3,n4,n5): #define las funciones del punto numero 26
    nota_final=(n1*0.15)+(n2*0.2)+(n3*0.15)+(n4*0.3)+(n5*0.2) 
    return nota_final
def aprueba_reprueba(nota_final):
    respuesta='Felicitaciones :D'
    if nota_final<20:
        respuesta='No puede habilitar :('
    elif nota_final<30:
        respuesta='Reprobó, tendra que habilitar >:)'
    elif nota_final<=45:
        respuesta='Aprobó :3'
    return respuesta

#Punto 27
def mayor(num1,num2): #define la funcion del punto numero 27
    mayor=num1
    if num2>num1:
        mayor=num2
    return mayor

#Punto 28
def decimal(numero): #define la funcion del punto numero 28
    return float(numero)

#Punto 29
def mayor_menor(num1,num2,num3): #define la funcion del punto numero 29
    mayor=max(num1,num2,num3) #selecciona el maximo numero
    menor=min(num1,num2,num3) #selecciona el minimo numero
    return mayor,menor

#Punto 30
def suma_mayor_menor(num1,num2,num3): #define la funcion del punto numero 30
    suma=num1+num2
    respuesta='Mayor'
    if suma<num3:
        respuesta='Menor'
    elif suma==num3:
        respuesta='Igual'
    return respuesta

#Punto 31
def valor_pasaje(distancia,dias): #define la funcion del punto numero 31
    valor=distancia*5000
    if distancia>1000 and dias>7:
        valor=valor*0.85
    if valor<100000:
        valor=100000
    return valor

#Punto 32 
def anio_bisiesto(anio): #define la funcion del punto numero 32
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        respuesta="Es bisiesto"
    else:
        respuesta="No es bisiesto"
    return respuesta

#Punto 33
def ecuacion_cuadratica(a,b,c): #define la funcion del punto numero 33
    x1=(-b+math.sqrt(b**2-(4*a*c)))/2*a
    x2=(-b-math.sqrt(b**2-(4*a*c)))/2*a
    return x1,x2

#Punto 34
def usuario_contrasenia(usuario,contrasenia): #define la funcion del punto numero 34
    user=input('Ingrese su usuario: ')
    password=int(input('Digite su contraseña: '))
    mensaje=''
    contador=0
    while True: #crea un ciclo infinito
        contador+=1
        if user==usuario and contrasenia==password:
            mensaje='Inicio de sesión exitoso'
            break #cuando ambas condiciones se cumple rompe el ciclo
        else:
            if contador==3:
                mensaje='Excedio el numero de intentos, su computador explotara en 10 segundos'
                break #cuando se llega a 3 intentos fallidos de inicio de sesion rompe el ciclo
            print('Usuario o contraseña incorrectos')
            user=input('Ingrese su usuario nuevamente: ')
            password=int(input('Digite su contraseña nuevamente: '))    
    return mensaje

#Punto 35
def nombre_numero(numero): #define la funcion del punto numero 35
    nombre=''
    if numero==0:
        nombre='CERO'
    elif numero==1:
        nombre='UNO'
    elif numero==2:
        nombre='DOS'
    elif numero==3:
        nombre='TRES'
    elif numero==4:
        nombre='CUATRO'
    elif numero==5:
        nombre='CINCO'
    elif numero==6:
        nombre='SEIS'
    elif numero==7:
        nombre='SIETE'
    elif numero==8:
        nombre='OCHO'
    elif numero==9:
        nombre='NUEVE'
    elif numero==10:
        nombre='DIEZ'
    return nombre

#Punto 36
def cantidad_digitos(numero): #define la funcion del punto numero 36
    cantidad=len(str(numero))
    return cantidad

#Punto 37
def incremen_disminuyen(num1,num2,num3): #define la funcion del punto numero 37
    mensaje=''
    if num1<num2 and num2<num3:
        mensaje='Estan incrementando'
    elif num1>num2 and num2>num3:
        mensaje='Estan disminuyendo'
    else:
        mensaje='No incrementan ni disminuyen'
    return mensaje

#Punto 38
def entre_0y5(num1,num2): #define la funcion del punto numero 38
    resp=False
    if (num1>0 and num1<5) and (num2>0 and num2<5):
        resp=True
    return resp

#Punto 39
def dias_semana(numero): #define la funcion del punto numero 39
    resp=''
    if numero>0 and numero<8:
        if numero==1:
            resp='Lunes'
        elif numero==2:
            resp='Martes'
        elif numero==3:
            resp='Miercoles'
        elif numero==4:
            resp='Jueves'
        elif numero==5:
            resp='Viernes'
        elif numero==6:
            resp='Sabado'
        elif numero==7:
            resp='Domingo'
    else:
        resp='El numero no es valido'
    return resp

#Punto 40
def iguales(num1,num2,num3): #define la funcion del punto numero 40
    resp=False
    if num1==num2 or num1==num3 or num2==num3:
        resp=True
    return resp

#Punto 41
def numero_naturales(): #define la funcion del punto numero 41
    for x in range (1,11): #recorre cada numero de 1 a 10
        print('->',x)
    pass

#Punto 42
def numero_naturales_impar(): #define la funcion del punto numero 42
    for x in range(1,21): #recorre cada numero de 1 a 20
        if x%2!=0:
            print('->',x)
    pass

#Punto 43
def numero_naturales_par(): #define la funcion del punto numero 43
    for x in range(1,21): #recorre cada numero de 1 a 20
        if x%2==0:
            print('->',x)
    pass

#Punto 44
def numero_naturales_n(num): #define la funcion del punto numero 44
    for x in range (1,num+1): #recorre cada numero de 1 al numero ingresado
        print('->',x)
    pass

#Punto 45
def numero_naturales_secuencia(num): #define la funcion del punto numero 45
    for x in range (1,num+1): #recorre cada numero de 1 al numero ingresado
        if x%2==0:    
            print('->',-x)
        else:
            print('->',x)
    pass

#Punto 46
def numero_naturales_entre(num1,num2): #define la funcion del punto numero 46
    if num1<num2: #si el segundo numero es mayor 
        for x in range(num1,num2+1): #recorre cada numero entre los numeros ingresados
            print('->',x)
    else:  
        print('~ERROR~ El segundo numero no es mayor')
    pass

#Punto 47
def suma_numeros_entre(num1,num2): #define la funcion del punto numero 47
    suma=0
    if num1<num2: #si el segundo numero es mayor
        for x in range(num1,num2+1): #recorre cada numero entre los numeros ingresados
            suma+=x
    else:
        print('~ERROR~ El segundo numero no es mayor')
    return suma

#Punto 48 y 49
def suma_promedio_numeros(numero): #define la funcion del punto numero 48 y 49
    suma=0
    contador=0
    for x in range(1,numero+1): #recorre cada numero de 1 al numero ingresado
        num=int(input('Ingrese el numero '+str(x)+':\n->'))
        contador+=1
        suma+=num
    promedio=suma/contador
    return suma,promedio

#Punto 50
def promedio_par_impar(numero): #define la funcion del punto numero 50
    suma_par=0
    suma_impar=0
    contador_par=0
    contador_impar=0
    for x in range(1,numero+1): #recorre cada numero de 1 al numero ingresado
        num=int(input('Ingrese el numero '+str(x)+':\n->'))
        if num%2==0:
            contador_par+=1
            suma_par+=num
        else:
            contador_impar+=1
            suma_impar+=num
    #antes de realizar el promedio verifica que el divisor no sea 0
    if contador_par!=0: 
        promedio_par=suma_par/contador_par
    else:
        promedio_par=0
    if contador_impar!=0:
        promedio_impar=suma_impar/contador_impar
    else:
        promedio_impar=0
    return promedio_par,promedio_impar

#Punto 51
def es_positivo (valor): #define la funcion del punto numero 51
    while True: #crea un ciclo infinito 
        if valor<0:
            valor=int(input('~ERROR~Ingrese un numero entero positivo: '))
        else: 
            break #si el valor es mayor o igual a cero rompe el ciclo
    return valor

#Punto 52
def cantidad_mayor_menor_100(numero): #define la funcion del punto numero 52
    mayor=0
    menor=0
    for x in range(1,numero+1): #recorre cada numero de 1 al numero ingresado
        num=int(input('Ingrese el numero '+str(x)+':\n->'))
        if num>100:
            mayor+=1
        elif num<100:
            menor+=1
    return mayor,menor

#Punto 53
def clasificar_numeros(numero): #define la funcion del punto numero 53
    positivo=0
    negativo=0
    par=0
    impar=0
    mult_ocho=0
    for x in range(1,numero+1): #recorre cada numero de 1 al numero ingresado
        num=int(input('Ingrese el numero '+str(x)+':\n->'))
        #suma 1 a la variable de la condicion que se cumpla
        if num>=0:
            positivo+=1
        else:
            negativo+=1
        if num%2==0:
            par+=1
        else:
            impar+=1
        if num%8==0:
            mult_ocho+=1
    return positivo,negativo,par,impar,mult_ocho

#Punto54
def punto54(): #define la funcion del punto numero 54
    contador_par=0
    contador_5=0
    contador=0
    contador_impar=0
    while True: #crea un ciclo infinito
        contador+=1
        num=int(input('Ingrese el numero '+str(contador)+':\n->'))
        #suma 1 a la variable de la condicion que se cumpla
        if num==5:
            contador_5+=1
        if num%2==0:
            contador_par+=1
        else:
            contador_impar+=1
        if contador_par==10:
            break #rompe el ciclo cuando se ingresan 10 pares
        if contador_5==20:
            break #rompe el ciclo cuando se ingresan 20 numero '5'
    return contador, contador_par,contador_impar,contador_5

#Punto 55
def cantidad_factores(numero): #define la funcion del punto numero 55
    contador=0
    for num in range(2,numero): #recorre cada numero de 2 al numero ingresado
        if numero%num==0:
            contador+=1
    return contador

#Punto 56
def invertir_cadena(cadena): #define la funcion del punto numero 56
    return cadena[::-1] #retorna la cadena desde el final saltando -1 espacio hasta llegar al principio

#Punto 57
def patron(): #define la funcion del punto numero 57
    patron=''
    for x in range (1,11):#recorre cada numero de 1 a 11
        patron=patron+str(x)
        print(patron) 



#Inicia con 1, para comenzar el ciclo while
print('--------------------------------------------------------------\nINICIO DEL PROGRAMA\n--------------------------------------------------------------')
punto=1 
while punto!=0:    #Condicion del ciclo: Punto ingresado diferente a 0
    punto=int(input('Ingresa el punto a ejecutar\nPara finalizar ingresa 0: ')) #Pide el punto a ejecutar
    
    #Elige el punto que se ingreso y lo ejecuta:
    if punto==1: #Interfaz del punto 1
        nombre=input('Ingresa el nombre: ') #Pide el nombre
        calif=input('Ingresa el cualificativo: ') #Pide el calificativo
        print(calificativo(nombre, calif)) #Imprime el resultado del punto 1
        
    elif punto==2: #Interfaz del punto 2
        numero=int(input('Ingresa el numero: ')) #Pide el numero
        print('El cuadrado del numero es',cuadrado(numero)) #Imprime el cuadrado del numero
        
    elif punto==3: #Interfaz del punto 3
        num1=int(input('Ingresa el primer numero a sumar: ')) #Pide el primer numero
        num2=int(input('Ingresa el segundo numero a sumar: ')) #Pide el segundo numero
        print('La suma de los numeros es',suma(num1, num2)) #Imprime la suma de los numeros
        
    elif punto==4: #Interfaz del punto 4
        num1=int(input('Ingresa el primer numero: ')) #Pide el primer numero
        num2=int(input('Ingresa el segundo numero: ')) #Pide el segundo numero
        print('La suma es:',suma(num1, num2)) #Imprime la suma
        print('La resta es:',rest(num1, num2)) #Imprime la resta
        print('La multiplicacion es:',multi(num1, num2)) #Imprime la multiplicacion
        print('La division es:',div(num1, num2)) #Imprime la division 
    
    elif punto==5: #Interfaz del punto 5
        numero=float(input('Ingresa el numero con su decimal: '))
        print('La parte entera es',parte_entera(numero))
        print('La parte decimal es', round(numero-parte_entera(numero),3))        
        
    elif punto==6: #Interfaz del punto 6
        valor_prod=int(input('Ingrese el valor del producto: '))
        print('El valor del producto es: $', valor_prod)
        print('El valor del IVA es: $',valorIVA(valor_prod))
        print('El valor con IVA incluido es: $',valor_prod+valorIVA(valor_prod))
    
    elif punto==7: #Interfaz del punto 7
        radio=int(input('Ingrese el radio del circulo: '))
        area,perim= area_perim_circ(radio)
        print('El area del circulo es:',round(area,3))
        print('El perimetro del circulo es:',round(perim,3))
        
    elif punto==8: #Interfaz del punto 8
        lado=int(input('Ingrese el lado del hexagono: '))
        apot=int(input('Ingrese el apotema del hexagono: '))
        print('El area del hexagono es',area_hexag(lado, apot))   
        
    elif punto==9: #Interfaz del punto 9
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        num3=int(input('Ingrese el tercer numero: '))
        print('El promedio de los 3 numeros es:',promedio(num1, num2, num3))
        
    elif punto==10: #Interfaz del punto 10
        var1=int(input('Ingrese el primer valor: '))
        var2=int(input('Ingrese el segundo valor: '))
        var1,var2=intercambiar_var(var1, var2)
        print('Ahora el primer valor es',var1,'y el segundo es',var2)        
        
    elif punto==11: #Interfaz del punto 11
        altura=int(input('Ingresa la altura de la que cayo el objeto: '))
        print('El tiempo que tardo en caer fue',tiempo_caida(altura))
    
    elif punto==12: #Interfaz del punto 12
        acel=int(input('Ingresa la aceleracion: '))
        velIn=int(input('Ingresa la velocidad inicial: '))
        tiempo=int(input('Ingresa el tiempo donde se encontrara el objeto: '))
        print('La distancia recorrida en',tiempo,'segundos es:',distancia(acel, tiempo, velIn),'metros')
        
    elif punto==13: #Interfaz del punto 13
        acel=int(input('Ingresa la aceleracion: '))
        velIn=int(input('Ingresa la velocidad inicial: '))
        tiempo=int(input('Ingresa el tiempo donde se encontrara el objeto: '))
        print('La velocidad final del objeto es:',velocidad_final(acel, velIn, tiempo),'m/s')
    
    elif punto==14: #Interfaz del punto 14
        masa=int(input('Ingresa la masa del objeto: '))
        vel=int(input('Ingresa la velocidad del objeto: '))
        print('La energia en Julios es', energia(masa, vel))
        
    elif punto==15: #Interfaz del punto 15 
        x1=int(input('Ingrese el valor de la primer coordenada x1: '))
        y1=int(input('Ingrese el valor de la primer coordenada y1: '))
        x2=int(input('Ingrese el valor de la segunda coordenada x2: '))
        y2=int(input('Ingrese el valor de la segunda coordenada y2: '))
        print('La distancia entre las coordenadas es:',distancia_coor(x1, y1, x2, y2))
        
    elif punto==16: #Interfaz del punto 16
        segundos=int(input('Ingrese la cantidad de segundos: '))
        print('La cantidad de segundos en horas es',segundos_a_horas(segundos) ,'hora(s)')
        
    elif punto==17: #Interfaz del punto 17
        segundos=int(input('Ingrese la cantidad de segundos: '))
        print('La cantidad de segundos en minutos es',segundos_a_minutos(segundos) ,'minuto(s)')
        
    elif punto==18: #Interfaz del punto 18
        segundos=int(input('Ingrese la cantidad de segundos: '))
        hora,minuto,segundos=segundos_a_formato(segundos)
        str(hora)+':'+str(minuto)+':'+str(segundos)
        print('La hora es:',hora,'hora(s),',minuto,'minuto(s),',segundos,'segundo(s)')
        print(str(hora)+':'+str(minuto)+':'+str(segundos))
    
    elif punto==19: #Interfaz del punto 19
        dinero_cant=int(input('Ingresa la cantidad de dinero: '))
        print('La cantidad de billetes en miles es:\n'+str(billetes(dinero_cant)))
    
    elif punto==20: #Interfaz del punto 20
        numero=int(input('Ingresa el numero de 4 cifras a invertir: '))
        print('El numero invertido es:',inverso(numero))
    
    elif punto==21: #Interfaz del punto 21
        numero=int(input('Ingresa el numero: '))
        print('El numero ingresado es',par_impar(numero))

    elif punto==22: #Interfaz del punto 22
        numero=int(input('Ingresa el numero: '))
        print('El numero ingresado es',positivo_negativo(numero))

    elif punto==23: #Interfaz del punto 23
        numero=int(input('Ingresa el numero: '))
        print('El numero ingresado es',pos_neg_par_impar(numero))

    elif punto==24: #Interfaz del punto 24
        valor_prod=int(input('Ingrese el valor de la venta: '))
        print('El valor de la venta con IVA es:',descuento_5porc(valor_prod))

    elif punto==25: #Interfaz del punto 25
        numero=int(input('Ingresa el numero: '))
        if numero>=10:
            print('El triple del numero es:',punto25(numero))
        else:
            print('La cuarta parte del numero es:',punto25(numero))

    elif punto==26: #Interfaz del punto 26
        print('\nIngrese la notas a continuacion de 0 a 50')
        n1=int(input('Nota 1: '))
        n2=int(input('Nota 2: '))
        n3=int(input('Nota 3: '))
        n4=int(input('Nota 4: '))
        n5=int(input('Nota 5: '))
        nota_def=nota_final(n1, n2, n3, n4, n5)
        print('\nLa nota final es:',nota_def)
        print(aprueba_reprueba(nota_def))

    elif punto==27: #Interfaz del punto 27
        print('\nQué número es mayor?')
        num1=int(input('Ingrese el primer número: '))
        num2=int(input('Ingrese el segundo número: '))
        print('El númeró mayor es:',mayor(num1, num2))

    elif punto==28: #Interfaz del punto 28
        print('\nConvierte el numero a decimal')
        numero=int(input('Ingresa el numero: '))
        print('El decimal es',decimal(numero)) 
    
    elif punto==29: #Interfaz del punto 29
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        num3=int(input('Ingrese el tercer numero: '))
        mayor,menor=mayor_menor(num1, num2, num3)
        print('El numero mayor es',mayor)
        print('El numero menor es',menor)
        
    elif punto==30: #Interfaz del punto 30
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        num3=int(input('Ingrese el tercer numero: '))
        print('La suma del primer y el segundo numero es',
              suma_mayor_menor(num1, num2, num3),'que el tercer numero')
    
    elif punto==31: #Interfaz del punto 31
        print('Valor del pasaje de avión')
        distancia=int(input('Ingrese la distancia en km a recorrer: '))
        dias=int(input('Ingrese los dias de estancia: '))
        print('El valor del pasaje de avión es $',valor_pasaje(distancia, dias))

    elif punto==32: #Interfaz del punto 32
        anio=int(input('Ingresa el año: '))
        print('El año', anio_bisiesto(anio))
        
    elif punto==33: #Interfaz del punto 33
        print('Resolución de ecuacion cuadratica ax^2+bx+c')
        a=int(input('Ingresa el valor de a: '))
        b=int(input('Ingresa el valor de b: '))
        c=int(input('Ingresa el valor de c: '))
        x1,x2=ecuacion_cuadratica(a, b, c)
        print("""La solucion de las ecuaciones son:\n
              x1 = {}
              x2 = {}""".format(x1,x2))

    elif punto==34: #Interfaz del punto 34
        usuario=input('Usuario predeterminado: ')
        contrasenia=int(input('Contraseña predeterminada: '))
        print(usuario_contrasenia(usuario, contrasenia))

    elif punto==35: #Interfaz del punto 35
        numero=int(input('Ingresa el numero de 0 a 10: '))
        print('El',numero,'se escribe asi:',nombre_numero(numero))

    elif punto==36: #Interfaz del punto 36
        numero=int(input('Ingresa el numero: '))
        print('El numero de digitos de',numero,'es',cantidad_digitos(numero))

    elif punto==37: #Interfaz del punto 37
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        num3=int(input('Ingrese el tercer numero: '))
        print('Los numeros',incremen_disminuyen(num1, num2, num3))

    elif punto==38: #Interfaz del punto 38
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        print('Los dos numeros se encuentras entre 0 y 5:',entre_0y5(num1, num2))

    elif punto==39: #Interfaz del punto 39
        numero=int(input('Ingresa el numero de la semana: '))
        dia=dias_semana(numero)
        if len(dia)<8:
            print('El dia de la semana es',dias_semana(numero))        
        else:
            print(dia)

    elif punto==40: #Interfaz del punto 40
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        num3=int(input('Ingrese el tercer numero: '))
        print('Entre los tres hay dos numeros por lo menos iguales:',iguales(num1, num2, num3))

    elif punto==41: #Interfaz del punto 41
        print('10 primeros numeros naturales:')
        numero_naturales()
    
    elif punto==42: #Interfaz del punto 42
        print('10 primeros numeros naturales impares:')
        numero_naturales_impar()
    
    elif punto==43: #Interfaz del punto 43
        print('10 primeros numeros naturales pares:')
        numero_naturales_par()

    elif punto==44: #Interfaz del punto 44
        num=int(input('Ingrese el numero: '))
        print('Los',num,'primeros numeros naturales:')
        numero_naturales_n(num)

    elif punto==45: #Interfaz del punto 45
        num=int(input('Ingresa el numero: '))
        print('La secuencia es:')
        numero_naturales_secuencia(num)       

    elif punto==46: #Interfaz del punto 46
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        print('Los numeros entre',num1,'y',num2,'son:')
        numero_naturales_entre(num1, num2)
        
    elif punto==47: #Interfaz del punto 47
        num1=int(input('Ingrese el primer numero: '))
        num2=int(input('Ingrese el segundo numero: '))
        print('La suma de los numeros entre',num1,'y',num2,'es:')
        print('->',suma_numeros_entre(num1, num2))

    elif punto==48: #Interfaz del punto 48
        print('Suma y promedio')
        suma,promedio=suma_promedio_numeros(10)
        print('La suma es:',suma,'\nEl promedio es:',promedio)
    
    elif punto==49: #Interfaz del punto 49
        print('Suma y promedio')
        numero=int(input('Ingrese la cantidad de numeros a digitar: '))
        suma,promedio=suma_promedio_numeros(numero)
        print('La suma es:',suma,'\nEl promedio es:',promedio)

    elif punto==50: #Interfaz del punto 50
        print('Promedio pares e impares')
        numero=int(input('Ingrese la cantidad de numeros a digitar: '))
        prom_par,prom_impar=promedio_par_impar(numero)
        print('El promedio de los numeros pares es:',prom_par,
              '\nEl promedio de los numeros impares es:',prom_impar)
       
    elif punto==51: #Interfaz del punto 51
        valor=int(input('Ingrese un numero entero positivo: '))
        print('Muy bien, su numero es:',es_positivo(valor))
        
    elif punto==52: #Interfaz del punto 52
        numero=int(input('Ingrese la cantidad de numeros a digitar: '))
        mayor,menor= cantidad_mayor_menor_100(numero)
        print('La cantidad de numeros mayores a 100 es:',mayor,
              '\nLa cantidad de numeros menores a 100 es:',menor)
        
    elif punto==53: #Interfaz del punto 53
        numero=int(input('Ingrese la cantidad de numeros a digitar: '))
        positivo,negativo,par,impar,mult_ocho=clasificar_numeros(numero)
        print('La cantidad de numeros positivos es:',positivo,
              '\nLa cantidad de numeros negativos es:',negativo,
              '\nLa cantidad de numeros pares es:',par,
              '\nLa cantidad de numeros impares es:',impar,
              '\nLa cantidad de numeros multiplos de 8:',mult_ocho)        
        
    elif punto==54: #Interfaz del punto 54
        total,par,impar,num5=punto54()
        print('La cantidad total de numeros es:',total,
              '\nLa cantidad de numeros pares es:',par,
              '\nLa cantidad de numeros impares es:',impar,
              '\nLa cantidad de numero 5 digitados es:',num5)
        
    elif punto==55: #Interfaz del punto 55
        numero=int(input('Ingrese el numero: '))
        print('La cantidad de factores de',numero,'ademas del mismo y 1 es:',cantidad_factores(numero))
    
    elif punto==56: #Interfaz del punto 56
        cadena=input('Ingrese la cadena a invertir: ')
        print('La cadena invertida es:\n'+invertir_cadena(cadena))
          
    elif punto==57: #Interfaz del punto 57
        patron()
    
    elif punto==0:
        print('--------------------------------------------------------------\nFIN DEL PROGRAMA\n--------------------------------------------------------------')
        break #si se ingresa 0 rompe el ciclo y el programa finaliza
    
    else:
        print('El punto ingresado no existe') #imprime si se ingresa un punto que no existe 
        




























