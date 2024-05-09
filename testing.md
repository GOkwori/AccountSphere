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

### Tested Browsers

| **Browser** | **Compatibility** | **Performance** |
|-------------|--------------------|-----------------|
| **Google Chrome** | Fully Compatible | Excellent |
| **Mozilla Firefox** | Fully Compatible | Excellent |
| **Safari** | Fully Compatible | Excellent |
| **Microsoft Edge** | Fully Compatible | Excellent |
| **Opera** | Fully Compatible | Excellent |

### Specific Tests Conducted

1. **Functionality Testing**:
   - All CRUD operations (Create, Read, Update, Delete) across all user roles were tested to ensure smooth functionality.
   - Navigation and responsive design elements were verified to perform well.

2. **Visual Testing**:
   - Checked for consistent rendering of layout and styles.
   - Ensured that all interactive elements like buttons and links function correctly.

3. **Performance Testing**:
   - Pages were tested for quick load times and responsive interactions under typical usage conditions.

