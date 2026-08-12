from bs4 import BeautifulSoup

def process():
    with open('work/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all project cards
    cards = soup.find_all('div', class_='card')
    for card in cards:
        # Find the image container
        img_container = card.find('div', style=lambda s: s and 'aspect-ratio: 16/9' in s)
        if not img_container:
            continue
            
        # Find the project URL from the buttons (View Project or similar)
        btn = card.find('a', class_='btn btn-secondary')
        if not btn:
            # Game Art cards have 'Explore Environments ->' etc
            btn = card.find('a', class_='btn')
            
        if btn and btn.has_attr('href'):
            url = btn['href']
            
            # Change the div to an a tag
            img_container.name = 'a'
            img_container['href'] = url
            # Make sure display is block
            img_container['style'] = img_container['style'].replace('position: relative;', 'position: relative; display: block;')
            
    with open('work/index.html', 'w', encoding='utf-8') as f:
        f.write(str(soup))
        
    print("Done")

if __name__ == '__main__':
    process()
