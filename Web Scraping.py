#Nawal Othman
import pytube
print('Download video from web by python')
url = input('Enter Video URL : ')
pytube.YouTube(url).streams.get_highest_resolution().download('Desktop')






#https://www.youtube.com/watch?v=LdJbP0NbFRw