# Flask and React Dashboard

This project consists of a Flask backend with WebSocket support and a React frontend dashboard. The backend provides a REST API and real-time updates via WebSockets, while the frontend interacts with these services to display and manage data.

## Project Structure

- **Backend**: Flask application with Flask-SocketIO for real-time communication and SQLite for data storage.
- **Frontend**: React application to display and interact with data from the Flask API.

## Prerequisites

- Python 3.12 or higher
- Node.js 18.x or higher
- npm or yarn

## Setup

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Bhavesh-Rawat/Flask_React_Dashboard.git
   cd Flask_React_Dashboard/backend
`

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the database:**
   The `dishes.db` file should be created in the root directory of the `backend`. You can use SQLite commands or a script to initialize your database. `create_database.py` helps you to populate the database with this json in `dishes.json` data.

6. **Run the Flask server:**
   ```bash
   python app.py
   ```

   The server will be available at `http://127.0.0.1:5000`.

### Frontend Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd ../dishes dashboard
   ```

2. **Install the required packages:**
   ```bash
   npm install
   ```

   or if using yarn:
   ```bash
   yarn install
   ```

3. **Run the React development server:**
   ```bash
   npm start
   ```

   or if using yarn:
   ```bash
   yarn start
   ```

   The frontend will be available at `http://localhost:3000`.

## API Endpoints

- **GET /api/dishes**: Retrieve all dishes.
- **POST /api/dishes/<dish_id>/toggle**: Toggle the publication status of a dish by its ID.

## WebSocket Events

- **Event: `update`**: Emitted when a dish's publication status is updated. The payload contains:
  ```json
  {
    "dishId": <dish_id>,
    "isPublished": <new_status>
  }
  ```

## Testing

1. **For the backend**, you can use tools like Postman or curl to test the API endpoints.
2. **For the frontend**, manual testing can be performed by interacting with the React application.



## Demo

You can watch a demo of the project here: [Demo Video](https://drive.google.com/file/d/1jeVloUdIePmZ_pH12gQJHPO8nRKWp8um/view?usp=sharing)





## Troubleshooting

If you encounter issues, consider the following steps:

1. **Check Dependencies**: Ensure all required packages are installed. Run `pip install -r requirements.txt` and `npm install` in their respective directories.
2. **Database Setup**: Verify that the `dishes.db` file is correctly set up. Reinitialize if needed.
3. **Environment Variables**: Ensure any required environment variables are set up correctly. Update configuration files as necessary.
4. **Logs and Errors**: Check the terminal or console for error messages and logs. They often provide clues to resolve issues.

Feel free to reach out via [Issues](https://github.com/Bhavesh-Rawat/Flask_React_Dashboard/issues) for any further assistance.

---
