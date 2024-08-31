# PlugNPlay

**PlugNPlay** is a Django-based video playing application developed as a college major project. The application features a user-friendly interface for streaming videos and includes an admin portal for uploading and managing video content.

## Features

- **Video Playback:** Stream videos directly from the platform with a responsive and intuitive player.
- **Admin Portal:** Upload and manage videos through a secure admin interface.
- **User Interface:** Built using Bootstrap to ensure a clean and responsive design.
- **Backend:** Developed with Django and Python to handle video management and playback.
- **Database:** Uses MySQL for storing video and user information.
- **Client-Side Interactions:** Implemented using JavaScript for enhanced user experience.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/imriadutta/plugnplay.git
    cd plugnplay
    ```

2. **Set Up Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Database:**

    Update the `DATABASES` setting in `plugnplay/settings.py` to match your MySQL configuration.

5. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

7. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

    Visit `http://127.0.0.1:8000/` in your browser to view the application.

## Usage

- **Admin Portal:** Access the admin portal at `http://127.0.0.1:8000/admin-panel/` to upload and manage videos.
- **Video Playback:** Users can browse and play videos from the main interface.

