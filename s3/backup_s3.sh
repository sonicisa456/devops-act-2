#!/bin/bash

# Parámetros
DIRECTORIO=$1
BUCKET=$2

# Validación
if [ -z "$DIRECTORIO" ] || [ -z "$BUCKET" ]; then
    echo "validando directorio..."
    echo "Uso: ./backup_s3.sh <directorio> <bucket>"
    exit 1
fi

# Fecha para nombre único
FECHA=$(date +%Y%m%d_%H%M%S)

# Nombre del archivo comprimido
ARCHIVO="backup_$FECHA.tar.gz"

# Log
LOG="logs/backup.log"

echo "[$FECHA] Iniciando backup..." >> $LOG

# Comprimir
tar -czf $ARCHIVO $DIRECTORIO

if [ $? -ne 0 ]; then
    echo "[$FECHA] Error al comprimir" >> $LOG
    exit 1
fi

# Subir a S3
aws s3 cp $ARCHIVO s3://$BUCKET/

if [ $? -ne 0 ]; then
    echo "[$FECHA] Error al subir a S3" >> $LOG
    exit 1
fi

echo "[$FECHA] Backup exitoso: $ARCHIVO" >> $LOG

# Limpiar archivo local (opcional)
rm $ARCHIVO
