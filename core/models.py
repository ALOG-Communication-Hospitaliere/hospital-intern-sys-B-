from django.db import models

class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    num = models.CharField(max_length=20, unique=True) 
    def __str__(self):
        return f"{self.prenom} {self.nom} - {self.num}"
    
class Data(models.Model):
    patient=models.ForeignKey(Patient , on_delete=models.CASCADE, related_name='datas')
    data=models.TextField()
    type = models.CharField(max_length=50)  # Type of data    
    def __str__(self):
        return f"here is the data : {self.data} for {self.patient.nom} - {self.patient.prenom}"