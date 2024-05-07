# AccountSphere

![AccountSphere shown on a variety of screen sizes](./accountsphere/static/documentation/web_pages/landing_page.png)

Visit the deployed site: [AccountSphere](https://flask-accountsphere-d734c062c293.herokuapp.com/)

Welcome to AccountSphere! An advanced financial workflow management platform designed to streamline and simplify your organisation's accounting, product management, user administration, and more.

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
  - [Flow Chart](#flow-chart)
  - [Use Case Diagram](#use-case-diagram)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Features](#features)
    - [Landing Page](#landing-page)
    - [Login Page](#login-page)
    - [Registration Page](#registration-page)
    - [Profile Page](#profile-page)
    - [Account Management](#account-management)
    - [Product Management](#product-management)
    - [Active Directory Groups](#active-directory-groups)
    - [News Board](#news-board)
    - [User Role Management](#user-role-management)
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
  - [Content Sources](#content-sources)
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