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

    // Phone number formatting
    const phoneInput = document.getElementById('id_phone_number');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            // Remove all non-digit characters
            let phoneNumber = e.target.value.replace(/\D/g, '');
            
            
            const match = phoneNumber.match(/^(\d{0,1})(\d{0,2})(\d{0,2})(\d{0,2})$/);
            if (match) {
                phoneNumber = '';
                if (match[1]) phoneNumber += '(' + match[1];
                if (match[2]) phoneNumber += ') ' + match[2];
                if (match[3]) phoneNumber += '-' + match[3];
                if (match[4]) phoneNumber += '-' + match[4];
            }
            
            e.target.value = phoneNumber;
        });
    }

    // Add Bootstrap classes to form elements
    function bootstrapifyForm() {
        const inputs = document.querySelectorAll('input, textarea, select');
        inputs.forEach(input => {
            if (input.tagName === 'SELECT') {
                input.classList.add('form-select');
            } else if (input.type !== 'submit' && input.type !== 'button') {
                input.classList.add('form-control');
            }
        });
    }
    
    bootstrapifyForm();
});