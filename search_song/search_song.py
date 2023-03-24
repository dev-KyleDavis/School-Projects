# Description
print("Welcome to the music library search program.") 
print("Enter a search query to search for a music library.")
print("The music libraries are: country, rock, pop.")

# Music Libary database, maybe SQL or Cassandra
library = {
    "country": ["Thought You Should Know by Morgan Wallen", "Thank God by Kane Brown & Katelyn Brown", "The Kind of Love We Make by Luke Combs", "Tennessee Whiskey by Chris Stapleton", "etc."],
    "rock": ["Immigrant Song by Led Zeppelin", "Great Gig In The Sky by Pink Floyd", "Seven Nation Army by The White Stripes", "Angie by The Rolling Stones", "etc." ],
    "pop": ["Flowers by MILEY CYRUS", "Die For You by THE WEEKND", "Shivers. Shivers by Ed Sheeran", "UPTOWN FUNK! by Mark Ronson Feat. Bruno Mars", "etc."],
}
# Search function
def search_song(search_query):
    if search_query in library:
        print("The songs in the", search_query, "library are:")
        for song in library[search_query]:
            print(song)
    if search_query not in library:
        print("Error: The library does not contain", search_query)
    elif search_query == "":
        print("Error: Please enter a search query.") 
                        
# Main program
while True:
    search_query = input("Enter a search query: ")
    # Call the search function
    search_song(search_query)
    # Ask user if they want to search again
    search_again = input("Do you want to search again? Enter Y for Yes or N for No: ")
    if search_again.lower() == "n":
        break

# Pause program
input("Press Enter to exit...")