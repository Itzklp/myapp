# Copyright (c) 2025, Kalp Dalsania and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
    def validate(self):
        self.calculatePercentage()

    def calculatePercentage(self):
        total = 0
        maxMarks = 0
        isFail = False

        if self.get("stu_academics"):
            for row in self.stu_academics: 
                total += row.sub_marks
                maxMarks += row.sub_total

                passingMarks = 0.35 * row.sub_total
                if row.sub_marks < passingMarks:
                    isFail = True

            if maxMarks > 0:
                percentage = (total / maxMarks) * 100
                self.stu_total = f'{total} out of {maxMarks}'
                self.stu_percentage = round(percentage, 2)

                self.stu_grade = self.get_grade(percentage)

                self.stu_status = "Fail" if isFail else "Pass"
                frappe.msgprint(f"Student Percentage: {self.stu_percentage}% | Status: {self.stu_status}")
        else:
            frappe.msgprint("Plz Enter Subjects to get percentage!!!")

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
