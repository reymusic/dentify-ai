from django.db import models
from accounts.models import SupabaseStorage, User
import datetime as dt

class Prediction(models.Model):
    pred_id = models.BigAutoField(primary_key=True, verbose_name='home_prediction_pk')
    message = models.TextField(max_length=300, blank=True)
    xray_file = models.FileField(upload_to='', storage=SupabaseStorage())
    # prediction detail
    pred_ts = models.DateTimeField(auto_now=True)
    result = models.CharField(max_length=30)
    confidence = models.FloatField()
    # user information
    user = models.ForeignKey(User, on_delete=models.CASCADE)
   
    class Meta:
        db_table = "Predictions"
        verbose_name = "Prediction"

    def __str__(self):
        return f'{self.user.email} : {self.result} - {self.confidence : .2f}%'