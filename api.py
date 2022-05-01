
Signup
import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    userid=event['queryStringParameters']['userid']
    password=event['queryStringParameters']['password']
    print("User id entered is :",userid)
    print("Password entered is :",password)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userinfo')
    res=table.get_item(
       Key={
            'userid':userid,
           
        }
    )
    
    
    print(res)
    responsevar=''
    if 'Item' in res:
        responsevar='User id is already present so please select new user id'
    else:
        responsevar='Welcome to the sysetm'
        res1=table.put_item(
          Item={
             'userid':userid,
             'password':password,
          }
        )
        print(res1)
    return {
        'statusCode': 200,
        'body': json.dumps(responsevar)
    }
    
 
 

Delete

import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
   
    userid=event['queryStringParameters']['userid']
    #password=event['queryStringParameters']['password']
    
    print("User id entered is :",userid)
    #print("Password entered is :",password)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userinfo')
    
    table.delete_item(
        Key={
            'userid':userid 
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('User deleted succesfull')
    }
    
    
    Update 
    
    import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    userid=event['queryStringParameters']['userid']
    password=event['queryStringParameters']['password']
    print("User id entered is :",userid)
    print("Password entered is :",password)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userinfo')
    
    table.update_item(
        Key={
                'userid':userid
        },
        UpdateExpression='SET password = :val1',
        ExpressionAttributeValues={
            ':val1':password
        }
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

Signin

import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print(event)
    userid = event['queryStringParameters']['userid']
    password=event['queryStringParameters']['password']
    
    print("User id entered is :",userid)
    print("Password entered is :",password)
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('userinfo')
    res = table.get_item(
        Key={
            'userid':userid,
            
        }
    )
    if 'Item' in res:
        responsevar="Welcome user"
    else:
        responsevar="Not valid"
    
    print(res)
    return {
        'statusCode': 200,
        'body': json.dumps(responsevar)
    }


