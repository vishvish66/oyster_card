# Oyster Card System

## Overview

This project models a simplified version of London's Oyster card system. It allows users to manage their Oyster card balance, simulate trips (both tube and bus), and view fare and station information through a web interface.

## Components

### `oyster_card.py`

**Description:**

The `oyster_card.py` file contains the core functionality for managing the Oyster card system. It includes the following classes:

1. **`Station`**:
   - Represents a station with a name and associated zones.
   - Adheres to the Single Responsibility Principle (SRP) by focusing on station details.

2. **`Trip`**:
   - Handles the details of a journey between two stations, including fare calculation.
   - Follows the Open/Closed Principle (OCP), allowing for extension of fare calculation methods.

3. **`OysterCard`**:
   - Manages the card balance and transactions, including loading money and deducting fares.
   - Adheres to SRP and the Dependency Inversion Principle (DIP) by using the `Trip` class for fare calculations.

**Testing:**

Includes a test function that uses a Test-Driven Development (TDD) approach to ensure correct operation by simulating transactions and verifying the final balance.

### `app.py`

**Description:**

The `app.py` file sets up the Flask web server for the Oyster card system. It includes:

1. **Flask Routes**:
   - `/`: Renders the main page (`index.html`) and displays the current balance.
   - `/load_money`: Handles POST requests to load money onto the card.
   - `/take_trip`: Handles POST requests to simulate a tube journey.
   - `/take_bus_trip`: Handles POST requests to simulate a bus journey.

2. **Flask Application Setup**:
   - Configures and runs the Flask application.
   - Imports the `OysterCard` class and manages HTTP requests to perform operations on the card.

### `index.html`

**Description:**

The `index.html` file provides the user interface for the Oyster card system. It includes:

1. **Current Balance Display**:
   - Shows the current balance on the Oyster card.

2. **Forms for User Actions**:
   - **Load Money**: Allows users to load an amount onto the card.
   - **Take Tube Trip**: Allows users to specify start and end stations for a tube journey.
   - **Take Bus Trip**: Provides a button to simulate a bus journey.

3. **Fare and Station Information**:
   - Displays details about station zones and fare calculations, helping users understand fare pricing.

4. **Styling**:
   - Includes CSS for a modern, clean look with responsive design and improved visual appeal.

## Getting Started

1. **Install Dependencies**:
   - Ensure Python is installed.
   - Install Flask using `pip install flask`.

2. **Run the Application**:
   - Start the Flask server by running `python app.py`.
   - Open a web browser and navigate to `http://localhost:5000/`.

3. **Interacting with the System**:
   - Use the web interface to load money, take tube and bus trips, and view the balance.
  
   - <img width="344" alt="image" src="https://github.com/user-attachments/assets/0643b3c9-9624-48fa-b916-484298e56cfc">
   - <img width="379" alt="image" src="https://github.com/user-attachments/assets/c0b7bb06-8fe0-413b-bb83-50d3cd778b25">




