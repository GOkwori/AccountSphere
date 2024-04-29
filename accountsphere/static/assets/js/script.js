document.addEventListener("DOMContentLoaded", function () {
  console.log("Document loaded and script starting...");

  // Function to handle flash messages
  function handleFlashMessages() {
    const flashMessagesContainer = document.getElementById("flash-messages");
    if (flashMessagesContainer) {
      const messages =
        flashMessagesContainer.querySelectorAll(".flash-message");
      if (messages.length > 0) {
        console.log(`Found ${messages.length} flash messages.`);
        messages.forEach((messageDiv) => {
          const message = messageDiv.getAttribute("data-message");
          const category = messageDiv.getAttribute("data-category");
          setTimeout(() => {
            alert(`${category.toUpperCase()}: ${message}`);
            // Check for redirection attribute and redirect if present
            if (messageDiv.dataset.redirect) {
              window.location.href = messageDiv.dataset.redirect;
            }
          }, 500); // Delay to ensure users see the message
        });
      } else {
        console.log("No flash messages found.");
      }
    } else {
      console.log("Flash messages container not found.");
    }
  }

  // Call the function to handle and display flash messages
  handleFlashMessages();

  // Remaining event listeners and functions for other features
  const accountTypeSelect = document.getElementById("account_type");
  const productIdInput = document.getElementById("product_id");
  if (accountTypeSelect && productIdInput) {
    accountTypeSelect.addEventListener("change", function () {
      productIdInput.value = accountTypeSelect.value;
      console.log("Product ID updated to: ", productIdInput.value);
    });
  }

  const panel = document.querySelector(".news-panel");
  if (panel) {
    let requestID;
    function smoothScroll() {
      if (panel.scrollTop < panel.scrollHeight - panel.clientHeight) {
        panel.scrollTop += 0.5;
        requestID = requestAnimationFrame(smoothScroll);
      } else {
        panel.scrollTop = 0;
        requestID = requestAnimationFrame(smoothScroll);
      }
    }
    requestID = requestAnimationFrame(smoothScroll);

    panel.addEventListener("mouseenter", () => {
      window.cancelAnimationFrame(requestID);
    });

    panel.addEventListener("mouseleave", () => {
      requestID = requestAnimationFrame(smoothScroll);
    });
  } else {
    console.log("News panel not found for smooth scrolling.");
  }
});
