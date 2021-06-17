from scipy import stats

def soma(v):
    i=0
    for x in v:
        i+=x


    return i

def crescente(v):
    
    i = 0
    j=0
    aux =0
    while i<len(v) - 1:
        j= i+1
        while j < len(v):
        
            if v[i] >= v[j]:
            
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
            j+=1
        i+=1


    return v

def media(v):
    media= soma(v)/len(v)
    return media

def mediana(v):
    i=0
    v=crescente(v)
    
    if len(v)%2:
        i=int((len(v)-1)/2)
        i = v[i]
    else:
        aux = [v[int(len(v)/2)], v[int((len(v)/2)-1)]]
        i=media(aux)
    
    return i

def moda(v):
    
    x = list(stats.mode(v))
    return x
    
    

v = [0]
v[0] = int(input("Digite algum numero: "))
i=0

while v[i]:
    v.append(int(input("Digite outro numero ou digite 0 para sair: ")))
    i+=1

v.pop()
i=0

print("\n\nO resultado da soma é: " + str(soma(v)))
print("\ncrescente: " + str(crescente(v)))
print("\nA media é: " + str(media(v)))
print("\nA mediana é: " + str(mediana(v)))
print("\nA moda é: " + str(moda(v)))


