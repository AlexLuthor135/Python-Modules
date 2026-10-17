from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for element in light_spell_allowed_ingredients():
        if element in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
