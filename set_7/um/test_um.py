from um import count

def test_um_in_midle():
    assert count('as i, um, walk alone') == 1

def test_zero_um():
    assert count('as i, walk alone i wonder') == 0

def test_um_in_word():
    assert count('mum... as i, walk alone i wonder') == 0

def test_um():
    assert count('um') == 1

def test_case():
    assert count('UM') == 1
