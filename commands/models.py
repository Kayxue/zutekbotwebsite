from django.db import models

# Create your models here.
class Command(models.Model):

    command_name=models.CharField(max_length=20,verbose_name="指令名稱")

    command_usage=models.CharField(max_length=100,verbose_name="指令用法")

    command_info=models.CharField(max_length=100,verbose_name="指令說明")

    create_date=models.DateField(verbose_name="指令完成時間",auto_now_add=False)

    def __str__(self):
        return self.command_name+" "+self.command_usage+" "+self.command_info