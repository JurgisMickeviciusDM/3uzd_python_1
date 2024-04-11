#Tikrinu ar vienas žodis yra kito žodžio anagrama 9 uzd 
def anagrama_ar_atitinka(zodis1, zodis2):
    """
    
    >>> anagrama_ar_atitinka("Jurgis", "Pijus")
    False
    >>> anagrama_ar_atitinka("Labas", "Asbal")
    True
    >>> anagrama_ar_atitinka("Mesti", "Nesti")
    False
    >>> anagrama_ar_atitinka("gimti", "migti")
    True
    >>> anagrama_ar_atitinka("pienas", "sapnie")
    True
    >>> anagrama_ar_atitinka("guli", "ligu")
    True
    >>> anagrama_ar_atitinka("123", "321")
    Traceback (most recent call last):
    ...
    ValueError: Tik raidinė įvestis leidžiama.
    >>> anagrama_ar_atitinka("!!!", "***")
    Traceback (most recent call last):
    ...
    ValueError: Tik raidinė įvestis leidžiama.
    
    """
#tikrinu kad raides butu ir kad anagrama 
    assert isinstance(zodis1, str) and isinstance(zodis2, str), "Turi būti simboliu eilute"
    if not all(char.isalpha() for char in zodis1.replace(" ", "")) or not all(char.isalpha() for char in zodis2.replace(" ", "")):
        raise ValueError("Tik raides")


    zodis1 = zodis1.replace(" ", "").lower()
    zodis2 = zodis2.replace(" ", "").lower()

    return sorted(zodis1) == sorted(zodis2)

 
#Dokumentacinis testas
if __name__=="__main__":
    import doctest
    doctest.testmod(verbose=True)

    
####testavimui_zodziai = [
####    ("Jurgis" , "Pijus"),
####    ("labas", "asbal"),
####    ("mesti", "nesti"),
####    ("gimti","migti"),
####    ("pienas","sapnie"),
####    ("guli", "ligu"),
####    ("123","321"),
####    ("!!!", "***")]

#Prideta....... i unitesta su subtest

####for zodis1, zodis2 in testavimui_zodziai:
####    try:
####        rezultatas = anagrama_ar_atitinka(zodis1, zodis2)
####        pranesimas = f"Ar '{zodis1}' ir '{zodis2}' yra anagrama? {rezultatas}"
####    except ValueError as e:
####        pranesimas = f"Klaida: {e}"
####    print(pranesimas)
####

#unitestas


import unittest

class TestAnagramaArAtitinka(unittest.TestCase):
    def testai(self):
        test_cases = [
            ("Labas", "Asbal", True),
            ("gimti", "migti", True),
            ("Jurgis", "Pijus", False),
            ("Mesti", "Nesti", False),
            ("Pienas", "Spnie", False),
            ("Guli", "lygu", False),
            ("Guli", "lygus", False),
            ("La bas", "aSba l", True),
            ("123", "321", ValueError),  # Klaida 
            ("!!!", "***", ValueError)    
        ]

        for zodis1, zodis2, expected in test_cases:
            with self.subTest(zodis1=zodis1, zodis2=zodis2):
                if isinstance(expected, bool):
                    self.assertEqual(anagrama_ar_atitinka(zodis1, zodis2), expected)
                else:
                    with self.assertRaises(expected):
                        anagrama_ar_atitinka(zodis1, zodis2)






####class TestAnagramaArAtitinka(unittest.TestCase):
####    def test_anagrama_tikri(self):
####        self.assertTrue(anagrama_ar_atitinka("Labas", "Asbal"))
####        self.assertTrue(anagrama_ar_atitinka("gimti", "migti"))
####    
####    def test_anagrama_netikri(self):
####        self.assertFalse(anagrama_ar_atitinka("Jurgis", "Pijus"))
####        self.assertFalse(anagrama_ar_atitinka("Mesti", "Nesti"))
####        self.assertFalse(anagrama_ar_atitinka("Pienas", "Spnie"))
####        self.assertFalse(anagrama_ar_atitinka("Guli", "lygu"))
####    
####    def test_anagrama_skirtingos_ilgis(self):
####        self.assertFalse(anagrama_ar_atitinka("Guli", "lygus"))
####
####    def test_anagrama_su_tarpais_ir_didziosiomis(self):
####        self.assertTrue(anagrama_ar_atitinka("La bas", "aSba l"))
####
####    def test_neleidziami_simboliai(self):
####        with self.assertRaises(ValueError):
####            anagrama_ar_atitinka("***", "!!!")
####    
####    def test_klaida(self):
####        with self.assertRaises(ValueError):
####            anagrama_ar_atitinka("123", "321")
####



if __name__ == '__main__':
    unittest.main()
