import pandas as pd
from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

print(movies_df.head())
print(ratings_df.head())

# Prepare the data for Surprise
reader = Reader(rating_scale=(1, 5))
surprise_data = Dataset.load_from_df(ratings_df[['userId', 'movieId', 'rating']], reader)

# Split the dataset into training and testing sets
train_set, test_set = train_test_split(surprise_data, test_size=0.2)

# Initialize and train the SVD model
svd_model = SVD()
svd_model.fit(train_set)

# Evaluate the model
predictions = svd_model.test(test_set)
rmse_score = accuracy.rmse(predictions)
print(f'Collaborative Filtering RMSE: {rmse_score}')


# Create a TF-IDF Vectorizer based on movie genres
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genres'])

# Calculate the cosine similarity matrix
cosine_similarity_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

# Function to recommend movies based on a given title
def recommend_similar_movies(movie_title, cosine_sim=cosine_similarity_matrix):
    idx = movies_df.index[movies_df['title'] == movie_title].tolist()[0]
    similarity_scores = list(enumerate(cosine_sim[idx]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    top_movies_indices = [i[0] for i in sorted_scores[1:6]]  # Get top 5 similar movies
    return movies_df['title'].iloc[top_movies_indices]

def recommend_movies_for_user(user_id, movie_title):
    # Collaborative filtering recommendations
    movie_id = movies_df[movies_df['title'] == movie_title]['movieId'].values[0]
    similar_movie_ids = svd_model.get_neighbors(movie_id, k=5)
    
    print(f"Collaborative Recommendations for User {user_id}:")
    for movie in similar_movie_ids:
        print(movies_df[movies_df['movieId'] == movie]['title'].values[0])

    # Content-based recommendations
    print("\nContent-Based Recommendations:")
    content_recommendations = recommend_similar_movies(movie_title)
    print(content_recommendations)
