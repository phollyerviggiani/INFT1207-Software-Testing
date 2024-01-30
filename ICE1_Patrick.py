# INFT1207 Software Testing and Automation
# ICE1 Python Review
# Patrick Hollyer-Viggiani 100910706
# Description: A program that enables the user to add a new movie and its budget to a list, then compares its budget to the list, and calcuates the average

# List containing movies names and movie budget
movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

count_over_avg = 0
# Taking input for how many movies have been added
new_movie_num = int(input("Enter how many new movies you wish to add: "))
# Looping the amount of times the user inputed above
for i in range(new_movie_num):
    new_movie_name = input("Enter new movie name: ")
    new_movie_budget = int(input("Enter new movie budget: "))
    movies.append((new_movie_name, new_movie_budget))
    print("Movie has been added.")

# Calculating the budget increase, calculating the average by dividing total budget of all movies by new length
total_budget = sum([movies[1] for movies in movies])
average_budget = total_budget / len(movies)
print(f"The average budget for the movies is {average_budget}")

# Checking the over avg budget movies, and displaying them
for movie in movies:
    if movie[1] > average_budget:
        differences = movie[1] - average_budget
        print(f"{movie[0]} costed {movie[1]}, and was {differences:.2f} over budget")
        count_over_avg += 1

print(f" There were {count_over_avg} movies over average.")
