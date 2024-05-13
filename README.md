# AccountSphere

![AccountSphere shown on a variety of screen sizes](./accountsphere/static/documentation/web_pages/landing_page.png)

Visit the deployed site: [AccountSphere](https://flask-accountsphere-d734c062c293.herokuapp.com/)

Welcome to AccountSphere! A financial workflow management platform designed to streamline and simplify your organisation's accounting, product management, user administration, and more.

In today's complex financial landscape, AccountSphere offers a comprehensive solution that provides effortless control over your financial workflows. Whether you're managing accounts, overseeing products, or maintaining user roles and permissions, our platform is tailored to meet your specific needs.

Explore a feature-rich environment where you can:

- `Manage Accounts Efficiently`: Gain insights and control over accounts, ensuring accurate and secure financial records.
- `Oversee Product Management`: Monitor and optimise your product lifecycle from introduction to phase-out, keeping everything organised.
- `Handle Active Directory Groups`: Securely manage user access controls, ensuring the right permissions for each team member.
- `Stay Informed with the News Board`: Keep up-to-date with industry news, internal updates, and essential announcements.

AccountSphere empowers you to manage your financial workflows seamlessly in one integrated platform. Embrace smarter financial management today!

![GitHub Last Commit](https://img.shields.io/badge/Last%20Commit%20-%20May%202024%20-%20blue)
![GitHub Languages](https://img.shields.io/badge/Languages%20-%204%20-%20teal)
![HTML](https://img.shields.io/badge/1%20-%20HTML%20-%20orange)
![CSS](https://img.shields.io/badge/2%20-%20CSS%20-%20blueviolet)
![JavaScript](https://img.shields.io/badge/3%20-%20JavaScript%20-%20gold)
![Python](https://img.shields.io/badge/4%20-%20Python%20-%20green)
![Contributors](https://img.shields.io/badge/Contributors%20-%201%20-%20navy)
![Testing](https://img.shields.io/badge/Testing%20-%20Passed%20-%20lime)

- - -

## `CONTENTS`

- **[User Experience](#user-experience-ux)**

  - [Project Overview](#project-goal)
  - [Target Audience](#target-audience)
  - [User Goals](#user-goals)
  - [Business Objectives](#business-goal)
  - [User Stories](#user-stories)

- **[Design Choices](#design-choices)**

  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [FlowChart](#flowchart)
  - [Entity-Relationship Diagram](#entity-relationship-diagram)
  - [Features](#features)
    - [Landing Page](#landing-page)
    - [Login Page](#login-page)
    - [Registration Page](#registration-page)
    - [Profile Page](#profile-page)
    - [Account Management](#account-management)
    - [Active Directory Groups](#active-directory-groups)
    - [News Board](#news-board)
    - [Product Management](#product-management)
    - [User Role Management](#user-role-management)
    - [Log out Functionality](#log-out-functionality)
    - [404 Page](#404-page)
    - [Future Implementations](#future-implementations)
  - [Accessibility](#accessibility)

- **[Technologies Used](#technologies-used)**

  - [Languages](#languages)
  - [Frameworks and Libraries](#frameworks-and-libraries)

- **[Deployment & Local Development](#deployment--local-development)**

  - [Deployment](#deployment)
  - [Local Development](#local-development)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)

- **[Testing](#testing)**

  - [Solved Bugs](#solved-bugs)

- **[Credits](#credits)**
  - [Code References](#code-references)
  - [Acknowledgments](#acknowledgments)

---

![AccountSphere Banner](./accountsphere/static/assets/favicon/android-chrome-192x192.png)

## User Experience (UX)

### Project Goal

The primary goal of AccountSphere is to deliver a comprehensive, intuitive financial management platform that simplifies complex financial processes for businesses and organisations. This project is designed to enhance productivity by integrating account management, product management, user role management, and news dissemination into a single, seamless platform. By leveraging modern web technologies and best practices, AccountSphere aims to offer dynamic interaction, data-driven insights, and a customisable user experience that adapts to the unique needs of each organisation.

Through AccountSphere, we strive to empower users to effectively manage their financial workflows, improve operational efficiency, and make informed decisions quickly and accurately. The platform is designed not only to streamline daily tasks but also to provide strategic insights that help businesses grow and adapt in an ever-changing financial landscape.

### Target Audience

The target audience of AccountSphere is diverse, encompassing various professionals and individuals who require efficient financial management tools tailored to their unique needs. This platform is crafted to accommodate Account Officers, Administrators, Product Managers, News Analysts, and first-time users, ensuring each finds features and functionalities aligned with their roles and goals. By addressing the distinct requirements of each user group, AccountSphere provides a seamless experience that empowers users to effectively manage their accounts, monitor trends, and optimise their workflows.

#### `Account Officers`:
- Professionals responsible for managing client financial accounts and transactions.
- Require a centralised platform to streamline daily tasks and deliver accurate financial services.

#### `Administrators`:
- System administrators tasked with maintaining platform security, user roles, and permissions.
- Seek comprehensive management controls to oversee user access, compliance, and data integrity.

#### `Product Managers`:
- Individuals overseeing product development and lifecycle management.
- Need detailed insights into product performance and market trends to make data-driven decisions.

#### `News Analysts`:
- Analysts focused on industry trends and internal news for their organisations.
- Require efficient tools to collect, curate, and disseminate relevant information to stakeholders.

#### `First-Time Users`:
- New users unfamiliar with AccountSphere seeking an intuitive platform to manage their workflow.
- Want a user-friendly onboarding experience and clear guidance on accessing key features.

#### `Business Owners`:
- Entrepreneurs and executives needing a comprehensive financial management solution.
- Look for a platform to streamline workflows, optimise resource allocation, and ensure data compliance.

### User Goals

#### `First Time User Goal`

For first-time users of AccountSphere, the objective is to provide an intuitive, welcoming interface that demystifies financial management. The platform aims to deliver a clear, straightforward onboarding process that helps new users quickly understand the core functionalities and how they can benefit their specific roles. From setting up an account to navigating through the various management modules, first-time users will find guidance and support at each step.

The design and structure of AccountSphere are crafted to reduce the learning curve and enhance user confidence, ensuring that users can start managing their financial tasks efficiently from their first login. The system is designed to offer quick wins for new users, such as easy setup of financial accounts or user roles, encouraging continued use and deeper exploration of the platform's capabilities.

#### `Account Officer Goal`

For Account Officers, AccountSphere aims to streamline their daily tasks by providing a centralised platform where they can efficiently manage client accounts. The platform's goal is to empower Account Officers with the tools they need to easily create, update, and monitor financial records while ensuring accuracy and compliance. Features like search functionality, detailed transaction histories, and customisable reports allow Account Officers to quickly access the information they need and identify opportunities or potential issues. With AccountSphere, Account Officers can deliver a high level of service while minimising administrative overhead.

#### `Administrator Goal`

Administrators are focused on maintaining system integrity and ensuring that the platform runs smoothly for all users. AccountSphere's goal for Administrators is to offer comprehensive management controls that enable them to handle user roles, permissions, and data security with precision and ease. Administrators can manage user access, monitor system usage, and enforce compliance policies directly within the platform. By providing a robust set of administrative features, AccountSphere helps Administrators maintain security, data integrity, and smooth operations while reducing complexity.

#### `Product Manager Goal`

For Product Managers, AccountSphere aims to provide a holistic view of product lifecycles, enabling them to oversee product development, track market trends, and make data-driven decisions. The goal is to help Product Managers efficiently manage their product portfolios by centralising product information, facilitating collaboration, and providing in-depth analytics. They can easily update product details, monitor sales data, and identify opportunities for product optimisation or expansion. AccountSphere helps Product Managers translate insights into actionable strategies that align with broader business objectives.

#### `News Analyst Goal`

AccountSphere's objective for News Analysts is to simplify the process of collecting, organising, and analysing industry news and internal updates. The platform is designed to help News Analysts efficiently curate and disseminate relevant information to different teams, ensuring everyone stays informed about key developments. Analysts can track trends, identify emerging risks, and provide stakeholders with timely, accurate insights. AccountSphere also supports collaborative feedback, enabling Analysts to refine their news content based on user engagement and strategic goals.

#### `Business Goal`

The overarching business goal of AccountSphere is to establish itself as a leader in the financial management software industry, recognised for innovation, reliability, and user satisfaction. By delivering a high-quality, scalable solution that meets the diverse needs of businesses across industries, AccountSphere aims to expand its market share and foster a loyal user base.

The business strategy includes continuous improvement based on user feedback, leveraging cutting-edge technology to enhance features, and maintaining rigorous security standards to protect user data. Through strategic partnerships, targeted marketing, and exceptional customer support, AccountSphere plans to grow its presence globally and help organisations around the world achieve financial clarity and success.

### User Stories

#### `First Time User Stories`

- Create: As a first-time user, I want to create my initial profile during onboarding so that I can start using AccountSphere quickly.
- Read: As a first-time user, I want a clear guide on how to set up and manage my accounts so that I can navigate the platform without confusion.
- Update: As a first-time user, I want to customise my dashboard view so that I can prioritise the features I use most often.
- Delete: As a first-time user, I want to remove any test data created during onboarding so that I can maintain an accurate account record.

#### `Account Officer User Stories`

- Create: As an Account Officer, I want to create new client accounts so that I can expand the client base and deliver accurate services.
- Read: As an Account Officer, I want to quickly search for specific accounts so that I can retrieve information efficiently.
- Update: As an Account Officer, I want to update existing client accounts so that I can ensure accurate information and compliance.
- Delete: As an Account Officer, I want to deactivate or delete outdated client accounts so that I can maintain a clean and relevant database.

#### `Administrator User Stories`

- Create: As an Administrator, I want to create user roles and permissions so that I can control access levels across the platform.
- Read: As an Administrator, I want to monitor user activity so that I can identify any potential system issues or suspicious behavior.
- Update: As an Administrator, I want to modify user permissions so that I can provide the necessary access as responsibilities evolve.
- Delete: As an Administrator, I want to remove inactive or unauthorised users so that I can maintain system security.

#### `Product Manager User Stories`

- Create: As a Product Manager, I want to create new product entries so that I can manage the entire lifecycle from development to release.
- Read: As a Product Manager, I want to oversee product lifecycles so that I can make data-driven decisions on product strategies.
- Update: As a Product Manager, I want to update product details easily so that I can ensure information is accurate and current.
- Delete: As a Product Manager, I want to archive or remove obsolete products so that I can keep the portfolio clean and relevant.

#### `News Analyst User Stories`

- Create: As a News Analyst, I want to create new articles and reports so that I can keep stakeholders informed about industry trends.
- Read: As a News Analyst, I want to analyse news trends and readership so that I can identify emerging risks or opportunities.
- Update: As a News Analyst, I want to revise or update articles to ensure the information remains relevant and accurate.
- Delete: As a News Analyst, I want to remove outdated or inaccurate articles so that I can provide a clean and reliable news board.

- - -

## Design Choices

### Colour Scheme

The colour scheme of AccountSphere has been deliberately selected to establish a professional, clear, and appealing interface that enhances usability and visual aesthetics. The primary colours used throughout the platform include shades of grey and vibrant highlights, which not only create a modern look but also aid in distinguishing between different UI elements effectively. Here’s a detailed breakdown of the colour palette:

- `#3a405a (Slate Blue)`: Serving as the dominant background and accent colour, this shade defines the overall visual identity of the platform. It appears prominently in the navbar, buttons, and cards, providing a professional look that conveys sophistication and confidence.

- `#ffffff (White)`: White is primarily used for the text and main background of forms, dashboards, and other elements, ensuring high contrast and readability. This universal and clean shade gives a fresh and uncluttered feel to the user interface.

- `#fff (White) and #3a405a (Slate Blue)`: The combination of these colours makes interactive buttons prominent, enhancing the navigation and actions across the interface. These colours also highlight key UI elements and cards to create an intuitive and user-friendly experience.

- `#fff (White) and Black for Buttons`: For the buttons, a classic white-on-black and black-on-white contrast is employed, creating visual appeal and drawing attention to call-to-action areas.

- `#000000 (Black)`: Appears in close buttons and provides contrast against white backgrounds.

- `#f0f0f0 (Light Gray`): Used for the news panel to differentiate the section and improve content readability.

- `Slate Blue Accents`: Various UI components, such as panels, headlines, and borders, are highlighted in slate blue to maintain consistency across the platform. These accents are crucial for intuitive navigation and visual hierarchy.

- `News Panel Accent`: The news panel utilises a subtle gradient of white and grey to distinguish it from other sections. This panel retains the visual theme but incorporates a gentle distinction to improve the readability of content.

![Colour Scheme](./accountsphere/static/documentation/colour_palette/colour-palette.PNG)

This carefully curated colour scheme leverages a mix of neutral tones and vibrant accents to create a professional, engaging, and accessible platform. The deliberate use of white and slate blue ensures that essential information stands out, while the uniformity across the platform provides a seamless experience for users navigating through different sections of AccountSphere.

### Typography

For the typography of AccountSphere, the Roboto font from Google Fonts was selected to align with the platform's modern and professional aesthetic.

- `Primary Font: Roboto` - This sans-serif typeface offers a clean, contemporary look that enhances the platform's user experience. Its narrow letterforms and balanced proportions lend themselves well to both headings and body text, ensuring clarity and legibility across various screen sizes and devices.

![Colour Scheme](./accountsphere/static/documentation/google_font/google-fonts.PNG)

The use of Roboto throughout AccountSphere reinforces the platform's focus on streamlined functionality and effective communication. This font choice complements the platform's focus on financial management and business operations, providing a professional yet approachable appearance that aligns with the target audience's needs and preferences.

### Imagery

The imagery used in AccountSphere enhances the user experience by creating a visually engaging and professional platform that aligns with its financial management focus. The visual elements have been carefully curated to reflect the platform's branding and thematic focus, providing a cohesive and appealing atmosphere for users.

- `Background Images`: The background images for AccountSphere are high-quality visuals that align with the platform's business-oriented focus. These images, sourced from [Vecteezy](https://www.vecteezy.com/), provide a clean and modern backdrop that supports the user interface without overwhelming it. The choice of images ensures a professional appearance that resonates with the platform's audience.

- `Iconography and Logo`: The logo and icons used in AccountSphere reflect the platform's emphasis on financial management and business operations. The logo, a stylised representation of financial elements, serves as a visual anchor for the site, reinforcing the platform's identity and purpose. The icons, sourced from [Vecteezy](https://www.vecteezy.com/), offer clear visual communication and thematic consistency, enhancing the platform's usability and user experience.

### Wireframes

The development of AccountSphere began with the creation of detailed wireframes that outlined the structure and layout of each page. These wireframes served as the visual blueprint for designing a user-friendly interface that ensures a seamless experience across the platform. 

Each wireframe was crafted with careful attention to user experience, emphasising intuitive navigation and efficient workflows that align with the goals of various user roles, including administrators, account officers, product managers, and news analysts.

<details>
  <summary>Expand to view wireframes</summary>

#### `Login Page Wireframe`

The login page wireframe shows a streamlined, user-friendly design focused on getting users into the system efficiently. It includes fields for username and password, as well as buttons for submission and navigation to the registration page for new users.

![Login Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_7.png)

#### `Profile Page Wireframe`

The profile page wireframe provides a structured layout where users can view and manage their personal information. This design is optimized for ease of navigation, allowing users to edit their profile, view their recent activities, and access different management features.

![Profile Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_1_main.png)

#### `Account Management Page Wireframe`

The account management page wireframe illustrates a comprehensive view where Account Officers can manage user accounts. The interface allows for viewing detailed account information, performing search operations, and initiating account modifications.

![Account Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_1.png)
![Account Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_2.png)

#### `AD_Group Management Page Wireframe`

This wireframe details the Active Directory group management page, providing administrators with an intuitive interface to manage user groups and their permissions. The layout facilitates easy group creation, editing, and deletion.

![AD_Group Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_3.png)
![AD_Group Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_6.png)


#### `Product Management Page Wireframe`

The product management page wireframe provides Product Managers with a clear overview of all products. They can update product details, analyse performance, and coordinate with other teams to optimise the product lifecycle.

![Product Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_4.png)
![Product Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_9.png)

#### `User Management Page Wireframe`

These wireframes depict the user management page, where administrators can efficiently manage user roles and permissions. The design ensures ease of adding new users, editing their roles, and handling deletions while maintaining data integrity.

![User Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_5.png)
![User Management Page Wireframe](./accountsphere/static/documentation/wireframes/wireframe_10.png)

These wireframes guided the design process to ensure that AccountSphere provides a visually consistent and efficient user interface that aligns with the platform's overall goals.
</details>

### Flowchart

To visualise the user journey and functionality of AccountSphere, detailed flowcharts were developed. These flowcharts outline the interactions between the different components of the platform, demonstrating how users navigate through various features and perform essential tasks.

Each flowchart focuses on a specific aspect of AccountSphere, capturing the logical flow of user actions and system responses, ensuring that the platform operates smoothly and efficiently. The flowcharts serve as valuable guides for understanding the system's architecture and how different roles—such as administrators, account officers, product managers, and news analysts—interact with the platform.

<details>
  <summary>Expand to view flowcharts</summary>

#### `Authentication Flow`

The authentication flow diagram outlines how users gain access to AccountSphere. It covers the steps for login and registration, ensuring secure access and proper onboarding.

![Authentication Flowchart](./accountsphere/static/documentation/flow_chart/authentication.PNG)

#### `Account Management Flow`

This flowchart shows how Account Officers handle account creation, updates, and deletions. It provides a streamlined approach for managing client data and maintaining accurate records.

![Account Management Flowchart](./accountsphere/static/documentation/flow_chart/account_officer.PNG)

#### `Product Management Flow`

The product management flow outlines how Product Managers oversee product lifecycles. It emphasises efficient coordination between product development, market trend analysis, and portfolio optimisation.

![Product Management Flowchart](./accountsphere/static/documentation/flow_chart/product_manager.PNG)

#### `News Management Flow`

The news management flowchart displays how News Analysts curate and disseminate relevant information. It demonstrates the steps involved in collecting, organising, and sharing important updates with stakeholders.

![News Management Flowchart](./accountsphere/static/documentation/flow_chart/news_analyst.PNG)

#### `Administrator Flow`

This diagram illustrates the responsibilities of Administrators in maintaining system integrity. It highlights their role in managing user roles, permissions, and ensuring compliance and data security.

![Settings Flowchart](./accountsphere/static/documentation/flow_chart/admin.PNG)


These flowcharts illustrate the interactions between users and the system, highlighting key functionalities and decision points within AccountSphere. They ensure that the platform is designed to meet user needs effectively while maintaining robust security and operational efficiency.

</details>

### Entity-Relationship Diagram
The Entity-Relationship Diagram (ERD) provides a visual overview of the relationships and data structure within the AccountSphere application. This diagram illustrates how different data entities such as users, groups, accounts, products, and news items interact with each other, helping to clarify the system's architecture.

The ERD is crucial for understanding how data is organised, stored, and accessed within the application. Each entity corresponds to a table in the database, with attributes representing the columns of that table. Relationships between entities, indicated by lines, depict foreign key constraints, showing how data is linked together.

In this diagram:

- `User`: Represents an individual accessing the platform, who belongs to a specific group.
- `Group`: Contains information about various user groups for role-based access management.
- `Account`: Represents financial accounts linked to a specific product.
- `Product`: Contains details about products available within the system, each having a unique association with multiple accounts.
- `NewsItem`: Contains information about various news articles related to finance.

![ERD](./accountsphere/static/documentation/entity_diagram/erd.PNG)

This diagram not only showcases the logical structure of the database but also provides insight into how CRUD operations are performed across different modules in the application. Understanding this structure is essential for maintaining, enhancing, and scaling the application over time.

### Features

The AccountSphere web application provides a comprehensive solution for financial management, offering a range of interactive features that cater to different user roles for ease of use and enhanced productivity.

![Responsive Pages](./accountsphere/static/documentation/web_pages/landing_page.png)

**All Pages Feature:**

* `Responsive Navigation`: Consistent navigation across all pages ensures that users can seamlessly access sections like accounts, products, and user management. Navigation links are well-labeled and intuitive, reducing the learning curve for new users.

  ![Responsive Pages](./accountsphere/static/documentation/web_pages/nav-feature.PNG)

* `Search Functionality`: Each management page includes a dedicated search bar that filters data quickly, enabling efficient information retrieval. Users can search based on keywords and multiple criteria to locate the information they need swiftly.

  ![Responsive Pages](./accountsphere/static/documentation/web_pages/search_feature.PNG)

* `Mobile-Friendly Layout`: The application's responsive design ensures a seamless user experience across desktops, tablets, and mobile devices. Content adapts dynamically to different screen sizes, maintaining usability and clarity across devices.


* `Access Control`: Role-based access control ensures that each user has permissions aligned with their role, whether it's an Account Officer, Administrator, Product Manager, or News Analyst. This minimises risks associated with data security and unauthorized access.

**Specific Role-Based Features:**

* `Account Officer Features`: 
  - Efficient account creation, updating, and management
  - Quick search for client accounts and data filtering

* `Administrator Features`:
  - Manage user roles and permissions for maintaining system security
  - Enforce compliance policies directly within the platform

* `Product Manager Features`:
  - Comprehensive product lifecycle oversight
  - Efficient product creation, updating, and management

* `News Analyst Features`:
  - Efficiently collect, organise, and analyse industry news and updates
  - Track trends and emerging risks for accurate insights
  - Curate and disseminate relevant information to stakeholders efficiently

These features collectively contribute to a robust financial management platform that addresses the unique needs of different user roles, ensuring accurate, efficient, and secure workflows.

<details>
  <summary>Expand to view web pages</summary>

#### `Login Page`
![Login Page](./accountsphere/static/documentation/web_pages/login_page.png)

The login page offers a secure and user-friendly gateway to AccountSphere:

* `Simple Login Form`: Features username and password fields for authentication. Users can quickly enter their credentials to access their accounts securely.

* `Sign-Up Link`: Directs new users to the registration page for account creation. This option ensures that first-time users can easily set up their accounts.

* `Error Handling`: Provides feedback for incorrect login credentials. If a user enters invalid information, clear error messages guide them to rectify the issue.


#### `Registration Page`

![Registration Page](./accountsphere/static/documentation/web_pages/register_page.png)

The registration page is designed to provide a seamless onboarding experience for new users:

* `Intuitive Form Layout`: Presents fields for entering personal information, including first name, last name, username, email, and password.

* `Role Selection`: Allows users to choose their role within the organisation, ensuring appropriate access to platform features.

* `Password Confirmation`: Ensures that users enter their desired password correctly by requiring re-entry in the confirmation field.

* `Error Handling`: Offers user-friendly error messages if mandatory fields are incomplete or if passwords do not match.


#### `Profile Page`

![Profile Page](./accountsphere/static/documentation/web_pages/profile_page.png)

The Profile Page in AccountSphere serves as a centralised dashboard for users, providing them with immediate access to a wide array of features and functionalities tailored to their roles within the platform:

* `Dynamic Greeting and Time Display`: At the top of the page, users are greeted with a personalised message that changes based on the time of day, enhancing the user experience with a warm welcome. Additionally, a real-time clock displays the current day and time, helping users manage their schedule more effectively.

* `Carousel of Visual Highlights`: A visually appealing carousel showcases relevant images such as world maps, teamwork concepts, and transformational changes, offering users an engaging and informative visual experience right on their profile page.

* `Quick Access Cards`: Below the carousel, a series of cards provide quick access to major management sections like Accounts, Groups, Products, Users, and News Board. Each card includes a thumbnail image related to the section and a direct link, simplifying navigation and enhancing efficiency:

  * `Accounts Card`: Directs users to manage financial accounts.
  * `Groups Card`: Provides access to group management functionalities.
  * `Products Card`: Links to product management settings.
  * `Users Card`: Offers a shortcut to user management tools.
  * `News Board Card`: Leads to the latest news and updates within the organisation.

* `Interactive News Panel`: Adjacent to the quick access cards, a dedicated panel for Trending Articles displays the latest news items. This panel supports scrolling, making it easy for users to browse through various articles. Each news item is presented with a headline and a brief description, ensuring users are well-informed about recent developments.

* `Responsive Design`: The entire profile page is designed to be responsive, ensuring that all elements display correctly across different devices and screen sizes, enhancing the user's experience whether on desktop, tablet, or mobile.


#### `Account Management`

![Account Management Page](./accountsphere/static/documentation/web_pages/account_dashboard.png)

The Account Management Board in AccountSphere enables Account Officers and other relevant roles to efficiently oversee client accounts and manage key financial data.

* `Search Bar`: A search function allows users to quickly find specific accounts by filtering based on client name, email, or other relevant data fields.

* `Account Overview`: A table displays all managed accounts in a comprehensive view, including columns like client name, account type, balance, and currency. The table is sortable, providing flexibility in reviewing data.

* `Create New Account`: A prominently positioned button enables the creation of new client accounts. Clicking this button redirects to the "Add Account" page, where users can fill out necessary client information.
  ![Create Account](./accountsphere/static/documentation/web_pages/create_account.png)

* `Edit and Delete Options`: Each row in the table provides edit and delete icons that let Account Officers update client information or remove an account if needed. A modal prompts the user to confirm their choice before deleting.
  ![Edit Account](./accountsphere/static/documentation/web_pages/update_account.png)
  ![Delete Account](./accountsphere/static/documentation/web_pages/delete_account.png)

* `Responsive Design`: The board is optimised for various screen sizes, ensuring Account Officers can access data and perform their tasks effectively across desktop, tablet, and mobile devices.

* `Navigation Links`: Quick links to other sections, like Product and User Management Boards, are included to streamline navigation.


#### `Active Directory Groups`

![AD Group Management Page](./accountsphere/static/documentation/web_pages/ad_group_page.png)

The AD Group Management Page in AccountSphere offers Administrators an organised interface for managing Active Directory groups efficiently.

* `Search Bar`: Allows Administrators to filter groups by name, description, or group type to quickly locate relevant information.

* `Group List`: Displays all available groups in a sortable table format with columns like group name, description, and group type. This comprehensive overview helps Administrators manage and review group data effectively.

* `Create New Group`: A button that links to the "Add AD Group" page, where new Active Directory groups can be defined and added to the system.
  ![AD Group Management Page](./accountsphere/static/documentation/web_pages/create_ad.png)

* `Edit and Delete Actions`: Each group entry in the table includes edit and delete buttons, allowing Administrators to modify or remove a group. A confirmation modal ensures that groups are not deleted accidentally.
  ![AD Group Management Page](./accountsphere/static/documentation/web_pages/update_ad.png)
  ![AD Group Management Page](./accountsphere/static/documentation/web_pages/delete_ad.png)

* `Navigation Links`: Includes links to other management sections like Accounts and Products, helping Administrators quickly navigate between different management tasks.

* `Responsive Layout`: The page is optimised for various devices, ensuring seamless group management whether the Administrator is using a desktop or mobile device.

#### `News Board`

![News Board](./accountsphere/static/documentation/web_pages/news_board.png)

The News Board page in AccountSphere serves as a centralised hub for keeping team members updated with relevant articles and internal announcements.

* `Search Bar`: Helps News Analysts quickly find specific articles or announcements by filtering based on keywords in the title or description.

* `News List`: Displays a table with all published news items, organised by headlines, brief descriptions, and publication dates. This summary view allows stakeholders to quickly scan for key updates.

* `Create New Article`: A button links to the "Add News" page where analysts can draft and publish new articles for immediate dissemination.
  ![News Board](./accountsphere/static/documentation/web_pages/add_news.png)

* `Edit and Delete Actions`: Each article entry includes edit and delete buttons, providing Analysts with full control over the content. Confirmation dialogs are used to prevent accidental deletions.
  ![News Board Wireframe](./accountsphere/static/documentation/web_pages/update_news.png)
  ![News Board Wireframe](./accountsphere/static/documentation/web_pages/delete_news.pngg)

* `Trending Articles`: Highlights important or popular articles to draw attention to them. This helps team members prioritise their reading.

* `Collaboration and Feedback`: Team members can leave comments or suggestions, fostering a collaborative environment to refine the news content.

* `Responsive Design`: The layout ensures a smooth reading experience on devices ranging from desktops to smartphones.

#### `Product Management`

![Product Management Page](./accountsphere/static/documentation/web_pages/product_page.png)

The Product Management page in AccountSphere provides a comprehensive overview of the products available and allows efficient management for Product Managers.

* `Search Bar`: A quick search feature lets managers find specific products by name or description, streamlining the management process.

* `Product List`: Displays all available products in a card layout, with each card containing the product name, description, and type. This layout provides a clear overview of the product catalog.

* `Create New Product`: A button directs to the "Add Product" page, where new products can be defined and added to the catalog.
  ![Product Management Page](./accountsphere/static/documentation/web_pages/add_product.png)

* `Edit and Delete Actions`: Each product card includes edit and delete buttons, enabling quick modifications or removal of outdated products.
  ![Product Management Page](./accountsphere/static/documentation/web_pages/update_product.png)
  ![Product Management Page ](./accountsphere/static/documentation/web_pages/delete_product.png)

* `Product Details`: Clicking on a product card reveals more information, such as associated accounts, sales data, and performance metrics.

* `Analytics Integration`: Managers can view analytics and insights related to each product's lifecycle, helping them make data-driven decisions.

* `Responsive Design`: The layout adapts to different screen sizes, ensuring managers can easily access product information from any device.

#### `User Role Management`

![User Management Page](./accountsphere/static/documentation/web_pages/user_page.png)

The User Board in AccountSphere allows administrators to manage user accounts effectively through various functionalities.

* `Search Functionality`: The search bar helps administrators quickly find users based on their first name, last name, username, email, or role.

* `User List`: Displays a table of all registered users with columns for the first name, last name, username, email, and role. This table provides a comprehensive overview of the user base.

* `Add New User`: A button leads to the "Add User" page, where new user accounts can be created with details like name, email, username, and password.
  ![User Management Page](./accountsphere/static/documentation/web_pages/add_user.png)

* `Edit and Delete Actions`: Each row contains edit and delete buttons, allowing administrators to update user information or remove accounts.
  ![User Management Page](./accountsphere/static/documentation/web_pages/update_user.png)
  ![User Management Page](./accountsphere/static/documentation/web_pages/delete_user.png)

* `Role Management`: Administrators can assign, update, or change user roles directly from the board, ensuring that the right permissions are granted.

* `Responsive Layout`: The table is fully responsive, ensuring that administrators can easily manage users on both desktop and mobile devices.

#### `Password Reset Page`

![Password Reset Page](./accountsphere/static/documentation/web_pages/change_password.png)

The Password Reset page provides users with a secure way to change their passwords directly in AccountSphere.

* `Old Password Verification`: Users must input their current password to verify their identity before setting a new one.

* `New Password Fields`: Two fields for the new password and its confirmation ensure accuracy and prevent typos.

* `Validation`: Password validation checks that the new password meets length and complexity requirements.

* `Update Button`: The "Update" button securely saves the new password after successful verification and validation.

* `Cancel Button`: A "Cancel" button allows users to exit without making changes, returning them to the profile page.

* `Responsive Design`: The form adjusts to different screen sizes, ensuring ease of use across devices.

#### `Log Out Functionality`

The log-out feature ensures secure exit from AccountSphere:

* `Secure Logout`: Upon logging out, the current session is terminated, and all authenticated data is cleared.

* `Confirmation Message`: Users receive a notification confirming their successful logout.

* `Redirect to Home`: After logout, users are redirected to the Home page to start a new session or browse public content.

* `Access Restriction`: Access to protected pages is immediately revoked for logged-out users, preventing unauthorised access.

* `Login Prompt`: The login page encourages users to authenticate again if required, ensuring a secure re-entry.

* `Mobile Compatibility`: The log-out feature works seamlessly across different devices, enhancing user security on the go.


#### `404 Page`

![404 Page](./accountsphere/static/documentation/web_pages/404.png)

The 404 error page provides a user-friendly way to handle navigation issues:

* `Clear Error Message`: Informs users that the page they tried to access is not available, providing clarity on the issue.

* `Navigation Options`: Offers links back to the Home Page and other relevant sections, enabling users to quickly find their way back to familiar content.

* `Consistent Design`: Maintains the overall style of the platform to ensure a cohesive user experience, even in error states.

* `Mobile Responsiveness`: Adapts gracefully across screen sizes to ensure users can always recover from errors on any device.
</details>

### Future Implementations

AccountSphere is committed to continuous improvement and user-centric enhancements. Here are some of the future implementations planned to enrich the platform's capabilities and user experience:

#### `Advanced Analytics Dashboard`
- **Goal**: To provide users, especially Account Officers and Product Managers, with more sophisticated tools for data analysis and decision-making.
- **Features**: Interactive charts, real-time data updates, and customisable reports that cater to the specific needs of different user roles.

#### `Mobile Application`
- **Goal**: To offer a dedicated mobile application for iOS and Android to enhance accessibility and on-the-go management.
- **Features**: Seamless synchronisation with the web platform, offline access to critical data, and mobile-specific user interface enhancements.

#### `Integration with External Financial Services`
- **Goal**: To expand functionality by integrating with external financial APIs, allowing users to manage payments, invoicing, and other financial services directly through AccountSphere.
- **Features**: Secure connections to major financial platforms, streamlined payment processing, and expanded reporting capabilities.

#### `AI-Driven Insights for Account Management`
- **Goal**: To implement artificial intelligence technologies to provide predictive analytics and personalised insights for account management.
- **Features**: AI algorithms that analyse user data to predict trends, suggest optimisations, and alert users about important account changes or opportunities.

#### `Customisable User Interface`
- **Goal**: To allow users to customise the interface according to their preferences and organisational branding.
- **Features**: Theme options, layout configurations, and the ability to add custom logos and color schemes.

#### `Enhanced Security Features`
- **Goal**: To further enhance the security of the platform to protect sensitive financial data.
- **Features**: Two-factor authentication, advanced encryption methods, and continuous security audits.

#### `Multi-language Support`
- **Goal**: To make AccountSphere accessible to a global audience by supporting multiple languages.
- **Features**: Language selection options, culturally relevant user interface adaptations, and support for right-to-left text layouts.

### `Accessibility`

AccountSphere prioritises accessibility to ensure an inclusive and user-friendly platform. We strive to create an environment where all users, regardless of their abilities or disabilities, can effectively use the application. Here are some key accessibility features and considerations:

#### `Semantic HTML`
- **Goal**: Improve screen reader compatibility and navigation for visually impaired users.
- **Features**: Proper use of headings, landmarks (e.g., `<nav>`, `<main>`, `<footer>`), and descriptive `<alt>` attributes for images to provide context.

#### `Keyboard Navigation`
- **Goal**: Enable navigation and control of all interactive elements via keyboard for users with mobility impairments.
- **Features**: Logical tab order, focus indicators, and keyboard shortcuts ensure a seamless user experience without a mouse.

#### `Contrast and Color Choices`
- **Goal**: Enhance readability and visibility for users with color blindness or low vision.
- **Features**: High-contrast color schemes and color-blind-friendly designs.

#### `Form Accessibility`
- **Goal**: Make form inputs and labels usable and understandable by all users.
- **Features**: Explicit `<label>` elements associated with their respective inputs, informative error messages, and user-friendly validation.

#### `Text Resizing and Scaling`
- **Goal**: Allow users to adjust text size without compromising layout or functionality.
- **Features**: Responsive design, flexible font sizes, and media queries to ensure content adapts to user preferences.

#### `Assistive Technology Compatibility`
- **Goal**: Ensure the application functions smoothly with popular assistive technologies.
- **Features**: Regular testing with screen readers, magnifiers, and speech recognition tools to address compatibility issues.

- - -

## Technologies Used

The development of AccountSphere involves a range of modern web technologies and software tools, ensuring a robust, secure, and user-friendly platform for financial management. Below is a detailed overview of the key technologies and tools utilized in creating AccountSphere:

### Languages Used

|  |  |
| -- | --|
| ![HTML](https://img.shields.io/badge/HTML%20-%23e34f26.svg?&style=for-the-badge&logo=html5&logoColor=white) | The structural foundation of our application, used to build the framework and content layout of the web pages. |
| ![CSS](https://img.shields.io/badge/CSS%20-%231572B6.svg?&style=for-the-badge&logo=css3&logoColor=white) | Enhances the presentation of our web application, controlling the layout, colors, and fonts to ensure an engaging and adaptive user interface. |
| ![JavaScript](https://img.shields.io/badge/JavaScript%20-%23F7DF1E.svg?&style=for-the-badge&logo=javascript&logoColor=black) | Powers the dynamic aspects of AccountSphere, enabling interactive elements and real-time functionality without the need for page reloads. |
| ![Python](https://img.shields.io/badge/Python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white) | Utilized for server-side logic, including request handling, data manipulation, and interacting with the database. |
| | |

### Frameworks, Libraries & Programs Used

* [Adobe Express](https://new.express.adobe.com/tools/convert-to-gif) - Used to remove background from logo image and to convert videos to GIF

* [Am I Responsive?](http://ami.responsivedesign.is/) - To show the website image on a range of devices.

* [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
  
* [Bootstrap](https://getbootstrap.com/) - Extensive library of HTML, CSS, and JS tools used to create mobile-first and responsive web pages.

* [Favicon.io](https://favicon.io/) - To create favicon.

* [Flask](https://flask.palletsprojects.com/) - A lightweight WSGI web application framework, used to facilitate the backend setup, URL routing, and the integration of front-end technologies.

* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - An extension that handles SQLAlchemy database migrations for Flask applications using Alembic.

* [Font Awesome](https://fontawesome.com/) - A font and icon toolkit based on CSS and LESS, used to incorporate custom icons throughout the application.

* [Git](https://git-scm.com/) - For version control to track changes in the source code during development.

* [GitHub](https://github.com/) - Hosts the repository that can be deployed to GitHub Pages, providing backup and version control.

* [Github Project Board](https://github.com/users/GOkwori/projects/3/views/3) - For project management and tracking.

* [Heroku](https://www.heroku.com/) - A cloud platform as a service supporting several programming languages, used to deploy the web application.

* [Jinja](https://jinja.palletsprojects.com/) - A modern and designer-friendly templating language for Python, modeled after Django’s templates. Used to dynamically render HTML templates.

* [Microsoft Visio](https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software) - Employed for creating clear and detailed flowcharts and ERDs (Entity-Relationship Diagrams) to visualize data relationships and process flows in the application.

* [PostgreSQL](https://www.postgresql.org/) - An open-source relational database system used to manage the application’s data effectively.

* [SQLAlchemy](https://www.sqlalchemy.org/) - The Python SQL toolkit and Object-Relational Mapping (ORM) system that gives application developers the full power and flexibility of SQL.

* [Visual Studio Code](https://code.visualstudio.com/) - The source-code editor used for software development, offering features such as debugging, syntax highlighting, and code refactoring.

- - -

## Deployment & Local Development

### Deployment

AccountSphere is deployed using Heroku, a cloud platform that enables developers to build, run, and operate applications entirely in the cloud.

To deploy the site using Heroku:

1. Login (or signup) to [Heroku](https://www.heroku.com/).
2. From the dashboard, create a new app by selecting "New" -> "Create new app."
3. Give your app a name (must be unique) and select the region closest to your location.
4. Once the app is created, connect your app to your GitHub repository:
    - Go to the "Deploy" tab in your Heroku dashboard.
    - Select "GitHub" as the deployment method.
    - Connect to GitHub by entering your GitHub account credentials.
    - Search for the repository name and click "Connect".
5. Configure environment variables under "Settings" -> "Reveal Config Vars". Set keys like `SECRET_KEY`, `DATABASE_URL`, etc.
6. Go back to the "Deploy" tab and scroll down to "Manual deploy".
    - Choose the branch you want to deploy (usually "main" or "master").
    - Click "Deploy Branch".
7. After deployment, Heroku will give you a URL to access your deployed application.
8. Click on "Open app" in the top right of the dashboard to view your deployed site.

### Local Development

#### `How to Fork`

To fork the repository:

1. Log in (or sign up) to GitHub.
2. Navigate to the repository for this project on GitHub.
3. Click the "Fork" button in the top-right corner of the page.

#### `How to Clone`

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Navigate to the repository for this project on GitHub.
3. Click on the "Code" button, then choose to clone via HTTPS, SSH, or GitHub CLI, and copy the URL provided.
4. Open your terminal.
5. Change the current working directory to the location where you want the cloned directory.
6. Type `git clone`, then paste the URL you copied earlier.
7. Press Enter to create your local clone.

- - -

## Testing

For a comprehensive overview of all testing conducted during the development of AccountSphere, please refer to the [Testing.md](testing.md) file. This document includes detailed test cases, results, and methodologies used.

### Solved Bugs

The development of AccountSphere involved identifying and resolving several bugs to enhance functionality and user experience. Below is a table detailing some of the notable bugs encountered and the fixes applied:

| No | Bug | Description | Fix Applied | 
| --- | --- | --- | --- | 
| 1 | `Form submission error` | Users experienced form submission issues on the account creation page due to incorrect form data validation. | Corrected the form validation logic to ensure accurate data processing. |
| 2 | `Login redirect error` | After successful login, users were not redirected to their profile page. | Implemented a redirect to the profile page upon successful authentication. |
| 3 | `Database connection timeout` | The application experienced frequent database timeouts. | Optimised database queries and revalidated database connection settings. |
| 4 | `Responsive layout issues` | Some pages were not displaying correctly on mobile devices. | Applied additional responsive CSS fixes to ensure compatibility across all devices. |
| 5 | `Search functionality not working` | The search feature in user management was returning incorrect results. | Refined the search algorithm to accurately filter and display results based on user queries. |
| 6 | `Security vulnerability in user session` | A security vulnerability was discovered that could allow an unauthorized user to access session data. | Enhanced session management and implemented additional security checks. |
| 7 | `Missing error messages` | Error messages were not displayed to the user on failed login attempts. | Added error handling to catch and display appropriate feedback messages to the user. |
| 8 | `Product deletion error` | Users were unable to delete products due to a foreign key constraint error. | Adjusted the database schema to properly handle deletions with cascade rules. |
| 9 | `Group management access rights` | Non-administrative users were able to access and modify group settings. | Revised access controls to restrict group management functionalities to administrators only. |

These fixes have significantly improved the stability, security, and usability of AccountSphere, ensuring a reliable and efficient experience for all users.

- - -

## Credits

### Code References

#### `Web Frameworks and Libraries`
- **Flask**: Used for server-side logic including routing and session management.
- **Jinja2**: Templating engine for rendering HTML from data.
- **SQLAlchemy**: ORM used for database interactions.
- **Flask-Login**: For handling user authentication.
- **Bootstrap**: For responsive design and UI components.

#### `Tutorials and Guides`
- **YouTube Python Authentication and Role Based Access Control (RBAC) Tutorial**: Provided guidance for setting up authentication features.
  - [YouTube Python Authentication Tutorial](https://www.youtube.com/watch?v=71EU8gnZqZQ)
  - [YouTube Python Authentication Tutorial](https://www.youtube.com/watch?v=7AkJvQXOjYg)
- **YouTube Series for User Management System**: Helped in implementing user roles and permissions.
  - [Code Maven](https://www.youtube.com/watch?v=SzWNnUdY6ZE&list=PL193izPqf5X51LG3xhVgeLuIUKbe9a_qs)
- **Code Institute Walkthrough Projects**: Offered foundational knowledge and reusable patterns.
- **OpenAI**: Generated textual content and descriptions within the site.

#### `Design and Media`
- **Vecteezy.com**: Source for stock images used across the platform.
  - [Vecteezy](https://www.vecteezy.com/)
- **Icons and UI Enhancements**: Leveraged Bootstrap icons and custom graphics from various sources.

#### `Database and Tools`
- **PostgreSQL**: Database system used for storing application data.
- **Microsoft Visio**: Used for creating ERDs and flowcharts.

#### `Miscellaneous Tools`
- **Git**: For version control.
- **GitHub**: For repository hosting and deployment.
- **CI PEP8 Linter**: Validator for ensuring PEP8 compliance.
  - [CI PEP8 Linter](https://pep8ci.herokuapp.com/)
- **Python Tutor**: Tool for Python code visualization and debugging.
  - [Python Tutor](https://pythontutor.com/python-compiler.html#mode=edit)
- **Microsoft Visio**: For creating flowcharts and ERD diagrams.

### Acknowledgements
- **`Code Institute`**: For comprehensive educational resources.
- **`Jubril Akolade - Mentor Support`**: Acknowledging the invaluable support from my mentor.
- **`Amy Richardson - Cohort Facilitator`**: For providing guidance and educational resources throughout the development process. 
- **`Real Python & W3Schools`**: For Python programming resources and tutorials.

