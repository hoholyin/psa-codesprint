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

  constructor(@Inject(MAT_DIALOG_DATA) public data: EmployeeData) { 
    this.selectedEmployee = data;
  }

  ngOnInit(): void {
    console.log(this.selectedEmployee);
  }

}
