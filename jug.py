from lxml import etree
doc=etree.parse('jugueteria.xml')
raiz=doc.getroot()
nombres=raiz.xpath("product/name")
print(nombres)