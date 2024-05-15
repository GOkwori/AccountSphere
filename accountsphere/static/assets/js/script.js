document.addEventListener("DOMContentLoaded", function () {
  // Function to update product ID
  function updateProductID() {
    var accountTypeSelect = document.getElementById("account_type");
    var productIdInput = document.getElementById("product_id");
    if (accountTypeSelect && productIdInput) {
      productIdInput.value = accountTypeSelect.value;
      console.log("Product ID updated to: " + accountTypeSelect.value);
    } else {
      console.log("Error: Elements not found.");
    }
  }

  var accountTypeSelect = document.getElementById("account_type");
  if (accountTypeSelect) {
    accountTypeSelect.addEventListener("change", updateProductID);
  }

  // Update day and time panel
  const dateTimeElement = document.getElementById("datetime");

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

  setInterval(updateDateTime, 1000);

  // Initialize greeting
  const greetingElement = document.getElementById("greeting");
  const userDataDiv = document.getElementById("user-data");
  const userName = userDataDiv ? userDataDiv.dataset.name : "User";

  function updateGreeting() {
    const hours = new Date().getHours();
    let greeting = "Good Day,";
    if (hours < 12) greeting = "Good Morning";
    else if (hours < 16) greeting = "Good Afternoon";
    else greeting = "Good Evening";
    greetingElement.textContent = `${greeting} ${userName}`;
    smoothScrollGreeting(greetingElement);
  }

  updateGreeting();

  function smoothScrollGreeting(element) {
    let scrollPosition = element.parentElement.offsetWidth;

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

  // Smooth scroll for the news panel
  function smoothScrollNews() {
    const newsPanel = document.querySelector(".news-panel");
    if (!newsPanel) {
      console.error("News panel element not found!");
      return;
    }

    let lastPosition = -1;
    let frame;

    function scroll() {
      if (newsPanel.scrollTop !== lastPosition) {
        lastPosition = newsPanel.scrollTop;
        newsPanel.scrollTop = lastPosition + 1;
      } else {
        newsPanel.scrollTop = 0; // Reset if reached the bottom
      }
      frame = requestAnimationFrame(scroll);
    }

    function stopScrolling() {
      cancelAnimationFrame(frame);
      frame = requestAnimationFrame(scroll); // Restart scrolling
    }

    newsPanel.addEventListener("mouseenter", function () {
      cancelAnimationFrame(frame); // Pause on hover
    });

    newsPanel.addEventListener("mouseleave", function () {
      stopScrolling(); // Resume scrolling
    });

    scroll(); // Start scrolling
  }

  smoothScrollNews();
});
