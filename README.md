# spotify_likes_analyzer
Hello, 
this program displays and visualizes the average musical properties of your Spotify likes.

At the end the program shows you the number and the average tempo of your favorite songs on Spotify.
A radar graph is also displayed, which contains the following average properties of your favorite songs:
  - danceability
  - energy 
  - loudness 
  - speechiness 
  - acousticness 
  - instrumentalness 
  - liveness 
  - valence
  
For security reasons I have removed my Spotify username and API tokens from the program. The following steps are necessary to start the program:
  - Add your username to the Main.py (token = create_token('USERNAME', 'user-library-read'))
  - Register your application at https://developer.spotify.com/dashboard/applications
  - Add your Client_ID to the UtilClass.py (client_id = 'YOUR_CLIENT_ID')
  - Add your Client_Secret to the UtilClass.py (client_secret='YOUR_CLIENT_SECRET')
  - Add your Redirect_URI to the UtilClass.py (redirect_uri='YOUR_REDIRECT_URI')
  - Run the Main.py
    
Have fun!
