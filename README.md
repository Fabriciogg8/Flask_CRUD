# FLASK Create Read Update Delete

<a name="top"></a>

## [English](#item1)
## [Español](#item2)

 
<a name="item1"></a>

### English
 
#### Used technology: PYTHON, FLASK

##### Abstract

In this repository I will cover HTTP methods: GET, POST, PUT, PATCH, DELETE. Basically what they are, when to use it, and where.

## INTRODUCTION

We will create a dictionary, to use it as a mock database. 

By default our @app.route("/some_url") will work wiht a **GET** request. With GET we are getting a resource from the server, we are not providing any information.  

**POST** we create a new resource in the server, for example a new user. 
**PUT** should be used when it is necessary to do a full replacement of a resource. That is, if we have a Users table and we want to update all the data of a user, we should implement it. PUT will expect the new data to be completely the same as what was received via a form.
**PATCH** it should be used when you want to modify a single field. For example, if we only want to update the email of one of our users, PATCH would be the recommended one.
**DELETE** we will be able to delete data. 

**Thunder Client** is an extension of Visual Studio Code, that is a REST API client, so we can use it to call the different routes we are creating. So we enter in collections, create a new one, and we give it a name preferably referring to the work we are doing, in this case flask_rest_API. After that, we can create a new Request, where we can specify the name of the method for that request and the name of what it does, so we can have a better understanding.

## IMPLEMENTATION

We wil create a function that returns a json representation of the stock dictionary. With **make_response** we will build our response, and with **jsonify** we can parse a python object into a json object.  

**make_response** function takes one, two, or three arguments, the same values that can be returned from a view function, and returns a Response object. Sometimes it is useful to perform this conversion inside the view function and then use the methods of the response object to further configure the response.

## GET

So, in this case when we call our route **/stock** with the function get_stock we have a json response of our dictionary. 

We also can create a route where we specify a key existing inside stock, and that is what we do in the function **get_collection**. We use a variable to specify inside the route what is what we want to display. 

After that, we can also dig deeper into the Python dict, to look up a member in the collection. We do this in the **get_member** route, as we did before, if the member is not in the collection, we will throw an error.

## POST

In this case we create the route with a < variable >. This **variable** provides the key for the new collection, if the collection already exists we send a message and do not enable saving it. 

We must pass in the request the data of the members and the quantities. Obviously I did it through Thunder Client.
The method that we use is **update** (stock.update({collection:req})). 

## PUT

We create a function similar to the one with POST, but in this case if the collection exists the new data will replace the member or amounts we passed. 

## PATCH

We always use the same url as in the other methods. In this case, we check the members, if there is a change in the members, we save it, or if we want to add a new member to a collection, we can do it. Other ways if the collection is new we created. 

The diference with PUT is that, if we pass the url: stock/animals 
{
    "horse" : 3,
    "sheep" : 2,
    "catlle" : 8,
}

With PUT it changes to that, so if we already have: 
{
    "horse" : 1,
    "sheep" : 1,
    "catlle" : 5,
    "sea_lion" : 1
}
sea_lion will we erased. In the other hand, with PATCH, only the quantities will be modify, and sea lion will be continue existing in the data base.

Then we can do the same, but instead of looking for the collection we look for the member, inside a collection. If the member already exists we change its value. In other ways we create it. 

Keep in mind that the key that we enter in the request does not matter, but to search for the member, the variable in the url is taken into account.

## DELETE

In this function, we pass a collection via url, the function searches the stock to find the collection. If it exists, it deletes it. We return an empty message, with a status code of 204, which means action enacted (performed). We could send a 200, it doesn't matter.

If the collection does not exist in the stock, we send a message.

After that, we create a new function, where we can remove a member from a collection. It works like the previous function.  

