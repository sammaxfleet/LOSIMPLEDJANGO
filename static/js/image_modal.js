 
  document.addEventListener('DOMContentLoaded', function () {
    // Get the modal element
    const modal = document.getElementById('imageModal');

    // Get the image to display in the modal
    const modalImage = document.getElementById('modalImage');

    // Get all modal triggers (image links)
    const modalTriggers = document.getElementsByClassName('modal-trigger');

    // Function to open the modal
    function openModal(imageSrc) {
      modal.style.display = 'block';
      modalImage.src = imageSrc;
    }

    // Function to close the modal
    function closeModal() {
      modal.style.display = 'none';
    }

    // Add click event listeners to all modal triggers
    for (let i = 0; i < modalTriggers.length; i++) {
      modalTriggers[i].addEventListener('click', function (event) {
        event.preventDefault(); // Prevent the link's default action
        const imageSrc = this.getAttribute('href');
        openModal(imageSrc);
      });
    }

    // Add click event listener to close the modal when the close button is clicked
    document.querySelector('.close-modal').addEventListener('click', closeModal);

    // Add click event listener to close the modal when clicking outside the modal content
    window.addEventListener('click', function (event) {
      if (event.target === modal) {
        closeModal();
      }
    });
  });
