import streamlit as st
import pandas as pd
import pickle
import os

st.set_page_config(page_title="Recommandation MovieLens", layout="wide")
st.title("Dashboard Recommandation — MovieLens 100k")

# =========================
# Charger les objets (pickle)
# =========================
PKL_PATH = os.path.join("artifacts", "reco_objects.pkl")

if not os.path.exists(PKL_PATH):
    st.error("❌ artifacts/reco_objects.pkl introuvable. Lance le notebook et sauvegarde les artefacts.")
    st.stop()

with open(PKL_PATH, "rb") as f:
    data = pickle.load(f)

cf_recos = data.get("cf_recos", {})
tfidf_recos = data.get("tfidf_recos", {})
svd_recos = data.get("svd_recos", {})
nmf_recos = data.get("nmf_recos", {})
mlp_recos = data.get("mlp_recos", {})
ae_recos  = data.get("ae_recos", {})
lstm_recos = data.get("lstm_recos", {})

item_id_to_title = data.get("item_id_to_title", {})
summary_df = data.get("summary_df", pd.DataFrame())
emb2d_dict = data.get("emb2d_dict", {})

# =========================
# Sidebar: user + méthode
# =========================
all_users = set()
for d in [cf_recos, tfidf_recos, svd_recos, nmf_recos, mlp_recos, ae_recos, lstm_recos]:
    all_users |= set(d.keys())
all_users = sorted(list(all_users))

if not all_users:
    st.error("Aucune reco chargée depuis le pickle. Vérifie que cf_recos/tfidf_recos/... contiennent des users.")
    st.stop()

user_id = st.sidebar.selectbox("Utilisateur", all_users)

method = st.sidebar.selectbox(
    "Approche",
    [
        "Collaboratif (Item-based)",
        "Contenu (TF-IDF)",
        "SVD (TruncatedSVD)",
        "NMF (Matrix Factorization)",
        "Deep Learning (MLP)",
        "Autoencoder",
        "LSTM"
    ]
)

def get_recos(u, m):
    if m == "Collaboratif (Item-based)":
        return cf_recos.get(u, [])
    if m == "Contenu (TF-IDF)":
        return tfidf_recos.get(u, [])
    if m == "SVD (TruncatedSVD)":
        return svd_recos.get(u, [])
    if m == "NMF (Matrix Factorization)":
        return nmf_recos.get(u, [])
    if m == "Deep Learning (MLP)":
        return mlp_recos.get(u, [])
    if m == "Autoencoder":
        return ae_recos.get(u, [])
    if m == "LSTM":
        return lstm_recos.get(u, [])
    return []

# =========================
# Zone 1: Top-10 recommandations
# =========================
st.subheader("Top-10 recommandations")
recos = get_recos(user_id, method)

df = pd.DataFrame({"item_id": recos[:10]})
df["title"] = df["item_id"].map(item_id_to_title)
st.dataframe(df, use_container_width=True)

# =========================
# Zone 2: métriques
# =========================
st.subheader("Comparaison des approches (métriques)")
if isinstance(summary_df, pd.DataFrame) and not summary_df.empty:
    st.dataframe(summary_df, use_container_width=True)
else:
    st.info("summary_df est vide. Calcule-le dans le notebook puis re-sauvegarde le pickle.")

# =========================
# Zone 3: embeddings
# =========================
st.subheader("Visualisations des embeddings (t-SNE)")

if emb2d_dict:
    emb_method = st.selectbox("Choisir la méthode", list(emb2d_dict.keys()))
    emb_df = emb2d_dict[emb_method].copy()

    st.scatter_chart(
        emb_df.set_index("item_id")[["x", "y"]],
        use_container_width=True
    )

    with st.expander("Voir les points (films)"):
        st.dataframe(emb_df[["item_id", "title", "x", "y"]].head(50), use_container_width=True)
else:
    st.info("Aucun embedding 2D disponible. Génère emb2d_dict dans le notebook puis re-sauvegarde le pickle.")
