from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import pickle

# Set pandas display option
pd.set_option('display.max_colwidth', None)

# Load the dataset
df = pd.read_csv('flipkartData.csv')

# Preprocessing
df = df.dropna(subset=['description', 'product_name'])
df['content'] = df['description'] + df['product_name']

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read embeddings and cosine similarity matrix from pickle files
with open('embeddings.pkl', 'rb') as f:
    embeddings = pickle.load(f)

with open('cosine_sim.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

def get_recommendations(user_input, model=model, embeddings=embeddings, cosine_sim=cosine_sim, df=df):
    user_input_embedding = model.encode([user_input], convert_to_tensor=False)
    cosine_sim_input = cosine_similarity(user_input_embedding, embeddings)
    sim_scores = list(enumerate(cosine_sim_input[0]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[0:10]
    product_indices = [i[0] for i in sim_scores]
    return df[['uniq_id', 'product_name', 'product_url']].iloc[product_indices]

