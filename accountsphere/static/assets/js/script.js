/*!
 * Start Bootstrap - Full Width Pics v5.0.6 (https://startbootstrap.com/template/full-width-pics)
 * Copyright 2013-2023 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-full-width-pics/blob/master/LICENSE)
 */
// Side bar offcanvas and smooth scrolling implementation

document.addEventListener("DOMContentLoaded", function () {
  console.log("Document fully loaded and parsed");

  // Sidebar offcanvas setup
  var offcanvasElement = document.querySelector(".offcanvas");
  if (!offcanvasElement) {
    console.error("Offcanvas element not found");
    return;
  }
  var offcanvas = new bootstrap.Offcanvas(offcanvasElement);
  var mainContent = document.getElementById("main-content");
  var allContentContainers = document.querySelectorAll(
    ".dashboard-content, .form-content"
  );

  offcanvasElement.addEventListener("shown.bs.offcanvas", function () {
    console.log("Offcanvas shown");
    var offcanvasWidth = offcanvasElement.offsetWidth; // Get the actual width of the sidebar
    mainContent.style.marginLeft = `${offcanvasWidth}px`; // Adjust margin of main content

    allContentContainers.forEach(function (container) {
      container.style.marginLeft = "4px"; // Set the left margin to 2px directly
    });
  });

  offcanvasElement.addEventListener("hidden.bs.offcanvas", function () {
    console.log("Offcanvas hidden");
    mainContent.style.marginLeft = "0"; // Reset margin when sidebar is closed

    allContentContainers.forEach(function (container) {
      container.style.marginLeft = ""; // Reset the left margin to default
    });
  });

  // Product ID update based on account type selection
  var accountTypeSelect = document.getElementById("account_type");
  var productIdInput = document.getElementById("product_id");

  if (accountTypeSelect) {
    accountTypeSelect.addEventListener("change", function () {
      console.log("Account type changed");
      productIdInput.value = accountTypeSelect.value; // Set the product ID input to the selected option's value
    });
  }

  // News panel smooth scroll implementation
  const panel = document.querySelector(".news-panel");
  if (!panel) {
    console.error("News panel not found");
    return;
  }
  let requestID; // Variable to keep track of the animation frame ID

  function smoothScroll() {
    if (panel.scrollTop < panel.scrollHeight - panel.clientHeight) {
      panel.scrollTop += 0.5; // Smaller increment for smoother animation
      requestID = requestAnimationFrame(smoothScroll);
    } else {
      panel.scrollTop = 0;
      requestID = requestAnimationFrame(smoothScroll);
    }
  }

  // Initialize the smooth scrolling
  requestID = requestAnimationFrame(smoothScroll);

  // Event listeners to pause and resume scrolling on mouse enter and leave
  panel.addEventListener("mouseenter", () => {
    console.log("Mouse entered news panel");
    window.cancelAnimationFrame(requestID); // Stop scrolling
  });

  panel.addEventListener("mouseleave", () => {
    console.log("Mouse left news panel");
    requestID = requestAnimationFrame(smoothScroll); // Resume scrolling
  });
});
