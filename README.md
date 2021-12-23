# testToken
Implemente un servicio REST que exponga un recurso para consultar usuarios, el cual
soporte el método GET, para una colección o tabla de usuarios. La url de la petición debe ser
de la siguiente manera:
GET http://myurl.com/user/<user_document>
Donde user_document, corresponde a su número de cédula y TOKEN será creado
implementado al gusto del postulante.
El token de autenticación debe ir en una cabecera HTTP de la forma:
Authentication: TOKEN
El método, debe devolver los siguientes resultados.
400, cuando la petición a este recurso es inválida (user_document, no es entero)
401, cuando el usuario envía un token inválido
404, cuando el usuario no se encuentra en la base de datos
200, cuando el usuario es encontrado. En este caso se debe devolver la información del
usuario en formato JSON


# obtener token 
```
 http://test1.jhancastano.com/token/
username    :   user
password    :   user

```
return
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY0MDMzMjk2MiwianRpIjoiZGFjNDk3YjVhYWRmNDk3MWE0MTFlNmJkZTA2MmFmMDgiLCJ1c2VyX2lkIjoxfQ.zkTKZPvb5agyffZ6f3wW49O2b6et9IRpk936UqthTVw",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwMzMyOTYyLCJqdGkiOiJlMWY3NGJlMmRjNmM0MmJiOWFkY2FlOTFjNmI0NTI5ZSIsInVzZXJfaWQiOjF9.-rQZgBMk7e1Vxv2tr4rmsTmkwM2WbarrzpkpWwEjedQ"
}
```
### Copiar access
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwMzMyOTYyLCJqdGkiOiJlMWY3NGJlMmRjNmM0MmJiOWFkY2FlOTFjNmI0NTI5ZSIsInVzZXJfaWQiOjF9.-rQZgBMk7e1Vxv2tr4rmsTmkwM2WbarrzpkpWwEjedQ
# servicio get
```
 http://test1.jhancastano.com/user/123456
 Authentication:Token
```
 cedulas de usuarios   123456 , 789

- 400 no es entero 
- 401 token invalido 
- 404 no encontrado usuario 
- 200 json usuario 

## en localhost
- instalar posgresql
- instalar entorno virtual
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver