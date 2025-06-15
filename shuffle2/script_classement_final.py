import json
from collections import defaultdict
from statistics import mode

# Charger le fichier JSON
input_file = "reduced_votes.json"

try:
    with open(input_file, "r") as f:
        data = json.load(f)

    total_votes = defaultdict(int)
    all_votes_flat = []

    for entry in data:
        for vote in entry["votes"]:
            song = vote["song_number"]
            count = vote["count"]
            total_votes[song] += count
            all_votes_flat.extend([song] * count)

    # Classement final
    final_ranking = sorted(total_votes.items(), key=lambda x: x[1], reverse=True)

    print("\n🎵 CLASSEMENT FINAL DES CHANSONS 🎵\n")
    for i, (song, votes) in enumerate(final_ranking, start=1):
        print(f"{i}. Chanson {song} : {votes} votes")

    winner_mode = mode(all_votes_flat)
    winner_total = final_ranking[0][0]

    print(f"\n📊 Mode() donne comme gagnant : Chanson {winner_mode}")
    print(f"🏆 Gagnant total par votes : Chanson {winner_total}")

    if winner_mode == winner_total:
        print("✅ Les deux méthodes confirment le même gagnant.")
    else:
        print("⚠️ Attention : résultats différents entre mode() et total.")

except FileNotFoundError:
    print(f"❌ Le fichier {input_file} est introuvable.")
except json.JSONDecodeError:
    print("❌ Erreur de lecture du JSON.")
except Exception as e:
    print(f"❌ Erreur inattendue : {e}")
