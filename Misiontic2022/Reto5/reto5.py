#funciones


#cuerpo de programa



N=int(input("N:"))
codigo=[]
cantidad=[]
tipo=[]
valor_producto=[]
iva=[]
valor_final=[]
total_ventas=0
total_iva=0

articulos={1:"Lapiz",2:"Cuaderno",3:"Borrador",4:"Regla",5:"ColoresX12",6:"Escuadra",7:"Calculadora",8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

for i in range(N):
    codigo.append(int(input()))
    cantidad.append(int(input()))
    tipo.append(int(input()))
for i in range(N):
    valor_producto.append(cantidad[i]*precios.get(codigo[i]))
    if tipo[i]==1:
        iva.append(0)
    elif tipo[i]==2:
        iva.append(valor_producto[i]*0.05)
    elif tipo[i]==3:
        iva.append(valor_producto[i]*0.19)
    valor_final.append(valor_producto[i]+iva[i])
    total_iva=total_iva+iva[i]
    total_ventas=total_ventas+valor_final[i]
codigo,cantidad,iva,valor_producto,valor_final=ordenamiento(N,codigo,cantidad,iva,valor_producto,valor_final)
for i in range(N):
    print(codigo[i])
    print(articulos.get(codigo[i]))
    print(valor_producto[i])
    print(valor_final[i])
print(total_ventas)
print(total_iva)
