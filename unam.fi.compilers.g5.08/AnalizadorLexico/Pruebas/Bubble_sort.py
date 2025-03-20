import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n=len(arr)
    i=0
    while i<n:
        j=0
        while j<n-i-1:
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1], arr[j]
            j+=1
        i+=1
    return arr

def bubble_sort_graf(arr):
    time=0
    n=len(arr)
    i=0
    while i<n:
        time+=1
        j=0
        while j<n-i-1:
            time+=1
            #if arr[j]>arr[j+1]:
                #arr[j], arr[j+1]=arr[j+1], arr[j]
            j+=1
        i+=1
    return time

if __name__=="__main__":
    x=[]
    y=[]
    esp=int(input("Ingrese el tamaño de la entrada: "))
    for tam in range(1,esp+1):
        l=[]
        for val in range(tam):
            l.append(random.randint(-500, 500))
            t=bubble_sort_graf(l)
        y.append(t)
        x.append(tam)
    print("Lista por ordenar", l, "De tamaño", esp)
    print("Qué quisieras hacer con el programa?\n")
    print("1)Ordenamiento\t2)Gráfica\n3)Salir")
    op=input("Opción: ")
    if op=='1':
        print("Lista por ordenar", l)
        bubble_sort(l)
        print("Lista ordenada: ", l)
    elif op=='2':            
        print(x)
        print(y)
        plt.plot(x,y)
        plt.xlabel('Entrada')
        plt.xlabel('Tiempo')
        plt.title('Complejidad')
        plt.show()
    else:
        print("Adios")
        