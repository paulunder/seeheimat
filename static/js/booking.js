document.addEventListener('DOMContentLoaded', function() {
    const timeSlotButtons = document.querySelectorAll('input[name="time_slot"]');
    const hiddenInput = document.querySelector('input[name="time_slot"]');

    timeSlotButtons.forEach(button => {
        button.addEventListener('change', function() {
            hiddenInput.value = button.value;
        });
    });
});
