#BH 2nd Movie Recommender
#import csv
import csv
#parser function to load movies from csv file and clean the data
def load_movies(file_path):
    movies = [] 
    
    with open(file_path, mode='r') as f:
        for row in csv.DictReader(f):
            clean_movie = {
                'title': row['Title'].strip(),
                'director': row['Director'].strip(), 
                'genre': row['Genre'].strip(),
                'rating': row['Rating'].strip(),
                'length': int(row['Length (min)']),
                'actors': row['Notable Actors'].strip().split(", ")
            }
            movies.append(clean_movie)
            
    return movies
def display_movies(movies):
    for movie in movies:
        print(f"Title: {movie['title']}, Director: {movie['director']}, Genre: {movie['genre']}, Rating: {movie['rating']}, Length: {movie['length']} minutes, NotableActors: {', '.join(movie['actors'])}\n")
#filter by ____ functions
def filter_by_genre(movies, query):
    results = [m for m in movies if query in m['genre'].lower()]
    return results
def filter_by_director(movies, query):
    results = [m for m in movies if query in m['director'].lower()]
    return results
def filter_by_actor(movies, query):
    filtered_movies = []
    for movie in movies:
        for actor in movie['actors']:
            if query in actor.lower():
                filtered_movies.append(movie)
                break
    return filtered_movies
def filter_by_length(movies, min_length, max_length):
    filtered_movies = []
    for movie in movies:
        if (min_length is None or movie['length'] >= min_length) and (max_length is None or movie['length'] <= max_length):
            filtered_movies.append(movie)
    return filtered_movies
#function to apply filters to the movie list
def filter_movies(filters, movies):
    filtered_movies = movies
    for filter in filters:
        if filter['type'] == 'genre':
            filtered_movies = filter_by_genre(filtered_movies, filter['query'])
        elif filter['type'] == 'director':
            filtered_movies = filter_by_director(filtered_movies, filter['query'])
        elif filter['type'] == 'actor':
            filtered_movies = filter_by_actor(filtered_movies, filter['query'])
        elif filter['type'] == 'length':
            filtered_movies = filter_by_length(filtered_movies, filter['min_length'], filter['max_length'])
    return filtered_movies
#main function that runs the code
def main():
    #one-time introduction to the application
    print("Welcome to the Movie Recommender!\n")
    #load movies from csv file
    try:
        movies = load_movies("notes\Movies list.csv")
    except Exception as e:
        print(f"Error loading movies: {e}")
        return  # Exit if movies can't be loaded
    #while loop so code repeats
    while True:
        #main menu
        continue_or_exit = input("Would you like to find a movie (m), see the movie list (l), or exit (e)?\n")
        #if they want to find a movie, ask them which filters they want to apply and then display the results
        if continue_or_exit == "m":
            filters = []
            print("\nFilters: 1:Genre, 2:Director, 3:Actor, 4:Length")
            selected_options = input("Choose filters (e.g. 1,4): ").split(",")
            for option in selected_options:
                if option == '1':
                    query = input("Enter Genre: ").strip().lower()
                    filters.append({'type': 'genre', 'query': query})
                elif option == '2':
                    query = input("Enter Director: ").strip().lower()
                    filters.append({'type': 'director', 'query': query})
                elif option == '3':
                    query = input("Enter Actor: ").strip().lower()
                    filters.append({'type': 'actor', 'query': query})
                elif option == '4':
                    min_length = input("Enter Minimum Length or leave blank: ").strip()
                    min_length = int(min_length) if min_length else None
                    max_length = input("Enter Maximum Length or leave blank: ").strip()
                    max_length = int(max_length) if max_length else None
                    filters.append({'type': 'length', 'min_length': min_length, 'max_length': max_length})
                else:
                    print(f"Invalid option: {option}")
            results = filter_movies(filters, movies)
            if len(results) == 0:
                print("\n-No movies found matching your criteria. Try relaxing a filter.-\n")
            else:
                print(f"\nFound {len(results)} match(es):")
                display_movies(results)
        elif continue_or_exit == "l":
            #if they want to see the movie list, display it
            display_movies(movies)
        elif continue_or_exit == "e":
            #if they want to exit, break the loop
            break
        else:
            #if they have a typo, tell them and repeat the loop
            print("That is not an option.")
main()