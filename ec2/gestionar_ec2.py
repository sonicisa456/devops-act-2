import boto3

# Crear cliente de EC2
ec2 = boto3.client('ec2', region_name='us-east-1')

def listar_instancias():
    response = ec2.describe_instances()

    for reserva in response['Reservations']:
        for instancia in reserva['Instances']:
            instance_id = instancia['InstanceId']
            estado = instancia['State']['Name']

            print(f"ID: {instance_id}")
            print(f"Estado: {estado}")
            print("-" * 20)
	    print("todo bien :)")

if __name__ == "__main__":
    listar_instancias()
