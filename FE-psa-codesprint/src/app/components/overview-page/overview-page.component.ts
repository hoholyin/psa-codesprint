import { Component, OnInit, ViewChild } from '@angular/core';
import { MatPaginator } from '@angular/material/paginator';
import { MatTableDataSource } from '@angular/material/table';
import { EmployeeRating } from 'src/app/models/employee-rating';
import { EmployeeData } from 'src/app/models/employee-data';
import { MentalHealthService } from 'src/app/services/mental-health.service';
import { MatDialog } from '@angular/material/dialog';
import { EmployeeInfoDialogComponent } from 'src/app/dialogs/employee-info-dialog/employee-info-dialog.component';
import { MatSort } from '@angular/material/sort';

@Component({
  selector: 'app-overview-page',
  templateUrl: './overview-page.component.html',
  styleUrls: ['./overview-page.component.scss']
})
export class OverviewPageComponent implements OnInit {

  displayedColumns = ['name', 'rating'];
  dataSource: MatTableDataSource<EmployeeRating>;

  employeeScores: EmployeeRating[] = [];
  employeeDatas: EmployeeData[] = [];

  isLoading = true;

  @ViewChild(MatPaginator) paginator: MatPaginator;
  @ViewChild(MatSort) sort: MatSort;

  constructor(private mentalHealthSerivce: MentalHealthService,
    private dialogControl: MatDialog) { }

  ngOnInit(): void {
    this.mentalHealthSerivce.getAllUsers().subscribe(res => {
      
      this.isLoading = false;

      this.employeeScores = this.sortRatingInAscendingOrder(res.result);
      this.employeeDatas = res.allEmployeeData;

      console.log(res);

      this.dataSource = new MatTableDataSource<EmployeeRating>();
      this.dataSource.data = this.employeeScores as EmployeeRating[];
      this.dataSource.paginator = this.paginator;
      this.dataSource.sort = this.sort;
    });
  }

  sortRatingInAscendingOrder(employeeScores: EmployeeRating[]) : EmployeeRating[] {
    return employeeScores.sort((a,b) => {
      if (!a.name) {
        a.name = '';
      }
      if (!b.name) {
        b.name = '';
      }

      return (a.name < b.name) ? -1 : 1;
    });
  }

  openDetailsDialog(name: string, rating: number) {
    const selectedEmployee = this.employeeDatas.find( employee => employee.name === name);
    this.dialogControl.open(EmployeeInfoDialogComponent, {width: '40%', data: {selectedEmployee, rating}});
  }

  getRatingColor(rating: number): string {
    if (rating < 0.3) {
      return 'tomato';
    } else if (rating >= 0.3 && rating < 0.8) {
      return 'yellow';
    } else {
      return 'springgreen';
    }
  }
}
