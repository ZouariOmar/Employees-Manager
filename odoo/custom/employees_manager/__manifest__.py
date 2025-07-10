# -*- coding: utf-8 -*-
{
    "name": "employees_manager",
    "summary": "Manages employee data, roles, and organizational structure.",
    "description": """
    - The `employees_manager` module handles employee-related operations within an organization.
    - It provides functionality for:
       - Creating employee records
       - Updating employee records
       - Deleting employee records
       - Assigning roles and departments
       - Managing organizational hierarchy
    - Ensures centralized and consistent employee data management
    - Supports both administrative and HR processes
    """,
    "author": "Zouari Omar",
    "website": "https://www.yourcompany.com",
    "category": "Human Resources",
    "version": "0.1",
    "license": "LGPL-3",
    # any module necessary for this one to work correctly
    "depends": ["base"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/statistiques.xml",
        "views/views.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "application": True,
}
