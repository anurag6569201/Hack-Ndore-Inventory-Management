# Hack-Ndore Inventory Management System

## Overview

The Hack-Ndore Inventory Management System is developed for the Indore Municipal Corporation hackathon to address six key problem statements. This system integrates GenAI technology to enhance data accessibility and management through advanced language models and embeddings.

## Features

- **Automated Shelf-Life Management**: Efficiently track and manage the shelf life of perishable items.
- **Internal Communication**: Streamline communication between departments regarding inventory needs and updates.
- **Workflow Management**: Oversee inventory item movement and status with systematic workflows.
- **Authorization Controls**: Define user permissions for inventory status changes to ensure security and accountability.
- **Notification System**: Receive alerts for critical inventory events such as low stock levels and expired items.
- **Comprehensive Asset Database**: Maintain an up-to-date database of all assets, supplies, and equipment.

## Key Sections

1. **Asset Management**:
   - Track and manage vehicles.
   - Monitor fuel usage and gain insights into non-usable vehicles for maintenance and improvement.

2. **Health Inventory Management**:
   - Manage inventory related to health, including beds, ambulances, oxygen cylinders, and staff.
   - Track health-related supplies and their status.

3. **Maintenance Management**:
   - Record and manage machinery servicing and maintenance history.
   - Track service schedules and maintenance activities.

4. **Public Queries**:
   - Receive and manage public queries submitted through the system.
   - Track and resolve queries efficiently.

5. **Workforce Management**:
   - Monitor workforce activities and assignments.
   - Manage query resolutions and workforce-related tasks.

## GenAI Integration

The Hack-Ndore Inventory Management System leverages GenAI to provide advanced data processing and management capabilities:

- **Language Model**: **Gemini-Pro** handles complex language tasks, allowing the system to process and understand natural language queries effectively. This enables admins to interact with the system using simple, prompt-based queries to retrieve and manage data.
  
- **Embedding Model**: **Embedding-001** is used for generating and managing embeddings, which helps in mapping and retrieving related data points efficiently. This improves the accuracy and relevance of search results and recommendations within the system.

- **Implementation**: The integration with **LangChain** and **Chroma DB** ensures efficient data handling and management. LangChain helps in building and chaining complex language models, while Chroma DB supports high-performance data storage and retrieval.

### Benefits of GenAI Integration

- **Enhanced Data Accessibility**: Admins can quickly access and manage data by using natural language prompts, reducing the need for complex queries or manual searches.
- **Improved Accuracy**: Advanced language processing and embedding technologies improve the accuracy of data retrieval and management.
- **Efficient Data Management**: Streamlines data handling processes and enhances the ability to manage large datasets effectively.
- **User-Friendly Interaction**: Simplifies interaction with the system, making it more intuitive for users to perform data-related tasks.

## User Roles

- **Simple User**: Can submit and view queries.
- **Admin**: Manages assets, health inventory, maintenance, public queries, and workforce.
- **Super Admin**: Oversees all aspects of the system with full access and control.


## Team

- **Team Lead**: Anurag Singh
- **Team Members**: Gaurav Aske, Aneet Raghuvanshi


## Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/hack-ndore-inventory-management.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd hack-ndore-inventory-management
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

5. **Access the Application:**

    Open your browser and go to `http://127.0.0.1:8000`.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For inquiries, please contact [anuragsingh6569201@gmail.com].

