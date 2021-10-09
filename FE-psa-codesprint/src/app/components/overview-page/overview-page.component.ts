import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { EmployeeRating } from 'src/app/models/employee-rating';
import { EmployeeData } from 'src/app/models/employee-data';
import { MentalHealthService } from 'src/app/services/mental-health.service';
import { MatDialog } from '@angular/material/dialog';
import { EmployeeInfoDialogComponent } from 'src/app/dialogs/employee-info-dialog/employee-info-dialog.component';

@Component({
  selector: 'app-overview-page',
  templateUrl: './overview-page.component.html',
  styleUrls: ['./overview-page.component.scss']
})
export class OverviewPageComponent implements OnInit {

  displayedColumns = ['name', 'score'];
  dataSource: MatTableDataSource<EmployeeRating>;

  employeeScores: EmployeeRating[] = [];
  employeeDatas: EmployeeData[] = [];

  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private mentalHealthSerivce: MentalHealthService,
    private dialogControl: MatDialog) { }

  ngOnInit(): void {
    this.mentalHealthSerivce.getAllUsers().subscribe(res => {
      
      this.employeeScores = res.allEmployeeScore;
      this.employeeDatas = res.allEmployeeData;

      this.dataSource = new MatTableDataSource<EmployeeRating>();
      this.dataSource.data = this.employeeScores as EmployeeRating[];
      this.dataSource.paginator = this.paginator;
    });
  }

  openDetailsDialog(name: string) {
    const selectedEmployee = this.employeeDatas.find( employee => employee.name === name);
    this.dialogControl.open(EmployeeInfoDialogComponent, {data: selectedEmployee});

  }

}
