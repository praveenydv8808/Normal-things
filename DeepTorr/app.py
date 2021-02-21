import requests
import subprocess
import sys

titleArt=r"""!!!......[Dee℘T𐍉rr]......!!!"""
print(titleArt+'\n')

def main():
    movieName=input("Enter the movie name which you want to steam: \n")
    baseUrl=f"https://api.sumanjay.cf/torrent/?query={movieName}"

    torrentResults=requests.get(baseUrl).json()
    index=1
    magnet=[]
    for result in torrentResults:
        print(index,"=)",result['name'],"-->",result['size'])
        index+=1
        magnet.append(result['magnet'])

    print("\n\n")
        
    choise=1#int(input("Enter the index no of the movie that you want to steam|download: "))
    magnetLink=magnet[choise-1]

    download=False
    streamChoice=int(input("press 1 for stream and press 2 for download the movie.\n"))
    if streamChoice ==1:
        download=False
    elif streamChoice == 2:
        download=True
    else:
        print("Invalid choise!!..\n\n...Exiting......!")
    
    handler(magnetLink,download)

def handler(magnetLink,download):
    cmd=[]
    cmd.append('webtorrent')
    cmd.append(magnetLink)
    if not download:
        cmd.append('--vlc')
    if sys.platform.startswith('win32'):
        subprocess.call(cmd,shell=True)
    elif sys.platform.startswith('linux'):
        subprocess.call(cmd)
main()
