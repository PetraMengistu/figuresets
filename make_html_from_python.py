import os
html_content = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="carousel.css">
</head>
<div>
  <div class="carousel">
    <ul class="slides">
"""

# ending
html_end = """
    </ul>
</div>
</html>
"""
# portion to iterate over
def iter_image(index, fname):
    l1 = f'     <input type="radio" name="radio-buttons" id="img-{index}" checked />\n'
    doc1 ="""
            <li class="slide-container">
                <div class="slide-image">
        """
    l2 = f'             <img src="{fname}">\n'
    doc2= """  
                </div>
                <div class="carousel-controls">
                """
    doc3 = """
                        <span>&lsaquo;</span>
                    </label>
        """
    l3 = f'                <label for="img-{index-1}" class="prev-slide">\n'
    l4 = f'                <label for="img-{index+1}" class="next-slide">\n'
    doc4 = """
                        <span>&rsaquo;</span>
                    </label>
                </div>
        </li>
    """
    if i not in [0,90]:
        return l1+doc1+l2+doc2+l3+doc3+l4+doc4
    elif i==0:
        l3_alt = f'                <label for="img-90" class="prev-slide">\n'
        return l1+doc1+l2+doc2+l3_alt+doc3+l4+doc4
    else:
        l4_alt = f'                <label for="img-0" class="next-slide">\n'
        return l1+doc1+l2+doc2+l3+doc3+l4_alt+doc4
figuresets_fpath = os.listdir('nirspec_dr4')
body_html = """"""
for i,f in enumerate(figuresets_fpath):
    body_html += iter_image(i, f'nirspec_dr4/{f}')
full_html = html_content + body_html + html_end
print(full_html)
with open("nirspec_dr4_figuresets.html", "w") as f:
    f.write(full_html)