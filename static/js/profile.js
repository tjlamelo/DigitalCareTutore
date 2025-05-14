document.addEventListener('DOMContentLoaded', function() {
    // Add Bootstrap classes to all form elements
    function bootstrapifyForm() {
        const inputs = document.querySelectorAll('input:not([type="submit"]):not([type="button"]), select, textarea');
        inputs.forEach(input => {
            if (input.tagName === 'SELECT') {
                input.classList.add('form-select');
            } else if (input.type === 'file') {
                input.classList.add('form-control');
            } else {
                input.classList.add('form-control');
            }
        });

        // Special handling for textareas
        const textareas = document.querySelectorAll('textarea');
        textareas.forEach(textarea => {
            textarea.classList.add('form-control');
            textarea.style.minHeight = '100px';
        });
    }

    // Initialize form validation
    function initFormValidation() {
        const forms = document.querySelectorAll('.needs-validation');
        Array.from(forms).forEach(form => {
            form.addEventListener('submit', event => {
                if (!form.checkValidity()) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }

    // Preview profile picture
    function initImagePreview() {
        const fileInput = document.querySelector('input[type="file"]');
        if (fileInput) {
            fileInput.addEventListener('change', function(e) {
                const file = e.target.files[0];
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(event) {
                        const preview = document.getElementById('profile-picture-preview');
                        if (!preview) {
                            const div = document.createElement('div');
                            div.id = 'profile-picture-preview';
                            div.style.marginTop = '10px';
                            div.innerHTML = `<img src="${event.target.result}" class="img-thumbnail" style="max-width: 200px; max-height: 200px;">`;
                            fileInput.parentNode.appendChild(div);
                        } else {
                            preview.innerHTML = `<img src="${event.target.result}" class="img-thumbnail" style="max-width: 200px; max-height: 200px;">`;
                        }
                    }
                    reader.readAsDataURL(file);
                }
            });
        }
    }

    // Initialize all functions
    bootstrapifyForm();
    initFormValidation();
    initImagePreview();
});