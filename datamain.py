import pandas as pd
import numpy as np
import operator


def load():

#loading the files into movies and ratings...
	movies = pd.read_csv('./movies.csv', sep=',')
	ratings = pd.read_csv('./ratings.csv', sep=',')

#----
#initialising no of users and movies here----

	userid=list(set(list(ratings.userId)))
	movieid=list(set(list(movies.movieId)))
	num_users=len(userid)
	num_movies=len(movieid)//10
	
#--- constructing a bipartitegraph with dimensions (num_users* num_movies) 

	bipartiteGraph = np.zeros((num_users, num_movies))


#----filling that values in matrix for all users who have watched particular movie with its movieID



	for name, group in ratings.groupby(["userId", "movieId"]):
		user_id, movie_id = name
		if(user_id<=num_users and movie_id<=num_movies):
			user_index = userid.index(user_id)
			movie_index = movieid.index(movie_id)
			bipartiteGraph[user_index, movie_index] = 1

#--- Asking user to enter the userID in order to search its recommended movies---


	print("Enter the userId to be searched")
	a=int(raw_input())
	if(a<=num_users):

#---generating a list of genres, movie IDs, Ratings and also Titles---

		Genres=list(movies.genres)
		ID=list(movies.movieId)
		Title=list(movies.title)
		Rate=list(ratings.rating)
		gen_dict={}
		gen_count={}
		c=0
		for i in range(num_movies):
#---checking if a movie has beeen watched by the above requested user??----

			if(bipartiteGraph[a][i]==1):
				# c=c+1
				B=list(Genres[i].split("|"))
				for j in range(len(B)):
# -------generating a dict of generes watched by a user
#---------generating a count of ratings given by a user for a particular genre

					if(B[j] in gen_dict.keys() and B[j] in gen_count.keys()):
						gen_dict[B[j]]=gen_dict[B[j]]+1
						gen_count[B[j]]=gen_count[B[j]]+Rate[i]
					else:
						gen_dict[B[j]]=1
						gen_count[B[j]]=Rate[i]
		
		k1=list(gen_dict.keys())

#----selecting out the top 5 most viewed genres and recommending the movies which are not yet watched by the user ----
		for i in k1:
			gen_count[i]=gen_dict[i]/gen_count[i]
		# print(gen_count)

		sorted_x = sorted(gen_count.items(), key=operator.itemgetter(1))
		if(len(sorted_x)>=5):
			A1=sorted_x[-1][0]
			A2=sorted_x[-2][0]
			A3=sorted_x[-3][0]
			A4=sorted_x[-4][0]
			A5=sorted_x[-5][0]

			d1=0
			d2=0
			d3=0
			d4=0
			d5=0

			print("Top 30 recommended movies are :")
			print("")



			for k in range(len(Title)):
				if(A1 in Genres[k] and d1<=6 and bipartiteGraph[a][k]!=1):
					print(Title[k])
					d1=d1+1
				elif(A2 in Genres[k] and d2<=6 and bipartiteGraph[a][k]!=1):
					print(Title[k])
					d2=d2+1
				elif(A3 in Genres[k] and d3<=6 and bipartiteGraph[a][k]!=1):
					print(Title[k])
					d3=d3+1
				elif(A4 in Genres[k] and d4<=6 and bipartiteGraph[a][k]!=1):
					print(Title[k])
					d4=d4+1
				elif(A5 in Genres[k] and d5<=6 and bipartiteGraph[a][k]!=1):
					print(Title[k])
					d5=d5+1

#----Program Ends

	else:

		#-----incase the user enters the userID which does not exists in the database----
		print("Sorry this userId does not exists")





if __name__ == '__main__':

	print("")

	print(" ")
	print("Do you want to create a new userId or not")
	print("y/n")

	a=str(raw_input())
	if(a=='n' or a=='N'):
		load()
	else:
		print("YEAH")





	


