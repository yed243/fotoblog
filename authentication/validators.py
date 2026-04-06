from django.core.exceptions import ValidationError

class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(c.isalpha() for c in password):
            raise ValidationError(
                "Le mot de passe doit contenir au moins une lettre.",
                code='password_no_letter',
            )

    def get_help_text(self):
        return "Votre mot de passe doit contenir au moins une lettre."

class ContainsDigitValidator:
    def validate(self, password, user=None):
        if not any(c.isdigit() for c in password):
            raise ValidationError(
                "Le mot de passe doit contenir au moins un chiffre.",
                code='password_no_digit',
            )

    def get_help_text(self):
        return "Votre mot de passe doit contenir au moins un chiffre."