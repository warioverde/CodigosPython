diccionario = {"Guatemala": "Ciudad de Guatemala", 
"El Salvador": "San Salvador", "Honduras": "Honduras",
"Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama",
 "Argentina": "Buenos Aires", "Colombia": "Bogota",
  "Venezuela": "Caracas", "España": "Madrid"}

respuesta = input("Ingrese Pais ")
if(diccionario.get(respuesta)):
    print(diccionario.get(respuesta))
else:
    print("El pais no se encuentra")