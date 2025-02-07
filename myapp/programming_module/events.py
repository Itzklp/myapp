# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Events(Document):
    def validate(self):
        self.calculate_percentage()

    def calculate_percentage(self):
        total = 0
        max_marks = 0

        if self.get("stu_academics"):
            for row in self.stu_academics:
                total += row.sub_marks
                max_marks += row.sub_total

            if max_marks > 0:
                percentage = (total / max_marks) * 100
                self.stu_total = f"{total} out of {max_marks}"
                self.stu_percentage = round(percentage, 2)
                self.stu_grade = self.get_grade(percentage)

                if percentage < 33:
                    self.stu_status = "Failed"
                elif 33 <= percentage <= 50:
                    self.stu_status = "Pass"
                else:
                    self.stu_status = "Excellent"

                frappe.msgprint(f"Student Percentage: {self.stu_percentage}% | Status: {self.stu_status}")
        else:
            frappe.msgprint("Please enter subjects to calculate the percentage!")

    def get_grade(self, percentage):
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

