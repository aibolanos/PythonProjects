#!/usr/bin/env python
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from time import sleep
import random

DEVICE_ID="98bb0735e28656bac098d927d410c3138a4b5bca"
CLIENT_ID="8af092f4a9d54e00a19f9a328acc557b"
CLIENT_SECRET="3e3abf36e2d544c98b72401ad4954245"
isShuffle = False

while True:
    try:
        reader=SimpleMFRC522()
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                       client_secret=CLIENT_SECRET,
                                                       redirect_uri="http://localhost:8080",
                                                       scope="user-read-playback-state,user-modify-playback-state"))
        
        sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
        # Will need a scan here to scan toggle shuffle card
        

        
        # create an infinite while loop that will always be waiting for a new scan
        while True:
            print("Waiting for record scan...")
            id= reader.read()[0]
            print("Card Value is:",id)
            sp.transfer_playback(device_id=DEVICE_ID, force_play=False)
            
            # DONT include the quotation marks around the card's ID value, just paste the number
            #Album: Nostalgia, Eslabon Armado
            if (id==740341055182):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:72rN7YPXX4BxMQ3nNmipAd')
                sleep(2)
                
            #Album: Demon Days, Gorillaz    
            if (id==946465930940):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:0bUTHlWbkSQysoM3VsWldT')
                sleep(2)
                
            #Album: Collide With The Sky, Peirce The Veil    
            if (id==190602018417):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:661Hz0qJK8WIp7vAWsqKvk')
                sleep(2)
                
            #Album: Blond, Frank Ocean
            if (id==396726894143):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:3mH6qwIy9crq0I9YQbOuDf')
                sleep(2)
                
            #Album: DAMN., Kendrick Lamar
            if (id==396710116924):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:4eLPsYPBmXABThSJ821sqY')
                sleep(2)

            #Album: Te Presumo, Banda El Recodo
            if (id==1):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6rIeG5N7Dr1KxvmCMigPcK')
                sleep(2)
                
            #Album: Thriller, Michael Jackson
            if (id==2):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2ANVost0y2y52ema1E9xAZ')
                sleep(2)

            #Album: haha, The Garden
            if (id==3):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:2tH1S9Q2RUcLrOizMy9I1K')
                sleep(2)

            #Album: OK Computer, Radiohead
            if (id==4):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6dVIqQ8qmQ5GBnJ9shOYGE')
                sleep(2)

            #Album: Greatest Hits, Al Green
            if (id==16):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:6W0V8B0fJItvOwC8v114rZ')
                sleep(2)

            #Album: Back to Black, Amy Winehouse
            if (id==99):
                # playing an album
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:album:097eYvf9NKjFnv4xA9s2oV')
                sleep(2)
                
            #Artist Playlist: Muse
            if (id==5):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DZ06evO0yp56w', offset={'position': random.randrange(1,50)})
                sleep(2)

            #Artist Playlist: Lana Del Rey
            if (id==6):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DX3XuY09ikg3x', offset={'position': random.randrange(1,50)})
                sleep(2)

            #Artist Playlist: Kanye
            if (id==7):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DZ06evO3nMr04', offset={'position': random.randrange(1,50)})
                sleep(2)

            #Artist Playlist: Radiohead
            if (id==8):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DZ06evO2VxlyE', offset={'position': random.randrange(1,50)})
                sleep(2)

            #Artist Playlist: SZA
            if (id==9):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DWZ8Cy8eCcjXW', offset={'position': random.randrange(1,39)})
                sleep(2)

            #Artist Playlist: Kendrick Lamar
            if (id==10):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:37i9dQZF1DX5EkyRFIV92g', offset={'position': random.randrange(1,50)})
                sleep(2)

            #Playlist: HW
            if (id==11):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:4tlueudilLNs9xjN9XEjOG', offset={'position': random.randrange(1,23)})
                sleep(2)

            #Playlist: Lo Wasted
            if (id==12):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:0mUNrqqXnYuemrIo56yM7q', offset={'position': random.randrange(1,30)})
                sleep(2)

            #Playlist: Car Crash
            if (id==13):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:6rD3QL6U40ORW7fxpEJ08Q', offset={'position': random.randrange(1,34)})
                sleep(2)

            #Playlist: Die
            if (id==14):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:6WDIJC3O6YTQw75HQcDXvS', offset={'position': random.randrange(1,132)})
                sleep(2)

            #Playlist: Comfort Movie
            if (id==15):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:2PhKJlvjbvqzYXqriktjRd', offset={'position': random.randrange(1,38)})
                sleep(2)

            #Playlist: Wolf Valley
            if (id == 98):
                # playing a playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:5jEvpP0P4TB7rJdNZTxwfW', offset={'position': random.randrange(1,41)})

            #Playlist: Money Shift
            if (id==97):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:4hLgdpfEtPmqCaHkcMsCej', offset={'position': random.randrange(1,40)})
                sleep(2)

            #Playlist: mi piel x el sol
            if (id==97):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:3Ate8aOM4PhvZUBAFKp9Yb', offset={'position': random.randrange(1,44)})
                sleep(2)

            #Playlist: need
            if (id==97):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:7ALRmpmYCMtK9YRawqFWAg', offset={'position': random.randrange(1,65)})
                sleep(2)
            

            if (id==0):
                # playing an playlist
                sp.shuffle(state=isShuffle, device_id=DEVICE_ID)
                sp.start_playback(device_id=DEVICE_ID, context_uri='spotify:playlist:3degF5XHPn0cBQ13lCXBeT', offset={'position': random.randrange(1,50)})
                sleep(2)
                
            # continue adding as many "elifs" for songs/albums that you want to play

    # if there is an error, skip it and try the code again (i.e. timeout issues, no active device error, etc)
    except Exception as e:
        print(e)
        pass

    finally:
        print("Cleaning  up...")
        GPIO.cleanup()