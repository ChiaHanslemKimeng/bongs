import os
import urllib.request

images = {
    'hero1.jpg': 'https://images.unsplash.com/photo-1579998188177-3363e72dc779?auto=format&fit=crop&q=80&w=800',
    'hero2.jpg': 'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?auto=format&fit=crop&q=80&w=800',
    'hero3.jpg': 'https://images.unsplash.com/photo-1600216676332-94ea40fbfba8?auto=format&fit=crop&q=80&w=800',
    'hero4.jpg': 'https://images.unsplash.com/photo-1582230303102-18151f15dbbc?auto=format&fit=crop&q=80&w=800',
    'cat1.jpg': 'https://images.unsplash.com/photo-1584916201218-f4242ceb4809?auto=format&fit=crop&q=80&w=800',
    'cat2.jpg': 'https://images.unsplash.com/photo-1597075687490-8f673c6c17f6?auto=format&fit=crop&q=80&w=800',
    'cat3.jpg': 'https://images.unsplash.com/photo-1544144433-d50aff500b91?auto=format&fit=crop&q=80&w=800',
    'story.jpg': 'https://images.unsplash.com/photo-1505075955904-b5546f047714?auto=format&fit=crop&q=80&w=800',
    'about_hero.jpg': 'https://images.unsplash.com/photo-1534045582305-654e954e7d95?auto=format&fit=crop&q=80&w=1920',
    'about_detail.jpg': 'https://images.unsplash.com/photo-1506544777-62ccb7ee11cc?auto=format&fit=crop&q=80&w=1200'
}

os.makedirs('static/images', exist_ok=True)

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
urllib.request.install_opener(opener)

for filename, url in images.items():
    path = os.path.join('static/images', filename)
    print(f"Downloading {filename}...")
    try:
        urllib.request.urlretrieve(url, path)
    except Exception as e:
        print(f"Failed to download {filename}: {e}")
print("Done.")
