from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


class Customer(models.Model):
    """
    Model to store customer personal and financial information
    """
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    monthly_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Customer's monthly salary in the local currency"
    )
    approved_limit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Total credit limit approved for the customer"
    )
    current_debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        help_text="Current outstanding debt for the customer"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.customer_id})"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ['last_name', 'first_name']


class Loan(models.Model):
    """
    Model to store loan-specific information
    """
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='loans'
    )
    loan_id = models.AutoField(primary_key=True)
    loan_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        help_text="Total amount of the loan"
    )
    tenure = models.DecimalField(
        max_digits=32,
        decimal_places=0,
        help_text="Loan tenure in months"
    )
    interest_rate = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Annual interest rate for the loan"
    )
    monthly_repayment = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Monthly Equated Monthly Installment (EMI)"
    )
    emis_paid_on_time = models.DecimalField(
        max_digits=32,
        decimal_places=0,
        help_text="Number of EMIs paid on time"
    )
    start_date = models.DateField(
        help_text="Date when the loan was initiated"
    )
    end_date = models.DateField(
        help_text="Date when the loan is scheduled to be fully repaid"
    )

    def __str__(self):
        return f"Loan {self.loan_id} "

    class Meta:
        verbose_name = "Loan"
        verbose_name_plural = "Loans"
        ordering = ['-start_date']