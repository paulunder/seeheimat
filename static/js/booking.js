document.addEventListener("DOMContentLoaded", function() {
    const timeSlots = document.querySelectorAll(".time-slot");
    const selectedTimeSlotInput = document.getElementById("selected-time-slot");

    timeSlots.forEach(slot => {
        slot.addEventListener("click", function() {
            console.log("Slot clicked");
            // Remove active class from all slots
            timeSlots.forEach(s => s.classList.remove("active"));
            // Add active class to clicked slot
            this.classList.add("active");
            // Set the value of the hidden input to the selected slot
            selectedTimeSlotInput.value = this.dataset.slot;
        });
    });
});