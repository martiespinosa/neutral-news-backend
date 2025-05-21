A través de **Cloud Scheduler**, ejecutamos cada hora una función que hace fetch de las nuevas noticias desde los RSS de distintos medios y las almacena en la col **Firebase Firestore**.
Después, agrupamos noticias que tratan sobre el mismo tema generando *embeddings* con **SBERT** y aplicando algoritmos de *clustering* como **DBSCAN** y **KMeans**.
Finalmente, generamos una versión neutral de cada grupo de noticias usando la **API de OpenAI**, y guardamos esos resúmenes en una colección aparte de Firestore.

![Neutral News (2)](https://github.com/user-attachments/assets/e169886a-4081-4ac6-990f-2238d3097141)
