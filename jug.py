from lxml import etree
doc=etree.parse('jugueteria.xml')
raiz=doc.getroot()
#1º apartado
nombres=raiz.xpath("product/name")
precio=raiz.xpath("product/price")
iva=raiz.xpath("product/iva")
for x,y,z in zip(nombres,precio,iva):
	total=float(y.text)+float(z.text)
	print("Artículo:",x.text)
	print("Precio Total:",total)
	print()
#2º apartado	
print("Nº de juguetes:",len(nombres))
#3º apartado
fecha=input("Introduce la fecha en la que se añadió el juguete separado por -: ")
fechas=raiz.xpath("product/date_add")
fallo=False
for elem in fechas:
	Pfecha=elem.text.split(" ")[0]
	if Pfecha == fecha:
		print("Artículo:",nombres[fechas.index(elem)].text)
		fallo=True		
if fallo != True:
	print("No existe ningún artículo introducido en esa fecha")
#4º apartado
articulo=input("Introduce un artículo: ")
stock=raiz.xpath("product/stock")
fallo=False
for elem in nombres:
	if articulo == elem:
		print("Artículos en stock:",stock[nombres.index(elem)].text)
		fallo=True
if fallo != True:
	print("Ese artículo no existe")