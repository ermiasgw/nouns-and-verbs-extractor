from djongo import models

class ExtractedData(models.Model):
    email = models.EmailField(unique=True, null=True)
    nouns = models.JSONField()
    verbs = models.JSONField()

    

