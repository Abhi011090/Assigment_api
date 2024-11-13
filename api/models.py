from django.db import models

class Invoice(models.Model):
    invoice_number = models.IntegerField(unique=True)  # Removed max_length
    customer_name = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.customer_name}"

class InvoiceDetail(models.Model):  
    invoice = models.ForeignKey(Invoice, related_name='details', on_delete=models.CASCADE)  # Lowercase 'invoice'
    description = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    line_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detail for Invoice {self.invoice.invoice_number} - {self.description}"
