document.addEventListener('DOMContentLoaded', () => {
    const forms = document.querySelectorAll('form');

    forms.forEach((form) => {
        form.addEventListener('submit', (e) => {
            let isValid = true;
            const inputs = form.querySelectorAll('input[required]');

            inputs.forEach((input) => {
                const errorElement = input.nextElementSibling;

                if (!input.value.trim()) {
                    isValid = false;
                    if (errorElement) errorElement.textContent = `${input.name} is required.`;
                    input.classList.add('is-invalid');
                } else {
                    if (errorElement) errorElement.textContent = '';
                    input.classList.remove('is-invalid');
                }

                // Additional checks for specific fields
                if (input.name === 'email' && input.value.trim()) {
                    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailPattern.test(input.value)) {
                        isValid = false;
                        if (errorElement) errorElement.textContent = `Invalid email format.`;
                        input.classList.add('is-invalid');
                    }
                }

                if (input.name === 'price' && input.value.trim()) {
                    if (isNaN(input.value)) {
                        isValid = false;
                        if (errorElement) errorElement.textContent = `Price must be a number.`;
                        input.classList.add('is-invalid');
                    }
                }
            });

            if (!isValid) {
                e.preventDefault(); // Prevent form submission if validation fails
            }
        });
    });
});