[Go up](#top)

<a name="item2"></a>

### Español
 
#### Tecnologías utilizadas: JAVASCRIPT, HTML, CSS

##### Resumen

En este repositorio cubrire los métodos HTTP: GET, POST, PUT, PATCH, DELETE. Básicamente qué son, cuándo usarlos y dónde.

## INTRODUCCIÓN

Crearemos un diccionario, para usarlo como una base de datos simulada.

Por defecto, nuestra @app.route("/some_url") funcionará con una solicitud **GET**. Con GET obtenemos un recurso del servidor, no proporcionamos ninguna información.

**POST** creamos un nuevo recurso en el servidor, por ejemplo un nuevo usuario.
**PUT** debe usarse cuando es necesario hacer un reemplazo completo de un recurso. Es decir, si tenemos una tabla de Usuarios y queremos actualizar todos los datos de un usuario, debemos implementarla. PUT esperará que los nuevos datos sean completamente iguales a los que se recibieron a través de un formulario.
**PATCH** debe utilizarse cuando se desee modificar un solo campo. Por ejemplo, si solo queremos actualizar el correo electrónico de uno de nuestros usuarios, PATCH sería el recomendado.
**DELETE** podremos borrar datos.

**Thunder Client** es una extensión de Visual Studio Code, que es un cliente API REST, por lo que podemos usarlo para llamar a las diferentes rutas que estamos creando. Así que entramos en colecciones, creamos una nueva, y le damos un nombre preferiblemente haciendo referencia al trabajo que estamos haciendo, en este caso flask_rest_API. Después de eso, podemos crear una nueva Solicitud, donde podemos especificar el nombre del método para esa solicitud y el nombre de lo que hace, para que podamos tener una mejor comprensión.

## IMPLEMENTACIÓN

Crearemos una función que devuelva una representación json del diccionario de valores. Con **make_response** construiremos nuestra respuesta, y con **jsonify** podemos parsear un objeto python a un objeto json.

La función **make_response** toma uno, dos o tres argumentos, los mismos valores que se pueden devolver desde una función de vista, y devuelve un objeto de Respuesta. A veces es útil realizar esta conversión dentro de la función de vista y luego usar los métodos del objeto de respuesta para configurar aún más la respuesta.

## GET

Entonces, en este caso cuando llamamos a nuestra ruta **/stock** con la función get_stock tenemos una respuesta json de nuestro diccionario.

También podemos crear una ruta donde especificamos una clave existente dentro del stock, y eso es lo que hacemos en la función **get_collection**. Usamos una variable para especificar dentro de la ruta qué es lo que queremos mostrar.

Después de eso, también podemos profundizar en el dict de Python para buscar un miembro en la colección. Hacemos esto en la ruta **get_member**, como hicimos antes, si el miembro no está en la colección, arrojaremos un error.

## POST

En este caso creamos la ruta con una <variable>. Esta **variable** proporciona la clave para la nueva colección, si la colección ya existe enviamos un mensaje y no habilitamos guardarla.

Debemos pasar en la solicitud los datos de los integrantes y las cantidades. Obviamente lo hice a través de Thunder Client.
El método que usamos es **actualizar** (stock.update({collection:req})).

## PUT

Creamos una función similar a la de POST, pero en este caso si la colección existe, los nuevos datos reemplazarán al miembro o las cantidades que pasamos.

## PATCHE

Siempre usamos la misma url que en los otros métodos. En este caso, comprobamos los miembros, si hay un cambio en los miembros, lo guardamos, o si queremos agregar un nuevo miembro a una colección, podemos hacerlo. En otro caso si la colección es nueva la creamos.

La diferencia con PUT es que si le pasamos la url: stock/animals
{
    "caballo": 3,
    "oveja": 2,
    "gato" : 8,
}

Con PUT cambia a eso, así que si ya tenemos:
{
    "caballo": 1,
    "oveja": 1,
    "gato" : 5,
    "león_marino": 1
}

sea_lion sera borrado. En cambio, con PATCH, sólo se modificarán las cantidades, y el león marino seguirá existiendo en la base de datos.

Luego podemos hacer lo mismo, pero en lugar de buscar la colección buscamos el miembro, dentro de una colección. Si el miembro ya existe, cambiamos su valor. De otras maneras lo creamos.

Tener en cuenta que la clave que ingresamos en la solicitud no importa, pero para buscar el miembro, se tiene en cuenta la variable en la url.

## DELETE

En esta función, pasamos una colección a través de url, la función busca en el stock para encontrar la colección. Si existe, lo borra. Devolvemos un mensaje vacío, con un código de estado de 204, lo que significa acción *enacted* (realizada). Podríamos enviar un 200, no importa.

Si la colección no existe en el stock, enviamos un mensaje.

Después de eso, creamos una nueva función, donde podemos eliminar un miembro de una colección. Funciona como la función anterior.

[Subir](#top)