from lxml import etree
doc=etree.parse('jugueteria.xml')
raiz=doc.getroot()
nombres=raiz.xpath("product/name")
precio=raiz.xpath("product/price")
iva=raiz.xpath("product/iva")
for x,y,z in zip(nombres,precio,iva):
	total=float(y.text)+float(z.text)
	print("Articulo:",x.text)
	print("Precio Total:",total)
	print()
print("Nº de juguetes:",len(nombres))