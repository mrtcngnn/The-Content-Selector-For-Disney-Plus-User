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