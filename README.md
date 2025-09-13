# Experimento de Disponibilidad con FastAPI y Google Cloud Load Balancer

Este experimento demuestra cómo un **Load Balancer en Google Cloud Platform (GCP)** puede redirigir automáticamente el tráfico hacia instancias sanas de una aplicación, descartando aquellas que presentan fallas.

## Descripción
Se construyeron dos instancias de **FastAPI** en contenedores Docker:
- **Healthy Instance**: responde normalmente (`SIMULATE_ERROR=false`).
- **Faulty Instance**: devuelve errores intencionales (`SIMULATE_ERROR=true`).

Ambas instancias se desplegaron en **Managed Instance Groups (MIGs)** y se registraron en un **HTTP(S) Load Balancer** con un health check en `/health`.

El objetivo es demostrar que, cuando una instancia falla, el LB la marca como **UNHEALTHY** y redirige todo el tráfico a las instancias saludables.

## Resultados
- El LB descartó correctamente la instancia defectuosa.
- Requests a `/` y `/health` retornaron mayoritariamente `200 OK`.
- Con JMeter se validó que el throughput se mantuvo estable (~200 req/s) con solo un 0.2% de errores iniciales durante la transición de health checks.

## Conclusión
Este experimento confirma el **failover automático** de GCP Load Balancer, garantizando disponibilidad del servicio aún cuando una parte de la infraestructura falla.
