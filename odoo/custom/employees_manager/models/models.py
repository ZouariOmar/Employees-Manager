# @file      models.py
# @author    @ZouariOmar (zouariomar20@gmail.com)
# @brief     models.py python file
# @version   0.1
# @date      2025-07-03
# @copyright Copyright (c) 2025
# @link https://github.com/ZouariOmar ZouariOmar @endlink
# -*- coding: utf-8 -*-

from datetime import date
from typing import Self
from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re
import logging
from ..pkg.colors import ANSI  # pyright: ignore


class employees_manager(models.Model):
    """
    Employee Manager Model

    Args:
        None

    Returns:
        None
    """

    _logger = logging.getLogger(__name__)  # For Debuging

    # === Model Info ===
    _name = "employees.manager"
    _description = "Employees Manager App"

    # === Fields Part ===
    name = fields.Char(string="Name", required=True, size=20)
    prename = fields.Char(string="Preame", required=True, size=20)
    email = fields.Char(string="Email", required=True)
    tel = fields.Char(string="Tel", required=True)
    hire_date = fields.Date(string="Hire Date", default=date.today())
    department = fields.Selection(
        string="Department",
        default="developer",
        required=True,
        selection=[
            ("developer", "Developer"),
            ("frontend_dev", "Frontend Developer"),
            ("backend_dev", "Backend Developer"),
            ("fullstack_dev", "Full Stack Developer"),
            ("helpdesk", "Helpdesk"),
            ("support_engineer", "Support Engineer"),
            ("tech_support", "Technical Support"),
            ("qateset", "QA Test Engineer"),
            ("qa_automation", "QA Automation Engineer"),
            ("qa_manual", "Manual QA Tester"),
            ("project_manager", "Project Manager"),
            ("product_owner", "Product Owner"),
            ("ui_ux", "UI/UX Designer"),
            ("devops", "DevOps Engineer"),
            ("intern", "Intern"),
        ],  # type: ignore
        help="Select the employee's department.",
    )

    salary = fields.Float(
        string="Salary", default="1000", help="Select the employee salary (DT)"
    )
    is_active = fields.Boolean(string="Active", default=True)

    # === Contraints Part ===
    @api.model_create_multi
    def create(self, vals_list) -> Self:
        """
        Verify The unicity of `email` and `tel`

        Note:
            No need to check the unicity of the `id` (odoo auto-increment id by default)

        Args:
            self (object): employees_manager object
            vals_list (list[dict]): All employees_manager records

        Returns:
            type: Self
        """
        for vals in vals_list:
            email = vals.get("email")
            tel = vals.get("tel")
            if email and self.search_count(
                [("email", "=", email)]
            ):  # Unicity check: email
                raise ValidationError(f"This Email Already Exists: {email}")
            if tel and self.search_count([("tel", "=", tel)]):  # Unicity check: tel
                raise ValidationError(
                    f"This Phone Number Already Exists: {tel}")

        # Record Pass the unicity verification!
        self._logger.info(
            f"""{ANSI.BLUE}[INFO] Pass the unicity verification succesfully!{
                ANSI.RESET
            }"""
        )
        return super(employees_manager, self).create(vals_list)

    @api.constrains("email")
    def _check_email(self) -> None:
        """
        Verify if the passed email is like example@example.example

        Args:
            self (object): employees_manager object

        Returns:
            type: None
        """
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        for record in self:
            if record.email and not re.match(pattern, record.email):
                raise ValidationError(
                    "Invalid Email Format: %s" % record.email)
        # Email check pass
        self._logger.info(
            f"""{ANSI.BLUE}[INFO] Pass the `Email` Check succesfully!{
                ANSI.RESET}"""
        )

    @api.constrains("tel")
    def _check_tel(self) -> None:
        """
        Verify if the passed phone number is a digital number whith length
        equal 8 chars

        Args:
            self (object): employees_manager object

        Returns:
            type: None
        """
        for record in self:
            if record.tel and not (record.tel.isdigit() and len(record.tel) == 8):
                raise ValidationError("Invalid Tel Format: %s" % record.tel)
        # Tel check pass
        self._logger.info(
            f"""{ANSI.BLUE}[INFO] Pass the `Tel` Check succesfully!{
                ANSI.RESET}"""
        )
