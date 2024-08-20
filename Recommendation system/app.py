from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Sample dataset of movies
movies = pd.DataFrame({
    'title': ['Karthikeya', 'Remo', 'Pokiri', 'Jathi Ratnalu', 'DJ Tillu'],
    'genres': [['Action', 'Adventure'], ['Drama', 'Romance'], ['Action', 'Thriller'], ['Comedy'], ['Action', 'Comedy']]
})

# Content-based filtering function to recommend movies by genre
def get_recommendations(preferred_genre):
    preferred_genre = preferred_genre.lower()
    recommended_movies = movies[movies['genres'].apply(lambda genres: any(preferred_genre == genre.lower() for genre in genres))]
    return recommended_movies['title'].tolist()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    genre = request.form.get('genre')
    recommendations = get_recommendations(genre)
    return render_template('index.html', recommendations=recommendations, genre=genre)

if __name__ == '__main__':
    app.run(debug=True)




