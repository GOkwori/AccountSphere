# AccountSphere - Testing

![Profile Page](./accountsphere/static/documentation/web_pages/profile_page.png)

Visit the deployed site: [AccountSphere](https://flask-accountsphere-d734c062c293.herokuapp.com/)

- - -

## CONTENTS

* [Feature Testing](#feature-testing)
* [User Story Testing](#user-story-testing)
* [Browser Compatibility](#browser-compatibility)
* [Responsiveness Testing](#responsiveness-testing)
* [Code Validation](#code-validation)
* [Lighthouse Performance Assessment](#lighthouse-performance-assessment)

Throughout the development process, Chrome Developer Tools and other browser tools have been employed to identify and resolve issues promptly. This involved monitoring console logs, diagnosing JavaScript and Python errors, and ensuring consistent styles across browsers.

To ensure responsiveness across multiple screen sizes and devices, every page was tested using Chrome Developer Tools and Microsoft Edge Inspector.

- - -

## Feature Testing

Each feature was tested to ensure seamless user interactions, proper form validation, intuitive navigation, and functional features. Testing involved verifying accuracy, reliability, and usability.

### `Login Page`

| **Description** | **Functionality** | **Test Steps** | **Expected Result** | **Actual Result** | **Status** | **Snapshot** |
|-----------------|-------------------|----------------|----------------------|------------------|------------|--------------|
| Verify login form | Login Form | Load the login page <br> Enter credentials <br> Submit | Redirects to the profile page | Redirects to the profile page | Pass | ![Login Form](./accountsphere/static/documentation/web_pages/login_page.png) |

### `Registration Page`

| **Description** | **Functionality** | **Test Steps** | **Expected Result** | **Actual Result** | **Status** | **Snapshot** |
|-----------------|-------------------|----------------|----------------------|------------------|------------|--------------|
| Verify registration form | Registration Form | Load the registration page <br> Enter user details <br> Submit | Registers new user and redirects to login page | Registers new user and redirects to login page | Pass | ![Registration Form](./accountsphere/static/documentation/web_pages/register_page.png) |

### `Profile Page`

| **Description**                              | **Functionality**            | **Test Steps**                                                            | **Expected Result**                         | **Actual Result**                          | **Status** | **Snapshot**                                                      |
|----------------------------------------------|------------------------------|--------------------------------------------------------------------------|---------------------------------------------|--------------------------------------------|------------|--------------------------------------------------------------------|
| Verify profile greeting                      | Profile Greeting             | Navigate to the profile page <br> Check for personalised greeting        | Displays personalised greeting              | Displays personalised greeting             | Pass       | ![Profile Greeting](./accountsphere/static/testing/feature_testing/greeting-feature.PNG) |
| Verify navigation links                      | Navigation Links             | Click each navigation link <br> Observe page redirection                 | Each link redirects to the correct page     | Each link redirects to the correct page    | Pass       | ![Navigation Links](./accountsphere/static/testing/feature_testing/nav_links.PNG) |
| Verify Home button functionality             | Home Button                  | Click the Home button on the profile page                               | Redirects to the home/dashboard page        | Redirects to the home/dashboard page       | Pass       | ![Home Button](./accountsphere/static/testing/feature_testing/home_logo.PNG)          |
| Verify News Panel Display                    | News Panel Display           | Scroll through the news panel <br> Check for news item visibility        | All news items are visible and scrollable   | All news items are visible and scrollable  | Pass       | ![News Panel](./accountsphere/static/testing/feature_testing/news_panel.PNG)            |
| Verify dynamic greeting update               | Dynamic Greeting Update      | Visit the profile page at different times of the day                     | Greeting updates based on the time of day    | Greeting updates based on the time of day   | Pass       | ![Dynamic Greeting](./accountsphere/static/testing/feature_testing/dynamic_time.PNG) |
| Verify functional responsiveness             | Profile Page Responsiveness  | View the profile page on different devices and orientations              | Page layout adjusts appropriately            | Page layout adjusts appropriately           | Pass       | ![Responsive Profile](./accountsphere/static/documentation/web_pages/profile_page.png) |
| Verify smooth scrolling in the news panel    | Smooth Scrolling             | Use the mouse or touchpad to scroll through the news panel               | Smooth and uninterrupted scrolling experience | Smooth and uninterrupted scrolling experience | Pass       | ![Smooth Scrolling](./accountsphere/static/testing/feature_testing/news_panel.PNG) |


### `Account Management Page`

| **Description**                               | **Functionality**            | **Test Steps**                                                                                 | **Expected Result**                               | **Actual Result**                                | **Status** | **Snapshot**                                                               |
|-----------------------------------------------|------------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|------------|-------------------------------------------------------------------------|
| Verify account management functionality       | Account Management           | Navigate to the account management page <br> Create, update, and delete accounts               | Manages accounts correctly                        | Manages accounts correctly                       | Pass       | ![Account Management](./accountsphere/static/documentation/web_pages/account_dashboard.png) |
| Verify account search functionality           | Account Search               | Use the search bar to find specific accounts by name or email                                  | Accounts matching search criteria are displayed  | Accounts matching search criteria are displayed | Pass       | ![Account Search](./accountsphere/static/testing/feature_testing/account_search.PNG)         |
| Verify form validation during account creation| Form Validation              | Attempt to create an account with invalid data                                                 | Displays appropriate validation error messages   | Displays appropriate validation error messages   | Pass       | ![Form Validation](./accountsphere/static/testing/feature_testing/validation.PNG)       |
| Verify responsiveness of the account page     | Account Page Responsiveness  | View the account management page on various devices and orientations                           | Layout adjusts appropriately                       | Layout adjusts appropriately                      | Pass       | ![Responsive Layout](./accountsphere/static/documentation/web_pages/account_dashboard.png)  |


### `AD Group Management Page`

| **Description**                               | **Functionality**            | **Test Steps**                                                                                  | **Expected Result**                               | **Actual Result**                                | **Status** | **Snapshot**                                                             |
|-----------------------------------------------|------------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|------------|-------------------------------------------------------------------------|
| Verify AD group management functionality      | AD Group Management           | Navigate to the AD group management page <br> Create, update, delete AD groups                  | Manages AD groups correctly                        | Manages AD groups correctly                       | Pass       | ![AD Group Management](./accountsphere/static/documentation/web_pages/ad_group_page.png) |
| Verify search functionality for AD groups     | AD Group Search               | Use the search bar to find specific AD groups                                                   | Groups matching search criteria are displayed     | Groups matching search criteria are displayed    | Pass       | ![AD Group Search](./accountsphere/static/documentation/web_pages/search_feature.PNG)         |
| Verify form validation during AD group creation| Form Validation              | Attempt to create an AD group with invalid data                                                 | Displays appropriate validation error messages   | Displays appropriate validation error messages   | Pass       | ![Form Validation](./accountsphere/static/testing/feature_testing/ad_validation.PNG)       |
| Verify responsiveness of the AD group page    | AD Group Page Responsiveness  | View the AD group management page on various devices and orientations                           | Layout adjusts appropriately                       | Layout adjusts appropriately                       | Pass       | ![Responsive Layout](./accountsphere/static/documentation/web_pages/ad_group_page.png)  |

### `Product Management Page`

| **Description**                            | **Functionality**           | **Test Steps**                                                                                  | **Expected Result**                              | **Actual Result**                               | **Status** | **Snapshot**                                                             |
|--------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------|------------------------------------------------|------------------------------------------------|------------|-------------------------------------------------------------------------|
| Verify product management functionality   | Product Management          | Navigate to the product management page <br> Create, update, delete products                    | Manages products correctly                        | Manages products correctly                       | Pass       | ![Product Management](./accountsphere/static/documentation/web_pages/product_page.png) |
| Verify search functionality for products  | Product Search              | Use the search bar to find specific products                                                    | Products matching search criteria are displayed   | Products matching search criteria are displayed | Pass       | ![Product Search](./accountsphere/static/documentation/web_pages/search_feature.PNGg)         |
| Verify form validation during product creation| Form Validation            | Attempt to create a product with invalid data                                                   | Displays appropriate validation error messages   | Displays appropriate validation error messages  | Pass       | ![Form Validation](./accountsphere/static/testing/feature_testing/product_validation.PNG)       |
| Verify responsiveness of the product page | Product Page Responsiveness | View the product management page on various devices and orientations                            | Layout adjusts appropriately                      | Layout adjusts appropriately                      | Pass       | ![Responsive Layout](./accountsphere/static/documentation/web_pages/product_page.png)  |

### `User Board Page`

| **Description**                           | **Functionality**           | **Test Steps**                                                                                  | **Expected Result**                               | **Actual Result**                                | **Status** | **Snapshot**                                                         |
|-------------------------------------------|-----------------------------|------------------------------------------------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|------------|---------------------------------------------------------------------|
| Verify user board functionality          | User Board                  | Navigate to the user board page <br> Create, update, delete users                               | Manages users correctly                           | Manages users correctly                           | Pass       | ![User Board](./accountsphere/static/documentation/web_pages/user_page.png)        |
| Verify search functionality for users    | User Search                 | Use the search bar to find specific users                                                       | Users matching search criteria are displayed      | Users matching search criteria are displayed      | Pass       | ![User Search](./accountsphere/static/documentation/web_pages/search_feature.PNG)      |
| Verify responsiveness of the user page   | User Page Responsiveness    | View the user board page on various devices and orientations                                   | Layout adjusts appropriately                       | Layout adjusts appropriately                       | Pass       | ![Responsive Layout](./accountsphere/static/documentation/web_pages/user_page.png) |

### `News Board Page`

| **Description** | **Functionality** | **Test Steps** | **Expected Result** | **Actual Result** | **Status** | **Snapshot** |
|-----------------|-------------------|----------------|----------------------|------------------|------------|--------------|
| Verify news board functionality | News Board | Navigate to the news board page <br> Create, update, delete news items | Manages news items correctly | Manages news items correctly | Pass | ![News Board](./accountsphere/static/documentation/web_pages/news_board.png) |

### `Password Reset Page`

| **Description** | **Functionality** | **Test Steps** | **Expected Result** | **Actual Result** | **Status** | **Snapshot** |
|-----------------|-------------------|----------------|----------------------|------------------|------------|--------------|
| Verify password reset functionality | Password Reset | Load the password reset page <br> Enter existing password <br> Enter new password <br> Confirm new password <br> Update | Changes Password | Changes Password | Pass | ![Password Reset](./accountsphere/static/documentation/web_pages/change_password.png) |

### `Logout Functionality`

| **Description** | **Functionality** | **Test Steps** | **Expected Result** | **Actual Result** | **Status** | **Snapshot** |
|-----------------|-------------------|----------------|----------------------|------------------|------------|--------------|
| Verify logout functionality | Logout | Navigate to the logout Icons <br> Click logout button | Logs out and redirects to welcome page | Logs out and redirects to welcome page | Pass | ![Logout](./accountsphere/static/documentation/web_pages/landing_page.png) |

### `Error Pages`

| **Description** | **Functionality** | **Test Steps** | **Expected Result** | **Actual Result** | **Status** | **Snapshot** |
|-----------------|-------------------|----------------|----------------------|------------------|------------|--------------|
| Verify 404 page functionality | 404 Page | Load a non-existent page | Displays custom 404 page | Displays custom 404 page | Pass | ![404 Page](./accountsphere/static/documentation/web_pages/404.png) |


## User Story Testing

To verify that AccountSphere meets the needs of different user types, we conducted thorough user story testing based on their specific goals. Here's a detailed breakdown of how each role's CRUD functionalities were tested and achieved:

### `First-Time User Stories`

| **Action** | **How Was It Achieved?** |
|---|---|
| **Create** | During onboarding, users are guided through profile creation with step-by-step instructions to start using AccountSphere efficiently. |
| **Read** | The onboarding guide provides detailed instructions on how to set up and manage accounts for easy navigation of the platform. |
| **Update** | The dashboard allows users to customise their view, letting them prioritise frequently used features. |
| **Delete** | Users can remove any test data created during onboarding via clear data management controls, ensuring accurate records. |

### `Account Officer User Stories`

| **Action** | **How Was It Achieved?** |
|---|---|
| **Create** | Account Officers can create new client accounts using standardised templates that help expand the client base while maintaining accuracy. |
| **Read** | An advanced search function enables Account Officers to quickly find and retrieve specific account information efficiently. |
| **Update** | Officers can update client details directly on the account management page to ensure accurate data and compliance. |
| **Delete** | They can deactivate or delete outdated client accounts through the account management dashboard to maintain a clean database. |

### `Administrator User Stories`

| **Action** | **How Was It Achieved?** |
|---|---|
| **Create** | Administrators can create user roles and permissions through a comprehensive role management module, ensuring controlled access. |
| **Read** | They can monitor user activity and system health via the admin dashboard, identifying potential issues or suspicious behavior. |
| **Update** | Permissions can be modified easily to reflect changing responsibilities, using the flexible role management controls. |
| **Delete** | Administrators can remove inactive or unauthorised users via user management tools to ensure system security. |

### `Product Manager User Stories`

| **Action** | **How Was It Achieved?** |
|---|---|
| **Create** | New product entries can be created easily with the product creation module, enabling managers to handle lifecycles efficiently. |
| **Update** | Managers can update product details directly via the product page to ensure current and accurate information. |
| **Delete** | Obsolete products can be archived or removed, helping managers maintain a clean product portfolio. |

###    `News Analyst User Stories`

| **Action** | **How Was It Achieved?** |
|---|---|
| **Create** | News Analysts can create articles and reports quickly using the in-platform news creation tools to keep stakeholders informed. |
| **Update** | Analysts can revise or update articles through intuitive editing controls to keep information accurate. |
| **Delete** | Outdated or inaccurate articles can be removed with ease, providing a clean and reliable news board. |


## Browser Compatibility

AccountSphere was thoroughly tested to ensure consistent performance across different web browsers. This step is crucial to ensure that every user experiences the platform as intended regardless of their choice of browser.

### `Tested Browsers`

| **Browser** | **Compatibility** | **Performance** |
|-------------|--------------------|-----------------|
| **Google Chrome** | Fully Compatible | Excellent |
| **Mozilla Firefox** | Fully Compatible | Excellent |
| **Safari** | Fully Compatible | Excellent |
| **Microsoft Edge** | Fully Compatible | Excellent |
| **Opera** | Fully Compatible | Excellent |

### `Specific Tests Conducted`

1. **Functionality Testing**:
   - All CRUD operations (Create, Read, Update, Delete) across all user roles were tested to ensure smooth functionality.
   - Navigation and responsive design elements were verified to perform well.

2. **Visual Testing**:
   - Checked for consistent rendering of layout and styles.
   - Ensured that all interactive elements like buttons and links function correctly.

3. **Performance Testing**:
   - Pages were tested for quick load times and responsive interactions under typical usage conditions.

## Responsiveness Testing

AccountSphere was designed with a mobile-first approach, ensuring that it provides an optimal user experience across devices of varying screen sizes. This testing process involved using browser developer tools and real devices to confirm that the platform is fully responsive.

### `Tested Devices`

| **Device** | **Screen Size** | **Compatibility** |
|------------|-----------------|-------------------|
| **iPhone 12 Pro** | 390px x 844px | Fully Responsive |
| **iPhone 14 Pro Max** | 430px x 932px | Fully Responsive |
| **iPad Mini** | 768px x 1024px | Fully Responsive |
| **Samsung Galaxy S21** | 360px x 800px | Fully Responsive |
| **Google Pixel 6** | 412px x 915px | Fully Responsive |
| **Laptop (13-inch)** | 1280px x 800px | Fully Responsive |
| **Desktop (Full HD)** | 1920px x 1080px | Fully Responsive |

### `Testing Results`

1. **Navigation**:
   - The navigation menu was checked to ensure it adapts properly to smaller screen sizes.
   - On larger screens, the navigation menu is displayed, ensuring a consistent user experience.

2. **Layout and Elements**:
   - All grid layouts, forms, and tables were verified to ensure they resize appropriately.
   - Elements like buttons, images, and text adapt well to various screen sizes.

3. **Performance**:
   - Each page was tested for smooth scrolling, quick load times, and responsive interactions on all screen sizes.

### Visual Examples of Responsiveness

| **Device** | **Screenshot** |
|------------|----------------|
| **iPhone 12 Pro** | ![iPhone 12 Pro Screenshot](./accountsphere/static/testing/responsiveness/iphone.PNG) |
| **iPad Mini** | ![iPad Mini Screenshot](./accountsphere/static/testing/responsiveness/ipad.PNG) |
| **Laptop (13-inch)** | ![Laptop Screenshot](./accountsphere/static/testing/responsiveness/desktop.PNG) |

### Tools Used

- **Google Chrome DevTools**: Verified responsiveness through simulated devices and screen sizes.
- **BrowserStack**: Allowed live testing across multiple device simulators.
- **Real Devices**: Ensured that the platform works seamlessly on physical devices for a real-world experience.

The comprehensive responsiveness testing ensures that AccountSphere adapts flawlessly to different devices and screen sizes, providing a consistent, reliable experience for all users.


## Code Validation

To ensure AccountSphere adheres to web standards and delivers a high-quality experience across all browsers and platforms, extensive code validation was conducted. This involved using industry-standard tools to assess the HTML, CSS, JavaScript, and Python files against current web standards, accessibility guidelines, and best practices.

### `HTML Validation`

The HTML code from all pages in AccountSphere was validated using the [W3C Markup Validation Service](https://validator.w3.org/) to ensure they are error-free and standards-compliant.

| Page | Validation Result |
|------|-------------------|
| Login Page | ![HTML Validation](./accountsphere/static/testing/code_validation/html/login_page.PNG) |
| Registration Page | ![HTML Validation](./accountsphere/static/documentation/validation/registration_page.png) |
| Landing Page | ![HTML Validation](./accountsphere/static/testing/code_validation/html/landing_page.PNG) |
| Account Management Page | ![HTML Validation](./accountsphere/static/documentation/validation/account_management_page.png) |
| Account Add Page | ![HTML Validation](./accountsphere/static/documentation/validation/account_add_page.png) |
| Account Edit Page | ![HTML Validation](./accountsphere/static/documentation/validation/account_edit_page.png) |
| AD Group Management Page | ![HTML Validation](./accountsphere/static/documentation/validation/ad_group_management_page.png) |
| AD Group Add Page | ![HTML Validation](./accountsphere/static/documentation/validation/ad_group_add_page.png) |
| AD Group Edit Page | ![HTML Validation](./accountsphere/static/documentation/validation/ad_group_edit_page.png) |
| Product Management Page | ![HTML Validation](./accountsphere/static/documentation/validation/product_management_page.png) |
| Product Add Page | ![HTML Validation](./accountsphere/static/documentation/validation/product_add_page.png) |
| Product Edit Page | ![HTML Validation](./accountsphere/static/documentation/validation/product_edit_page.png) |
| User Board Page | ![HTML Validation](./accountsphere/static/documentation/validation/user_board_page.png) |
| User Add Page | ![HTML Validation](./accountsphere/static/documentation/validation/user_add_page.png) |
| User Edit Page | ![HTML Validation](./accountsphere/static/documentation/validation/user_edit_page.png) |
| Settings Page | ![HTML Validation](./accountsphere/static/documentation/validation/settings_page.png) |
| Profile Page | ![HTML Validation](./accountsphere/static/documentation/validation/dashboard.png) |
| 404 Error Page | ![HTML Validation](./accountsphere/static/documentation/validation/404_error_page.png) |
| 500 Error Page | ![HTML Validation](./accountsphere/static/documentation/validation/500_error_page.png) |


### `CSS Validation`

CSS files were checked using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to confirm adherence to CSS3 standards and improve visual consistency across platforms.

| CSS File | Validation Output |
|----------|-------------------|
| Main Stylesheet | ![CSS Validation](./accountsphere/static/documentation/validation/css_validation.png) |

### `JavaScript Validation`

JavaScript code was scrutinized for syntax errors and compatibility issues using [JSHint](https://jshint.com/), ensuring smooth functionality and interactivity across different browsers.

| JavaScript File | Validation Output |
|-----------------|-------------------|
| Main Script | ![JavaScript Validation](./accountsphere/static/documentation/validation/main_script_validation.png) |
| Dashboard Functions | ![JavaScript Validation](./accountsphere/static/documentation/validation/dashboard_functions_validation.png) |
| Login Functions | ![JavaScript Validation](./accountsphere/static/documentation/validation/login_functions_validation.png) |

### `Python Validation`

All Python files were validated for PEP8 compliance using the [CI PEP8 Linter](https://pep8ci.herokuapp.com/). This step ensures that the Python code follows the coding conventions outlined in PEP8, improving code readability and maintainability.

| Python File | Validation Output |
|-------------|-------------------|
| `models.py` | ![Python Validation](./accountsphere/static/documentation/validation/python_validation_models.png) |
| `views.py` | ![Python Validation](./accountsphere/static/documentation/validation/python_validation_views.png) |
| `app.py` | ![Python Validation](./accountsphere/static/documentation/validation/python_validation_app.png) |

Through these validation efforts, AccountSphere aims to maintain a high standard of quality, delivering a reliable, accessible, and user-friendly platform for all users.
