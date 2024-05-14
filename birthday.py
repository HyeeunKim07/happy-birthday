from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def letter(request):
    letter_content = "사랑하는 동생에게,\n\n생일 축하해! 항상 행복하길 바라며 이 작은 선물을 준비했어. 사랑해!"
    return render(request, 'letter.html', {'letter_content': letter_content})

def photos(request):
    photos_list = ['photo1.jpg', 'photo2.jpg', 'photo3.jpg']
    return render(request, 'photos.html', {'photos_list': photos_list})

def youtube(request):
    youtube_link = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    return render(request, 'youtube.html', {'youtube_link': youtube_link})