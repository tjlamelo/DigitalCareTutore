document.addEventListener('DOMContentLoaded', function() {
    // Initialize form validation
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        }, false);
    });

    // Password strength indicator
    const passwordInput = document.getElementById('id_password1');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const strengthIndicator = document.getElementById('password-strength');
            if (strengthIndicator) {
                const strength = checkPasswordStrength(this.value);
                strengthIndicator.textContent = strength.message;
                strengthIndicator.className = 'password-strength ' + strength.class;
            }
        });
    }

    // Password match verification
    const passwordConfirm = document.getElementById('id_password2');
    if (passwordConfirm) {
        passwordConfirm.addEventListener('input', function() {
            const matchIndicator = document.getElementById('password-match');
            if (matchIndicator && passwordInput) {
                if (this.value === passwordInput.value) {
                    matchIndicator.textContent = 'Passwords match';
                    matchIndicator.className = 'password-match text-success';
                } else {
                    matchIndicator.textContent = 'Passwords do not match';
                    matchIndicator.className = 'password-match text-danger';
                }
            }
        });
    }

    // Helper function for password strength
    function checkPasswordStrength(password) {
        const strongRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})/;
        const mediumRegex = /^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})/;
        
        if (strongRegex.test(password)) {
            return { message: 'Strong password', class: 'text-success' };
        } else if (mediumRegex.test(password)) {
            return { message: 'Medium strength password', class: 'text-warning' };
        } else {
            return { message: 'Weak password', class: 'text-danger' };
        }
    }

    // Apply Bootstrap classes to form elements
    function bootstrapifyForm() {
        const inputs = document.querySelectorAll('input, select, textarea');
        inputs.forEach(input => {
            if (input.type !== 'submit' && input.type !== 'checkbox') {
                input.classList.add('form-control');
            }
        });
    }
    
    bootstrapifyForm();
});