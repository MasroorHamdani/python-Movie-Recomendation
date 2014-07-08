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
                       "rating":''
                       }
            movie_data[words[0]]=movie_temp
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
        file_object.close()
        return user_data
 
    
    def read_from_rating_file(self):
        file_object = open('ratings.data', 'r')
        user_list = []
        movie_rating_list={}
        movie_list = []
        for line in file_object:
            words = line.split("\t")
            user_list.append(words[0])
            movie_list.append(words[1])
            temp_list ={
                        "movie_id":words[1],
                        "user_id":words[0],
                        "rating":words[2]
                       }
            movie_rating_list[words[1]]=temp_list
        file_object.close()
        return movie_list,user_list,movie_rating_list
    
    
    def most_watched_movie(self,movie_list,movie_data):
        cnt = Counter()
        for movie in movie_list:
            cnt[movie] += 1
        print "Highest watched movies : "
        print movie_data.__getitem__(max(cnt.iteritems(), key=operator.itemgetter(1))[0])
        
        
    def most_active_user(self,user_list,user_data):
        cnt = Counter()
        for user in user_list:
            cnt[user] += 1
        print "Most Active User : "
        print user_data.__getitem__(max(cnt.iteritems(), key=operator.itemgetter(1))[0])

      
    def find_rating(self,movie_rating_list,movie_data):
        count=0
        rating=0
        list = {}
        for movie in movie_data:
            if movie_data.get(movie)["movieId"] in movie_rating_list:
                count=count+1
                rating=rating + int(movie_rating_list.__getitem__(movie_data.get(movie)["movieId"])["rating"])
                avg = rating/count
            movie_data.get(movie)["rating"] = avg
            list[movie_data.get(movie)["movieId"]] = avg
            return list
  
                
    def top_movie_by_year(self,movie_data,find_by_year):
        print find_by_year
        for key in movie_data:
            full_year = movie_data.get(key)["releaseYear"]
            date = full_year.split("-")
            if date[2]:
                year =date[2]
                
     
    def most_rated_movie(self,movie_data,rating_list):
        return movie_data.get(max(rating_list))
        
        
if __name__ == "__main__":
    s=TakeData()
    movie_data = s.read_from_movie_file()
    user_data = s.read_from_user_file()
    movie_list , user_list , movie_rating_list= s.read_from_rating_file()
    s.most_watched_movie(movie_list,movie_data)
    s.most_active_user(user_list,user_data)
    rating_list = s.find_rating(movie_rating_list,movie_data)
    most_rated_movie = s.most_rated_movie(movie_data,rating_list)
    print "most rated movie"
    print most_rated_movie
    #print "Enter movie Year"
    #year = raw_input()
    #s.top_movie_by_year(movie_data,year)