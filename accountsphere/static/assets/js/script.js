document.addEventListener("DOMContentLoaded", function () {
  console.log("Document loaded and script starting...");

  // Handle flash messages with a slight delay
  function handleFlashMessages() {
    const flashMessagesContainer = document.getElementById("flash-messages");
    if (flashMessagesContainer) {
      const messages =
        flashMessagesContainer.querySelectorAll(".flash-message");
      if (messages.length > 0) {
        console.log(`Found ${messages.length} flash messages.`);
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
  handleFlashMessages();

  // Date and time panel setup
  const dateTimeElement = document.getElementById("datetime");
  function updateDateTime() {
    const now = new Date();
    const dateString = now.toLocaleDateString("en-US", {
      weekday: "long",
    });
    const timeString = now.toLocaleTimeString("en-US", {
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    });
    dateTimeElement.innerHTML = `<span>${dateString}</span> <span>${timeString}</span>`;
  }
  setInterval(updateDateTime, 1000);

  // Greeting and smooth scrolling
  const greetingElement = document.getElementById("greeting");
  const userDataDiv = document.getElementById("user-data");
  const userName = userDataDiv ? userDataDiv.dataset.name : "User";
  function updateGreeting() {
    const hours = new Date().getHours();
    let greeting = "Good Day,";
    if (hours < 12) greeting = "Good Morning,";
    else if (hours < 18) greeting = "Good Afternoon,";
    else greeting = "Good Evening,";
    greetingElement.textContent = `${greeting} ${userName}`;
  }
  updateGreeting();
  smoothScrollGreeting(greetingElement);

  function smoothScrollGreeting(element) {
    let startPosition = -element.offsetWidth;
    function scroll() {
      startPosition += 2; // Move right
      if (startPosition > window.innerWidth) {
        startPosition = -element.offsetWidth;
      }
      element.style.transform = `translateX(${startPosition}px)`;
      requestAnimationFrame(scroll);
    }
    scroll();
  }

  // Smooth scrolling for the news panel
  function smoothScrollNews(panel) {
    let requestID;
    let direction = 1; // Scroll down initially
    function scroll() {
      if (panel.scrollTop >= panel.scrollHeight - panel.clientHeight) {
        direction = -1; // Scroll up when reach bottom
      } else if (panel.scrollTop <= 0) {
        direction = 1; // Scroll down when reach top
      }
      panel.scrollTop += direction * 0.5; // Adjust scrolling speed here
      requestID = requestAnimationFrame(scroll);
    }

    panel.addEventListener("mouseenter", () => {
      cancelAnimationFrame(requestID);
    });

    panel.addEventListener("mouseleave", () => {
      requestID = requestAnimationFrame(scroll);
    });

    requestID = requestAnimationFrame(scroll);
  }
  const newsPanel = document.querySelector(".news-panel");
  if (newsPanel) {
    smoothScrollNews(newsPanel);
  }
});
