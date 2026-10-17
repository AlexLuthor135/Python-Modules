from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for element in dark_spell_allowed_ingredients():
        if element in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
