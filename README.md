<h1 align="center">Neutral News – Backend</h1>

> ⚠️ Este repositorio contiene únicamente el **backend** de *Neutral News*.  
> El sistema completo incluye tres partes:
>
> - 📡 **Backend (este repo)** – Extracción, agrupación y generación de noticias neutrales. (Ezequiel & Martí)  
> - 🤖 [Android](https://github.com/EzequielGaribotto/neutral-news-android) – Aplicación móvil nativa para Android. (Ezequiel)  
> - 🍎 [iOS](https://github.com/martiespinosa/neutral-news) – Aplicación móvil nativa para iOS. (Martí)

## 📰 ¿Qué es Neutral News?

Neutral News es una plataforma que recopila noticias de distintos medios, identifica las coberturas sobre un mismo hecho y genera una versión **neutral** utilizando Inteligencia Artificial.  
**El objetivo** es **reducir el sesgo mediático** y ofrecer una visión más equilibrada de la actualidad.

## 🚀 ¿Cómo funciona?

Todo el backend funciona bajo un flujo **ETL (Extract, Transform, Load) automatizado** que se ejecuta cada hora:

### 🔄 1. Extracción (Extract)

- Una Cloud Function se ejecuta con **Cloud Scheduler**.
- Obtiene noticias desde feeds **RSS**.
- Se almacenan en **Firestore**.

### 🧠 2. Agrupación (Transform)

- Se generan **embeddings semánticos** con **SBERT**.
- Se agrupan noticias similares con algoritmos de clústering de **DBSCAN** y **KMeans**.

### ✍️ 3. Generación neutral (Load)

- Para cada grupo, se crea un **resumen neutral** usando la **API de OpenAI**.
- Se guarda en Firestore para posterior uso en las apps.

## 🛠️ Tecnologías

| Categoría                        | Herramientas / Tecnologías                                                       |
|----------------------------------|----------------------------------------------------------------------------------|
| **Lenguajes**                    | Python, Bash, PowerShell, Dockerfile                                             |
| **Embeddings semánticos**        | SBERT (Sentence-BERT)                                                            |
| **Clustering**                   | DBSCAN, KMeans                                                                   |
| **Generación de texto**          | OpenAI GPT (API)                                                                 |
| **Automatización ETL**           | Cloud Scheduler, Cloud Functions                                                 |
| **Base de datos**                | Firebase Firestore (NoSQL)                                                       |
| **Infraestructura / Cloud**      | Google Cloud Platform (GCP), Docker                                              |
| **Control de versiones**         | Git                                                                              |

## 🗺️ Arquitectura

![Diagrama](https://github.com/user-attachments/assets/e169886a-4081-4ac6-990f-2238d3097141)

## 🎓 Proyecto académico

El desarrollo comenzó como proyecto final del CFGS de Desarrollo de Aplicaciones Multiplataforma en el Institut Tecnològic de Barcelona, realizado por Ezequiel Garibotto y Martí Espinosa, y continúa de forma independiente tras su presentación.

📅 [Ver presentación – 20/05/2025](https://www.canva.com/design/DAGniT2itZA/xQ5kseKfUXHrKU7Y1SUJ8Q/view?utm_content=DAGniT2itZA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he99b512169)
