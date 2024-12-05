# VRV-Security


Project Overview
The VRV project is a role-based authentication and authorization system that ensures secure
access to application resources. It includes user registration, login, and functionality based on
roles: Admin, Client, and Moderator. The project uses JWT (JSON Web Tokens) for
session management and Role-Based Access Control (RBAC) to enforce permissions.

Features
1. User Registration
• Inputs Required:
o Valid Name
o Valid Email ID (Unique and formatted correctly)
o Valid Phone Number
o Password (with strength validation)
o Confirm Password (must match Password)
o User Type: Client or Moderator
• Validation:
o Client- and server-side validations for input data.
o Duplicate email and phone number checks during registration.
• Flow:
o Users fill in the form and select their role.
o Successful registrations store user details in the database with default inactive
status.
2. User Login
• Users authenticate using their registered email and password.
• A valid JWT token is issued upon successful authentication.
3. Admin Dashboard
• Features:
o View a list of all registered users.
o Activate/deactivate Client and Moderator accounts by refreshing their JWT
tokens.
o Role management capabilities.
o Access audit logs to track user activities.
4. Role-Based Authorization
• Admin:
o Full access to manage users and roles.
o Permission to activate user accounts.
• Moderator:
o Access to manage assigned resources.
o Monitor and moderate content or data submitted by clients.
• Client:
o Access their dashboard after activation.
o View their account details and personalized content.
5. Session Management
• JWTs are used for secure session handling:
o Tokens have expiration times to enhance security.
o Admin has the privilege to refresh tokens for specific accounts.
Client and Moderator Dashboard Features
Client Dashboard
• Personalized user interface with the following features:
o View account details.
o Access exclusive content or resources based on the application's use case.
o View notifications and messages from Admin or Moderators.
o Request support or raise tickets for issues.
Moderator Dashboard
• Features to manage client activities:
o Monitor submitted content or reports from clients.
o Approve or flag client content.
o Communicate directly with clients for clarifications.
Technical Implementation
1. Authentication
• JWT Implementation:
o Tokens are signed with a secret key.
o Each token includes user role and expiration information.
• Password Hashing:
o Passwords are stored securely using algorithms like bcrypt.
2. Authorization
• Middleware checks the JWT token validity and extracts the user's role.
• RBAC ensures that access to endpoints is restricted based on the user role.
Endpoints
Endpoint Method Description Roles
/register POST Registers a new user All Users
/login POST Logs in and provides JWT token All Users
/admin/users GET Lists all registered users Admin
/admin/activate/:id POST Activates a user account Admin
/moderator/review GET Fetches flagged client content Moderator
/client/dashboard GET Access client-specific resources Client (Active)
Database Schema :
Users Table
Column Name Data Type Description
id INT Primary Key
name VARCHAR User's full name
email VARCHAR User's email (unique)
phone VARCHAR User's phone (unique)
password VARCHAR Hashed password
role ENUM Admin, Client, Moderator
status BOOLEAN Active/Inactive
created_at TIMESTAMP Registration timestamp
