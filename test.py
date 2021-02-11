import os
print("Current WD: " + os.getcwd())

def loadMovieNames():
    movieNames = {}
#    with open("movies.dat") as f:
    with open("C:\\SparkCourse\\movies.dat") as f:
        for line in f:
            fields = line.split("::")
            movieNames[int(fields[0])] = fields[1]
    return movieNames

movies = loadMovieNames()
print(movies[0])