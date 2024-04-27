/*!
 * Start Bootstrap - Full Width Pics v5.0.6 (https://startbootstrap.com/template/full-width-pics)
 * Copyright 2013-2023 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-full-width-pics/blob/master/LICENSE)
 */
// This file is intentionally blank
// Use this file to add JavaScript to your project

function updateProductID() {
  var select = document.getElementById("account_type");
  var input = document.getElementById("product_id");
  input.value = select.value; // Assuming the value of the option is the product ID
}

updateProductID(); // Call the function once when the page loads
document
  .getElementById("account_type")
  .addEventListener("change", updateProductID); // Call the function whenever the select changes
