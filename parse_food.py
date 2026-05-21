text = """
| Alimento              | Carboidratos | Proteínas | Gorduras |
| --------------------- | -----------: | --------: | -------: |
| Arroz branco cozido   |        28.1g |      2.5g |     0.2g |
| Arroz integral cozido |        25.8g |      2.6g |     1.0g |
| Feijão carioca cozido |        13.6g |      4.8g |     0.5g |
| Feijão preto cozido   |          14g |      4.5g |     0.5g |
| Lentilha cozida       |        16.3g |      6.3g |     0.5g |
| Grão-de-bico cozido   |        22.5g |      6.7g |     2.1g |
| Aveia em flocos       |        66.6g |     13.9g |     8.5g |
| Quinoa cozida         |        21.3g |      4.4g |     1.9g |
| Milho verde cozido    |        18.7g |      3.4g |     1.4g |
| Tapioca               |        87.5g |      0.3g |     0.2g |
| Macarrão cozido       |          25g |        5g |     1.1g |
| Pão branco            |          49g |      9.4g |     3.2g |
| Pão integral          |        39.9g |      7.6g |       3g |
| Batata inglesa cozida |        11.9g |      1.2g |       0g |
| Batata-doce cozida    |        18.4g |      0.6g |     0.1g |
| Mandioca cozida       |          30g |        1g |     0.3g |
| Inhame cozido         |          28g |      1.5g |     0.2g |
| Cuscuz                |          25g |        2g |     0.7g |
| Farinha de mandioca   |          80g |      1.5g |     0.3g |
| Pipoca                |        70.3g |      9.9g |    15.9g |
| Peito de frango grelhado |           0g |       32g |     2.5g |
| Coxa de frango           |           0g |       26g |      10g |
| Carne bovina magra       |           0g |     32.4g |    15.5g |
| Patinho                  |           0g |       35g |       6g |
| Carne moída              |           0g |       26g |      15g |
| Porco                    |           0g |       27g |      14g |
| Salmão                   |           0g |     20.4g |    13.4g |
| Tilápia                  |           0g |       26g |     2.7g |
| Atum                     |           0g |       29g |       1g |
| Sardinha                 |           0g |       25g |      11g |
| Camarão                  |           0g |       20g |     1.7g |
| Ovo cozido               |         0.6g |     13.3g |     9.5g |
| Clara de ovo             |         0.7g |       11g |     0.2g |
| Tofu                     |         2.1g |      6.6g |       4g |
| Soja cozida              |          10g |       12g |       6g |
| Leite integral           |           5g |      3.2g |     3.3g |
| Leite desnatado          |           5g |      3.4g |     0.2g |
| Iogurte natural integral |         1.9g |      4.1g |       3g |
| Iogurte desnatado        |         5.8g |      3.8g |     0.3g |
| Queijo muçarela          |           3g |     22.6g |    25.2g |
| Ricota                   |         3.8g |     12.6g |     8.1g |
| Queijo cottage           |           3g |       11g |       4g |
| Whey protein (média)     |           8g |       75g |       6g |
| Banana   |       24.5g |    1.15g | 0.2g |
| Maçã     |       14g |      0.3g |     0.2g |
| Laranja  |         8.9g |        1g |     0.1g |
| Mamão    |          11g |      0.5g |     0.1g |
| Manga    |          15g |      0.8g |     0.4g |
| Melancia |           8g |      0.6g |     0.2g |
| Uva      |          18g |      0.7g |     0.2g |
| Abacaxi  |          13g |      0.5g |     0.1g |
| Morango  |         7.7g |      0.7g |     0.3g |
| Abacate  |         7.5g |      1.5g |    11.5g |
| Amendoim          |          16g |       26g |      49g |
| Pasta de amendoim |          20g |       25g |      50g |
| Castanha de caju  |          30g |       18g |      44g |
| Castanha-do-pará  |          12g |       14g |      66g |
| Amêndoas          |          21g |       21g |      50g |
| Chia              |          42g |       17g |      31g |
| Linhaça           |          29g |       18g |      42g |
| Azeite            |           0g |        0g |     100g |
| Manteiga          |           0g |        1g |      81g |
"""

import re
import json

lines = [l.strip() for l in text.splitlines() if l.strip() and l.startswith('|') and 'Alimento' not in l and '---' not in l]
output = []
for line in lines:
    parts = [p.strip() for p in line.split('|')[1:-1]]
    if len(parts) == 4:
        name = parts[0]
        c = float(re.sub(r'[^0-9.]', '', parts[1]))
        p = float(re.sub(r'[^0-9.]', '', parts[2]))
        g = float(re.sub(r'[^0-9.]', '', parts[3]))
        kcal = (p*4) + (c*4) + (g*9)
        p_g = round(p / 100, 3)
        c_g = round(c / 100, 3)
        g_g = round(g / 100, 3)
        kcal_g = round(kcal / 100, 3)
        keys = []
        name_clean = re.sub(r'\\(.*\\)|cozido|cozida|grelhado|integral|desnatado|natural|média|branca|verde|doce|carioca|preto', '', name, flags=re.I).strip().lower()
        name_clean = ' '.join(name_clean.split())
        keys.append(name.lower())
        if name_clean and name_clean not in keys:
            keys.append(name_clean)
        
        unit = 'g'
        if 'leite' in name.lower() or 'azeite' in name.lower():
            unit = 'ml'
        elif 'ovo' in name.lower() or 'pão' in name.lower() or 'banana' in name.lower() or 'maçã' in name.lower() or 'laranja' in name.lower():
            unit = 'un'
        
        keys_str = ','.join(f"'{k}'" for k in keys)
        output.append(f"  {{keys:[{keys_str}], unit:'{unit}', p:{p_g}, c:{c_g}, g:{g_g}, kcal:{kcal_g}}},")

with open('food_parsed.txt', 'w', encoding='utf-8') as f:
    f.write('const foodDb=[\n' + '\n'.join(output) + '\n];')
