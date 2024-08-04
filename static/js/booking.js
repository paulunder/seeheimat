document.addEventListener('DOMContentLoaded', function() {
    const timeSlotButtons = document.querySelectorAll('.btn-slot');
    const hiddenInput = document.getElementById('selected-time-slot');

    timeSlotButtons.forEach(button => {
        button.addEventListener('click', function() {
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
