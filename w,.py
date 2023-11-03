a= """<iframe width="868" height="488" src="https://www.youtube.com/embed/acF0HQH-223VGc" title="PASTER - YENİDƏN (Official Music Video)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>"""
b = a.find('src="')

if b != -1:

    e = a.find('"', b + 5)  
    
    if e != -1:
        src_url = a[b + 5:e]