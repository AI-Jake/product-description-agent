"""
Product Description Agent V1 MVP
Generates Polish product descriptions for Allegro

MANUAL WORKFLOW (Using Claude Pro):
1. Run this script to generate the prompt
2. Copy the prompt
3. Paste into Claude.ai
4. Copy Claude's response
5. Paste back here for formatting
6. Deliver to client

NO API needed for V1!
"""

import sys
from prompts import get_allegro_prompt, validate_output


def print_separator(char="=", length=60):
    """Print a visual separator"""
    print(char * length)


def get_product_info():
    """
    Collect product information from user
    
    Returns:
        dict: Product information
    """
    print("\n🛒 GENERATOR OPISÓW PRODUKTÓW - ALLEGRO")
    print_separator()
    
    print("\n📝 Wprowadź informacje o produkcie:\n")
    
    # Product name
    product_name = input("Nazwa produktu: ").strip()
    if not product_name:
        print("❌ Nazwa produktu jest wymagana!")
        sys.exit(1)
    
    # Features
    print("\n✨ Cechy produktu (wpisz po kolei, Enter po każdej, pusta linia = koniec):")
    features = []
    i = 1
    while True:
        feature = input(f"  {i}. ").strip()
        if not feature:
            break
        features.append(feature)
        i += 1
    
    if not features:
        print("❌ Musisz podać przynajmniej jedną cechę!")
        sys.exit(1)
    
    # Target audience (optional)
    print("\n👥 Grupa docelowa (opcjonalnie, Enter aby pominąć):")
    target_audience = input("  ").strip()
    
    return {
        "product_name": product_name,
        "features": features,
        "target_audience": target_audience
    }


def save_to_file(content, filename="opis_produktu.txt"):
    """Save the generated description to a file"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\n💾 Zapisano do pliku: {filename}")
        return True
    except Exception as e:
        print(f"\n❌ Błąd zapisu: {e}")
        return False


def main():
    """Main workflow"""
    
    print("\n" + "🚀" * 30)
    print("   PRODUCT DESCRIPTION AGENT V1 MVP")
    print("   Opisy produktów dla Allegro - Polski")
    print("🚀" * 30)
    
    # Step 1: Collect product info
    product_info = get_product_info()
    
    # Step 2: Generate prompt
    print("\n" + "=" * 60)
    print("📋 KROK 1: GENEROWANIE PROMPTU")
    print("=" * 60)
    
    prompt = get_allegro_prompt(
        product_name=product_info["product_name"],
        features=product_info["features"],
        target_audience=product_info["target_audience"]
    )
    
    # Step 3: Show prompt for user to copy
    print("\n✅ Prompt wygenerowany!\n")
    print("=" * 60)
    print("📋 SKOPIUJ TEN PROMPT I WKLEJ DO CLAUDE.AI:")
    print("=" * 60)
    print()
    print(prompt)
    print()
    print("=" * 60)
    
    # Step 4: Wait for user to paste Claude's response
    print("\n📥 KROK 2: WKLEJ ODPOWIEDŹ Z CLAUDE.AI")
    print("=" * 60)
    print("\n(Skopiuj całą odpowiedź Claude i wklej poniżej)")
    print("(Wpisz 'KONIEC' w nowej linii i naciśnij Enter)\n")
    
    # Collect multi-line input
    lines = []
    print("Wklej odpowiedź (KONIEC aby zakończyć):")
    while True:
        try:
            line = input()
            if line.strip().upper() == "KONIEC":
                break
            lines.append(line)
        except EOFError:
            break
    
    if not lines:
        print("\n❌ Nie wklejono żadnej odpowiedzi!")
        return
    
    claude_response = "\n".join(lines)
    
    # Step 5: Parse and format output
    print("\n" + "=" * 60)
    print("📝 KROK 3: FORMATOWANIE WYNIKU")
    print("=" * 60)
    
    # Try to extract sections from Claude's response
    formatted_output = format_output(claude_response)
    
    # Display formatted result
    print("\n✅ GOTOWY OPIS PRODUKTU:")
    print("=" * 60)
    print(formatted_output)
    print("=" * 60)
    
    # Step 6: Save to file
    save_choice = input("\n💾 Zapisać do pliku? (t/n): ").strip().lower()
    if save_choice == 't':
        filename = input("Nazwa pliku (Enter = opis_produktu.txt): ").strip()
        if not filename:
            filename = "opis_produktu.txt"
        if not filename.endswith('.txt'):
            filename += '.txt'
        save_to_file(formatted_output, filename)
    
    print("\n✅ Gotowe! Możesz teraz skopiować opis i wkleić na Allegro.")
    print("\n💡 TIP: Ten opis możesz edytować przed wklejeniem na Allegro.\n")


def format_output(text):
    """
    Format Claude's response for easy copy-paste
    
    Args:
        text: Raw text from Claude
    
    Returns:
        Formatted text ready for Allegro
    """
    # For now, just return cleaned text
    # You can add more sophisticated parsing later
    
    formatted = text.strip()
    
    # Add some visual improvements
    formatted = "\n" + formatted + "\n"
    
    return formatted


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Przerwano przez użytkownika.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Wystąpił błąd: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)