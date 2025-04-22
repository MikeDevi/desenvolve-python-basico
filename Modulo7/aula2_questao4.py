# 04
import re
def validador_senha(senha):
    if len(senha) < 8 :
        return False
    if not re.search(r'[A-Z]', senha):
        return False
    if not re.search(r'[a-z]', senha):
        return False
    if not re.search(r'[0-9]', senha):
        return False
    if not re.search(r"[@#$%&]", senha):
        return False
    
    return True

senha01 = 'Mik@el0322'
senha02 = 'Mik@el'

print(f'A senha {senha01} é válida? {validador_senha(senha01)}')
print(f'A senha {senha02} é válida? {validador_senha(senha02)}')