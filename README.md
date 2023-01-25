# Basic Blog
------------------------------------------------------------------------------

Hay que realizar la copia de nuestro archivo de configuración

```
	cp config.ini.dist config.ini
```

Posteriormente editar el el archivo config.ini, se recomienda que sea con el valor de env = production y rellenar el valor de secret_key, se recomienda utilizar el siguiente comando para generarlo y copiar su salida.

```
openssl rand -base64 32
```

Si el protocolo final es https, rellenarlo apropiadamente, así como el dominio y el host de la aplicación, debido a que no es capaz de reconocerlo automáticamentem esto con el fin de generar apropiadamente el mapa del sitio.

- Instalar el proyecto:
```
	docker-compose build
```

- Levantar el proyecto:
```
	docker-compose up -d
```

Para correr cualquier comando de django se puede hacer con:

```
	docker exec -it gf_django [command]
```

Hay que realizar migraciones necesarias

```
	docker exec -it gf_django python3 manage.py makemigrations
	docker exec -it gf_django python3 manage.py migrate
```

Despues crear el super usuario
```
	docker exec -it gf_django python3 manage.py createsuperuser
```

En la url de nuestro nuevo admin estará disponible en el root de nuestro proyecto más la ruta "/gf-admin", debemos entrar ahí y crear nuestra primer entrada de "sitio"

Listo, deberíamos ser capaces de ver nuestro proyecto corriendo apropiadamente el puerto 8000
