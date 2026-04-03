#!/bin/bash

# Parámetros
ACCION=$1
INSTANCE_ID=$2
DIRECTORIO=$3
BUCKET=$4

LOG="logs/deploy.log"
FECHA=$(date +%Y%m%d_%H%M%S)

echo "[$FECHA] Iniciando despliegue..." >> $LOG

# Validación de parámetros
if [ -z "$ACCION" ] || [ -z "$INSTANCE_ID" ] || [ -z "$DIRECTORIO" ] || [ -z "$BUCKET" ]; then
    echo "Uso: ./deploy.sh <accion> <instance_id> <directorio> <bucket>"
    exit 1
fi

# Ejecutar script EC2 (Python)
echo "[$FECHA] Ejecutando acción EC2: $ACCION" >> $LOG

python3 ec2/gestionar_ec2.py $ACCION $INSTANCE_ID

if [ $? -ne 0 ]; then
    echo "[$FECHA] Error en script EC2" >> $LOG
    exit 1
fi

# Ejecutar backup en S3
echo "[$FECHA] Ejecutando backup en S3..." >> $LOG

./s3/backup_s3.sh $DIRECTORIO $BUCKET

if [ $? -ne 0 ]; then
    echo "[$FECHA] Error en backup S3" >> $LOG
    exit 1
fi

echo "[$FECHA] Deploy completado correctamente" >> $LOG
