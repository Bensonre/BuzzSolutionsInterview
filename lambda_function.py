import json
import boto3
from lambda_proxy.proxy import API
client = boto3.client('dynamodb')

@app.get("/")
def get_health_check():
    return ('OK', 200)

@app.get("/Resume")
def get_all_Resume():
    response = client.scan(
        TableName='Resumes',
        Limit=123,
        Select='ALL_ATTRIBUTES'
    )
    return ('OK', 'application/json', json.dumps(response.items))

@app.get("/Resume/<ID>")
def get_resume(id):
    response = client.get_item(
        TableName='Resumes',
        Key={ 'id': {'N': 1}}
        )
    return ('OK', 'application/json', json.dumps(response.items))

def lambda_handler(event, context):
    try:
        app = API(name="app", debug = True)
        response = app(event, None)    
        return response
    except Exception as e:
        print(e)
        return ('Internal Error', 'application/json', json.dumps(e.message))
