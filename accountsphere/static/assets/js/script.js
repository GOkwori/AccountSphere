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

  // Initialize the greeting and smooth scrolling
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

  // Smooth scrolling for the news panel
  const newsPanel = document.querySelector(".news-panel");
  function smoothScrollNews() {
    let requestID;
    function scroll() {
      if (
        newsPanel.scrollTop <
        newsPanel.scrollHeight - newsPanel.clientHeight
      ) {
        newsPanel.scrollTop += 0.5;
        requestID = requestAnimationFrame(scroll);
      } else {
        newsPanel.scrollTop = 0;
        requestID = requestAnimationFrame(scroll);
      }
    }
    requestID = requestAnimationFrame(scroll);

    newsPanel.addEventListener("mouseenter", () => {
      cancelAnimationFrame(requestID);
    });

    newsPanel.addEventListener("mouseleave", () => {
      requestID = requestAnimationFrame(scroll);
    });
  }
  smoothScrollNews();
});
