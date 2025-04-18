import json
import random
import secrets
import string
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def homepage(request):
    """Render the homepage."""
    return render(request, 'generator/homepage.html')

def password_generator(request):
    """Render the password generator page."""
    return render(request, 'generator/password_generator.html')

@csrf_exempt
def generate_password(request):
    """API endpoint to generate a secure password."""
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST method is allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        
        # Get password parameters
        length = int(data.get('length', 16))
        use_uppercase = data.get('uppercase', True)
        use_lowercase = data.get('lowercase', True)
        use_numbers = data.get('numbers', True)
        use_symbols = data.get('symbols', True)
        exclude_similar = data.get('excludeSimilar', True)
        exclude_ambiguous = data.get('excludeAmbiguous', True)
        
        # Validate parameters
        if length < 8 or length > 32:
            return JsonResponse({'error': 'Password length must be between 8 and 32'}, status=400)
        
        if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
            return JsonResponse({'error': 'At least one character type must be selected'}, status=400)
        
        # Build character set
        charset = ""
        if use_lowercase:
            charset += string.ascii_lowercase
        if use_uppercase:
            charset += string.ascii_uppercase
        if use_numbers:
            charset += string.digits
        if use_symbols:
            charset += "!@#$%^&*()_+~`|}{[]:;?><,./-="
        
        # Handle exclusions
        if exclude_similar:
            charset = ''.join(c for c in charset if c not in "il1Lo0O")
        if exclude_ambiguous:
            charset = ''.join(c for c in charset if c not in "{}[]\\()/\\'\",;.<>")
        
        if not charset:
            return JsonResponse({'error': 'No characters available with current settings'}, status=400)
        
        # Generate password
        password = ''.join(secrets.choice(charset) for _ in range(length))
        
        # Ensure password contains at least one character from each selected type
        password_list = list(password)
        
        if use_lowercase and not any(c.islower() for c in password):
            password_list[secrets.randbelow(length)] = secrets.choice(string.ascii_lowercase)
        
        if use_uppercase and not any(c.isupper() for c in password):
            password_list[secrets.randbelow(length)] = secrets.choice(string.ascii_uppercase)
        
        if use_numbers and not any(c.isdigit() for c in password):
            password_list[secrets.randbelow(length)] = secrets.choice(string.digits)
        
        if use_symbols and not any(c in "!@#$%^&*()_+~`|}{[]:;?><,./-=" for c in password):
            password_list[secrets.randbelow(length)] = secrets.choice("!@#$%^&*()_+~`|}{[]:;?><,./-=")
        
        # Shuffle the password to ensure randomness
        random.shuffle(password_list)
        password = ''.join(password_list)
        
        # Calculate password strength
        strength = check_password_strength(password)
        
        # Get charset description
        charset_description = []
        if use_lowercase:
            charset_description.append("lowercase")
        if use_uppercase:
            charset_description.append("uppercase")
        if use_numbers:
            charset_description.append("numbers")
        if use_symbols:
            charset_description.append("symbols")
        
        return JsonResponse({
            'password': password,
            'length': len(password),
            'charset': ', '.join(charset_description),
            'strength': strength
        })
        
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def check_password_strength(password):
    """
    Check the strength of a password.
    Returns a dictionary with text and color.
    """
    strength = 0
    
    # Length check
    if len(password) < 8:
        return {'text': 'Weak', 'color': '#ff3c00'}
    elif len(password) >= 12:
        strength += 2
    else:
        strength += 1
    
    # Character type checks
    has_lowercase = any(c.islower() for c in password)
    has_uppercase = any(c.isupper() for c in password)
    has_numbers = any(c.isdigit() for c in password)
    has_symbols = any(not c.isalnum() for c in password)
    
    character_types_used = sum([has_lowercase, has_uppercase, has_numbers, has_symbols])
    
    if character_types_used >= 3:
        strength += 2
    elif character_types_used >= 2:
        strength += 1
    
    # Determine strength text and color
    if strength <= 1:
        return {'text': 'Weak', 'color': '#ff3c00'}
    elif strength <= 2:
        return {'text': 'Moderate', 'color': '#ffd700'}
    else:
        return {'text': 'Strong', 'color': '#00ff9d'}