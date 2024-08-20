import os
import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from dataset_app.models import Student

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        # Construct the file path dynamically
        file_path = os.path.join(settings.DATASET_DIR, 'ganison_dataset_6.csv')

        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row

                for row in reader:
                    Student.objects.create(
                        school_name=row[0],
                        student_id=row[1],
                        first_name=row[2],
                        last_name=row[3],
                        year=row[4],
                        level=row[5],
                        class_name=row[6],
                        subject=row[7],
                        answers=row[8],
                        correct_answers=row[9],
                        question=row[10],
                        subject_class=row[11],
                        assessment=row[12],
                        sydney_cc=row[13],
                        sydney_as=row[14],
                        sydney_ps=row[15],
                        student_s=row[16],
                        student_t=row[17],
                        student_a=row[18],
                        total_area=row[19],
                        participation=row[20]
                    )

            self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))

        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f'File not found: {file_path}'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'An error occurred: {str(e)}'))
