from django.db import models

class Problem(models.Model):
    DIFFICULTIES = [ ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard') ]

    number = models.IntegerField(unique=True)
    title = models.CharField(max_length=500)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTIES)
    topic = models.CharField(max_length=50)
    leetcode_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.number}. {self.title} ({self.difficulty})'

class Attempt(models.Model):
    STATUSES = [ ('Not Attempted', 'Not Attempted'), ('Attempted', 'Attempted'), ('Solved', 'Solved') ]

    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUSES, default='Not Attempted')
    date_attempted = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.problem.title} - {self.status}'