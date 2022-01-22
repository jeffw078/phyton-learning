#LEARNING HOW TO HANDLE WITH EXTERNAL LIBS
#USING PIP TO INSTALL LIBS

from pygeocoder import Geocoder

# endereco = "1222, Lins de Vasconcelos, Sao Paulo, SP"
# print(Geocoder('AIzaSyDlnuBEOc0G2L3WYvpr5pe9KvEWXIq3WuM').geocode(endereco).coordinates)

endereco2 = 'av paulista, 100, sp'
resultado = Geocoder('AIzaSyDlnuBEOc0G2L3WYvpr5pe9KvEWXIq3WuM').geocode(endereco2)
print(resultado)