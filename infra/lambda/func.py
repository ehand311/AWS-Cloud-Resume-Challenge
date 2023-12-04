import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloudresume-test')

def lambda_handler(event, context):
    try:
        # Increment the views count for the specified item ('1')
        response = table.update_item(
            Key={'id': '1'},
            UpdateExpression='SET #v = if_not_exists(#v, :zero) + :incr',
            ExpressionAttributeNames={'#v': 'views'},
            ExpressionAttributeValues={':zero': 0, ':incr': 1},
            ReturnValues='UPDATED_NEW'
        )

        # Get the updated views count and convert Decimal to float
        views = float(response.get('Attributes', {}).get('views', 0))

        # Prepare the response
        api_response = {
            'statusCode': 200,
            'body': json.dumps({'views': views})
        }

        return api_response

    except Exception as e:
        print(f"Error: {str(e)}")
        # Handle the error and return an appropriate response
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Internal Server Error'})
        }
   