# FLASK

## INTRODUCTION

In this repository I will cover HTTP methods: GET, POST, PUT, PATCH, DELETE. Basically what they are, when to use it, and where.

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
