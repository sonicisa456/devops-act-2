import boto3
import sys

ec2 = boto3.client('ec2', region_name='us-east-1')


def listar_instancias():
    response = ec2.describe_instances()

    for reserva in response['Reservations']:
        for instancia in reserva['Instances']:
            print("ID:", instancia['InstanceId'])
            print("Estado:", instancia['State']['Name'])
            print("-" * 20)


def iniciar_instancia(instance_id):
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f"Instancia {instance_id} iniciada")
    except Exception as e:
        print("Error al iniciar:", e)


def detener_instancia(instance_id):
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Instancia {instance_id} detenida")
    except Exception as e:
        print("Error al detener:", e)


def terminar_instancia(instance_id):
    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Instancia {instance_id} terminada")
    except Exception as e:
        print("Error al terminar:", e)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("python3 gestionar_ec2.py listar")
        print("python3 gestionar_ec2.py iniciar <id>")
        print("python3 gestionar_ec2.py detener <id>")
        print("python3 gestionar_ec2.py terminar <id>")
        sys.exit(1)

    comando = sys.argv[1]

    if comando == "listar":
        listar_instancias()

    elif comando == "iniciar":
        if len(sys.argv) < 3:
            print("Debes proporcionar el ID de la instancia")
        else:
            iniciar_instancia(sys.argv[2])

    elif comando == "detener":
        if len(sys.argv) < 3:
            print("Debes proporcionar el ID de la instancia")
        else:
            detener_instancia(sys.argv[2])

    elif comando == "terminar":
        if len(sys.argv) < 3:
            print("Debes proporcionar el ID de la instancia")
        else:
            terminar_instancia(sys.argv[2])

    else:
        print("Comando no válido")
