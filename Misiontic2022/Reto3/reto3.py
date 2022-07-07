


N=int(input())
Valortotal=0
Valortotaliva=0
codigo=[]
nombre=[]
cantidad=[]
unitario=[]
tipo_iva=[]
valor_producto=[]
iva=[]
valor_final=[]


for i in range(N):
    codigo.append(int(input()))
    nombre.append(input())
    cantidad.append(float(input()))
    unitario.append(float(input()))
    tipo_iva.append(int(input()))

for i in range(N):
    valor_producto.append(cantidad[i]*unitario[i])
    if tipo_iva[i]==1:
        iva.append(0)
    elif tipo_iva[i]==2:
        iva.append(valor_producto[i]*0.05)
    elif tipo_iva[i]==3:
        iva.append(valor_producto[i]*0.19)

    valor_final.append(valor_producto[i]+iva[i])
    Valortotaliva=Valortotaliva+iva[i]
    Valortotal=Valortotal+valor_final[i]
cod=len(codigo)
nom=len(nombre)
can=len(cantidad)
uni=len(unitario)
tiva=len(tipo_iva)

print(cod)
print(nom)
print(can)
print(uni)
print(tiva)

for i in range(N):
    print(codigo[i])
    print(nombre[i])
    print(valor_producto[i])
    print(valor_final[i])
print(Valortotal)
print(Valortotaliva)
