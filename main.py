from pytube import YouTube


print("\nWELCOME TO YOUTUBE VIDEO DOWNLOADER")
print("\n----------------------------------------------------")
print("\nTO DOWNLOAD A VIDEO PRESS 1")
print("\nTO DOWNLOAD A PLAYLIST PRESS 2")
selection=int(input("\nENTER YOUR CHOICE:"))

if(selection==1):
    url=input("ENTER THE URL OF THE VIDEO YOU WANT TO DOWNLOAD:")

    my_video=YouTube(url) 

    print("\n----------------------------------------------------")
    print("\nTHE TITLE OF THE VIDEO IS:")
    print(my_video.title)

    print("\n----------------------------------------------------")

    print("\n\nTHE LINK OF THE THUMBNAIL OF THE VIDEO:")
    print(my_video.thumbnail_url)
    print("\n----------------------------------------------------")

    print("\nIS THE VIDEO AGE RESTRICTED:")
    print(my_video.age_restricted)

    print("\n----------------------------------------------------")

    print("\nDESCRIPTION OF THE VIDEO:")
    print(my_video.description)

    print("\n----------------------------------------------------")

    print("\nLENGTH OF THE VIDEO:")
    print(my_video.length)

    print("\n----------------------------------------------------")

    print("\nAUTHOR OF THE VIDEO:")
    print(my_video.author)

    print("\n----------------------------------------------------")

    print("\nTHE VIDEO ID IS:")
    print(my_video.video_id ) 

    print("\n----------------------------------------------------")
    print("\nSELECT THE RESOLUTION OF THE VIDEO:")
    print("\nFOR HIGHEST RESOLUTION PRESS 1 ")
    print("\nFOR LOWEST RESOLUTION PRESS 2")
    print("\nTO DOWNLOAD ONLY AUDIO PRESS 3")
  
    choice=int(input("\nENTER YOUR CHOICE:"))

    if(choice==1):
      my_video=my_video.streams.get_highest_resolution()
      my_video.download()
      print("\nVIDEO DOWNLOADED SUCCESSFULLY")
    elif(choice==2):
     my_video=my_video.streams.get_lowest_resolution()
     my_video.download()
     print("\nVIDEO DOWNLOADED SUCCESSFULLY")
    elif(choice==3):
     my_video=my_video.streams.get_audio_only()
     my_video.download()
     print("\nAUDIO DOWNLOADED SUCCESSFULLY")
    else:
     print("\nINVALID CHOICE")
     
    


    
else:
    from pytube import Playlist
    videom=input("\nENTER THE URL OF THE PLAYLIST")
    playlist = Playlist(videom)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download()
    print("\nPLAYLIST SUCCESSFULLY DOWNLOADED")
