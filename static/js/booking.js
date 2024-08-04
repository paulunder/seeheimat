document.addEventListener('DOMContentLoaded', function() {
    const serviceField = document.getElementById('id_service');
    const dateField = document.getElementById('id_date');
    const form = document.getElementById('booking-form');
    const timeSlotButtons = document.querySelectorAll('.btn-slot');
    const hiddenInput = document.getElementById('selected-time-slot');

    serviceField.addEventListener('change', function() {
        form.submit();
    });

    dateField.addEventListener('change', function() {
        form.submit();
    });

    timeSlotButtons.forEach(button => {
        button.addEventListener('click', function() {
            console.log('Selected time slot:', button.getAttribute('data-time-slot'));
            // Reset all buttons
            timeSlotButtons.forEach(btn => btn.classList.remove('btn-success'));
            timeSlotButtons.forEach(btn => btn.classList.add('btn-primary'));

            // Set selected button
            button.classList.remove('btn-primary');
            button.classList.add('btn-success');

            // Set hidden input value
            hiddenInput.value = button.getAttribute('data-time-slot');
        });
    });
});