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


def iniciar_instancia(instance_id):
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Instancia {instance_id} iniciada")


def detener_instancia(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Instancia {instance_id} detenida")



if __name__ == "__main__":
    listar_instancias()
