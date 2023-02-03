from watch import convert_html_link

def test_1():
    assert convert_html_link('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_2():
    assert convert_html_link('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_3():
    assert convert_html_link('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == 'https://youtu.be/xvFZjo5PgG0'

def test_4():
    assert convert_html_link('<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == 'https://youtu.be/xvFZjo5PgG0'