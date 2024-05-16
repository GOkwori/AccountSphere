// This script is used to update the product ID based on the account type selected by the user.

document.addEventListener("DOMContentLoaded", function () {
  // Function to update product ID
  function updateProductID() {
    const accountTypeSelect = document.getElementById("account_type");
    const productIdInput = document.getElementById("product_id");
    if (accountTypeSelect && productIdInput) {
      productIdInput.value = accountTypeSelect.value;
      console.log("Product ID updated to: " + accountTypeSelect.value);
    } else {
      console.error("Error: Elements not found.");
    }
  }

  const accountTypeSelect = document.getElementById("account_type");
  if (accountTypeSelect) {
    accountTypeSelect.addEventListener("change", updateProductID);
  } else {
    console.error("Error: Element with id 'account_type' not found.");
  }
});
