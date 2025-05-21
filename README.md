<h1 align="center">Neutral News – Backend</h1>

> ⚠️ **Este repositorio corresponde únicamente al backend del proyecto Neutral News**.  
> El sistema completo está compuesto por tres partes:
>
> - 📡 **Backend (este repositorio)** – Extracción, procesamiento, agrupación y generación de noticias neutralizadas. (Ezequiel & Martí)  
> - 📱 [**App Android**](https://github.com/EzequielGaribotto/neutral-news-android) – Aplicación móvil nativa para Android. (Ezequiel Garibotto)  
> - 🍎 [**App iOS**](https://github.com/martiespinosa/neutral-news) – Aplicación móvil nativa para iOS. (Martí Espinosa)

Neutral News nace del proyecto final de CFGS en Desarrollo de Aplicaciones Multiplataforma.  
A esta aplicación se le ha puesto especial énfasis al backend, aunque cuenta con unas aplicaciones nativas Android e iOS funcionales, a las que se les tiene pensado implementar varias mejoras y arreglos.  
Para más información, puedes ver la [presentación (20/05/2025)](https://www.canva.com/design/DAGniT2itZA/xQ5kseKfUXHrKU7Y1SUJ8Q/view?utm_content=DAGniT2itZA&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=he99b512169).

---

## 📑 Índice

- [📰 ¿Qué es Neutral News?](#-qué-es-neutral-news)
- [🚀 ¿Cómo funciona el backend?](#-cómo-funciona-el-backend)
  - [🔄 1. Extracción (Extract)](#-1-extracción-extract)
  - [🧠 2. Transformación (Transform)](#-2-transformación-transform)
  - [✍️ 3. Carga (Load)](#-3-carga-load)
- [🛠️ Tecnologías utilizadas](#️-tecnologías-utilizadas)
- [📷 Diagrama de la arquitectura](#-diagrama-de-la-arquitectura)
- [📍 Formación](#-formación)

---

## 📰 ¿Qué es Neutral News?

**Neutral News** es una plataforma que recopila noticias de múltiples medios de comunicación, las agrupa por temática y genera una **versión neutral** de los acontecimientos.  
El objetivo es **combatir el sesgo mediático** mediante el uso de técnicas avanzadas de Inteligencia Artificial.

---

## 🚀 ¿Cómo funciona el backend?

El backend está basado en un flujo **ETL (Extract, Transform, Load)** completamente automatizado con tecnologías modernas de **cloud computing** e **IA**:

### 🔄 1. Extracción (Extract)

- Usamos **Cloud Scheduler** para ejecutar cada hora una **Cloud Function**.
- Esta función accede a diversos **feeds RSS** y obtiene las noticias nuevas.
- Las noticias se almacenan en **Firebase Cloud Firestore** (base de datos NoSQL).

### 🧠 2. Transformación (Transform)

- Se generan **embeddings semánticos** de cada noticia usando **SBERT (Sentence-BERT)**.
- Se agrupan noticias similares mediante algoritmos de clustering como:
  - **DBSCAN**
  - **KMeans**

Esto permite detectar diferentes coberturas del mismo suceso.

### ✍️ 3. Carga (Load)

- Para cada grupo de noticias, se genera un resumen neutralizado utilizando la **API de OpenAI (GPT)**.
- Los resúmenes se guardan en otra colección de **Firestore**, listos para ser consumidos por las apps móviles.

---

## 🛠️ Tecnologías utilizadas

| Categoría                         | Herramientas / Tecnologías                                                       |
|----------------------------------|----------------------------------------------------------------------------------|
| **Lenguajes**                    | Python, Shell Script (Bash), PowerShell, Dockerfile                             |
| **Embeddings semánticos**        | SBERT (Sentence-BERT)                                                            |
| **Clustering**                   | DBSCAN, KMeans                                                                   |
| **Generación de texto**          | OpenAI GPT API                                                                   |
| **ETL**                          | Cloud Scheduler, Cloud Functions                                                 |
| **Base de datos**                | Firebase Cloud Firestore (NoSQL)                                                 |
| **Infraestructura / Automatización** | Google Cloud Platform, Docker                                                  |
| **Control de versiones**         | Git                                                                              |

---

## 📷 Diagrama de la arquitectura

![Neutral News](https://github.com/user-attachments/assets/e169886a-4081-4ac6-990f-2238d3097141)

---

## 📍 Formación

Este proyecto ha sido desarrollado como parte del **proyecto final del ciclo formativo de Desarrollo de Aplicaciones Multiplataforma (DAM)** en el **Institut Tecnològic de Barcelona**.  
A través de este backend se ha puesto en práctica el aprendizaje en **IA, Big Data, procesamiento de texto, backend cloud y automatización de procesos**.
