"""
Prompts for generating Polish product descriptions for Allegro
"""

# Words to avoid (AI clichés in Polish)
BANNED_WORDS = [
    "rewolucyjny",
    "innowacyjny", 
    "wyjątkowy",
    "niezrównany",
    "najlepszy na rynku",
    "przełomowy",
    "absolutnie",
    "premium",
    "eksluzywny"
]

def get_allegro_prompt(product_name, features, target_audience=""):
    """
    Generate prompt for Allegro product description in Polish
    
    Args:
        product_name: Name of the product
        features: List of key features
        target_audience: Optional target audience description
    
    Returns:
        String with complete prompt
    """
    
    # Convert features list to string if it's a list
    if isinstance(features, list):
        features_text = "\n".join([f"- {f}" for f in features])
    else:
        features_text = features
    
    prompt = f"""
Jesteś ekspertem od pisania opisów produktów na Allegro. 
Twoim zadaniem jest napisać opis produktu w języku polskim, który SPRZEDAJE.

PRODUKT: {product_name}

CECHY PRODUKTU:
{features_text}

{f"GRUPA DOCELOWA: {target_audience}" if target_audience else ""}

WYMAGANIA DOTYCZĄCE OPISU:

1. TYTUŁ (maksymalnie 50 znaków):
   - Zwięzły i konkretny
   - Zawiera najważniejsze słowa kluczowe
   - Format: [Nazwa produktu] [kluczowa cecha] [rozmiar/kolor jeśli dotyczy]

2. OPIS (100-150 słów):
   - Zacznij od emocjonalnego hooka (pytanie lub stwierdzenie)
   - Użyj 2-3 emoji (Polacy lubią emoji na Allegro! 🔥 ✅ 📦)
   - Pisz konwersacyjnie, jak do znajomego (ale profesjonalnie)
   - Skup się na KORZYŚCIACH, nie tylko cechach
   - Dodaj konkretny przykład użycia
   - Zakończ wezwaniem do działania

3. PUNKTY (5 punktów):
   - Każdy zaczyna się od ✅ lub ✓
   - Konkretne, mierzalne korzyści
   - Krótkie (maksymalnie 1 linia)

ZAKAZANE SŁOWA (NIE UŻYWAJ):
{', '.join(BANNED_WORDS)}

WAŻNE:
- Pisz w drugim osobie (Ty/Twój)
- Używaj języka korzyści (nie "ma", ale "zapewnia Ci", "zyskujesz")
- Bądź konkretny (nie "długo trzyma", ale "24 godziny")
- Optymalizuj pod mobile (krótkie zdania, akapity)
- Ton: przyjazny ale profesjonalny

PRZYKŁADOWA STRUKTURA ODPOWIEDZI:

TYTUŁ:
[twój tytuł - max 50 znaków]

OPIS:
[twój opis 100-150 słów]

PUNKTY:
✅ [punkt 1]
✅ [punkt 2]
✅ [punkt 3]
✅ [punkt 4]
✅ [punkt 5]

SŁOWA KLUCZOWE (10 słów):
[słowo1], [słowo2], [słowo3]...

---

Napisz opis zgodnie z powyższymi wytycznymi.
"""
    
    return prompt


def validate_output(title, description, bullets):
    """
    Basic validation of generated content
    
    Returns:
        tuple: (is_valid, error_message)
    """
    errors = []
    
    # Check title length
    if len(title) > 50:
        errors.append(f"Tytuł za długi: {len(title)} znaków (max 50)")
    
    # Check description length
    word_count = len(description.split())
    if word_count < 80:
        errors.append(f"Opis za krótki: {word_count} słów (min 80)")
    elif word_count > 200:
        errors.append(f"Opis za długi: {word_count} słów (max 200)")
    
    # Check for banned words
    description_lower = description.lower()
    found_banned = [word for word in BANNED_WORDS if word in description_lower]
    if found_banned:
        errors.append(f"Znaleziono zakazane słowa: {', '.join(found_banned)}")
    
    # Check bullet points
    if len(bullets) < 5:
        errors.append(f"Za mało punktów: {len(bullets)} (potrzeba 5)")
    
    if errors:
        return False, "\n".join(errors)
    
    return True, "✅ Walidacja przeszła pomyślnie!"


# Quick test function
if __name__ == "__main__":
    # Test the prompt generation
    test_prompt = get_allegro_prompt(
        product_name="Bidon stalowy 750ml",
        features=["Izolacja termiczna 24h", "BPA Free", "Szczelny", "Szeroka nakrętka"],
        target_audience="Osoby aktywne, siłownia, outdoor"
    )
    print("PRZYKŁADOWY PROMPT:")
    print("=" * 50)
    print(test_prompt)