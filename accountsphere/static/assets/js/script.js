// Event listener for the document ready event
document.addEventListener("DOMContentLoaded", function () {
  // Update the product ID based on the selected account type
  function updateProductID() {
    var accountTypeSelect = document.getElementById("account_type");
    var productIdInput = document.getElementById("product_id");
    if (accountTypeSelect && productIdInput) {
      // Update the product ID input field with the selected account type
      productIdInput.value = accountTypeSelect.value;
      console.log("Product ID updated to: " + accountTypeSelect.value);
    } else {
      console.log("Error: Elements not found.");
    }
  }

  // Add an event listener to the account type select element
  var accountTypeSelect = document.getElementById("account_type");
  if (accountTypeSelect) {
    accountTypeSelect.addEventListener("change", updateProductID);
  }

  // Handle flash messages
  function handleFlashMessages() {
    const flashMessagesContainer = document.getElementById("flash-messages");
    if (flashMessagesContainer) {
      const messages =
        // Get all flash messages
        flashMessagesContainer.querySelectorAll(".flash-message");
      if (messages.length > 0) {
        console.log(`Found ${messages.length} flash messages.`);

        // Display each flash message as an alert
        messages.forEach((messageDiv) => {
          setTimeout(() => {
            const message = messageDiv.getAttribute("data-message");
            const category = messageDiv.getAttribute("data-category");
            alert(`${category.toUpperCase()}: ${message}`);
          }, 100);
        });
      } else {
        console.log("No flash messages found.");
      }
    } else {
      console.log("Flash messages container not found.");
    }
  }

  // Call the function to handle flash messages
  handleFlashMessages();

  // Day and time panel setup
  const dateTimeElement = document.getElementById("datetime");

  // Update the date and time every second
  function updateDateTime() {
    const now = new Date();
    const dateString = now.toLocaleDateString("en-US", { weekday: "long" });
    const timeString = now.toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
    dateTimeElement.innerHTML = `<span>${dateString}</span> <span>${timeString}</span>`;
  }

  // Call the function to update the date and time
  setInterval(updateDateTime, 1000);

  // Initialize the greeting and smooth scrolling
  const greetingElement = document.getElementById("greeting");
  const userDataDiv = document.getElementById("user-data");
  const userName = userDataDiv ? userDataDiv.dataset.name : "User";

  // Update the greeting based on the time of the day
  function updateGreeting() {
    const hours = new Date().getHours();
    let greeting = "Good Day,";
    if (hours < 12) greeting = "Good Morning";
    else if (hours < 16) greeting = "Good Afternoon";
    else greeting = "Good Evening";
    greetingElement.textContent = `${greeting} ${userName}`;
    smoothScrollGreeting(greetingElement);
  }

  // Call the function to update the greeting
  updateGreeting();

  // Smooth scrolling for the greeting panel
  function smoothScrollGreeting(element) {
    let scrollPosition = element.parentElement.offsetWidth;
    // Scroll the greeting text to the left
    function scroll() {
      scrollPosition -= 1; // Move left
      if (scrollPosition < -element.offsetWidth) {
        scrollPosition = element.parentElement.offsetWidth;
      }
      element.style.transform = `translateX(${scrollPosition}px)`;
      requestAnimationFrame(scroll);
    }
    scroll();
  }

  // Smooth scrolling for the news panel
  const newsPanel = document.querySelector(".news-panel");

  // Smooth scrolling function for the news panel
  function smoothScrollNews() {
    console.log("Starting smooth scrolling for news panel.");
    let requestID;
    function scroll() {
      console.log(
        `Current scrollTop: ${newsPanel.scrollTop}, scrollHeight: ${newsPanel.scrollHeight}, clientHeight: ${newsPanel.clientHeight}`
      );
      if (
        newsPanel.scrollTop <
        newsPanel.scrollHeight - newsPanel.clientHeight
      ) {
        newsPanel.scrollTop += 0.5;
        requestID = requestAnimationFrame(scroll);
      } else {
        console.log("Restarting scroll from top.");
        newsPanel.scrollTop = 0;
        requestID = requestAnimationFrame(scroll);
      }
    }

    // Start the scrolling animation
    requestID = requestAnimationFrame(scroll);
    console.log("Request ID for animation frame:", requestID);

    newsPanel.addEventListener("mouseenter", () => {
      console.log(
        "Mouse entered, cancelling scroll animation frame:",
        requestID
      );
      cancelAnimationFrame(requestID);
    });

    newsPanel.addEventListener("mouseleave", () => {
      console.log("Mouse left, resuming scroll animation.");
      requestID = requestAnimationFrame(scroll);
    });
  }

  // Call the function to enable smooth scrolling for the news panel
  smoothScrollNews();
});
