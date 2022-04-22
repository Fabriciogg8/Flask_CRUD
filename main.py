from flask import Flask, make_response, jsonify, request, render_template


app = Flask(__name__)


stock = {
    "fruits" : {
        "banana" : 45,
        "apple" : 215,
        "cherry": 1150
    }
}


@app.route("/get_text")
def get_text():
    return "Example text "


@app.route("/stock")
def get_stock():
    
    res = make_response(jsonify(stock), 200)
    return res


@app.route("/stock/<collection>")
def get_collection(collection):
    ''' 
    Returns the collection from the stock 
    '''
    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res
    
    else:
        res = make_response(jsonify({"error": "Item not found"}), 400)                        
        return res
    

@app.route("/stock/<collection>/<member>")
def get_member(collection, member):
    ''' 
    Returns the quantity of a member from a collection in the stock 
    '''
    if collection in stock:
        member = stock[collection].get(member)
        if member:  
            res = make_response(jsonify(member), 200)
            return res
        else:
            res = make_response(jsonify({"error": "Unknow member"}), 400)                        
            return res
    
    else:
        res = make_response(jsonify({"error": "Collection not found"}), 400)                        
        return res


## POST

@app.route("/stock/<collection>", methods=["POST"])
def create_collection(collection):
    ''' 
    Creates a new collection if it doesn't exist 
    '''
    req = request.get_json()

    if collection in stock:
        res = make_response(jsonify({"error": "Collection already exists"}), 400)
        return res

    stock.update({collection: req})

    res = make_response(jsonify({"message": "Collection created"}), 201)
    return res


## PUT

@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    '''  
    Creates or replaces a collection. Expected body: { "member" : qty }
    '''
    req = request.get_json()
    
    stock[collection] = req
    
    res = make_response(jsonify({"message": "Collection created"}), 200)
    return res
    
    
## PATCH

@app.route("/stock/<collection>", methods=["PATCH"])
def patch_collection(collection):
    '''  
    Updates or creates a collection. Expected body: { "member" : qty }
    '''
    req = request.get_json()
    
    if collection in stock:
        for k, v in req.items():
            stock[collection][k] = v
            
        res = make_response(jsonify({"message": "Collection updated"}), 200)
        return res
    
    stock[collection] = req
    
    res = make_response(jsonify({"message": "Collection created"}), 200)
    return res


@app.route("/stock/<collection>/<member>", methods=["PATCH"])
def patch_member(collection, member):
    '''  
    Updates or creates a collection. Expected body: { "qty" : value }
    '''
    req = request.get_json()
    
    if collection in stock:
        for k, v in req.items():
            if member in stock[collection]:
                stock[collection][member] = v
                
                res = make_response(jsonify({"message": "Collection member updated"}), 200)
                return res
            
            stock[collection][member] = v
            
            res = make_response(jsonify({"message": "Collection member created"}), 200)
            return res
    
    res = make_response(jsonify({"message": "Collection not found"}), 400)
    return res


## DELETE

@app.route("/stock/<collection>", methods=["DELETE"])
def delete_collection(collection):
    '''  
    If the collection exists, delete it
    '''    
    if collection in stock:
        del stock[collection]
        
        res = make_response(jsonify({}), 204) #Action enacted
        return res
    
    res = make_response(jsonify({"message": "Collection not found"}), 400)
    return res


@app.route("/stock/<collection>/<member>", methods=["DELETE"])
def delete_member(collection, member):
    '''  
    If the collection exists, and the member exists, 
    delete it
    '''    
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
        
            res = make_response(jsonify({}), 204) #Action enacted
            return res
        
        res = make_response(jsonify({"message": "Collection member not found"}), 400)
        return res
    
    res = make_response(jsonify({"message": "Collection not found"}), 400)
    return res


if __name__ == "__main__":
    app.run(debug=True) 