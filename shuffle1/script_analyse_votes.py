from pyspark.sql import SparkSession
import json

# 🧠 Initialiser une session Spark
spark = SparkSession.builder \
    .appName("AnalyseVotesPublic") \
    .master("local[*]") \
    .getOrCreate()

# 📥 Fichier d'entrée (généré lors de l'étape précédente)
input_file = "stockage_resultat/script_votes_du_public_es.txt"

# 🔁 Lire le fichier dans un RDD
rdd = spark.sparkContext.textFile(input_file)

# 🧩 Transformation : ((country, song), 1) → count total
mapped = rdd.map(lambda line: line.strip().split(",")) \
            .map(lambda fields: ((fields[0], fields[2]), 1))

reduced = mapped.reduceByKey(lambda a, b: a + b)

# 📦 Réorganiser : {country: [{song, count}, ...]}
grouped = reduced.map(lambda x: (x[0][0], (x[0][1], x[1]))) \
                 .groupByKey() \
                 .mapValues(list)

# 📄 Créer la structure finale pour le JSON
result = grouped.map(lambda x: {
    "country": x[0],
    "votes": [{"song_number": song, "count": count} for song, count in x[1]]
}).collect()

# 💾 Sauvegarder dans un fichier JSON
output_file = "stockage_resultat/reduced_votes.json"
with open(output_file, "w") as f:
    json.dump(result, f, indent=4)

print(f"✅ Résultat sauvegardé dans {output_file}")
