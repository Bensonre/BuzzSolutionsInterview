import json
import boto3
from lambda_proxy.proxy import API
client = boto3.client('dynamodb')
app = API(name="app", debug = True)

@app.get("/health")
def get_health_check():
    return ('OK','application/json', 200)

@app.get("/Resume")
def get_all_Resume():
    response = client.scan(
        TableName='Resume',
        Limit=123,
        Select='ALL_ATTRIBUTES'
    )
    return ('OK', 'application/json', json.dumps(response['Items']))

@app.get("/Resume/<ID>")
def get_resume(ID):
    response = client.get_item(
        TableName='Resume',
        Key={ 
                "id": {
                    "S": ID,
                }, 
            }
        )
    return ('OK', 'application/json', json.dumps(response['Item']))

@app.post("/Resume")
def post_resume(body):
    body = json.loads(body)
    if "id" in body:
        response = client.put_item(
            TableName='Resume',
            Item= body
        )
        return ('OK', 'application/json', "{\"message\": \"Success\"}")
    # This was a simplified solution to increment the id by one. Due to the simplicity of the database and could result in data being over written so I instead decided to return a failure.
    #else:
    #    response = client.scan(
    #        TableName='Resume',
    #        Select='COUNT'
    #    )
    #    body["id"] = {"S": str(response["Count"]+1)}
    #    response = client.put_item(
    #        TableName='Resume',
    #        Item= body
    #    ) 
    #    return ('OK', 'application/json', "{\"message\": \"Success, no id provided, so the response was placed in the next aviable spot.\", \"id\": " + json.dumps(body["id"])+ "}")
    else:
        response = client.scan(
            TableName='Resume',
            Select='SPECIFIC_ATTRIBUTES',
            ProjectionExpression= 'id'
        ) 
        ids = list(map(lambda x: int(x["id"]["S"]), response["Items"]))
        ids.sort(reverse= True)
        body["id"] = {"S": str(ids[0]+1)} 
        response = client.put_item(
            TableName='Resume',
            Item= body
        ) 
        return ('OK', 'application/json', "{\"message\": \"Success, no id provided, so the response was placed in the next aviable spot.\", \"id\": " + json.dumps(body["id"])+ "}")


@app.route("/Resume/<ID>", methods=['POST','PUT'])
def post_resume(ID, body):
    body = json.loads(body)
    body["id"] = {"S": str(ID)}  
    response = client.put_item(
        TableName='Resume',
        Item= body
        )
    return ('OK', 'application/json', "{\"message\": \"Success\"}")

@app.route("/Resume/<ID>", methods=['DELETE'])
def delete_resume(ID):
    response = client.delete_item(
        TableName='Resume',
        Key={ 
                "id": {
                    "S": ID,
                }, 
            }
        )
    return ('OK', 'application/json', "{\"message\": \"Success\"}")

def lambda_handler(event, context):
    try:
        print("start")
        print(event)
        response = app(event, None)    
        return response
    except Exception as e:
        print(e)
        return ('Internal Error', 'application/json', json.dumps(e))
