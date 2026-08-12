import re

def process():
    with open('work/index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # We will split the HTML by cards
    cards = html.split('<div class="card"')
    new_cards = [cards[0]]
    
    for card_content in cards[1:]:
        card = '<div class="card"' + card_content
        
        # find the image container
        img_marker = '<div style="aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">'
        if img_marker in card:
            # find the URL
            btn_match = re.search(r'<a class="btn.*?href="([^"]+)"', card)
            if btn_match:
                url = btn_match.group(1)
                
                # construct the new container
                new_marker = f'<a href="{url}" style="display: block; aspect-ratio: 16/9; width: 100%; overflow: hidden; border-bottom: 1px solid rgba(255,255,255,0.04); position: relative;">'
                
                # replace marker
                card = card.replace(img_marker, new_marker, 1)
                
                # replace closing div of the image container with closing a
                # The image container looks like:
                # <div ...>
                #   <img ... />
                # </div>
                # We need to find the </div> after the <img> tag
                
                # Let's use a regex to replace the specific block
                pattern = re.compile(re.escape(new_marker) + r'(.*?)</div>', re.DOTALL)
                
                card = pattern.sub(lambda m: new_marker + m.group(1) + '</a>', card, count=1)
                
        new_cards.append(card)
        
    new_html = "".join(new_cards)
    with open('work/index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    print("Done")

if __name__ == '__main__':
    process()
