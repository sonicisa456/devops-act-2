# 🚀 Proyecto DevOps AWS

## 📌 Descripción
Este proyecto implementa una solución de automatización en AWS utilizando prácticas DevOps.

Incluye:
- Gestión de instancias EC2 con Python (boto3)
- Respaldo de archivos en S3 con Bash
- Control de versiones con Git
- Simulación de CI/CD con scripts

---

## ⚙️ Uso

### Ejecutar deploy

```bash
./deploy.sh iniciar

Flujo Git
main → producción
develop → integración
feature/* → desarrollo

Ejemplos
./deploy.sh iniciar
./deploy.sh detener

Tecnologías
Python (boto3)
Bash
AWS (EC2, S3)
Git / GitHub
