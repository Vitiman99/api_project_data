import json
import boto3

AWS_ACCESS_KEY_ID = 'TU_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'TU_SECRET_ACCESS_KEY'
S3_BUCKET_NAME = 'NOMBRE_DE_TU_BUCKET'


def save_result_to_s3(data):
    # Convertir los datos a formato JSON
    json_data = json.dumps(data)

    # Guardar el resultado en Amazon S3
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3.put_object(
        Body=(bytes(json_data.encode('UTF-8'))),
        Bucket=S3_BUCKET_NAME,
        Key='resultado.json'
    )


def load_result_from_s3():
    # Cargar el JSON desde Amazon S3
    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    response = s3.get_object(
        Bucket=S3_BUCKET_NAME,
        Key='resultado.json'
    )

    # Leer el contenido del objeto y convertirlo a JSON
    json_data = response['Body'].read().decode('UTF-8')
    data = json.loads(json_data)

    return data