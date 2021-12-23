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