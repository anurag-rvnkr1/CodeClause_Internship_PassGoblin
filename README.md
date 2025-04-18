<div align="center">
  
# 🔒 Pass-Goblin 🔒

###  Secure Password Intelligence Generation Tool

![GitHub stars](https://img.shields.io/github/stars/anurag-rvnkr1/CodeClause_Internship_PassGoblin?style=social)
![GitHub forks](https://img.shields.io/github/forks/anurag-rvnkr1/CodeClause_Internship_PassGoblin?style=social)
![GitHub issues](https://img.shields.io/github/issues/anurag-rvnkr1/CodeClause_Internship_PassGoblin)
![GitHub license](https://img.shields.io/github/license/anurag-rvnkr1/CodeClause_Internship_PassGoblin)

</div>

<div align="center">
  <img src="https://github.com/anurag-rvnkr1/CodeClause_Internship_PassGoblin/blob/main/screenshots/demo.gif" alt="Pass-Goblin Demo" width="700px">
  <br>
  <i>✨ Modern password generation with cyberpunk aesthetics ✨</i>
</div>

## 🚀 Overview

Pass-Goblin is a slick, cyberpunk-themed Django web application designed to generate cryptographically secure passwords. With its neon green interface and smooth animations, it not only provides high-security password generation but does so with style.

> "In a world where digital security is paramount, Pass-Goblin stands as your personal cryptographic sentinel." 

## ✨ Features

- 🔐 **Cryptographically Secure**: Uses Python's `secrets` module for true randomness
- 🎛️ **Customizable Options**: 
  - Adjust password length (8-32 characters)
  - Include/exclude character sets (uppercase, lowercase, numbers, symbols)
  - Exclude similar characters (i, l, 1, L, o, 0, O)
  - Exclude ambiguous symbols ({ } [ ] ( ) / \ ' " , ; . < >)
- 📊 **Password Strength Analysis**: Visual indicator of password security
- 📋 **One-Click Copy**: Seamlessly copy passwords to clipboard
- 🔄 **Animated UI**: Sleek animations and visual feedback
- 📱 **Responsive Design**: Optimized for all devices
- 🛡️ **Security Tips**: Built-in password security recommendations

## 🖥️ Snaps:

<div align="center">
  <table>
    <tr>
      <td><b>Homepage</b></td>
      <td><b>Password Generator</b></td>
    </tr>
    <tr>
      <td><img src="https://github.com/anurag-rvnkr1/CodeClause_Internship_PassGoblin/blob/main/screenshots/landing%20page.jpg" width="350px" /></td>
      <td><img src="https://github.com/anurag-rvnkr1/CodeClause_Internship_PassGoblin/blob/main/screenshots/generator%20page.jpg" width="350px" /></td>
    </tr>
  </table>
</div>

## 🔧 Technology Stack

- **Backend**: Django 4.2.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Security**: `cryptography` library integration
- **Data Analysis**: NumPy for password entropy calculations
- **Styling**: Custom CSS with cyberpunk theme

## 📋 Requirements

- Python 3.8+
- Django 4.2.0
- cryptography
- numpy

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/anurag-rvnkr1/CodeClause_Internship_PassGoblin.git
cd CodeClause_Internship_PassGoblin
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

### 6. Access the Application

Open your browser and visit:
```
http://127.0.0.1:8000/
```

## 🧪 Password Strength Assessment Algorithm

Pass-Goblin uses a multi-factor algorithm to determine password strength:

| Factor | Weak | Moderate | Strong |
|--------|------|----------|--------|
| Length | < 8 chars | 8-11 chars | ≥ 12 chars |
| Character Types | 1 type | 2 types | ≥ 3 types |
| Entropy Bits | < 40 bits | 40-60 bits | > 60 bits |

```python
# Password strength calculation (simplified)
def check_password_strength(password):
    strength = 0
    
    # Length check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    
    # Character diversity check
    char_types = sum([
        any(c.islower() for c in password),  # lowercase
        any(c.isupper() for c in password),  # uppercase
        any(c.isdigit() for c in password),  # digits
        any(not c.isalnum() for c in password)  # symbols
    ])
    
    if char_types >= 3:
        strength += 2
    elif char_types >= 2:
        strength += 1
    
    # Return strength assessment
    if strength <= 1:
        return {'text': 'Weak', 'color': '#ff3c00'}
    elif strength <= 2:
        return {'text': 'Moderate', 'color': '#ffd700'}
    else:
        return {'text': 'Strong', 'color': '#00ff9d'}
```

## 🔐 Security Best Practices

Pass-Goblin incorporates several security best practices:

- **Client-Server Architecture**: Passwords are generated server-side to prevent JavaScript predictability
- **CSRF Protection**: Django's built-in CSRF protection against cross-site request forgery
- **No Password Storage**: Generated passwords are never stored in a database
- **Secure Random Generation**: Uses `secrets` module instead of less secure `random` module
- **Front-End Validation**: Ensures at least one character type is selected

## 🖌️ UI/UX Features

- **Cyberpunk Theme**: Neon green on dark interface for a modern, tech feel
- **Responsive Animations**: Visual feedback for user actions
- **Custom Range Sliders**: Intuitive password length adjustment
- **Toast Notifications**: Sleek notifications for copy operations
- **Strength Indicators**: Color-coded strength assessment

## 📊 Project Structure

```
CodeClause_Internship_PassGoblin/
├── generator/                  # Main Django app
│   ├── static/                 # Static files (CSS, JS)
│   │   ├── css/
│   │   │   └── styles.css      # Cyberpunk-themed styling
│   │   └── js/
│   │       └── password_generator.js # Frontend logic
│   ├── templates/              # HTML templates
│   │   ├── base.html          # Base template
│   │   └── generator/
│   │       ├── homepage.html   # Landing page
│   │       └── password_generator.html # Generator interface
│   ├── views.py               # Backend views and API endpoints
│   ├── urls.py                # URL routing
│   └── models.py              # Database models (empty, no storage)
├── pass_gen/                  # Django project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```


### API Usage

Pass-Goblin's API endpoint can be used programmatically:

```javascript
// Example fetch request to generate a password
fetch('/api/generate-password/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        length: 16,
        uppercase: true,
        lowercase: true,
        numbers: true,
        symbols: true,
        excludeSimilar: true,
        excludeAmbiguous: true
    })
})
.then(response => response.json())
.then(data => console.log(data.password));
```

## ⚠️ Security Notice

While Pass-Goblin generates secure passwords, remember:

- Keep your Django `SECRET_KEY` private and change it in production
- Set `DEBUG = False` in production
- Use HTTPS in production to prevent password interception
- Consider adding rate limiting to prevent brute force attempts

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👏 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Cyberpunk UI inspiration](https://github.com/topics/cyberpunk-ui)
- [OWASP Password Security Guidelines](https://owasp.org/www-community/password-special-characters)

---

<div align="center">
  Made with 💚 by <a href="https://github.com/anurag-rvnkr1">Anurag Revankar</a>
  <br><br>
  <img src="https://github.com/anurag-rvnkr1/CodeClause_Internship_PassGoblin/blob/main/generator/static/img/footer.png" width="300px">
  <br>
</div>
