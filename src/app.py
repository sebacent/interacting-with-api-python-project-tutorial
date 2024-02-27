import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
# load the .env file variables
load_dotenv()
SPOTIPY_CLIENT_ID = os.environ.get("CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("TOKEN")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET,))
artist_id = 'spotify:artist:53XhwfbYqKCa1cC15pYq2q'
results = spotify.artist_top_tracks(artist_id)


tracks_df= pd.DataFrame.from_records(results['tracks'][:10])
tracks_df.sort_values(["popularity"], inplace = True)
print(tracks_df.head(5)['duration_ms'])

scatter_plot = sns.scatterplot(data = tracks_df, x = "popularity", y = "duration_ms")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")
#Como se puede ver en scatter_plot.png, no existe una relación entre la duración de la canción y la popularidad de la misma.
