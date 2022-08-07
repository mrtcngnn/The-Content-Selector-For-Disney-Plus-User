class ContentSelector:

    def __init__(self):
        pass

    def get_unique(self, data, col):    #For cast => Calculate that how many different Tv shows or movies that an actor acts on it
        output = {}
        for x in data[col]:
            keys = x.split(',') #list of actors like (John, Alex, Tom)
            for y in keys:
                y = y.strip()   #remove useless spaces
                if y not in output: #never seen before in any movie/TV show, add to list and start to increase counter when it arrives again
                    output[y] = 1
                else:
                    output[y] += 1  #it was already in output, increase the counter of it
        return output

    def clean_text(self, str):         #To create meta data soup, we create full text, without space just with ","
        s = str.replace(" ","")
        s = s.lower()
        return s

    def create_metadata_soup(self, X):   #to create metadata soup
        s = X['cast'] + ' ' + X['genre'] + ' ' + X['description']
        return s

    def get_recommendations_new(self, data, indices, title, cosine_sim):
        tmp = title
        title = title.replace(' ','').lower()
        idx = indices[title]

        # Get the pairwsie similarity scores of all movies with that movie
        sim_scores = list(enumerate(cosine_sim[idx]))

        # Sort the movies based on the similarity scores
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies
        sim_scores = sim_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sim_scores]
        print("Your Content:", tmp)
        # Return the top 10 most similar movies
        return data['title'].iloc[movie_indices], sim_scores