<script src="https://cdn.emailjs.com/dist/email.min.js"></script>

    // Initialize EmailJS
    emailjs.init("YOUR_USER_ID");  // Replace with your EmailJS User ID

    // Handle form submission
    document.getElementById("contact-form").addEventListener("submit", function(event) {
        event.preventDefault();  // Prevent the default form submission

        const formData = new FormData(this);

        // Send email using EmailJS
        emailjs.sendForm("YOUR_SERVICE_ID", "YOUR_TEMPLATE_ID", formData)
            .then(function(response) {
                console.log("Success:", response);
                // Show success message
                document.getElementById("success-message").classList.remove("hidden");
                // Optionally clear form fields
                document.getElementById("contact-form").reset();
            }, function(error) {
                console.error("Error:", error);
            });
    });

