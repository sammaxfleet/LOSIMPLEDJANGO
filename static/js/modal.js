  // Get the button and modal elements
  const bookButton = document.getElementById("bookButton");
  const modal = document.getElementById("confirmModal");
  const confirmButton = document.getElementById("confirmButton");
  const cancelButton = document.getElementById("cancelButton");

  // When the button is clicked, show the modal
  bookButton.addEventListener("click", function() {
    modal.style.display = "block";
  });

  // When the confirm button is clicked, submit the form
  confirmButton.addEventListener("click", function() {
    // Submit the form
    document.getElementById("bookingForm").submit();
  });

  // When the cancel button is clicked, close the modal
  cancelButton.addEventListener("click", function() {
    modal.style.display = "none";
  });

  // Prevent form submission when pressing Enter key
  document.getElementById("bookingForm").addEventListener("keypress", function(event) {
    if (event.keyCode === 13) {
      event.preventDefault();
    }
  });