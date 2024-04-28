/*!
 * Start Bootstrap - Full Width Pics v5.0.6 (https://startbootstrap.com/template/full-width-pics)
 * Copyright 2013-2023 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-full-width-pics/blob/master/LICENSE)
 */
// Smooth scrolling implementation for news panel and updating product ID based on account type

document.addEventListener("DOMContentLoaded", function () {
  // Update product ID based on account type selection
  const accountTypeSelect = document.getElementById("account_type");
  const productIdInput = document.getElementById("product_id");

  if (accountTypeSelect) {
    accountTypeSelect.addEventListener("change", function () {
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
    window.cancelAnimationFrame(requestID); // Stop scrolling
  });

  panel.addEventListener("mouseleave", () => {
    requestID = requestAnimationFrame(smoothScroll); // Resume scrolling
  });
});
