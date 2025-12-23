## 🎓Vishubh EduBridge

**Vishubh EduBridge** is a comprehensive educational platform designed to bridge the gap between students, faculty, and academic resources. It allows for the organized management of academic disciplines, branches, and subjects, while providing students with easy access to study materials, career guidance, and project ideas.

## Key Features
<img width="802" height="352" alt="image" src="https://github.com/user-attachments/assets/f12cecad-100f-4c8b-a0d9-8ff7a8590f94" />

### 🎓 Academic Management
- **Structured Learning**: Organized hierarchy of Disciplines (e.g., Engineering), Branches (e.g., CSE, IT), and Academic Years.
- **Subject Management**: Comprehensive list of subjects tailored to specific branches and years.

### 📚 Study Resources
- **Material Repository**: Centralized access to Syllabus, Video Lectures, eBooks, Notes, and Reference Links.
- **Easy Filtering**: Filter subjects and materials by Discipline for quick access.

### 🚀 Career & Guidance
- **Career Opportunities**: Detailed guidance on career paths, required skills, and salary expectations for each branch.
- **Project Ideas**: Curated list of project ideas categorized by difficulty (Beginner, Intermediate, Advanced) and technologies.

### 👥 User Roles & Dashboard
- **Role-Based Access**: Distinct portals for Students and Staff/Faculty.
- **Dynamic Dashboard**:
    - **Staff**: Manage subjects and study materials.
    - **Students**: Personalized view of relevant subjects and materials based on their branch and year.

## Tech Stack

- **Backend**: Python, Django 3.2
- **Database**: SQLite (Default)
- **Frontend**: HTML5, CSS3, Bootstrap (Templates)

## Installation

1.  **Clone the repository**
    ```bash
    git clone <repository_url>
    cd vishubh-edubridge
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Development Server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the Application**
    - Open your browser and go to `http://127.0.0.1:8000/`.
    - Access the admin panel at `http://127.0.0.1:8000/admin/`.

## Project Structure

- `academics`: Manages disciplines, branches, subjects, and study materials.
- `accounts`: Handles user authentication and custom profiles.
- `dashboard`: functionality for managing content (Staff view) and viewing resources.
- `guidance`: Provides career info and project ideas.
- `core`: Base templates and homepage views.

## Contributing

1.  Fork the project.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.
