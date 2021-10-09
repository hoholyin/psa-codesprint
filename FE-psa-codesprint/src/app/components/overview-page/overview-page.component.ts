import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { EmployeeRating } from 'src/app/models/employee-rating';
import { EmployeeData } from 'src/app/models/employee-data';
import { MentalHealthService } from 'src/app/services/mental-health.service';

@Component({
  selector: 'app-overview-page',
  templateUrl: './overview-page.component.html',
  styleUrls: ['./overview-page.component.scss']
})
export class OverviewPageComponent implements OnInit {

  displayedColumns = ['name', 'score'];
  dataSource: MatTableDataSource<EmployeeRating>;

  employeeScores: EmployeeRating[] = [];

  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private mentalHealthSerivce: MentalHealthService) { }

  ngOnInit(): void {
    this.mentalHealthSerivce.getAllUsers().subscribe(res => {
      
      this.employeeScores = res.allEmployeeScore;

      console.log(this.employeeScores)
      this.dataSource = new MatTableDataSource<EmployeeRating>();
      this.dataSource.data = this.employeeScores as EmployeeRating[];
      this.dataSource.paginator = this.paginator;
    });
  }

}
