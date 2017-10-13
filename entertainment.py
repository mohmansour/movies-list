import fresh_tomatoes
import media

#each movie as a new instance of Movie Class 

avatar = media.Movie("Avatar","http://cdn01.cdn.justjared.com/wp-content/uploads/headlines/2017/03/avatar-sequel-wont-be-ready-for-2018.jpg" , "https://www.youtube.com/watch?v=-9ceBgWV8ic")

hp_P5 = media.Movie("Harry Potter & Order OF Phoenix", "http://cima4up.tv/wp-content/uploads/2017/03/Harry-Potter-and-the-Order-of-the-Phoenix-2007-309x456.jpg","https://www.youtube.com/watch?v=E9alT_nulIM")

hp_P6 = media.Movie("Harry Potter & The half Blood Prince", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQSQHqCtnmALGZVgLguB11CRDVQs2supiDeFeFXN_iLGBp2yFwNQ","https://www.youtube.com/watch?v=jpCPvHJ6p90")

the_3idiots = media.Movie("3 Idiots","https://images-na.ssl-images-amazon.com/images/I/51vBBwlFi6L._SY445_.jpg","https://www.youtube.com/watch?v=xvszmNXdM4w")

shawshank = media.Movie("Shawshank Redemption", "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_UY1200_CR88,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=6hB3S9bIaco")

boss_baby = media.Movie("Boss Baby","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZrrs6Hj9d0swlG0Qx8jD7G2Hq5Wb3psvZFWn8oPoA3rIWp3dw","https://www.youtube.com/watch?v=k397HRbTtWI")

dangal = media.Movie("Dangal","https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg","https://www.youtube.com/watch?v=91ZI3IrojMU")

khan = media.Movie("My Name is Khan","https://resizing.flixster.com/tmX6XI2nWEfBw9gJsX5jgcN0f64=/206x305/v1.bTsxMTU1ODA4MjtqOzE3NTQ4OzEyMDA7NDMyOzU3Ng","https://www.youtube.com/watch?v=_uNDm6YfN2k")

lala_land = media.Movie("Lala Land","https://images-na.ssl-images-amazon.com/images/M/MV5BMzUzNDM2NzM2MV5BMl5BanBnXkFtZTgwNTM3NTg4OTE@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=VDMf9m7FXd4")

revenant = media.Movie("Revenant","https://upload.wikimedia.org/wikipedia/en/b/b6/The_Revenant_2015_film_poster.jpg","https://www.youtube.com/watch?v=QRfj1VCg16Y")

haksaw_ridge = media.Movie("The Hacksaw Ridge","https://pbs.twimg.com/media/CvOXoqGVIAASLKo.jpg","https://www.youtube.com/watch?v=s2-1hz1juBI")

toy_story = media.Movie("Toy Story","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v-vwyZH85NQC4")

#list of instances/movies

movies = [avatar,hp_P5,hp_P6,the_3idiots,shawshank,boss_baby,dangal,khan,lala_land,revenant,haksaw_ridge,toy_story]

#send the list of movies to fresh tomatoes to show them through the HTML file

fresh_tomatoes.open_movies_page(movies)
