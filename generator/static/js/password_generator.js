// DOM Elements
document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const passwordLengthSlider = document.getElementById('password-length');
    const lengthValue = document.getElementById('length-value');
    const generatedPasswordInput = document.getElementById('generated-password');
    const generatorResult = document.getElementById('generator-result');
    const resultPasswordText = document.getElementById('result-password-text');
    const resultCharset = document.getElementById('result-charset');
    const resultLength = document.getElementById('result-length');
    const resultStrength = document.getElementById('result-strength');
    const copyBtn = document.getElementById('copybtn');
    
    // Update length value display
    passwordLengthSlider.addEventListener('input', () => {
        lengthValue.textContent = passwordLengthSlider.value;
    });
    
    // Generate password function
    function generatePassword() {
        const passwordOptions = {
            length: parseInt(passwordLengthSlider.value),
            uppercase: document.getElementById('uppercase').checked,
            lowercase: document.getElementById('lowercase').checked,
            numbers: document.getElementById('numbers').checked,
            symbols: document.getElementById('symbols').checked,
            excludeSimilar: document.getElementById('exclude-similar').checked,
            excludeAmbiguous: document.getElementById('exclude-ambiguous').checked
        };
        
        // Validate at least one character type is selected
        if (!passwordOptions.uppercase && !passwordOptions.lowercase && 
            !passwordOptions.numbers && !passwordOptions.symbols) {
            alert('Please select at least one character type.');
            return;
        }
        
        // Call API to generate password
        fetch('/api/generate-password/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(passwordOptions)
        })
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.error || 'Failed to generate password');
                });
            }
            return response.json();
        })
        .then(data => {
            // Display the password
            generatedPasswordInput.value = data.password;
            
            // Show result section with details
            generatorResult.style.display = 'block';
            resultPasswordText.textContent = data.password;
            resultCharset.textContent = data.charset;
            resultLength.textContent = data.length;
            
            // Set strength and color
            resultStrength.textContent = data.strength.text;
            resultStrength.style.color = data.strength.color;
        })
        .catch(error => {
            console.error('Error:', error);
            alert(error.message);
        });
    }
    
    // Copy password to clipboard
    window.copyPassword = function() {
        const password = generatedPasswordInput.value;
        if (!password) return;
        
        navigator.clipboard.writeText(password).then(() => {
            const tooltip = document.getElementById("copyTooltip");
            tooltip.textContent = "Copied!";
            tooltip.classList.add("show");
            
            setTimeout(() => {
                tooltip.classList.remove("show");
                setTimeout(() => {
                    tooltip.textContent = "";
                }, 400);
            }, 2000);
        }).catch(err => {
            console.error('Failed to copy password: ', err);
            alert('Failed to copy password. Please try again.');
        });
    };
    
    // Initialize the generator with a random password on page load
    generatePassword();
    
    // Add event listener to generate button
    generateBtn.addEventListener('click', generatePassword);
});