from django.db import models

# Create your models here.

# employee table create

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=12,blank=True)
    department = models.CharField(max_length=50,blank=True)
    designation = models.CharField(max_length=100,blank=True)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_code} - {self.name}"

# crate attendance table

class Attendance(models.Model):
    ATTENDANCE_STATUS = [
            ("PRESENT", "Present"),
            ("ABSENT", "Absent"),
            ("HALF_DAY", "Half Day"),
            ("LEAVE", "Leave"),
    ]
    attend_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name="attendance_records"
    )
    attendance_date = models.DateField()
    check_in = models.DateTimeField(blank=True ,null=True)
    check_out = models.DateTimeField(blank=True , null=True)
    status = models.CharField(
        max_length=20,
        choices=ATTENDANCE_STATUS,
        default='PRESENT'
    )
    remark = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["employee", "attendance_date"],
                name="unique_employee_attendance_per_day"
            )
        ]
        ordering = ["-attendance_date", "employee"]  

    def __str__(self):
        return f"{self.employee.employee_code} - {self.status}"



