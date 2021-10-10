import { Component, Inject, OnInit } from '@angular/core';
import { MAT_DIALOG_DATA } from '@angular/material/dialog';
import { EmployeeData } from 'src/app/models/employee-data';

@Component({
  selector: 'app-employee-info-dialog',
  templateUrl: './employee-info-dialog.component.html',
  styleUrls: ['./employee-info-dialog.component.scss']
})
export class EmployeeInfoDialogComponent implements OnInit {

  selectedEmployee: EmployeeData;
  rating: number;
  moodMatIcon: string;

  constructor(@Inject(MAT_DIALOG_DATA) public data: any) { 
    this.selectedEmployee = data.selectedEmployee;
    this.rating = data.rating;
  }

  ngOnInit(): void {
    if (this.rating < 0.25) {
      this.moodMatIcon = 'sentiment_very_dissatisfied';
    } else if (this.rating >= 0.25 && this.rating < 0.5) {
      this.moodMatIcon = 'sentiment_dissatisfied';
    } else if (this.rating >= 0.5 && this.rating < 0.75) {
      this.moodMatIcon = 'sentiment_satisfied_alt';
    } else {
      this.moodMatIcon = 'sentiment_very_satisfied';
    }
  }

}
