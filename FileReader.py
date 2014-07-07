from collections import Counter
import operator
class TakeData:
    def read_from_movie_file(self):
        file_object = open('movie.data', 'r')
        movie_data = {}
        for line in file_object:
            movie_temp = {}
            #genreList =[]
            words = line.split("|")
            movie_temp={"movieId":words[0],
                       "movieName":words[1],
                       "releaseYear":words[2],
                       "url":words[4],
                       }
            movie_data[words[0]]=movie_temp
            #print movieData
        file_object.close()
        return movie_data
    
    def read_from_user_file(self):
        file_object = open('user.data', 'r')
        user_data = {}
        for line in file_object:
            user_temp = {}
            words = line.split("|")
            user_temp={"userId":words[0],
                      "userAge":words[1],
                      "userJob":words[2]
                      }
            user_data[words[0]]=user_temp
            #print userData
        file_object.close()
        return user_data
    
    def read_from_rating_file(self):
        file_object = open('ratings.data', 'r')
        rating_list = []
        for line in file_object:
            words = line.split("\t")
            rating_list.append(words[1])
            #print ratingList
        file_object.close()
        return rating_list
    
    def most_watched_movie(self,rating_list,movie_data):
        cnt = Counter()
        for movie in rating_list:
            cnt[movie] += 1
        print "Highest watched movies : "
        print movie_data.__getitem__(max(cnt.iteritems(), key=operator.itemgetter(1))[0])
        
         
if __name__ == "__main__":
    s=TakeData()
    movie_data = s.read_from_movie_file()
    user_data = s.read_from_user_file()
    #print movie_data
    rating_list = s.read_from_rating_file()
    #print ratingList
    s.most_watched_movie(rating_list,movie_data)