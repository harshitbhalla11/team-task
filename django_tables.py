import boto3

dynamodb = boto3.client('dynamodb')

table_name = 'Groups'
key_schema = [
    {'AttributeName': 'GroupID', 'KeyType': 'HASH'},  # Partition key
    {'AttributeName': 'CreationDateTime', 'KeyType': 'RANGE'}  # Sort key
]
attribute_definitions = [
    {'AttributeName': 'GroupID', 'AttributeType': 'S'},
    {'AttributeName': 'CreationDateTime', 'AttributeType': 'S'}
]
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create table
response = dynamodb.create_table(
    TableName=table_name,
    KeySchema=key_schema,
    AttributeDefinitions=attribute_definitions,
    ProvisionedThroughput=provisioned_throughput
)

# Print response
print("Table creation response:", response)

# Initialize DynamoDB resource
dynamodb_resource = boto3.resource('dynamodb')

# Get table resource
table = dynamodb_resource.Table(table_name)

# Sample data
sample_data = {
    'GroupID': 'group123',
    'CreationDateTime': '2023-01-01T00:00:00Z',
    'GroupMembers': ['user1', 'user2', 'user3'],
    'VisibilityType': 'public',
    'Description': 'Sample group description',
    'AdminUserID': 'admin123'
}

# store data
response = table.put_item(Item=sample_data)

print("Put item response:", response)
